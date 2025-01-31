import os
import logging
from pydub import AudioSegment

# Set up logging configuration
logging.basicConfig(
    filename='audio_converter.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AudioConverter:

    def __init__(self):
        self.supported_formats = ['.flac', '.m4a']

    def convert_audio(self, input_file):
        if not os.path.isfile(input_file):
            logging.error(f"File {input_file} does not exist.")
            return None

        file_extension = os.path.splitext(input_file)[1].lower()

        if file_extension == '.mp3':
            return self._convert_mp3(input_file)
        elif file_extension in self.supported_formats:
            logging.info(f"{input_file} is already in a supported format.")
            return input_file
        else:
            logging.error("Unsupported file format. Please provide an MP3, FLAC, or M4A file.")
            return None

    def _convert_mp3(self, input_file):
        output_file = os.path.splitext(input_file)[0] + '.flac'
        
        try:
            audio = AudioSegment.from_mp3(input_file)
            audio.export(output_file, format='flac')
            logging.info(f"Converted {input_file} to {output_file}.")
            return output_file
        except Exception as e:
            logging.error(f"Error converting {input_file}: {e}")
            return None

def main():
    # Example usage of AudioConverter class
    converter = AudioConverter()
    
    # Replace with your actual MP3 file path
    input_audio = "path/to/your/audio.mp3"
    
    converted_audio = converter.convert_audio(input_audio)
    
    if converted_audio:
        # Proceed with processing the converted audio
        logging.info(f"Audio ready for processing: {converted_audio}")
    else:
        logging.error("Audio conversion failed.")

if __name__ == "__main__":
    main()
