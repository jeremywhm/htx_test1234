#!/usr/bin/env python3

# Decode all of the cv-valid-dev utterances.

import os
import requests
import glob
import tqdm


data_dir = "/home/jeremy/datasets/common_voice/cv-valid-dev/cv-valid-dev"
output_filename = "/home/jeremy/htx_test1234/asr/cv-valid-dev.csv"
port = 8001

# Find all audio files
audio_filenames = glob.glob(os.path.join(data_dir, "*.mp3"))

transcriptions = dict()

for audio_filename in tqdm.tqdm(sorted(audio_filenames)):
    
    utt_name = os.path.join(os.path.basename(os.path.dirname(audio_filename)), os.path.basename(audio_filename))
    assert(utt_name not in transcriptions)
    
    # Setup audio file reader
    with open(audio_filename, "rb") as file:
        files = {"file": [audio_filename, file, "audio/mpeg"]}
    
        # Send ASR request to API
        reply = requests.post("http://localhost:{}/asr".format(port), files=files)
        reply = reply.json()
    
    transcriptions[utt_name] = reply["transcription"]
    
# Write transcriptions to file
with open(output_filename, "w", encoding="utf-8") as file:
    print("utternace_name,generated_text", file=file)
    for utt_name in sorted(transcriptions.keys()):
        print("{},{}".format(utt_name, transcriptions[utt_name]), file=file)
        
print("Done!")
