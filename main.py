import cv2
import os

# Set the video path and output folder
video_path = r"C:\Users\ADMIN\Desktop\TMRT\task1vid1.mp4"    #Replace with your video file
output_folder = 'fish_frames2'                  #Folder to save frames
frame_interval = 5                        #Extract every 5th frame

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
vid = cv2.VideoCapture(video_path)
frame_count = 0

# Loop through the video
while True:
    ret, frame = vid.read()
    if not ret:
        break

    # Save every 20th frame
    if frame_count % 40 == 0:
        filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    frame_count += 1

# Cleanup
vid.release()
print("Frame extraction complete.")
