from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def get_average(lines):
    average = 0
    for line in lines:
        average += int(line.strip().split(";;;")[1].split(";;")[3])
    
    return average / len(lines)

def get_dates(lines):
    dates = []
    for line in lines:
        dates.append(line.strip().split(";;;")[1].split(";;")[1].split(";")[1])

    return dates

def get_clicks(lines):
    clicks = []
    for line in lines:
        clicks.append(int(line.strip().split(";;;")[1].split(";;")[3]))

    return clicks

def get_meidan(clicks):
    medians = sorted(clicks)
    median = medians[0]

    pivot = int(len(clicks)/2)
    if len(clicks) % 2 != 0:
        median = clicks[pivot]
    else:
        median = (clicks[pivot - 1] + clicks[pivot]) / 2

    return median

# open CSV file
fileconnection = open("resources/jobentry_export_2019-8-23T9_59.csv", "r")
lines = fileconnection.readlines()

# calculate desired values
average = get_average(lines[1:])
dates = get_dates(lines[1:])
clicks = get_clicks(lines[1:])
median = get_meidan(clicks)

# close file
fileconnection.close()

@app.route("/")
def main_route():    
    return render_template("index.html", average=average, median=median)

@app.route("/chart_info")
def chart_info_route():
    return jsonify({"date_posted": dates, "apply_clicks": clicks })

if __name__ == "__main__":
    app.run(debug=False)
