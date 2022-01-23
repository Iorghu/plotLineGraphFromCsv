import serial
import sys
import webbrowser
import pandas as pd
import plotly.express as px
import time

# TODO: commentaries
if len(sys.argv) > 1:
    print("argument found, using '" + str(sys.argv[1]) + "' as name of the csv.")
    nameOfCsv = sys.argv[1]
else:
    nameOfCsv = "myLoggedData.csv"
    print("No argument found, using default filename: " + nameOfCsv)
    
webbrowser.open("autoUpdate.html") # opens a local html file, that reloads the graph every 15 seconds.

while True:
    df = pd.read_csv(nameOfCsv)
    cols = df.columns
    fig = px.line(df,x=cols[0],y=cols[1:])
    fig.write_html("graph.html")
    time.sleep(10)
