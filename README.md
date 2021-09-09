# TDD in Python

This repository contains exercices of book **Test-Driven Development with Python** and self exercices and tests.


## Install Python dependencies

`
$ pip3 install -r requirements.txt 
`


## Install selenium

### Docs
https://selenium-python.readthedocs.io/installation.html

https://trendoceans.com/how-to-install-and-setup-selenium-with-firefox-on-ubuntu/

### Comands

#### Make drivers dir
`
$ sudo mkdir -p /usr/bin/geckodriver/
`

#### Download last drivers
[releases](https://github.com/mozilla/geckodriver/releases/)

**or using wget**

`
$ wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
`

#### Extract files to drivers folder
`
$ tar xvf ~/Downloads/geckodriver-vX.XX.X-linux64.tar.gz -C /usr/bin/geckodriver
`

#### Export PATH variable
`
$ export PATH=$PATH:/usr/bin/geckodriver
`
