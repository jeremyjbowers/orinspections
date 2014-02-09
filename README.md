# OR INSPECTIONS
A site dedicated to restaurant inspections in Lane County, OR.

This code is open source under the MIT license. See ```LICENSE``` for complete details.

## Getting this running

### Setup your computer
Follow [these instructions](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html) for getting your computer set up to work with a Python project.

### Get the code
Check out this project from GitHub and cd to it's directory.
```
git clone git@github.com:jeremyjbowers/orinspections.git
cd orinspections
```
### Prepare an environment
Make a virtual environment for this project and install the requirements.
```
mkvirtualenv orinspections
pip install -r requirements.txt
```

### Get the data
Run the scraper. You will now have a ```restaurant_list.html``` file and a ```restaurant_list.json``` file in your ```data/``` directory.
```
./scrape.py
```


## What's coming
* A web application
* An ORM, probably [peewee](http://peewee.readthedocs.org/en/latest/index.html).
* A [fabfile](http://docs.fabfile.org/en/1.8/) for deployment and other automated tasks.

## What's this all about?
[Email Jeremy](mailto:jeremyjbowers@gmail.com) if you're confused.