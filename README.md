### Purpose of this project - 
Fueled by a desire to bridge technology and emotional well-being, I created StressLens, a web application built with FastAPI. As someone constantly navigating the digital landscape, I recognized the importance of self-awareness in managing stress. StressLens empowers users to track their moods over time, fostering valuable insights into their emotional patterns.
This project served as a springboard for my exploration of REST APIs and secure user authentication. By prioritizing user data privacy, StressLens ensures that all mood data remains strictly confidential and accessible only to the respective user. My commitment to user privacy reflects the importance of safeguarding personal information in today's digital age.

### Below guidelines to work on this repository - 
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
Run uvicorn - uvicorn blog.main(foldername.filename):app(fastapi instance) --reload<br /> 
Run Requirements file - pip install -r requirements.txt
Run - pip freeze to get revised requirements<br/>

Processes to check using the port : 8000 <br />
lsof -i :8000

To kill any process:<br />
kill -9 PID

Install Natural Client Libraries <br />
    - pip install --upgrade google-cloud-language

Download the google-cloud-sdk and install and initialize the gcloud CLI <br />
Create your credentials file <br/>
    - gcloud auth application-default login<br />
<i>A sign-in screen appears. After you sign in, your credentials are stored in the local credential file used by ADC.</i> <br />


