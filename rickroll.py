import moviepy.editor as mp
import numpy as np
import subprocess

# Created by Aptify!

video = mp.VideoFileClip("video.mp4")

subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "-i", "video.mp4"])

for frame in video.iter_frames(fps=24):
    gray = np.dot(frame, [0.2989, 0.5870, 0.1140])
    gray = gray.astype(np.uint8)
    for row in gray:
        for pixel in row:
            if pixel > 240:
                character = " "
            elif pixel > 200:
                character = "."
            elif pixel > 160:
                character = "*"
            elif pixel > 120:
                character = "+"
            elif pixel > 80:
                character = "#"
            else:
                character = "@"

            print(character, end="")
        print()
