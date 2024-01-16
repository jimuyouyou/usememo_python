# app/main.py
import logging
from fastapi import FastAPI, File, UploadFile
from datetime import datetime
from audio_processing import split_audio, compare_audio
from pydub import AudioSegment

# Configure logging to output to both console and a log file
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),            # Log to console
        logging.FileHandler('web.log'),     # Log to file
    ],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


app = FastAPI()

@app.post("/process_audio")
async def process_audio(audio_file: UploadFile = File(...)):
    logger.info("Audio processing started successfully")
    
    # Generate a dynamic file name based on the current time
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]  # Exclude the last 3 digits for milliseconds
    output_folder = f"./audios/uploaded_audio_{current_time}"
    uploaded_file_name = f"./audios/uploaded_audio_{current_time}.mp3"

    # Save the uploaded audio file with the dynamic file name
    with open(uploaded_file_name, "wb") as f:
        f.write(audio_file.file.read())

    # Split the uploaded audio file
    split_audio("uploaded_audio.mp3", output_folder)

    # Process the audio chunks or perform other actions
    # ...

    return {"output_folder": output_folder}

@app.post("/compare_audio")
async def compare_audio_endpoint(audio1: UploadFile = File(...), audio2: UploadFile = File(...)):
    logger.info(f"Audio comparison completed. start:")

    # Save the uploaded audio files
    with open("audio1.mp3", "wb") as f:
        f.write(audio1.file.read())

    with open("audio2.mp3", "wb") as f:
        f.write(audio2.file.read())

    # Load audio files
    audio1 = AudioSegment.from_file("audio1.mp3")
    audio2 = AudioSegment.from_file("audio2.mp3")

    # Compare audio and get similarity
    similarity = compare_audio(audio1, audio2)

    logger.info(f"Audio comparison completed. Similarity: {similarity}")

    return {"similarity": similarity}
