<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Script Title & Description
PHOTOSHARE

PhotoShare is a photo-sharing website where registered users can share 'Photos' and view a listing of other users' shared photos. It is built primarily on Python(Django)

<img width="1280" alt="The Shoppies Preview " src="https://github.com/hennessyisrael/The-Shoppies/blob/e7a41b4394563d72baa40076fb9c52e7cb038378/images/The_shoppies_app.png">

## ⚙️ Languages or Frameworks Used
<!--Remove the below lines and add yours -->
* PYTHON (Django)
* CSS Bootsrtaps
* HTML


## 🛠️ Features

* Users can register for an account.
* Users can log in into an existing account.
* Users can reset their password to an existing account
* Users can share a photo and add captions.
* Users can update an already shared photo or its captions.
* Users can delete a Photo.
* Users can like a photo.




## 🌟 How to run
Visit Twitter Developer Account Website and click on Create app to create a Twitter Devlopment Account for a Bearer Token


1. Save the script in the local machine.

2. Open a terminal/command prompt and change directory location to the folder where your script is located and run the below commands

    1. Create a virtual enviroment to install required package

        ```python
        python3 -m venv .venv /path/to/new/virtual/environment
        ```
    2. Activate virtual enviroment for for your OS
        On Windows, run:
        ```shell
        python3 -m venv .venv /path/to/new/virtual/environment
        ```

    3. To install required packages run the below command
        On Unix or MacOS, run:
        ```shell
        pip install -r requirements.txt
        ```

    4. To setup database migrations 

        ```shell
        'cd' into the photoshare directory 
        ```

        ```python
        python manage.py makemigrations
        ```

    5. To execute migration

        ```python
        python manage.py migrate
        ```

    6. To execute the script run the following command

        ```python
        python manage.py runserver
        ```

    After successful execution of the script you should see the 'URL localhost link to the website' outputed in command prompt/terminal


## 📺 Demo

![demo]



## 🤖 Author
[Israel Akinola](https://github.com/israelakinola)
