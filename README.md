# Random Face Generator

This repo creates a web application to display an nx4 grid of face images generated using a DCGAN generator. You can vary the output face images and see the transitions, by varying the input to the DCGAN. This is done by multiplying the input noise by a secondary noise through varying degrees. This project uses Streamlit for its web interfacing, and Pytorch JIT compiler for faster model performance.

## Requirements
 + PyTorch
 + Numpy
 + Streamlit

## Deploy
A deployed version of this repo on Heroku can be found [here](https://random-faces-codedev99.herokuapp.com/).

### Local Machine
You can deploy this project in a few simple steps.
+ Firstly, clone the repo to your local machine.
+ Open command line/terminal and cd to the directory.
+ Run the following command:

    streamlit run main.py
    
+ After deployment is complete, open the URL provided in the terminal, in a web browser.

### Heroku
Please ensure that Heroku CLI and Git CLI is installed on your computer. To deploy on Heroku, follow these steps.
+ Firstly, clone the repo to your local machine.
+ Open command line/terminal and cd to the directory.
+ Run the following commands:

    git init
    git add .
    git commit -m "heroku deployment"

+ Login to Heroku using:

    heroku login

+ After successful login, run the following:

    heroku create <nameofyourapp>
    heroku git:remote -a <nameofyourapp>
    git push heroku master

+ Once the app is deployed, open the link provided in the terminal (it would be in the style of <nameofyourapp>.herokuapp.com)

## This repo contains
+ *main.py* - The main app file containing streamlit and torch code.
+ *scripted-generator.pt* - Script file for the model using JIT compiler.
The following files are solely associated with Heroku deployment:
+ *requirements.txt* - Python requirements.
+ *Procfile* - Defines application type (web) and bash commands to run application.
+ *.profile* - Contains bash commands to run before app deployment (after slug compilation). Here, this file is used to install PyTorch. This is because PyTorch can't be installed during slug compilation due to large wheel size, hence a wheel of smaller size is installed using this file.
+ *runtime.txt* - Defines runtime for Heroku. Please note that python <= 3.9 is not compatible for torch model deployments using Streamlit.
+ *setup.sh* - Defines server configuration.