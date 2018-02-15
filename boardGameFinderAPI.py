'''
    boardGameFinderAPI.py
    Calypso Leonard, Tresa Xavier, Yingying Wang
    Flask API used for a board game finder web app
    for CS 257, Winter 2018.
'''

import flask
from flask import render_template, Flask, request
import sys
import psycopg2
import templates
import static
import datasource
import json 

app = flask.Flask(__name__)


#info = datasource.DataSource("0", "0", "Puzzel", "0")

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/About')
def aboutPage():
    return render_template('about.html')

@app.route('/results',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        inputCategory = request.form['Category']
        inputTime = request.form['Time']
        inputAge = request.form['Minimum Age']
        inputNumPlayer = request.form['No. of Players']
        info = datasource.DataSource(inputNumPlayers, inputAge, inputCategory, inputTime)
        action = info.selectFunction()
        query = info.search(action)
        if query == "Sorry! No games found":        
            return render_template('noResults.html')
        else:
            return render_template("results.html",result = query)
          
@app.route('/random', methods = ['POST', 'GET'])
def random():
    info = datasource.DataSource(5, 21, "Puzzel", 200)
    query = info.getRandomGame()
    return render_template('results.html', result = query)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    #info = datasource.DataSource()
    #info = datasource.DataSource("0", "0", "Puzzel", "0")

        
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

    app.run(debug = True)
