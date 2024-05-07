# image-hider

An easy-to-use steganography tool.

## Features

- Support of image file formats png, jpg, jpeg and tiff
- Hiding text in image
- Encryption of the text to be hidden in the image

## Installation

That's quite easy. Just go to the Releases section and get the `.exe` file!

## Building from source

It is recommended to create a virtual environment for this.

The project requirements are listed in `requirements.txt`

- Clone the repo using the url in the Code section of GitHub.
- Run `pip install -r requirements.txt`
- This installs the necessary packages
- Now everything is ready for build
- Editing the file adhering to the [MIT License](https://github.com/agnivomallick/image-hider/blob/main/LICENSE)
- Just open the file and run it
- Make sure no errors. If there is a package error, for example `base64` then you can do `pip install pybase64`
- You can download the zip file of UPX and extract it to some dir.
- If you don't want then remove the --upx-dir option from the pyinstaller command.
- Then stop the app and install pyinstaller `pip install pyinstaller`
- If you want a more GUI-based one then I suggest you use auto-py-to-exe. So, run `pip install auto-py-to-exe`
- Now on using command-line pyinstaller use this command:
`pyinstaller --noconfirm --onedir --windowed --icon "<your-icon-file-path>" --name "imghider" --upx-dir "<upx directory>" --version-file "<version file in repo (the yaml file)>" --add-data "<find ui_imagehider.py file in repo and link here>;." --add-data "<icon path>;."  "<the main file (imagehider.py) in the repo>"`
Accordingly, replace the <> following the specific instructions.
- On using auto-py-to-exe its fully customizable
- Use your own options.
- Make sure to select these options - its required.
- No.1 Select Onedir (package in one directory)
- No.2 Select Windowed in the Console Window option
- No.3 The icon will be linked to the icon file in the repo or using your own icon if you want
- No.4 The other files are as follows: link the `ui_imagehider.py` and `logo.ico`. Add in the additional files section
- No.5 In the Advanced section in Windows-specific options (if you use Windows) link the version file to the yaml file in the repo dir.
- No.6 If you use UPX then make sure to add it in UPX dir option.
- Tip: The name in Advanced section specifies the name of the result exe
- Tip: You can change the output dir in Settings section, Output directory option
- Then click Convert py to exe

## Packages and Tools Used

For editing this I used JetBrains' PyCharm Community Edition
Lots of debugging I could do because of this Python-themed IDE.

### Python Packages

The C++ toolkit Qt for the great GUI and management.
I used Qt 6.6.0.
The UI base was created using the Qt tool Qt Designer.

For steganography, I used the stegano python package.
Its very easy-to-use and has docs.

For encryption feature I used the base64, or rather the python package pybase64.
Again, easy to use.

Then the built-in python os module
A small part was required from it, but it served great purpose.

For display of my window icon in taskbar also used the built-in python module ctypes.
This contains C data types. I needed only the windll part (works only on Windows.)

Lastly I used the pyinstaller_versionfile package.
It created the version.yaml file for me when running.
Very easy, with just a function.

## Licensing
This project is licensed under the terms of the [MIT License](https://github.com/agnivomallick/image-hider/blob/main/LICENSE)

