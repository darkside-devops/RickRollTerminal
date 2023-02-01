import moviepy.editor as mp
import numpy as np
import subprocess

# Load the video file
video = mp.VideoFileClip("Rick roll.mp4")

# Extract the audio and play it in the background
subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "-i", "Rick roll.mp4"])

# Loop through each frame in the video
for frame in video.iter_frames(fps=24):
    # Convert the frame to grayscale
    gray = np.dot(frame, [0.2989, 0.5870, 0.1140])

    # Normalize the grayscale values to be between 0 and 255
    gray = gray.astype(np.uint8)

    # Loop through each row in the frame
    for row in gray:
        # Loop through each pixel in the row
        for pixel in row:
            # Map the grayscale value to ASCII characters
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

            # Print the ASCII character to the console
            print(character, end="")
        print()
