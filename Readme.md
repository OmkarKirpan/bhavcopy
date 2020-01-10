# [CherryPy - Bhavcopy](https://ok-bhavcopy.herokuapp.com/)

![dependencies](https://img.shields.io/hackage-deps/v/lens.svg)
![python](https://img.shields.io/badge/python-3.8-brightgreen.svg)
![platform](https://img.shields.io/conda/pn/conda-forge/python.svg)

BSE publishes a "Bhavcopy" file every day here: <https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx>

Write a Python script that:

- Downloads the Equity bhavcopy zip from the above page

- Extracts and parses the CSV file in it

- Writes the records into Redis into appropriate data structures(Fields: code, name, open, high, low, close)

Write a simple CherryPy python web application that:

- Renders an HTML5 + CSS3 page that lists the top 10 stock entries from the Redis DB in a table
- Has a searchbox that lets you search the entries by the 'name' field in Redis and renders it in a table
- Make the page look nice!

live preview here at <https://ok-bhavcopy.herokuapp.com/>

## Installation

```
$ pip install pipenv
```

```
$ pipenv install
```

## Run CherryPy server

```
$ pipenv shell
```

```
$ python run.py
```

## Seeding/Updating Data into Redis
go to
```
https://ok-bhavcopy.herokuapp.com/update
```
also to seed data of given date (specify date in %d%m%y)
```
https://ok-bhavcopy.herokuapp.com/update?date_str=080120
```

## Contributing ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

### Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off, or if you
   do not have permission to do that, you may request to merge it for you.

## Reference

Offical Website

- [CherryPy](https://cherrypy.org/)

[![alt text][1.1]][1][![alt text][2.1]][2]

[1.1]: http://i.imgur.com/P3YfQoD.png
[2.1]: http://i.imgur.com/0o48UoR.png
[1]: http://www.facebook.com/omkar.kirpan
[2]: http://www.github.com/omkarkirpan
