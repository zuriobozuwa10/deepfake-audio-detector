# Deepfake Audio Detector 

Uses deep learning to classify audio clips of people speaking as deepfake or non-deepfake.

Built in 2023.

Still works in 2025!

## Usage

```
python3 command_line_model_tester.py --model <path_to_model> --clips <path_to_audio>
```

## Example Usage

```
python3 command_line_model_tester.py --model model/model-1.keras --clips audio/ElevenLabs_2025-01-24T06_12_40_Rachel_pre_s50_sb75_se0_b_m2.flac
```

## Note

Flac and m4a files are supported.

Mp3 files are not supported. If you have an mp3, convert it to a supported format (google search for a conversion tool) before giving it to the model.

## SF

Hello from San Francisco!

