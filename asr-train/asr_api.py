#!/usr/bin/env python3

# This file defines the ASR API.

from fastapi import FastAPI, File, UploadFile
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import time
import torchaudio
import io


device = "cpu"
checkpoint_path = "/home/jeremy/htx_test1234/asr-train/wav2vec2-large-960h-cv.pt"

# Load model outside of API function, so that model is only loaded once.

# Load model from HF
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

# Load feature extractor from HF
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")

# Load fine-tuned model checkpoint
state_dict = torch.load(checkpoint_path, map_location="cpu")
new_state_dict = dict()
for key in state_dict:
    new_state_dict[key.replace("model.", "")] = state_dict[key]
model.load_state_dict(new_state_dict)
model.to(device)

app = FastAPI()
print("API server is ready to receive requests.")
    

@app.post("/asr")
async def asr(file: UploadFile=File(...)):
    """
    Recognise the words and find the duration of the speech in the specified audio file.
    
    Inputs:
    file [str] - Bytes of an MP3 file.
    
    Outputs:
    transcription [str] - The recognised words.
    duration [str] - The time in seconds of speech within the file.
    """
    
    audio_bytes = await file.read()
    
    with torch.no_grad():
        
        try:
            # Load audio from the bytes string
            audio, sr = torchaudio.load(io.BytesIO(audio_bytes), format="mp3")
            
            # Resample audio to expected sampling rate
            expected_sr = 16000
            if sr != expected_sr:
                audio = torchaudio.transforms.Resample(sr, 16000)(audio)
                
            if len(audio.size()) > 1:
                audio = audio.squeeze()
                
            # Compute the duration of the audio file, which includes silence.
            # If exclusion of silence is needed, then need to do a forced alignment.
            duration = len(audio) / expected_sr
            
            # Extract features from audio
            features = processor(audio, return_tensors="pt", sampling_rate=expected_sr).input_values
            
            # Parse audio through ASR model
            logits = model(features.to(device)).logits
            
            # Decode output distribution by choosing most likely token at each frame
            predict_ids = torch.argmax(logits, dim=-1)
            
            # Convert token sequence into word sequence
            transcription = processor.batch_decode(predict_ids)[0]
        
        except:
            return {
                "transcription": "",
                "duration": "",
                "error": True
            }

    return {
        "transcription": transcription,
        "duration": str(duration),
        "error": False
    }
    