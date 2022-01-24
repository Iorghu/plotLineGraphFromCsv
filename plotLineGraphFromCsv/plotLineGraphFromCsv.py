import serial
import sys
import webbrowser
import pandas as pd
import plotly.express as px
import time

# filename of the .csv file to be showed, can be changed via arguments. Be sure that the external app writes its data into the same file.
if len(sys.argv) > 1:
    print("argument found, using '" + str(sys.argv[1]) + "' as name of the csv.")
    nameOfCsv = sys.argv[1]
else:
    nameOfCsv = "myLoggedData.csv"
    print("No argument found, using default filename: " + nameOfCsv)
    
webbrowser.open("autoUpdate.html") # opens a local html file, that reloads the graph every x seconds.

while True:
    df = pd.read_csv(nameOfCsv)
    cols = df.columns
    fig = px.line(df,x=cols[0],y=cols[1:])
    fig.write_html("graph.html") # this file will be reloaded in autoUpdate.html
    time.sleep(10)
