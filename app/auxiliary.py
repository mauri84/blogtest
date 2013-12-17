from PIL import Image
import requests
from StringIO import StringIO
from flask import send_file
import time
from app import app

#---------------------------------
# Helper functions.
#---------------------------------

def ratio(height, width):
    ratio = float(width) / float(height)
    return ratio

def sanatize(value):
    #Make sure people don't crash the server with huge image sizes.
    value = int(value)
    if value > 400:
        value = 400
    return value

def measurements(image, width=None, height=None):
    #Get the current image size.
    (current_width, current_height) = image.size
    ratio = float(current_width) / float(current_height)

    #If nothing is passed in, set the width.
    if not width and not height:
        width = 300

    #If only the width passed in, calculate new height
    if width:
        width  = sanatize(width)
        height = int(width / ratio)

    #If only the height passed in, calculate new width
    if height:
        height = sanatize(height)
        width = int(height * ratio)

    return (width, height)

def image(url, name):
    #Download the image.
    #print type(url)
    #print url
    split =url.split('.')
    #print split
    #print split[-1]
    filename = name+time.strftime("%Y%m%d%s")
    path = app.config['UPLOAD_FOLDER']+'/'+ filename
    response = requests.get(url)
    extension = split[-1].upper()
    if extension != 'GIF':
        #print 'save as a image'
        #Open the image
        image = Image.open(StringIO(response.content))
        #Calculate the desired height and width of the image
        desired_width, desired_height = measurements(image)
        buffer_image = StringIO()
        #print "Number is", desired_width, desired_height
        resized_image = image.resize((desired_width, desired_height), Image.ANTIALIAS)
        resized_image.save(path, image.format, quality=90)
    else:
        #print 'save as a gif'
        f = open(path+'.gif', 'w')
        f.write(response.content)
        f.close()
        filename = filename+'.gif'    
    return filename

