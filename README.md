# travelTime

**When is the best time to leave by car?**

A collection of scripts to source and analyze realtime traffic information to make descriptive, predictive and prescriptive decisions on when to leave on a trip, and minimize traffic.

We'll plan ahead and capture realtime traffic data between two locations every 10 minutes, then identify when the best time to leave (quickest) is.

## Sourcing data

This project uses the [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/) (you'll need an API key), queried via [cron jobs](https://en.wikipedia.org/wiki/Cron).

* [travelTime.ipynb](travelTime.ipynb) is an interactive jupyter notebook to query traffic data
* [travelTime.py](travelTime.py) is a standalone CLI version for running as a cron job

Example crontab:

```*/10 * * * * $HOME/bin/travelTime.py -q "Origin" "Destination" >> $HOME/data/origin-destination.csv```

CSV header:

```Timestamp,Duration(s)```

I recommend you run through the interactive notebook to test out your origin/destination combinations before setting up the crontab.

## Analyzing data

TBD

## Contributing

Python is not my go-to language - any refactoring/improvements welcome via Issues or PRs.