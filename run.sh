#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

#branch_name=$(git symbolic-ref -q HEAD)
#branch_name=${branch_name##refs/heads/}
#branch_name=${branch_name:-HEAD}

export FLASK_APP=hello.py
#export FLASK_ENV=$branch_name

flask run