from moviepy.editor import VideoFileClip
import sys

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    """Convert MP4 video to MP3 audio."""
    # Load the video file
    video = VideoFileClip(mp4_file_path)
    
    # Extract the audio and save as MP3
    video.audio.write_audiofile(mp3_file_path)
    print(f"MP3 file saved: {mp3_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_mp4_to_mp3.py <input_file.mp4> <output_file.mp3>")
        sys.exit(1)

    input_mp4 = sys.argv[1]
    output_mp3 = sys.argv[2]
    
    convert_mp4_to_mp3(input_mp4, output_mp3)
