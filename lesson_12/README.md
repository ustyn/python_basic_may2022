# About pip

**pip** is the package manager for python.

Any serious application written in Python requires additional packages.

Python has [many thousands](https://pypi.org/) of additional packages already written that you can use to build any types of applications or perform tasks.

Parsing sites, connecting to DataBases, mathematics calculations, data analisys, natural language processing, audio operations or image processing, using Cloud services or 3rd party APIs or even downloading YouTube Videos - there are different packages already written and ready to use.  

That's one of the reasons why Python is so popular and so powerfull.

## Installing package

Activate your virtual env first, and install package into it.

It's much better than install everything on OS level to your base system Python.

On your env activated run command:
`pip install <package_name>`, 
for example to install [requests](https://pypi.org/project/requests/) run
`pip install requests`

## Working with requirements.txt

Large applications may have hundreds of packages to be installed , and it is boring to install them one by one.
You can keep all names in `requirements.txt` file and then install them just with one command:

`pip install -r requirements.txt`

This file is usually located on the top level folder of the project.

### You can also create/update your requirements.txt

For example you find that your project become larger and it is time to create such file, so all additional packages may be installed with previous command.

Run the command:

`pip freeze >> requirements.txt`

`>>` is a redirection of output, and you're redirecting result of `pip freeze` to overwrite file `requirements.txt'

The file will be created if it isn't exist in this folder, or overwritten.

### Usefull packages

[Flask](https://flask.palletsprojects.com/en/2.1.x/) - framework to build Web-Applications.

[Django](https://docs.djangoproject.com/en/4.0/) - high-level Python web framework.

[FastAPI](https://fastapi.tiangolo.com/) - framework to build asynchronous Web-Applications.

[SQLAlchemy](https://docs.sqlalchemy.org/en/14/) - ORM (object relational mapping) toolkit to work with SQL databases.

[requests](https://github.com/psf/requests) - library to work with HTTP requests.

[numpy](https://pypi.org/project/numpy/) - fundamental package for array computing with Python

[scikit-learn](https://scikit-learn.org/stable/) - module for machine learning .

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - library that makes it easy to scrape information from web pages.
