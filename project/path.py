import os

cwd = os.getcwd()
print(cwd)
MNIST_path = os.path.join(cwd, 'MNIST_DS')
print(MNIST_path)
classes = os.listdir(MNIST_path)
print(classes)
for c in classes:
    images_path = os.path.join(MNIST_path, c)
    image_files = os.listdir(images_path)
    print(image_files)
