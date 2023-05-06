# -*- coding: utf-8 -*-
"""UTS PSM - Image Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jMpeJ_c_uXJXai4zPuD-olwim1ASgTMm

## Digital Certificate Generator - Image Manipulation

### Install Required Packages
"""

# pip install matplotlib pillow numpy

"""### Import the packages"""

from matplotlib import image
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageColor
import numpy as np
import os

"""### Check Required Files and Directories"""

# Check template
if os.path.isfile("template.png"):
  print("✅ Template exist.")
else:
  print("🚩 Template doesn't exist.")

# Check Font
if os.path.isfile("Montserrat-Bold.otf"):
  print("✅ Font exist.")
else:
  print(" 🚩 Font doesn't exist.")

# Check Output Directory
if os.path.isdir("output"):
  print("✅ Output directory exist.")
else:
  os.mkdir("./output")
  print(" 🚩 Output Directory doesn't exist.")

"""### Preparing image

please upload your image to the session storage and rename the file to 'template.png'
"""

filename = 'template.png'
data = image.imread(filename)
plt.imshow(data)
plt.show()

"""### Selecting Coordinate for the name"""

x = 0
y = 0

x = int(input("Enter the coordinate for the x-axis (horizontal): "))
y = int(input("Enter the coordinate for the y-axis (vertical): "))

plt.plot(x, y, marker="v", color="black")
plt.imshow(data)
plt.show()

"""### Result"""

names = []
n = 0

def generate(names):
  for name in names:
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Montserrat-Bold.otf', 48)
    draw.text((x, y), name, font=font, fill='#F62B41')
    img.show()
    print("\n")
    # img.save("output/"+name+".png")
    img.save("output/"+name+".png", optimize = True, quality = 95)
  print("Image saved in ./output")

def inputName():
  n = int(input("How many certificate would you like to generate? "))
  for i in range(n):
    temp = input("Enter the name for the entry ["+str(i+1)+ "]: ")
    names.append(temp)

inputName()
generate(names)

# """### Compressing with K-Means Clustering (Experimental)"""

# def initialize_K_centroids(X, K):
#     """ Choose K points from X at random """
#     m = len(X)
#     return X[np.random.choice(m, K, replace=False), :]

# def find_closest_centroids(X, centroids):
#     m = len(X)
#     c = np.zeros(m)
#     for i in range(m):
#         # Find distances
#         distances = np.linalg.norm(X[i] - centroids, axis=1)

#         # Assign closest cluster to c[i]
#         c[i] = np.argmin(distances)

#     return c

# def compute_means(X, idx, K):
#     _, n = X.shape
#     centroids = np.zeros((K, n))
#     for k in range(K):
#         examples = X[np.where(idx == k)]
#         mean = [np.mean(column) for column in examples.T]
#         centroids[k] = mean
#     return centroids

# def find_k_means(X, K, max_iters=10):
#     centroids = initialize_K_centroids(X, K)
#     previous_centroids = centroids
#     for _ in range(max_iters):
#         idx = find_closest_centroids(X, centroids)
#         centroids = compute_means(X, idx, K)
#         if (centroids == previous_centroids).all():
#             # The centroids aren't moving anymore.
#             return centroids
#         else:
#             previous_centroids = centroids

#     return centroids, idx

# def load_image(path):
#     """ Load image from path. Return a numpy array """
#     image = Image.open(path)
#     return np.asarray(image) / 255

# try:
#     image_path = './output/Monkey D Garp.png'
#     assert os.path.isfile(image_path)
# except (IndexError, AssertionError):
#     print('Please specify an image')

# image = load_image(image_path)
# w, h, d = image.shape
# print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))
# X = image.reshape((w * h, d))
# K = 20 # the desired number of colors in the compressed image
# colors, _ = find_k_means(X, K, max_iters=20)
# idx = find_closest_centroids(X, colors)
# idx = np.array(idx, dtype=np.uint8)
# X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
# compressed_image = Image.fromarray(X_reconstructed)
# compressed_image.save('out.png')

# img = Image.open('./output/Monkey D Garp.png')
# cimg = Image.open('./out.png')
# img.show()
# print("\n")
# cimg.show()

# """### Singular Value Decomposition"""

# # Commented out IPython magic to ensure Python compatibility.
# # %matplotlib inline
# import matplotlib.pyplot as plt
# import numpy as np
# import time

# from PIL import Image

# img = Image.open('./output/Garp.png')
# imggray = img.convert('LA')
# # imggray = img
# plt.figure(figsize=(9, 6))
# plt.imshow(imggray)

# imgmat = np.array(list(imggray.getdata(band=0)), float)
# imgmat.shape = (imggray.size[1], imggray.size[0])
# imgmat = np.matrix(imgmat)
# plt.figure(figsize=(9,6))
# plt.imshow(imgmat, cmap='gray');

# U, sigma, V = np.linalg.svd(imgmat)

# reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
# plt.imshow(reconstimg, cmap='gray');

# for i in range(2, 4):
#     reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
#     plt.imshow(reconstimg, cmap='gray')
#     title = "n = %s" % i
#     plt.title(title)
#     plt.show()

# for i in range(5, 51, 5):
#     reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
#     plt.imshow(reconstimg, cmap='gray')
#     title = "n = %s" % i
#     plt.title(title)
#     plt.show()

# """### Compressing and Resizing using PIL"""

# import os
# from PIL import Image

# def get_size_format(b, factor=1024, suffix="B"):
#     """
#     Scale bytes to its proper byte format
#     e.g:
#         1253656 => '1.20MB'
#         1253656678 => '1.17GB'
#     """
#     for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
#         if b < factor:
#             return f"{b:.2f}{unit}{suffix}"
#         b /= factor
#     return f"{b:.2f}Y{suffix}"

# def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
#     # load the image to memory
#     img = Image.open(image_name)
#     # print the original image shape
#     print("[*] Image shape:", img.size)
#     # get the original image size in bytes
#     image_size = os.path.getsize(image_name)
#     # print the size before compression/resizing
#     print("[*] Size before compression:", get_size_format(image_size))
#     if new_size_ratio < 1.0:
#         # if resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
#         img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)
#         # print new image shape
#         print("[+] New Image shape:", img.size)
#     elif width and height:
#         # if width and height are set, resize with them instead
#         img = img.resize((width, height), Image.ANTIALIAS)
#         # print new image shape
#         print("[+] New Image shape:", img.size)
#     # split the filename and extension
#     filename, ext = os.path.splitext(image_name)
#     # make new filename appending _compressed to the original file name
#     if to_jpg:
#         # change the extension to JPEG
#         new_filename = f"{filename}_compressed.jpg"
#     else:
#         # retain the same extension of the original image
#         new_filename = f"{filename}_compressed{ext}"
#     try:
#         # save the image with the corresponding quality and optimize set to True
#         img.save(new_filename, quality=quality, optimize=True)
#     except OSError:
#         # convert the image to RGB mode first
#         img = img.convert("RGB")
#         # save the image with the corresponding quality and optimize set to True
#         img.save(new_filename, quality=quality, optimize=True)
#     print("[+] New file saved:", new_filename)
#     # get the new image size in bytes
#     new_image_size = os.path.getsize(new_filename)
#     # print the new size in a good format
#     print("[+] Size after compression:", get_size_format(new_image_size))
#     # calculate the saving bytes
#     saving_diff = new_image_size - image_size
#     # print the saving percentage
#     print(f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")

# compress_img('./output/Garp.png', 1.0, 90, 1080, 763, False)