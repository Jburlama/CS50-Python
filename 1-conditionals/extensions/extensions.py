file = input("File name: ")
file = file.strip()
file = file.lower()

if (file.endswith(".gif")):
    print("image/gif")
elif (file.endswith(".jpg")):
    print("image/jpeg")
elif (file.endswith(".jpeg")):
    print("image/jpeg")
elif (file.endswith(".png")):
    print("image/png")
elif (file.endswith(".txt")):
    print("text/plain")
elif (file.endswith(".pdf")):
    print("application/pdf")
elif (file.endswith(".zip")):
    print("application/zip")
elif (file.endswith(".bin")):
    print("application/octet-stream")
elif (file.find(".")):
    print("application/octet-stream")
else:
    print("application/pdf")
