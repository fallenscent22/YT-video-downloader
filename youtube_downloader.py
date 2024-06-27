from pytube import YouTube
from sys import argv

link=argv[1]
yt=YouTube(link)

streams = yt.streams.filter(progressive=True)
print("Available resolutions:")
for i, stream in enumerate(streams):
    print(f"{i}. {stream.resolution}")

# Prompt the user to select a resolution
stream_index = int(input("Enter the index of the resolution you want to download: "))
selected_stream = streams[stream_index]

# Download the selected stream
output_path = 'C:\\Users\\Nikhitha Chatla\\OneDrive\\Desktop'
selected_stream.download(output_path)
print(f"Downloaded: {yt.title} in {selected_stream.resolution} resolution to {output_path}")
