from pytube import YouTube

# Get user input for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Get user input for the directory where you want to save the video
output_directory = input("Enter the directory where you want to save the video: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
video_stream = yt.streams.get_highest_resolution()

# Download the video to the specified directory
video_stream.download(output_path=output_directory)

print(f'Video downloaded in the highest resolution available and saved to {output_directory} successfully!')
