# This text is describing the command below it. Don't type it.
$ this is a shell command, type it

installation steps
-----------------

# open the terminal 
# open the AutoScrapper_project folder in terminal

# install python-pip
$ sudo apt-get install python-pip

# install virtualenv and virtualenvwrapper
$ sudo pip install virtualenv virtualenvwrapper

# edit the .bashrc file
$ vim .bashrc

# to enable virtualenvwrapper add this line to the end of the file
source /usr/local/bin/virtualenvwrapper.sh
#save and quit your editor

# create a virtualenv, I usually give it the same name as my app
$ mkvirtualenv autoscrapper

# The virtualenv will be activated automatically.
# You can deactivate it like this
$ deactivate

# to activate a virtualenv, or change which one is active, do this
$ workon autoscrapper

# install the requirements
$ pip install requirements.txt

# cd into autoscrapper folder
$ cd autoscrapper

# make manage.py executable
$ chmod +x manage.py

# to create database tables and to create a super user
$ ./manage.py syncdb

# start the dev server
$ ./manage.py runserver

-------------------------------------------

open browser

visit this address
http://127.0.0.1:8000/
