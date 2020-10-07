import pafy

url = "https://www.youtube.com/watch?v=aHtmcP6Ow7k&list=PLYBRnlwDCyDhQxTF4mgunSaP8XGpgTQDJ&index=3"
video = pafy.new(url)

streams = video.streams

for i in streams:
    print(i)

best = video.getbest()

print(best.resolution, best.extension)

best.download()
print("Video Downloaded Successfully")
