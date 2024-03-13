from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import json

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the file upload and extracting variables
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    
    # Check if the file is present and is of allowed file types
    if file and allowed_file(file.filename):
        try:
            # Read the file into a DataFrame
            df = read_file(file)
            
            # Extract the column names for variable selection
            variables = df.columns.tolist()
            return jsonify({'variables': variables})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'No file or invalid file type uploaded'})

# Route for processing data and returning plots or stats
@app.route('/generate_plot', methods=['POST'])
def generate_plot():
    content = request.json
    dataset_path = content['dataset_path']
    chart_type = content['chart_type']
    column_x = content['column_x']
    column_y = content['column_y']

    # You would handle file reading and figure creation here
    # ...

    # Respond with the generated plot or statistics
    # ...

# Helper function to read the file into a DataFrame
def read_file(file):
    if file.filename.endswith('.csv'):
        return pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        return pd.read_excel(file)

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['csv', 'xlsx']

if __name__ == '__main__':
    app.run(debug=True)
