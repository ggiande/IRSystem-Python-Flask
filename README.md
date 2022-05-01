# Advanced Object-Oriented Programming
This Python Application uses the Kivy framework for the 
graphical user interface. This application can take text 
as an input from the end user and retrieve relevant documents
to the text.

## Set Up
This application requires the following requirements to be met
before expecting a successful launch. 

### Windows
Make sure to run PyCharm using Administrator. To set up your terminal and pip, run the following command at least one time.
`python -m pip install --upgrade pip setuptools virtualenv`

Create a virtual environment named kivy_venv in your current directory only one time:
`python -m virtualenv kivy_venv`

Activate the virtual environment. You will have to do this step from the current directory every time you start a new terminal. This sets up the environment so the new kivy_venv Python is used.

For Windows default CMD, in the command line do:
`kivy_venv\Scripts\activate`

If you are in a bash terminal on Windows, instead do:
`source kivy_venv/Scripts/activate`



### OSX 
Note that the following instructions
are only for OSX. For other operating systems, read the documentation
provided by the [Kivy Docs](https://kivy.org/doc/stable/gettingstarted/installation.html).
There are multiple ways to `install` kivy, explore your best option.

To install the Kivy virtualenv, you must:

Open the dmg

In the GUI copy the Kivy.app to /Applications by dragging the folder icon to the right.

Optionally create a symlink by running the following command:

``ln -s /Applications/Kivy.app/Contents/Resources/script /usr/local/bin/kivy``
This creates the kivy binary that you can use instead of python to run scripts. I.e. instead of doing python my_script.py or python -m pip install <module name>, write kivy my_script.py or kivy -m pip install <module name> to run it using the kivy bundled Python interpreter with the kivy environment.

As opposed to activating the virtualenv below, running with kivy will use the virtualenv but also properly configure the script environment required to run a Kivy app (i.e. setting kivy’s home path etc.).
Using the App Virtual environment¶
The path to the underlying virtualenv is /Applications/Kivy.app/Contents/Resources/venv. To activate it so you can use python, like any normal virtualenv, do:
```
pushd /Applications/Kivy.app/Contents/Resources/venv/bin
source activate
source kivy_activate
popd
```
On the default mac (zsh) shell you must be in the bin directory containing activate to be able to activate the virtualenv, hence why we changed the directory temporarily.

kivy_activate sets up the environment to be able to run Kivy, by setting the kivy home, gstreamer, and other variables.

Start this particular Kivy Application by running, `python3 main.py` after pasting the venv codeblock.

After running the application, you should see the following:
![Kivy Application Launched](https://i.imgur.com/yS8FWOO.png)
