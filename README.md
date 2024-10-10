# Utilities for Videos and Subtitles

## Create Subtitles
To allow dynamic control over the number of words per chunk (A to B words) via command-line arguments, we can modify the script to accept two additional arguments: one for the minimum number of words (A) and another for the maximum number of words (B). This way, the user can specify these values when running the script.

How to Use the Updated Script:
```bash
python create_srt.py <audio_file.mp3> <text_file.txt> <output_file.srt> <min_words> <max_words>
```
For example:

```bash
python create_srt.py sample.mp3 transcript.txt output.srt 3 5
```

This command will split the transcript into chunks of 3 to 5 words and generate an SRT file aligned with the audio duration.

Let me know if you need further assistance!


## Convert MP4 to MP3

Python application that converts an MP4 video to MP3 (extracting only the audio), you can use the moviepy library or ffmpeg through the subprocess module. 

How to Use:
Run it from the command line:
```bash
python convert_mp4_to_mp3.py input_video.mp4 output_audio.mp3
```