### Purpose of this project - 

Fueled by a desire to bridge technology and emotional well-being, I created StressLens, a web application built with FastAPI. As someone constantly navigating the digital landscape, I recognized the importance of self-awareness in managing stress. StressLens empowers users to track their moods over time, fostering valuable insights into their emotional patterns.
This project served as a springboard for my exploration of REST APIs and secure user authentication. By prioritizing user data privacy, StressLens ensures that all mood data remains strictly confidential and accessible only to the respective user. My commitment to user privacy reflects the importance of safeguarding personal information in today's digital age.

### Below guidelines to work on this repository - 

### Prerequisites
1. Docker
2. Docker Compose
3. Install Natural Client Libraries <br />
    - pip install --upgrade google-cloud-language

Download the google-cloud-sdk and install and initialize the gcloud CLI <br />
Create your credentials file <br/>
    - gcloud auth application-default login<br />
<i>A sign-in screen appears. After you sign in, your credentials are stored in the local credential file used by ADC.</i> <br />

### Steps to proceed ahead towards the repository

1. Clone the Repository
            git clone https://github.com/apoorva-machale/StressLens.git
2. Build Docker Images
            docker-compose build
            Run the Docker Containers - docker-compose up

3. Access the Applications
            FastAPI : http://localhost:3000/docs
