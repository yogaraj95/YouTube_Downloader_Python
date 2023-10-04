from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os


# Function to download and convert YouTube video to MP3
def download_youtube_video_as_mp3(video_url, output_directory):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Get the title of the YouTube video
        video_title = yt.title

        # Replace any invalid characters in the title with underscores
        video_title = "".join(x if x.isalnum() or x in [' ', '.', '-'] else '_' for x in video_title)

        # Download the video with the YouTube video's title as the file name
        video_filename = f"{video_title}.mp4"
        video_stream.download(output_path=output_directory, filename=video_filename)

        # Construct the paths for video and audio files
        video_path = os.path.join(output_directory, video_filename)
        mp3_filename = f"{video_title}.mp3"
        mp3_path = os.path.join(output_directory, mp3_filename)

        # Extract audio from the downloaded video and save it as an MP3 file
        ffmpeg_extract_audio(video_path, mp3_path)

        # Remove the downloaded video file (optional)
        os.remove(video_path)

        print(f'Video downloaded as MP3 with the YouTube title: {mp3_path}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


# Get user input for the YouTube video URL and the directory
video_url = input("Enter the YouTube video URL: ")
output_directory = input("Enter the directory where you want to save the MP3: ")

download_youtube_video_as_mp3(video_url, output_directory)
