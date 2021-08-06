#! /bin/bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --ignore-glob=service_1/tests/test_int.py --cov --cov-config=.coveragerc

python3 -m pytest 