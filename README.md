# Advanced OOP - Flask Application
This Python Application uses Python's Flask Library as a backend for a NextJS Application. This application can take text 
as an input from the end user and retrieve relevant documents, frequencies, and word snippets.

## Set Up
This application requires the following requirements to be met
before expecting a successful launch. 

* Python 3.7+
* Python 3.9.12
* Flask 2.1.2

### Windows
Make sure to run PyCharm using Administrator. To set up your terminal and pip, run the following command at least one time.
`python -m pip install --upgrade pip setuptools virtualenv`

Create a virtual environment named kivy_venv in your current directory only one time:
`> py -3 -m venv venv`

Activate the virtual environment.
`> venv\Scripts\activate`

### OSX 
Note that the following instructions are only for OSX. 
```bash
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```
Activate the virtual environment.
`$ . venv/bin/activate`

Start this particular Flask App by running, `python3 main.py` after pasting the venv codeblock.

Start Flask by clicking the run button in main().

## Future Optimizations
- [ ] A more advanced word_search for substrings using dijkstra's algorithm, substrings
- [ ] Refactor Result object to ResultEncoder using JSON library
- [ ] Revisit unit tests
- [ ] Implement for list comprehensions
- [ ] Refactor all packages

