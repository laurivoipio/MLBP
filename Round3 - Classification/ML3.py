from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# im = Image.open("images/image_"+srt(i)+".jpg");

# Determine the size of the image
#width, height = im.size;
#print('width: %d, height: %d' % (width, height))
       

# Convert the image to RGB
#rgb_im = im.convert('RGB');

# Determine the rgb values of the pixel at location (row,col) where both row and col are 0
#pixel = rgb_im.getpixel((0,0))
#print('Pixel (R, G, B): (%d, %d, %d)' % (pixel[0], pixel[1], pixel[2]))
i = 1
images = []
grass_images = []
while i < 56:
    # Read in an image from a jpg-file and store it in the variable im
    im = Image.open("images/image_"+str(i)+".jpg")

    # Determine the size of the image
    width, height = im.size
    rgb_im = im.convert('RGB')
    reds = 0
    greens = 0
    blues = 0
    img_size = (width*height)
    for x in range(width):
        for y in range(height):
            pixel = rgb_im.getpixel((x,y))
            reds += pixel[0]
            greens +=pixel[1]
            blues += pixel[2]
            #works also as
            #blues.append(pixel[2])
    avg_reds = reds/img_size
    avg_greens = greens/img_size
    avg_blues = blues/img_size
    images.append((avg_reds,avg_greens,avg_blues))

    if i < 21:
        grass_images.append(1)
    else:
        grass_images.append(0)
    i += 1
images_as_nparray = np.array(images)
print(grass_images)
print(sum(grass_images))
print(len(grass_images))
print(grass_images[0:20])
print(grass_images[20:])
print(len(grass_images[20:]))
#print(reds, greens, blues)
#print(avg_reds, avg_greens, avg_blues)
#print(images)

#def Visualize_data(X,y):

    # indx_1 = np.where(y == 1) # for grass.
    # indx_2 = np.where(y == 0) # for non-grass.
    
    # Set figure size (width, height)
fig, axes = plt.subplots(1, 3,figsize=(15, 5))
# PLOT GREENNESS AGAINST REDNESS
#Make a scatterplot of the average greenness vs redness. 
#Indicate Grass images by a cross, and others by a dot.

### STUDENT TASK ###
axes[0].scatter(images_as_nparray[0:20,1],images_as_nparray[0:20,0], c='g', marker ='x', label='Grass')
axes[0].scatter(images_as_nparray[20:,1],images_as_nparray[20:,0], c='r', marker ='o', label='Soil+Tiles')
# plt.show()
# YOUR CODE HERE
#raise NotImplementedError()
axes[0].set_xlabel('Greenness of Images')
axes[0].set_ylabel('Redness of Images')
axes[0].legend()
axes[0].set_title(r'$\bf{Figure\ 1.}$Green vs Red')

# PLOT GREENNESS AGAINST BLUENESS
#The same as above but now greenness vs blueness.
### STUDENT TASK ###
#axes[1].scatter(..., ..., c='g', marker ='x', label='Grass')
#axes[1].scatter(..., ..., c='b', marker ='o', label='Soil+Tiles')
axes[1].scatter(images_as_nparray[0:20,1],images_as_nparray[0:20,2], c='g', marker ='x', label='Grass')
axes[1].scatter(images_as_nparray[20:,1],images_as_nparray[20:,2], c='r', marker ='o', label='Soil+Tiles')
# YOUR CODE HERE
#raise NotImplementedError()
axes[1].set_xlabel('Greenness of Images')
axes[1].set_ylabel('Blueness of Images')
axes[1].legend()
axes[1].set_title(r'$\bf{Figure\ 2.}$Green vs Blue')

# PLOT REDNESS AGAINST BLUENESS
#The same as above but now redness vs blueness.
### STUDENT TASK ###
#axes[2].scatter(..., ..., c='r', marker ='x', label='Grass')
#axes[2].scatter(..., ..., c='b', marker ='o', label='Soil+Tiles')
axes[2].scatter(images_as_nparray[0:20,0],images_as_nparray[0:20,2], c='g', marker ='x', label='Grass')
axes[2].scatter(images_as_nparray[20:,0],images_as_nparray[20:,2], c='r', marker ='o', label='Soil+Tiles')
# YOUR CODE HERE
#raise NotImplementedError()
axes[2].set_xlabel('Redness of Images')
axes[2].set_ylabel('Blueness of Images')
axes[2].legend()
axes[2].set_title(r'$\bf{Figure\ 3.}$Red vs Blue')
plt.tight_layout()
plt.show()
#return axes

def sigmoid_func(z):
    ### STUDENT TASK ###
    sigmoid = 1/(1+np.exp(-z))
    #raise NotImplementedError()
    return sigmoid

def gradient(X,y,w):
    ### STUDENT TASK ###
    grad = []
    grad = np.dot(X, -(y-sigmoid_func(np.dot(X,w))))
    # YOUR CODE HERE
    raise NotImplementedError()
    return grad

answ = sigmoid_func(0.458)
print(answ)