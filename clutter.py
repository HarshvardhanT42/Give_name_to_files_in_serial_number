import os

files = os.listdir("meargpdf") # enter the  path to your directory here

i = 1
for file in files:
    if file.endswith(".pdf"): # enter  the file extension here

        print(file)
        os.rename(f"meargpdf/{file}",f"meargpdf/{i}.pdf") #enter  the path to your directory here to change the name of your files in to the seriel number

        i = i + 1