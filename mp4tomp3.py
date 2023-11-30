# Python code to convert video to audio
import moviepy.editor as mp
import os

answer = "O"

if (os.name == "posix"):
    os.system("clear")
elif (os.name == "nt"):
    os.system("cls")

print("[PYTHON SCRIPT TO TURN MP4 TO MP3]")
print("Before continuing, place your video file inside the mp4s folder.")
print("The audio file will be generated inside the mp3s folder.")
print("---------------------------------")


if (not os.path.isdir("mp4s")):
    dirname = "mp4s"
    os.mkdir(dirname)

if (not os.path.isdir("mp3s")):
    dirname = "mp3s"
    os.makedirs(dirname)


listFiles = input("Do you want to list the mp4 files? (O/N): ")
if (listFiles == "O" or listFiles == "o"):
    if (os.name == "posix"):
        os.system("ls -l mp4s/")
    elif (os.name == "nt"):
        os.system("dir mp4s")
    print("---------------------------------")

while (answer == "O" or answer == "o"):
    videoName = input("Please provide the name of the video file (example : video1.mp4): ")
    audioName = videoName[0:(len(videoName)-4)]

    try :
        if (videoName != ""):
            # Insert Local Video File Path 
            clip = mp.VideoFileClip(r"./mp4s/" + videoName)
            
            # Insert Local Audio File Path
            clip.audio.write_audiofile(r"./mp3s/" + audioName + ".mp3")
    except OSError as e:
        print("File not found! Don't forget to respect capital letters.")

    answer = input("Do you want to format another video file? (O/N): ")
