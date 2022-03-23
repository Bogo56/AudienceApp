<h1 align="center">
  <br>
  <img src="https://res.cloudinary.com/dawb3psft/image/upload/v1648020431/Portfolio/star.ico" alt="AudienceApp" width="150">
  <br>AudienceApp
</h1>

<h4 align="center">Python-Kivy App to reveal all targeting interests.</h4>

<p align="center">
  <a href="https://img.shields.io/badge/Made%20with-Python-blue">
    <img src="https://img.shields.io/badge/Made%20with-Python-blue"
         alt="Gitter">
  </a>
  <a href="https://img.shields.io/tokei/lines/github/Bogo56/AudienceApp">
      <img src="https://img.shields.io/tokei/lines/github/Bogo56/AudienceApp">
  </a>
  <a href="https://img.shields.io/github/languages/count/Bogo56/AudienceApp?color=f">
    <img src="https://img.shields.io/github/languages/count/Bogo56/AudienceApp?color=f">
  </a>
  <a href="https://badgen.net/github/commits/Bogo56/AudienceApp">
    <img src="https://badgen.net/github/commits/Bogo56/AudienceApp">
  </a>
</p>

<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#description">Description</a> •
  <a href="#how-to-use">How to use</a> •
  <a href="#project-structure">Project Structure</a> 
</p>

## Built With
###  Languages
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://res.cloudinary.com/dawb3psft/image/upload/v1647933330/Portfolio/kv-lang.png">
<p>
  
### Frameworks
<p>
<img src="https://res.cloudinary.com/dawb3psft/image/upload/v1647933068/Portfolio/kivy.png">
</p>

### Databases
<p>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

## About The Project
This is a very simple project, that I created. **The purpose of the app was to improve the process of setting advertising campaigns** in Facebook inside my team. The App communicates with the Facebook API to fetch a full list of targeting options based on a keyword.

* If you want you can download and unzip the app on your machine. The path to the executable is located at `dist/AudienceAPP/AudienceAPP.exe`

## Description
Each campaign in Facebook must have some targeting. So when choosing a targeting for your campaign inside the Facebook Ads Manager UI, you just type a keyword and a dropdown menu appears with suggestions for that keyword. The thing is that the number of suggestions is limited to about 30, while infact FB has a much larger list of "interest buckets" for a keyword - a couple of hundred at times. BUT it only displays a maximum of 30. At least that's the limitation when working with the UI. Getting all of the available targeting suggestions can be done only programatically trough the Facebook Marketing API. So I created this simple app, to make it an easy process.


## How To Use
1. **Cenerate an access token**
   - Go to https://developers.facebook.com/ and create an account (if you don't have one). Create a FB app to access the API - info here https://developers.facebook.com/docs/development/ . Go to the Graph API Explorer and generate your access token.
       
2. **Add the token and use the app.**
  - ![](gifs/audience_app.gif)
  

3. **Choose your mode**
    * **Standart keyword mode**
      - Get targeting options based on your keyword
      
    * **Suggestion mode**
      - Use this mode to get suggestions for targeting options outside of your keyword, but that are related to it.
      - **!** Currently FB has some issues with that service, so it might not work currently.
      


## Project Structure
I used PyInstaller to package all of the modules and files and make them executable through a single .exe file.

```
📦 AudienceApp
├─ .gitignore
├─ .idea
|
├─ App_executable
│  └─ Audience_App.zip
├─ README.md
├─ controller
│  └─ controller.py
├─ gifs
│  └─ audience_app.gif
├─ model
│  ├─ database.db
│  └─ model.py
├─ modules
│  └─ fb_api.py
└─ view
      ├─ app.py
      ├─ audience.kv
      ├─ menu.kv
      ├─ resources
      │  ├─ 175-1755232_create-icons-from-png-jpg-images-online-password.png
      │  ├─ 28152761935f3b72fbefd012fd2fbc78.psd
      |  ├─ 5360128.ai
      │  ├─ 5360128.psd
      │  ├─ 5360129.eps
      │  ├─ 5360130.jpg
      │  ├─ Fonts.txt
      │  ├─ background
      |  |   ├─ 5556661.jpg
      |  |   ├─ 5556662.ai
      │  │   ├─ 5556667.eps
      │  │   └─ BACKGROUND.png
      │  ├─ buttons
      |  |   ├─ AUDIENCE_TOOL.png
      |	 |   ├─ AUDIENCE_TOOL_PRESSED.png
      |	 |   ├─ Clone.png
      |	 |   ├─ Dark.png
      |	 |   ├─ Drone.png
      │  │   ├─ SEARCH.png
      │  │   ├─ SEARCH_PRESSED.png
      │  │   ├─ TOKEN_MANAGER.png
      │  │   ├─ TOKEN_MANAGER_PRESSED.png
      │  │   └─ Vader.png
      │  ├─ icons
      │  │  ├─ logo.ico
      │  │  └─ logo.png
      │  ├─ music
      │  │  ├─ 28152761935f3b72fbefd012fd2fbc78.png
      │  │  ├─ saber.mp3
      │  │  └─ star_wars.mp3
      │  └─ password.jpg
      └─ token.kv
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)
