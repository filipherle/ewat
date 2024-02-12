from PIL import Image
from appearance.hue import *
import pathlib
import os
import errno
def run_strip_metadata():
    print (info("Please enter the full path of the image you want to strip metadata from. eg. /home/xx/Desktop/example.jpg"))
    image_filename = input(que("Image: "))
    path = pathlib.Path(image)
    if path.exists() != True:
        print (bad("Image does not exist! Exiting..."))
        return
    image_file = open(image_filename)
    image = Image.open(image_file)
    print (info("Enter a name + file extension for the new CLEAN image to be saved as. eg. example.jpg"))
    print (info("I recommend keeping the file extension the same for the image, or the file may get corrupted."))
    new_image = raw_input(que("New Image name: "))
    try:
        image_data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(image_data)
        try:
            os.makedirs("output")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        image_without_exif.save(u"{}".format("output/" + new_image))
        print (good("Image saved into output/" + new_image))
    except Exception as e:
        print ("Error!")
        print (e)
        return
