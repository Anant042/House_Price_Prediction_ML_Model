# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import pickle
# import json
# import numpy as np

# app = Flask(__name__)
# CORS(app)

# __locations = None
# __data_columns = None
# __model = None

# @app.route('/')
# def index():
#     return render_template('index.html')

# def load_the_data():
#     global __data_columns
#     global __locations

#     with open("columns.json", "r") as f:
#         __data_columns = json.load(f)['data_columns']
#         __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

#     global __model
#     if __model is None:
#         with open('banglore_home_prices_model.pickle', 'rb') as f:
#             __model = pickle.load(f)


# def get_estimated_price(location, sqft, bhk, bath):
#     try:
#         loc_index = __data_columns.index(location.lower())
#     except:
#         loc_index = -1

#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index >= 0:
#         x[loc_index] = 1

#     return round(__model.predict([x])[0], 2)

# def get_location_names():
#     return __locations



# @app.route('/get_location_names', methods=['GET'])
# def get_location_names_route():
#     locations = get_location_names()
#     print("Locations:", locations)
#     response = jsonify({
#         'locations': locations
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/predict_home_price', methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     response = jsonify({
#         'estimated_price': get_estimated_price(location, total_sqft, bhk, bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Home Price Prediction...")
#     load_the_data()
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import json
import numpy as np

app = Flask(__name__)
CORS(app)


__data_columns = None
__model = None

@app.route('/')
def index():
    return render_template('index.html')

def load_the_data():
    global __data_columns
    # global __locations

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


# @app.route('/')
# def get_location_names_1():
#     locations_data = __locations
#     print("Locations:", locations_data)
#     response = jsonify({
#         'locations': locations_data
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return render_template('index.html', locations=locations_data)
#



@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    load_the_data()
    app.run(debug=True)
