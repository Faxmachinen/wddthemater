# Theme automater for WinDynamicDesktop
This is a script to automate the process of creating a theme for [WinDynamicDesktop](https://github.com/t1m0thyj/WinDynamicDesktop).

## Requirements
You will need Python 3.6 or later.

## How to use

### Folder struture
The root folder contains one or more theme folders, and each theme folder contains a "day" and a "night" folder.
The images are named in alphabetical order and are placed in the "day" and "night" folders.

Here is an example folder structure where SomeFolder is the root folder:

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

The "day" and "night" folders exist just to tell the script how to group the images. During processing, the script will move and rename the images. After a successful run, the structure should look like this:

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
