document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('dataset').addEventListener('change', handleFileUpload);
});

function handleFileUpload(event) {
    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.variables) {
            populateVariableSelection(data.variables);
        } else if (data.error) {
            console.error('Error:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function populateVariableSelection(variables) {
    const variableXSelect = document.getElementById('variableX');
    const variableYSelect = document.getElementById('variableY');

    // Clear existing options
    variableXSelect.innerHTML = '';
    variableYSelect.innerHTML = '';

    // Add a default option
    variableXSelect.add(new Option('Select Variable for X-axis', ''));
    variableYSelect.add(new Option('Select Variable for Y-axis', ''));

    // Populate with new options
    variables.forEach(variable => {
        variableXSelect.add(new Option(variable, variable));
        variableYSelect.add(new Option(variable, variable));
    });
}

function generatePlot() {
    const chartType = document.getElementById('chartType').value;
    const variableX = document.getElementById('variableX').value;
    const variableY = document.getElementById('variableY').value;
    const datasetPath = document.getElementById('dataset').value;

    // Ensure that the user has selected a chart type and variables
    if (!chartType || !variableX || !variableY) {
        alert('Please select a chart type and variables.');
        return;
    }

    const requestData = {
        dataset_path: datasetPath, // This will be handled differently based on how you store the uploaded file
        chart_type: chartType,
        column_x: variableX,
        column_y: variableY
    };

    fetch('/generate_plot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.plot) {
            displayPlot(data.plot);
        } else if (data.stats) {
            displayStatistics(data.stats);
        } else if (data.error) {
            console.error('Error:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayPlot(plotData) {
    const plotDiv = document.getElementById('plot');
    plotDiv.innerHTML = ''; // Clear any previous plots
    const plot = document.createElement('div');
    plotDiv.appendChild(plot);

    Plotly.newPlot(plot, plotData.data, plotData.layout);
}

function displayStatistics(stats) {
    // Function to display descriptive statistics
    // ...
}
