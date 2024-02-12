#!/bin/python
import os
import pathlib
import sys
#from PIL import Image
#from PIL.ExifTags import TAGS
from GPSPhoto import gpsphoto
import exifread
from appearance.hue import *

'''
print "Extra PIL data that's not needed."
for (tag,value) in Image.open(image)._getexif().iteritems():
        print '%s = %s' % (TAGS.get(tag), value)
'''
def run_metadata():
    print (info("Input the whole image path. eg. path/to/file.jpg"))
    image = raw_input(que("Image file: "))
    path = pathlib.Path(image)
    if path.exists() != True:
        print (bad("Image does not exist! Exiting..."))
        return

    print(good('Metadata extracted:'))

    with open(image, 'rb') as f:
        exif = exifread.process_file(f)

    for key in sorted(exif.keys()):
        # Modules that are not needed
        if key not in ['JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote']:
            print('%s = %s' % (key, exif[key]))
    else:
        print (bad("No info could be found"))

    if gpsphoto.getGPSData(image):
        print (good("GPS Location found!"))
        gps_info = gpsphoto.getGPSData(image)
        print (gps_info)
    else:
        print (bad("GPS location not found."))
