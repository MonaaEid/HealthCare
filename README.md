# Hospital Management System

<a href="http://monaeid.tech/">
<img src="flaskr/static/images/hospital-logo.png" > 
</a>

## Installation

### linux:

Installing flask:

    $ pip3 install flask


Installing mysql:

    $ sudo pip3 install mysql
    $ sudo apt-get install python3-mysqldb
    $ sudo apt-get install python3-dev default-libmysqlclient-dev


Installing SQLAlchemy:

    $ pip3 install SQLAlchemy

Installing gunicorn:

    $ pip3 install gunicorn

## Usage:

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/MonaaEid/Hospital-Mangement-System
    $ cd Hospital-Mangement-System

Start gunicorn:

    $ sudo systemctl daemon-reload
    $ sudo systemctl enable gunicorn
    $ sudo systemctl start gunicorn
    $ sudo systemctl status gunicorn

Run the application:

    $ gunicorn --bind 0.0.0.0:5000 flaskr.app:app

## Contributing
### Mohamed Nasef
### Mona Eid


