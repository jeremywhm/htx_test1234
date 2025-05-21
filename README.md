# htx_test1234

### Task 2b

To run ping API, run on the server terminal:\
```cd asr```\
```python3 asr/run_ping_api.py```

To test ping API call, run on the client terminal:\
```wget http://localhost:8001/ping```\
This should generate a ping file in the current directory that contains "pong".

### Task 2c

To run ASR API, run on the server terminal:\
```python3 asr/run_asr_api.py```

### Task 2d

Ensure that the ASR API in task 2c has been started.\
To decode cv-valid-dev audio, run on the client terminal:\
```python3 cv-decode.py```\
The output transcriptions are saved in cv-valid-dev.csv.

### Task 2e

To create the docker image, run:\
```docker build -t asr-api .```\
To run the docker image, run on the server terminal:\
```docker run -p 8001:8001 asr-api```\
It then possible to submit API calls to the running Docker API, by running on the client terminal:\
```python3 cv-decode.py```

### Task 3b

The fine-tuned model checkpoint saved as wav2vec2-large-960h-cv.ckpt by the Jupyter notebook is too large to fit in Github. Therefore, I first reduce the size by extracting out the state_dict of the model parameters and save it into wav2vec2-large-960h-cv.pt. Then, I upload to OneDrive, instead of Github.\
\
The fine-tuned model checkpoint can be downloaded from https://1drv.ms/f/c/52518ca9cf60839e/EmUNHf2pOZ9Lp9uwU-sCafYBO_uUNEbF4njQ0qhrmsxV7w?e=VSmIsz \
\
To load the fine-tuned model, run:\
```from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor```\
```model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")```\
```checkpoint_path = "wav2vec2-large-960h-cv.pt"```\
```state_dict = torch.load(checkpoint_path, map_location="cpu")```\
```new_state_dict = dict()```\
```for key in state_dict:```\
```    new_state_dict[key.replace("model.", "")] = state_dict[key]```\
```model.load_state_dict(new_state_dict)```\

### Task 4

To compute the WERs of the seed and fine-tuned models, run:\
```cd ../asr-train```\
```python3 compute_wer.py```
