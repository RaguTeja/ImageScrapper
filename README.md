# ImageScrapper
Automated code to download the required category of images from google with single click. 

USES:
1. we can easily download as many images we want into our local server or cloud.
2. we can create large datasets, so that they can be used for machine learning and deep learning algorithms.

DEPLOYMENT: HEROKU PLATFORM

Type of programming: Modular Programming

Framework : Flask

FILES INFORMATION:
UI.PNG : Web application after deployment

QUERYING.PNG : GIVING REQUIRED IMAGE NAME

OUTPUT.PNG : RESULTS RETRIEVED FROM GOOGLE API

Procfile : This file is important for deployment in heroku platform. Here we are telling the dynos applications of heroku to start the execution of source code from specified file with gunicorn server.

app.py: In this file we create flask application. Through this web application we take query from the user and provide the results.

templates: This is the folder where we have our html files. This folder is automatically recognized by the flask application.

static: In this folder we have css files and downloaded images.

scrapper.py: In this file we have implemented a code which follows the following steps:

             1. creating an url with the help of user query.
             
             2. From created url we retrieved raw html code.
             
             3. From raw html we collect image urls.
             
             4. By taking image urls we have downloaded images by requesting the google API
             

             
