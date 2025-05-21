#!/usr/bin/env python3

# This file simply ensures that the model and processor are downloaded from Huggingface.

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
