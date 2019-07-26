# integral-visualizer

# How to run Integral Visualizer locally (Windows)

1. Download the zip file on from GitHub
2. Unzip, and put the folder in the directory of your choosing
3. Install the latest version of python, including pip
4. open terminal and type in "pip install virtualenvwrapper-win"
5. in that same terminal window, type in "mkvirtualenv py1"
6. in that same terminal window, type in "workon py1"
7. in that same terminal window, type in "pip install django"
8. in a different terminal window, type in "pip install numpy"
9. in that same terminal window, type in "pip install matplotlib"
10. once django is installed, open the folder in your prefered text editor
11. in your original terminal window, cd into where the project is located until you can find the file "manage.py"
12. type in "python manage.py runserver" once you are in the same directory as the file "manage.py"
13. copy the url given in the terminal to your browser




# How to run Integral Visualizer locally (Mac OS)

1. Download the zip file on from GitHub
2. Unzip, and put the folder in the directory of your choosing
3. Install the latest version of python, including pip
4. In terminal do the following commands (steps 5-14) :
5. cd “folder directory where code is located”
6. pip install virtualenv
7. virtualenv -p python3 .
8. source bin/activate
9. pip install django
10. pip install numpy
11. pip install matplotlib
12. pip install Pillow
13. cd src
14. python manage.py runserver
15. Copy the given url into your browser


NOTE:
If you get the FileNotFoundError on Mac OS, follow these steps:
1. Open riemman.py in a text editor
2. Go to where ‘epic_path’ is defined
3. Change all of: this: '\\' to this: '/'
