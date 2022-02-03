# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
# Using with is also much shorter than writing equivalent try-finally blocks:


def read(file_name):
    with open(file_name, 'r') as cf:
        read_data = cf.read()
        print(read_data)


def write(file_name, message):
    with open(file_name, 'a+') as tf:
        tf.write(message)

# read('test.txt')
write("test3.txt","Hello World")