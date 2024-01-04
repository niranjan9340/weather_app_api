from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

stations = pd.read_csv("data-small/stations.txt", skiprows=17)
stations["STANAME"] = stations["STANAME                                 "]
stations = stations[["STANAME","STAID"]]

@app.route("/")
def home():
    return render_template("index.html", data=stations.to_html())

@app.route("/v1/<station>/<date>")
def detail(station, date):
    filename = "data-small/TG_STAID" + str(station).zfill(6)+ ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates= ["    DATE"])
    temp = df[df["    DATE"] == date]['   TG'].squeeze()/10
    return {
        "station": station,
        "date" : date,
        "temperature": temp
    }

@app.route("/v1/<station>")
def all_details(station):
    filename = "data-small/TG_STAID" + str(station).zfill(6)+ ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates= ["    DATE"])
    all_data = df.to_dict(orient="records")
    return all_data

@app.route("/v1/y/<station>/<year>")
def yearly_details(station,year):
    filename = "data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result
if __name__ == '__main__':
    app.run(debug=True)
