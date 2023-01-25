#!/usr/bin/python
# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

# Declare important program variables
prog_nm="CompressorWiz"
prog_ver="0.1alpha"

# Import front-end framework
import tkinter as gui
from tkinter.filedialog import askopenfilename
# Import "zipfile" module from python
import zipfile
# import package os
import os

filesrc=""
filenm=""
zipnm=""

def file_browser(event=None):
    global filesrc, filenm, zipnm
    filesrc = askopenfilename()
    filenm = filesrc.split('/')[len(filesrc.split('/'))-1]
    zipnm = os.path.splitext(filenm)[0]+".zip"

# compress_file definition/function
def compress_file(filesrc):
    # Initialize the compression parameters
    with zipfile.ZipFile(zipnm, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
        # Compress based on the file name provided
        zip.write(filesrc, arcname=filenm)
        # display original file size definition/function
        def display_filesize(filesrc):
            ogfilesize = (os.path.getsize(filesrc)) / 1024
            ogfilesize = round(ogfilesize, 2)
            ogfile = str(ogfilesize)
            return ogfile
        # display compressed file size definition/function
        def display_compressedfilesize(zipnm):
            compfilesize = (os.path.getsize(zipnm)) / 1024
            compfilesize = round(compfilesize, 2)
            compfile = str(compfilesize)
            return compfile
    ogfile = display_filesize(filenm)
    compfile = display_compressedfilesize(zipnm)
    label_sz.configure(text="Original file size is " + ogfile + "Kb" + "\n\n Compressed file size is "+compfile+"Kb.")

# decompress_file definition/function
def decompress_file():
    # Initialize the decompression parameters
    with zipfile.ZipFile(zipnm, 'r') as zip:
        # Decompress the file name provided to a folder named "extracted"
        zip.extractall(path="extracted")

window = gui.Tk()
window.title(prog_nm+"-("+prog_ver+")")
header = gui.Label(window, text=prog_nm+"-"+prog_ver, height=5, font="Helvetica 20 bold")
header.pack()
button_browse=gui.Button(window, text="File", command=file_browser)
button_browse.pack()
button_compress = gui.Button(window, text = "Compress", command = lambda: compress_file(filesrc))
button_compress.pack()
button_decompress= gui.Button(window, text = "Decompress", command=decompress_file)
button_decompress.pack()
label_sz = gui.Label(window, text = "No file selected.", width = 100, height = 4, fg = "blue")
label_sz.pack()

exit_button = gui.Button(window, text='Exit', command=window.destroy)
exit_button.pack()
window.mainloop()

#compress_file("testfile.txt")
#decompress_file("test.zip")
