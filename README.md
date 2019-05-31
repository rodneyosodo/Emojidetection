# Emojidetection
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/0x6f736f646f/Emojidetection/blob/master/LICENSE)
[![HitCount](http://hits.dwyl.io/0x6f736f646f/Emojidetection.svg)](http://hits.dwyl.io/0x6f736f646f/Emojidetection)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/0x6f736f646f/Emojidetection/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/0x6f736f646f/Emojidetection.svg?color=purple&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Flask.svg?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/0x6f736f646f/Emojidetection.svg?style=plastic)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/0x6f736f646f/Emojidetection.svg?style=plastic)

Replacing your emotions or signs you do with emojis
## Getting Started

These instructions will get you a copy of the code up and running on your local machine for development purposes and playing around 😂 and testing purposes. Deployment will focus on one of the available platforms.

### Prerequisites

Things you will need to bring the project up on your local machine
```
Docker (Not necessarily but adviced)
Python3
Text editor
Web browser
```

### Installing

A step by step series of getting a development env running on your local machine

#### Windows

```
mkdir Emoji
cd Emoji
virtualenv --no-site-packages Venv
Venv\Scripts\activate
git clone https://github.com/0x6f736f646f/Emojidetection.git
cd Emojidetection
```

#### Unix

```
mkdir Emoji
cd Emoji
virtualenv --no-site-packages Venv
.Venv/bin/activate
git clone https://github.com/0x6f736f646f/Emojidetection.git
cd Emojidetection
```

#### Installing requirements

```
pip install -r requirements
```

#### Running webapp

```
python3 app.py
```
### Dockerising your app

```
docker build -t emojidetection:1.0.1 .
```

* **-t** is to tag the image being built
* **emojidetection** is the image name your can replace it with your own image name
* **1.0.1** is the version

### Running docker web app container

```
docker run --name emoji --restart=always -d -p 8081:5000 emojidetection:1.0.1 python3 app.py
```
* **--name** gives the container a name
* **--restart** always restart when it goes down
* **-d** is running it as a daemon
* **-p** is for port mapping (We are mapping 5000 from docker container to 8081 to our localhost)
* **emojidetection** this is the image name we built
* **1.0** this is the version of the image we built
* **python3 app.py** this is passing a command to the container

### Running docker web app using compose
```
docker-compose up
```
* **up** to run the images


### Web app
#### Windows
Find your docker ip
```
docker-machine.exe ip
```
Then go to http:// *docker-machine ip*:8081

#### Otherwise
Go to [http://localhost:8081](http://localhost:8081) to find the web app

## Deployment

Procedure on how to deploy on heroku as a live system.

    install heroku cli for windows and linux users
```
heroku login
heroku create --region eu your_appname # creates app in eu region, common regions: eu, us
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
heroku logs --tail # If for some reason it’s not working, check the logs
```

## Built With

* [Docker](https://www.docker.com/) - Container development tool
* [Flask](https://maven.apache.org/) - The web framework used
* [Heroku](https://www.heroku.com/) - Platform
* [Opencv](https://opencv.org/) - For video streaming analysis

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* AI saturday Kenya
