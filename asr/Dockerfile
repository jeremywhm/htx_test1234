# Start from open-source PyTorch image
FROM pytorch/pytorch:2.7.0-cuda12.8-cudnn9-devel

# Create working directory
WORKDIR /app

# Install python packages
RUN python3 -m pip install fastapi transformers torchaudio uvicorn python-multipart

# Copy required files
COPY asr_api.py .
COPY run_asr_api.py .
COPY download_hf_model.py .

# Download wav2vec2-large-960h from Huggingface
RUN python download_hf_model.py

# Expose API port
EXPOSE 8001

# Run API
CMD ["python3", "run_asr_api.py"]
