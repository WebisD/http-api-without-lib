<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/WebisD/http-api-without-lib">

  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/WebisD/http-api-without-lib">
  
  <a href="https://github.com/WebisD/http-api-without-lib/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/WebisD/http-api-without-lib">
  </a>
  
   <img alt="GitHub" src="https://img.shields.io/github/license/WebisD/http-api-without-lib">
</p>
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/WebisD/http-api-without-lib">
    <img src=".github/logo.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">Pokebook</h3>

  <p align="center">
    A social media for pokemons based in the HTTP protocol
  </p>
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img alt="Made with python" src="http://ForTheBadge.com/images/badges/made-with-python.svg">
  </a>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#-documentation">Documentation</a>
    </li>
    <li>
      <a href="#-how-to-run">How To Run</a>
    </li>
    <li>
      <a href="#-methods">Methods</a>
        <ul>
          <li><a href="#-get">GET</a></li>
          <li><a href="#-post">POST</a></li>
          <li><a href="#-put">PUT</a></li>
          <li><a href="#%EF%B8%8F-delete">DELETE</a></li>
        </ul>
    </li>
    <li>
      <a href="#-status-code">Status Code</a>
    </li>
    <li>
      <a href="#-authors">Authors</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project
In this project, an HTTP/1.1 server were implemented, capable of interpreting some HTTP protocol commands received through requests from browsers, and respond appropriately to those requests.

The commands implemented were: GET, PUT, POST and DELETE.

The HTTP server were implemented according to [RFC 2616](https://tools.ietf.org/html/rfc2616), which defines the HTTP/1.1 protocol.

![app](https://github.com/WebisD/http-api-without-lib/blob/master/.github/app.gif)

<!-- DOCUMENTATION -->
## 📖 Documentation
You can read the documentation here:   

<a href="https://webisd.github.io/http-api-without-lib" target="_blank">
  <img alt="a" src="https://img.shields.io/badge/read-documentation-blue?style=for-the-badge">
</a>

<!-- HOW TO RUN -->
## 🚀 How To Run
```bash

# Clone the repository
$ git clone https://github.com/WebisD/http-api-without-lib.git

# Access the project folder in your terminal / cmd
$ cd http-api-without-lib

# Run the application
$ python3 main.py

# The application will open on the port: 8083 - go to http://localhost:8083

```


<!-- HOW TO RUN -->
## 🛠 Methods
### 🤲 GET
In your browser, go to `http://localhost:8083`

> This page and any other you navigate through the menu symbolizes a GET on our server

> Each image on the website is treated separately and has its own GET

![get](https://github.com/WebisD/http-api-without-lib/blob/master/.github/get.gif)

### 📮 POST
In your browser, go to `http://localhost:8083` and click in `Add new friends`

Then, fill in the fields and clik in `Add`

> This will send a post method to the server that will handle that data, store it in the databse and return a message

> The image is received by the server as data-uri that downloads the image and stores it locally

![post](https://github.com/WebisD/http-api-without-lib/blob/master/.github/post.gif)

### 🔀 PUT
In your browser, go to `http://localhost:8083` and click in `See your friends`

Choose a friend you want to edit the information and click `Edit`

Fill in the fields and clik in `Save Changes`

> This will send a POST method to the server requesting the replacement of the information
> > If it's an image, the server will delete the last image and replace with the new one


![put](https://github.com/WebisD/http-api-without-lib/blob/master/.github/put.gif)

### 🗑️ DELETE
In your browser, go to `http://localhost:8083` and click in `See your friends`

* Delete one

  Choose a friend you want to delete the information and click `Delete`

* Delete all

  Choose a friend you want to delete the information and click `Delete All`

> In both cases, the button will send a DELETE method to the server that will delete the image and the info related with that friend

![delete](https://github.com/WebisD/http-api-without-lib/blob/master/.github/delete.gif)

## 📜 Status Code

In most cases, the server will return status codes on your browser console (which you can see by pressing `F12`) saying whether the operation was successful or not

Here are the most common Status codes and how you can see them

### Successful 2xx

* #### 200 OK 👍

  This is the state that you will see the most, whenever a GET is successful this status code will be shown

* #### 201 Created 🆕

  This status will occur when you click `Add` to add a new friend on the `Add new friend`'s page

### Redirection 3xx

* #### 301 Moved Permanently 👉

  For this state to occur it is a little more complicated. Go to our server access this folder `./databaseUser/Images`

  Now, feel free to move some image around (just don't take it out of the main folder of this project)

  If you try a GET or click on `list all friends`, you can see this status code and the new image path on the terminal

  ![moved](https://github.com/WebisD/http-api-without-lib/blob/master/.github/moved.gif)

### Client Error 4xx

* #### 400 Bad Request 👎
  If the fields to register a friend are not completely filled out, an error will occur and will be shown in the browser (as in the following gif) and in the terminal

  ![badpost](https://github.com/WebisD/http-api-without-lib/blob/master/.github/postError.gif)

* #### 404 Not Found :man_shrugging:
  If the requested page does not exist, an error will occur and will be shown in the browser

  On this page, you can play the famous google dinosaur game or go back to the main page

  ![erro](https://github.com/WebisD/http-api-without-lib/blob/master/.github/erro.gif)

### Server Error 5xx

* #### 500 Internal Server Error

  In case you see this, something happened to our server and we will resolve it soon


<!-- AUTHORS -->
## 🤖 Authors

[Antonio Gustavo](https://github.com/antuniooh)           |  [João Vitor Dias](https://github.com/JoaoDias-223)           |  [Weverson da Silva](https://github.com/WebisD)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://avatars.githubusercontent.com/u/51217271?v=4" alt="drawing" width="150"/>  |  <img src="https://avatars.githubusercontent.com/u/63318342?v=4" alt="drawing" width="150"/>| <img src="https://avatars.githubusercontent.com/u/49571908?v=4" alt="drawing" width="150"/>
22.1190001-0 | 22.119.025-9 | 22.119.004-4
