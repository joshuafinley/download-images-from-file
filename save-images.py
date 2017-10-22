# Created by Joshua Finley
# Note this only works if there is 1 .jpg URL on each file

import urllib.request
import urllib.error
import sys
import os.path

if len(sys.argv) < 2:
    print("Error: Missing file argument.")
    print("Usage: \"python3 save-images.py URLS-FILENAME\"")
    exit()

file_name = sys.argv[1]
if os.path.isfile(file_name) is False:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("USAGE: \npython3 save-images.py URLS-FILENAME")
    else:
        print("Error finding file named: \"{0}\"".format(file_name))
    exit()

# Open the file
with open(file_name, "r") as f:
    found_image = False
    # Counter for the line counting
    i = 0
    image_num = 0
    for line in f:
        i += 1
        # Checks for the strings "http" and ".jpg" on each line
        line_lower = line.lower()
        http_index = line_lower.find("http")
        jpg_index = line_lower.find(".jpg")

        # If both indices exist
        if http_index != -1 and jpg_index != -1:
            # Increment image number
            image_num += 1
            print("Found http and .jpg in line:{0}".format(i))
            # Slice line between http and the end of .jpg
            url = line[http_index:jpg_index + 4]
            print("Retrieving image from url: {0}".format(url))
            # Download the image with image number
            try:
                urllib.request.urlretrieve(url, str(image_num) + "-image.jpg")
            except urllib.error.HTTPError as err:
                print(err)
                print("Unable to retrieve image from: {0}".format(url))
            if found_image is False:
                found_image = True

    if found_image is False:
        print("Error: Could not find any .jpg urls in given file")
    else:
        print("Completed! Downloaded a total of {0} images".format(image_num))
