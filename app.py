from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

def get_average(lines):
    average = 0
    for line in lines:
        average += get_click(line)
    
    return average / len(lines)

def get_meidan(lines):
    clicks = []
    for line in lines:
        clicks.append(get_click(line))

    medians = sorted(clicks)
    median = medians[0]
    pivot = int(len(clicks)/2)
    if len(clicks) % 2 != 0:
        median = clicks[pivot]
    else:
        median = (clicks[pivot - 1] + clicks[pivot]) / 2

    return median


def get_post_date(line):
    return line.strip().split(";;;")[1].split(";;")[1].split(";")[1]

def get_end_date(line):
    return line.strip().split(";;;")[1].split(";;")[1].split(";")[2]

def get_click(line):
    return int(line.strip().split(";;;")[1].split(";;")[3])

def get_date_intervals(lines):
    dates = {}
    for line in lines:
        post_date = datetime.strptime(get_post_date(line), '%d.%m.%Y')
        end_date = datetime.strptime(get_end_date(line), '%d.%m.%Y')
        interval = (end_date - post_date).days
        if interval in dates:
            dates[interval] += get_click(line)
        else:
            dates[interval] = get_click(line)

    return dates

# open CSV file
fileconnection = open("resources/jobentry_export_2019-8-23T9_59.csv", "r")
lines = fileconnection.readlines()

# calculate desired values
average = get_average(lines[1:])
median = get_meidan(lines[1:])
date_intervals = get_date_intervals(lines[1:])

# close file
fileconnection.close()

@app.route("/")
def main_route():    
    return render_template("index.html", average=average, median=median)

@app.route("/chart_info")
def chart_info_route():
    return jsonify({ "date_intervals": date_intervals })

if __name__ == "__main__":
    app.run(debug=True)
