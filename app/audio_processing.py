# audio_processing.py
import logging
from pydub import AudioSegment
from pydub.silence import split_on_silence
import essentia
from essentia.streaming import MonoLoader, Extractor

# Get the logger with the same name as in main.py
logger = logging.getLogger(__name__)

def split_audio(input_file, output_folder, chunk_duration_ms=5000):
    logger.info(f"Audio split completed. chunks created.")
    audio = AudioSegment.from_file(input_file, format="mp3")

    # Set parameters for split_on_silence
    silence_threshold = -30
    min_silence_len = 500  # milliseconds
    keep_silence = 150  # milliseconds

    # Split the audio using the specified parameters
    chunks = split_on_silence(audio, silence_thresh=silence_threshold, min_silence_len=min_silence_len, keep_silence=keep_silence)

    # Export each chunk as a separate file
    for i, chunk in enumerate(chunks):
        chunk.export(f"{output_folder}/chunk_{i}.mp3", format="mp3")

    

def compare_audio(audio1, audio2):
    # Load the audio files
    existing_audio = MonoLoader(filename=audio1)()
    recorded_audio = MonoLoader(filename=audio2)()

    # Extract audio features using Essentia
    extractor = Extractor()
    features_existing = extractor(existing_audio)
    features_recorded = extractor(recorded_audio)

    # Compare audio features
    similarity = essentia.array.cosine(features_existing, features_recorded)

    return similarity
