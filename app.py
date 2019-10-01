from flask import Flask, render_template
from pathlib import Path
from yaml import load, SafeLoader
from yaml.scanner import ScannerError

import json
import glob
import os
import sys


app = Flask(__name__)
app.config["data_source"] = os.environ["MISSIONS_DATA"]


@app.route("/")
def combined():
    """Show a radar chart containing the Teams ratings for this mission."""
    mission = Path(app.config.get("data_source")).name
    ratings = _get_data(app.config.get("data_source"))

    # get a persons ratings and extract the themes from it
    # this saves us from storing them statically but does
    # allow for errors if people misspell one
    labels = list(ratings[list(ratings.keys())[0]]["themes"].keys())
    labels.sort()

    datasets = []
    for person in ratings:
        numbers = []

        for theme in sorted(ratings[person]["themes"]):
            numbers.append(ratings[person]["themes"][theme])

        datasets.append({
            "label": ratings[person]["submitter"],
            "data": numbers
        })


    return render_template("theme-radar.html.j2",
         datasets=datasets,
         labels=labels,
         mission=mission)


@app.route("/ratings")
def get_ratings():
    """Show the team ratings in a JSON format."""
    # this route is mostly for debugging
    mission = Path(app.config.get("data_source"))
    ratings = _get_data(app.config.get("data_source"))
    return json.dumps(ratings)


#
# Private helper functions
#

def _yaml_loader(yaml_data):
    """Inflate the provided YAML and return it as a Python structure."""

    try:
        inflated_yaml = load(yaml_data, Loader=SafeLoader)
    except ScannerError as error:
        print(f"Invalid YAML: [{error}]", file=sys.stderr)
        sys.exit(1)

    return inflated_yaml


def _get_data(source):
    """Load all the team ratings for the given mission."""
    ratings = {}

    for filename in glob.glob(f"{source}/*.yaml"):
        datafile = Path(filename).name

        # meta.yaml contains information about the mission itself and so should be skipped
        if "meta.yaml" == datafile:
            continue

        contents = None

        with open(filename, "r") as file:
            contents = file.read()
            contents = _yaml_loader(contents)

            ratings[datafile] = contents

    return ratings
