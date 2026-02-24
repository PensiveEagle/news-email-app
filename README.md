<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">News Email App</h3>

  <p align="center">
    A simple Python app that sends a request to newsapi.org and then sends the news headlines to an email mailing list.
    <br />
  <!--  <a href="https://github.com/PensiveEagle/news-email-app"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/PensiveEagle/news-email-app">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/news-email-app/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/news-email-app/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple Python app that sends a request to newsapi.org and then sends the news headlines to an email mailing list.

<img src="https://github.com/PensiveEagle/asset-repo/blob/main/readme_assets/news-email-app/news-email-app-screenshot.png?raw=true" alt="project_capture" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][python-shield]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* __newsapi.org API key :-__ </br>
  Go to newsapi.org and signup to receive your FREE personal API key
* __Google app password to send emails from GMail account :-__ </br>
  Go to myaccount.google.com/apppasswords to setup an app password for the sender account

This application was designed to work for GMail email client only

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/news-email-app.git
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Set up .env file at the app root level (news-email-app/.env) and insert your API key and Google App Password
   ```
   API_KEY = "<your-newsapi.org-api-key>"
   GOOGLE_APP_PASSWORD = "<your-google-app-password>"
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote <new-url> origin PensiveEagle/news-email-app
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use the app all you need to do is run it, but you can adjust the default values for topic, language, and articles to customise the outputs. By default the app sends 20 articles in English about Dinosaurs

1. Set the API query parameters
    ```python
    # ----------- Set API query parameters ---------- #
    topic = "dinosaur"
    language = "en"
    articles = "20"
    ```
2. Set the <mailing_list>
   ```python
   # ---------- Setup mailing list ---------- #
   mailing_list = ["<recipient-email-1>", "<recipient-email-2>", ...]
3. Set the <sender-email>
   ```python
   # ---------- Send email ---------- #
   for receiver in mailing_list:
      send_email( message = email_message, sender_addr = "<sender-email>", sender_pass = email_sender_pass, receiver_addr = receiver)
   ```
4. Run the app
    ```sh
    python main.py
    ```
3. Emails are sent to all emails in the mailing list

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Mega Course: Build 20 Real-World Apps and AI Agents - Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/news-email-app.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/news-email-app/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/news-email-app.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/news-email-app/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/news-email-app.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/news-email-app/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/news-email-app.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/news-email-app/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/news-email-app.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/news-email-app/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
