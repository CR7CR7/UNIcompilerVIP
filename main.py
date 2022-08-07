from pytube import YouTube

link = input("Enter your youtube link here:\n")

you_tube = YouTube(link)

print(f"\nTitle: {you_tube.title}")

print(f"\nFormat: {you_tube.fmt_streams}")

print(f"\nRating: {you_tube.rating}")

print(f"\nViews: {you_tube.views}")

print(f"\nVideo Length: {you_tube.length} seconds")

print(f"\nDescription: {you_tube.description}\n")

print(f"\nAuthor: {you_tube.author}")

video = you_tube.streams.get_highest_resolution()

print("downloading...")

video.download()

print("Download complete!")

