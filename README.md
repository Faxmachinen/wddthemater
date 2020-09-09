# Theme automater for WinDynamicDesktop
This is a script to automate the process of creating custom themes for [WinDynamicDesktop](https://github.com/t1m0thyj/WinDynamicDesktop).
For detailed information on creating themes, see [Creating custom themes](https://github.com/t1m0thyj/WinDynamicDesktop/wiki/Creating-custom-themes).

## Requirements
You will need [Python](https://www.python.org/) version 3.6 or later.

## How to use

### Folder struture
Before you run the script, you will need to arrange the images you have in a particular folder structure. This folder structure is described below.

The root folder contains one or more theme folders, and each theme folder contains a `day` and a `night` folder with images.
The images are named in alphabetical order according to their chronology, but the actual names don't matter. The `day` folder contains everything from sunrise to sunset, and the `night` folder contains the rest.

> __Important__: Alphabetical ordering means `SomeFile_11.jpg` is ordered before `SomeFile_2.jpg` (but not `SomeFile_02.jpg`).

Here is an example folder structure where `SomeFolder` is the root folder:

* SomeFolder
  * Theme1
    * day
      * 01_sunrise.jpg
      * 02_morning.jpg
      * 03_midday.jpg
      * 04_evening.jpg
      * 05_sunset.jpg
    * night
      * night01.jpg
      * night02.jpg
      * night03.jpg
  * Theme2
    * day
      * ...
    * night
      * ...

The `day` and `night` folders exist just to tell the script how to group the images. During processing, the script will move and rename the images. After a successful run, the structure should look like this:

* SomeFolder
  * Theme1
    * Theme1.json
    * Theme1_1.jpg
    * Theme1_2.jpg
    * Theme1_3.jpg
    * Theme1_4.jpg
    * Theme1_5.jpg
    * Theme1_6.jpg
    * Theme1_7.jpg
    * Theme1_8.jpg
  * Theme2
    * Theme2.json
    * ...

### Running the script
Change the current working directory to the root folder, then run the python script:

```cmd
cd C:\my\root\folder
py -3 C:\path\to\makejson.py
```

### Known issues
The script only recognizes image files with the "JPG" extension.