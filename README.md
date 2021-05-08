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
      <a href="#-errors">Errors</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project
In this project, an HTTP/1.1 server were implemented, capable of interpreting some HTTP protocol commands received through requests from browsers, and respond appropriately to those requests.

The commands implemented were: GET, PUT, POST and DELETE.

The HTTP server were implemented according to [RFC 2616](https://tools.ietf.org/html/rfc2616), which defines the HTTP/1.1 protocol.

![app](https://github.com/WebisD/http-api-without-lib/blob/master/.github/app.gif)


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

## ❌ Errors
In most cases, the server will return status codes on your browser console (which you can see by pressing `F12`) saying whether the operation was successful or not

Here are the most common Error codes and how you can see them

### 404 Not Found
If the requested page does not exist, an error will occur and will be shown in the browser

On this page, you can play the famous google dinosaur game or go back to the main page

![erro](https://github.com/WebisD/http-api-without-lib/blob/master/.github/erro.gif)



