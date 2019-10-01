# Map your Work Themes to Radar Charts

Map your work missions against your chosen themes with a Radar chart

## Introduction

Deciding what to work on first can be a difficult judgement call. This
repository attempts to help you make that decision by allowing each member of
a team to estimate how a piece of work maps to your chosen principles
or themes.

![A Radar Chart to theme mapping screenshot](/images/radar-chart-theme-mapping.png "Radar Chart to theme mapping screenshot")

Each member of the team assigns a score to each theme, the higher the
score (ranged from 0-10) the more the work fits the theme. Once you can
then use the graphs created by this tool to view these ratings as a
whole and see if there are any obvious disagreements to discuss.

## Installing and running

This application is written in python and uses some HTML, JavaScript and
CSS. It does *not* require Node.

    # get the repo
    git clone git@github.com:deanwilson/themes-to-radar.git
    cd themes-to-radar

    # create the python virtual environment.
    # this keeps all the modules you install isolated
    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt

Now we're installed all the required software run the application with the sample data

    MISSIONS_DATA=sample-missions/cost-savings/ FLASK_APP=app.py flask run

Open your web browser and visit
[http://127.0.0.1:5000/](http://127.0.0.1:5000/ "Local flask webserver")

## Adding your own data

While the sample data is a pretty example you'll soon want to add your
own data and chart that. To build radar graphs for your own missions you
should create a directory, named for the mission, inside missions and
have each person taking part in the scoring add their own YAML file. In
this example I'm going to add a mission called `hands-off-scaling` and
we're going to judge it against our themes of `cost_saving`,
`resilience_improvement`, `learning_opportunity` and `enthusiasm`.

    # create the mission
    mkdir missions/hands-off-scaling

Each person can then create their own rating file and add their values.

    cat <<'EOF' > missions/hands-off-scaling/${team-member-name}.yaml
    submitter:
    themes: # rated 1-10
      cost_saving:
      resilience_improvement:
      learning_opportunity:
      enthusiasm:
    EOF

Here is a completed example:

    cat missions/hands-off-scaling/susan.yaml
    submitter: Susan Sto Helit
    themes: # 1-10
      cost_saving: 3
      resilience_improvement: 7
      learning_opportunity: 3
      enthusiasm: 5

### Author

  [Dean Wilson](https://www.unixdaemon.net)

### License

 * Released under the GPLv2
