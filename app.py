from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def main():    
    # open CSV file
    fileconnection = open("resources/jobentry_export_2019-8-23T9_59.csv", "r")
    lines = fileconnection.readlines()

    # calculate desired values
    average = 0
    for line in lines[1:]:
        raw_value = line.strip().split(";;;")
        average += int(raw_value[1].split(";;")[3])
    average = average / len(lines[1:])

    # close file and return
    fileconnection.close()
    return render_template("index.html", average=average)

@app.route("/chart_info")
def chart_info():
    # open CSV file
    fileconnection = open("resources/jobentry_export_2019-8-23T9_59.csv", "r")
    lines = fileconnection.readlines()

    # calculate desired values
    dates = []
    clicks = []
    for line in lines[1:]:  
        raw_value = line.strip().split(";;;")
        dates.append(raw_value[1].split(";;")[1].split(";")[1])
        clicks.append(int(raw_value[1].split(";;")[3]))

    # close file and return
    fileconnection.close()
    return jsonify({"date_posted": dates, "apply_clicks": clicks })

if __name__ == "__main__":
    app.run(debug=False)