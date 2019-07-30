# integral-visualizer

# How to run Integral Visualizer locally (Windows)

# Intstallation
1. Download the zip file on from GitHub
2. Unzip, and put the folder in the directory of your choosing
3. Install the latest version of python, including pip
4. open terminal and type in "pip install virtualenvwrapper-win"
5. in that same terminal window, type in "mkvirtualenv py1"
6. in that same terminal window, type in "workon py1"
7. in that same terminal window, type in "pip install django"
9. in a DIFFERENT terminal window, type in "workon py1"
8. in that same terminal window, type in "pip install numpy"
9. in that same terminal window, type in "pip install matplotlib"

# Running the code
1. in a terminal window, type in "workon py1"
12. cd into where the project is located until you can find the file "manage.py"
13. type in "python manage.py runserver" once you are in the same directory as the file "manage.py"
14. copy the url given in the terminal to your browser




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

To run server again after everything has been installed, follow steps 5, 8, 13-15

heroku stuff for mark:

python manage.py collectstatic

git status
git add --all
git commit -m ""
git push heroku master