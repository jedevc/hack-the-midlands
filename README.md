# Kitten Kollector

Kitten Kollector is that tool you've always wanted to run a scavenger hunt,
whether it be in one building or all over a city. Think Pokemon Go. But with
kittens. And made in 24 hours.

Simply generate any number of kittens that you like with a unique code, and
then write down the codes where people can find them. Anyone can then use the
website to redeem the codes and get their kitten.

## Tools

We created Kitten Kollector using flask with python on the backend and HTML5
with bootstrap on the frontend. The icons are generated using
[robohash](https://robohash.org/).

The app was made to be deployed to Google App Platform, but you could
conceivably host it anywhere.

## Installation

If for some reason you decide you actually want to run kitten kollector (not
really recommended as some parts are extremely hacky), run the following
commands to download kitten kollector and install all of its dependencies.

	$ git clone https://github.com/jedevc/kitten-kollector.git
	$ cd kitten-kollector
	$ pip install -r requirements.txt

Then running the app is just as easy as:

	$ python main.py
