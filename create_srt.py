import sys
import subprocess
import wave

def split_text_into_chunks(text, max_words=5):
    """Split text into chunks of 3 to 5 words."""
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk_size = min(max_words, len(words) - i)
        chunks.append(' '.join(words[i:i+chunk_size]))
        i += chunk_size
    return chunks

def convert_seconds_to_srt_time(seconds):
    """Convert seconds to SRT time format (HH:MM:SS,MS)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"

def get_audio_duration(audio_file_path):
    """Get the duration of the audio file using FFmpeg."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", audio_file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return float(result.stdout)

def create_srt_file(audio_file_path, text_file_path, output_srt_path):
    # Get the duration of the audio file in seconds
    duration_s = get_audio_duration(audio_file_path)

    # Read the text file
    with open(text_file_path, 'r') as file:
        text = file.read()

    # Split the text into chunks of 3 to 5 words
    chunks = split_text_into_chunks(text)

    # Calculate the time per chunk based on the audio duration
    time_per_chunk = duration_s / len(chunks)

    # Generate SRT content
    srt_content = ""
    start_time = 0
    for i, chunk in enumerate(chunks):
        end_time = start_time + time_per_chunk
        start_srt = convert_seconds_to_srt_time(start_time)
        end_srt = convert_seconds_to_srt_time(end_time)
        srt_content += f"{i+1}\n{start_srt} --> {end_srt}\n{chunk.strip()}\n\n"
        start_time = end_time

    # Save the SRT content to a file
    with open(output_srt_path, 'w') as srt_file:
        srt_file.write(srt_content)
    print(f"SRT file created: {output_srt_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_srt.py <audio_file.mp3> <text_file.txt> <output_file.srt>")
        sys.exit(1)

    audio_file = sys.argv[1]
    text_file = sys.argv[2]
    output_file = sys.argv[3]

    create_srt_file(audio_file, text_file, output_file)
