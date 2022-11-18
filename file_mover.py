import os 

downloads_folder = "/home/vsociety/Downloads/"

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename) 

        if extension in [".jpg", "jpeg", ".png"]:
            pictures_folder = "/home/vsociety/Pictures/"
            os.rename(downloads_folder + filename, pictures_folder + filename)

        if extension in [".mp3"]:
            music_folder = "/home/vsociety/Music/"
            os.rename(downloads_folder + filename, music_folder + filename)

        if extension in [".mp4", ".flv", ".avi"]:
            video_folder =  "/home/vsociety/Videos/"
            os.rename(downloads_folder + filename, video_folder + filename)
