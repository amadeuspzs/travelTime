# travelTime

**When is the best time to leave by car?**

![download](https://user-images.githubusercontent.com/534681/27839438-300f6034-60bf-11e7-8a12-cbf8f470e157.png)

A collection of scripts to source and analyze historical realtime (!) traffic information to make descriptive, predictive and prescriptive decisions on when to leave on a trip.

We'll plan ahead and capture realtime traffic data between two locations every 10 minutes, then identify when the best time to leave (quickest) is.

## Sourcing data

This project uses the [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/) (you'll need an API key), queried every 10 minutes via [cron jobs](https://en.wikipedia.org/wiki/Cron).

* [travelTime.ipynb](travelTime.ipynb) is an interactive jupyter notebook to query traffic data
* [travelTime.py](travelTime.py) is a standalone CLI version for running as a cron job

Example crontab:

```*/10 * * * * $HOME/bin/travelTime.py -q "Origin" "Destination" >> $HOME/data/origin-destination.csv```

CSV header:

```Timestamp,Duration(s)```

I recommend you run through the interactive notebook to test out your origin/destination combinations before setting up the crontab.

## Analyzing data

Captured data examples are in the `data/` folder. 

* [analysis.ipynb](analysis.ipynb) is an interactive jupyter notebook to analyse data (ongoing work)
* [analysis-pandas.ipynb](analysis-pandas.ipynb) is a pandas version of above
Objectives:

- [X] Week-by-week visualization
- [X] Long weekend visualization
- [ ] Day by Day overlap
- [X] Peak/valley detection
- [ ] Peak/valley overlay
- [ ] Average over weeks
- [ ] Prediction
	- Given a day of week and time of day, traffic will be X
- [ ] Prescription
	- You should wait 2.5 hours and leave at X to minimize traffic

## Contributing

Python is not my go-to language - any refactoring/improvements welcome via Issues or PRs.
