#A program that will parse the given name of a file to determine what type of file it is.

userinput = input("Please input your file name: ").lower().strip()

x = userinput.endswith(".gif")
if x == True:
    print("image/gif")
    exit()

y = userinput.endswith(".jpg")
if y == True:
    print("image/jpeg")
    exit()

z = userinput.endswith(".jpeg")
if z == True:
    print("image/jpeg")
    exit()

h = userinput.endswith(".png")
if h == True:
    print("image/png")
    exit()

i = userinput.endswith(".pdf")
if i == True:
    print("application/pdf")
    exit()

j = userinput.endswith(".txt")
if j == True:
    print("text/plain")
    exit()

k = userinput.endswith(".zip")
if k == True:
    print("application/zip")
    exit()

else:
    print("application/octet-stream")
