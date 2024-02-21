# FastAPI-Application

Check if you have python 3.8 > :  for using fastapi – python --version<br /> 
Create folder – fastapi-application<br /> 
Install Virtualenv in your folder - pip3 install virtualenv<br /> 
Create virtual environment - python3 -m venv .venv<br /> 
Activate your virtual environment - source .venv/bin/activate<br /> 
Deactivate – deactivate<br /> 
If you want to upgrade pip3:<br /> 
            1. python3 -m pip install --upgrade pip<br /> 
            2. python3 -m pip –version<br /> 
Install FastAPI – pip install fastapi<br /> 
Install uvicorn -  pip install uvicorn<br /> 
Run uvicorn - uvicorn main(filename):app(fastapi instance) --reload<br /> 
Run Requirements file - pip install -r requirements.txt

Processes to check using the port : 8000 <br />
lsof -i :8000

To kill any process:<br />
kill -9 PID
