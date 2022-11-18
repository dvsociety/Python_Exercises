from PIL import Image
import os 

downloads_folder = "/home/vsociety/Downloads/"
pictures_folder = "/home/vsociety/Pictures/"
music_folder = "/home/vsociety/Music/"
video_folder =  "/home/vsociety/Videos/"

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename) 

        if extension in [".jpg", "jpeg", ".png"]:
            picture = Image.open(downloads_folder + filename)
            picture.save(downloads_folder + "compressed_" + filename, optimize=True, quality=60)
