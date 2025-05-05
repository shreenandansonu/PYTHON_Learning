from pytube import Playlist, YouTube

# Replace this with your playlist link
playlist_url = input("Enter YouTube playlist URL: ")

try:
    playlist = Playlist(playlist_url)
    print(f"Fetching videos from playlist: {playlist.title}")

    with open("links.txt", "w") as file:
        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                if stream:
                    file.write(stream.url + "\n")
                    print(f"✔ Fetched: {yt.title}")
                else:
                    print(f"✖ No stream found for: {yt.title}")
            except Exception as e:
                print(f"Error processing video: {video_url}\n{e}")

    print("✅ All links saved to links.txt")

except Exception as e:
    print(f"Failed to fetch playlist: {e}")
