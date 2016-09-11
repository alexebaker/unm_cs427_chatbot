# UNM CS 427 ChatBot

Chatbot for CS 427

## Usage

1. Install pre-requisets

```bash
sudo apt-get install python-pip
pip install virtualenv
```

2. Setup the virtual environment.

```bash
./init-venv.sh
```

3. Activate the virtual env in your current shell

```bash
source .venv/bin/activate
```

4. run sickbot.py

```bash
python sickbot.py
```

## Description

The next part of the assignment is to turn your design into a chatbot. You should use three primary matching tools:

* Direct matching -- these are exact phrase matching and having a canned response returned.

* Partial matching -- these look for key phrases and return a response that is related to the input phrase.

* Stochasticity -- this randomly changes the response that is returned with some probability.

The development can be language independent, but it must run on our CS department systems or must be installed at a romote site
that the TA/Instructor can interact with your program.

You must turn in the following items (1-3 in .zip file email to TA/instructor as a team and 4 upload to Learn, individually):

1. Source code for your chatbot including database files for your knowledge base

2. A README file that includes either:

    * Instructions on how to run (execute) your program on the CS department systems

    **or**

    * Instructions how to connect to your remote site to execute your program

3. A text file named Output.txt showing you testing your program.

4. Upload to learn a text file explaining the breakdown of the work done by the team.

## Authors

* [David Sledge] (mailto:sledged@gmail.com)

* [Alex Baker] (mailto:alexebaker@unm.edu)
