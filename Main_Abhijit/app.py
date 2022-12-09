import json
from flask import Flask, render_template, request, jsonify
import folium

# Flask Startup
app = Flask(__name__)

# Initial 
@app.route('/')
def index():
     return render_template("index.html")

@app.route('/about')
def about():
    names = ['Abhijit Purru', 'Khaldoun Hamade', 'Martin Mathew', 'Yannick Baudru']
    return render_template("about.html", names = names)

@app.route('/maps')
def maps():
    folium_map = folium.Map(location=[40,-75.154839], zoom_start= 12)
    return folium_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)