def write_line_infile(text):
    f = open("test.txt", "a")
    f.write(text)
    f.close

def read_file():
    f=open("test.txt","r")
    content=f.read()
    print(content)

write_line_infile("hello")
read_file()