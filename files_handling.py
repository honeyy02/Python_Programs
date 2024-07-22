def write_to_file(filename, content):
    with open(filename,'w') as file:
        file.write(content)
    print("Content added to file: ",filename)  

def read_from_file(filename):
    with open(filename,'r') as file:
        content = file.read() 
        print("Content read from file")
        print(content)

def append_to_file(filename, content):
    with open(filename,'a') as file:
        file.write(content)
    print("Content is appended to file: ",filename)           



if __name__ == "__main__":
    filename = 'example.txt'
    content_to_write = "Hello world! This is program for file handling in python"
    content_to_append = "Appending this text to example file"

    write_to_file(filename,content_to_write)
    read_from_file(filename)
    append_to_file(filename,content_to_append)
    read_from_file(filename)