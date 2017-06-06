# Simona Floweshop

## Installation and Set Up

You must have the following installed :-

    1)Python 3.5
    2)virtualenv

Clone the repo
```
https://github.com/machariamarigi/simona_flowers.git
```

Create a virtual environment for the project and activate it:
```
virtualenv env
source env/bin/activate
```

Enter the app directory
```
cd simon_flowers
```

make sure you are in the development branch
```
git checkout development
```

Install the required packages:
```
pip install -r requirements.txt
```

## Launching the Program
Set the FLASK_APP and FLASK_CONFIG variables as follows:

* `export FLASK_APP=application.py`
* `export FLASK_CONFIG=development`

You can now run the app with the following command: `flask run`

