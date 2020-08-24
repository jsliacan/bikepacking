bikepacking
======

Basic script to scrape gender proportions from finisher tables at [dotwatcher.cc](https://dotwatcher.cc/results). The intention is to provide a working script that anyone can modify to retrieve their own data of interest.

## How to use

1. Clone this repo (comes with data scraped at the time of last commit) and change to the directory that was created:

	```bash
	git clone https://github.com/jsliacan/bikepacking.git
	cd bikepacking
	```

   To refresh the data, run `python scrape.py` (this can take a while -- depending on connection and how many race results there are on [dotwatcher.cc](https://dotwatcher.cc/results)).

2. Type `python gender.py` to get the average proportion of female/male finishers.

## Thanks

to [thisisgrace](https://www.instagram.com/thisisgrace_/) from [dotwatcher.cc](https://dotwatcher.cc/results) for collecting the results.


