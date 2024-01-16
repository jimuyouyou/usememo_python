import axios from 'axios';
import * as fs from 'fs/promises';

// Function to read a file as a buffer
const readFileAsBuffer = async (filePath: string): Promise<Buffer> => {
  return await fs.readFile(filePath);
};

// Function to make the process_audio API call
const processAudio = async () => {
  try {
    const audioFilePath = 'path/to/your/audio/file.mp3'; // Replace with the actual file path
    const fileBuffer = await readFileAsBuffer(audioFilePath);

    const response = await axios.post('http://localhost:8000/process_audio', fileBuffer, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    console.log(response.data);
  } catch (error) {
    console.error('Error calling process_audio API:', error.message);
  }
};

// Function to make the compare_audio API call
const compareAudio = async () => {
  try {
    const audio1FilePath = 'path/to/your/audio/file1.mp3'; // Replace with the actual file path
    const audio2FilePath = 'path/to/your/audio/file2.mp3'; // Replace with the actual file path

    const audio1Buffer = await readFileAsBuffer(audio1FilePath);
    const audio2Buffer = await readFileAsBuffer(audio2FilePath);

    const response = await axios.post('http://localhost:8000/compare_audio', {
      audio1: {
        data: audio1Buffer,
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      },
      audio2: {
        data: audio2Buffer,
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      },
    });

    console.log(response.data);
  } catch (error) {
    console.error('Error calling compare_audio API:', error.message);
  }
};

// Call the process_audio API
processAudio();

// Call the compare_audio API
compareAudio();
