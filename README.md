# scuba-portugal
Demonstration site

# team
Team 2 is ready

## Init (virtual) env
```
pip install -r requirements.txt
```

### Use pipenv for a virtual environment
```
pip install --user pipenv
pipenv install requests
pipenv shell
pipenv install
```
Then use ```pipenv shell``` to start work within the python virtual environment. Use ```pipenv graph``` to show all installed dependencies

## Start the dev webserver
First, ensure the database is up-to-date:
```
python manage.py migrate
```
Then run the webserver:
```
export PORT=5000
python manage.py runserver $PORT
```

## Run BDD tests
```
cd tutorial
behave
```
