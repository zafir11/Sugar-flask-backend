from flask import Blueprint, request, jsonify
import pandas as pd
import plotly.graph_objects as go
import os
from flask_cors import CORS

# Create a Blueprint instance
api = Blueprint("api", __name__)
CORS(api) 
# Define the route and associated view function
@api.route('/process_csv', methods=['POST'])
def process_csv():
    try:
        # Get the CSV file from the request
        file = request.files['file']
        
        # Save the file temporarily to disk
        file.save('temp.csv')
        
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv('temp.csv')
        
        # Create a candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=df['Time'],
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Last'],
                                            increasing_fillcolor='green',
                                            decreasing_fillcolor='red')])
        
        # Customize the layout (optional)
        fig.update_layout(title="Sugar Price Candlestick Chart",
                          xaxis_title="Date",
                          yaxis_title="Price",
                          xaxis_rangeslider_visible=False)
        
        # Convert the figure to JSON
        candlestick_data = fig.to_json()
        
        # Clean up the temporary CSV file
        os.remove('temp.csv')
        
        return jsonify(candlestick_data)

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify(error=str(e)), 500
