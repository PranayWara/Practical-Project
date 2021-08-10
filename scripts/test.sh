#! /bin/bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest service_1/testing/test_unit_1.py --cov=application --disable-pytest-warnings --cov-config=.coveragerc
python3 -m pytest service_2/testing/test_unit_2.py --cov=app --disable-pytest-warnings --cov-config=.coveragerc --cov-report term-missing
python3 -m pytest service_3/testing/test_unit_3.py --cov=app --disable-pytest-warnings --cov-config=.coveragerc --cov-report term-missing
python3 -m pytest service_4/testing/test_unit_4.py --cov=app --disable-pytest-warnings --cov-config=.coveragerc