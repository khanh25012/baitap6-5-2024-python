from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import random

app = FastAPI()
# random data lượng mưa và độ ẩm
def generate_random_rainfall():
    return round(random.uniform(500, 700), 2)

def generate_random_humidity():
    return round(random.uniform(70, 90), 2)
#đọc data
@app.get("/", response_class=HTMLResponse)
async def read_data():
    rainfall = generate_random_rainfall()
    humidity = generate_random_humidity()
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rainfall and Humidity Data</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                }}
                #data-container {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                p {{
                    margin: 10px 0;
                    font-size: 1.2em;
                }}
                button {{
                    display: block;
                    margin: 0 auto;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Rainfall and Humidity Data</h1>
                <div id="data-container">
                    <p><i class="fas fa-cloud"></i> Thai Nguyen</p>
                    <p id="rainfall"><i class="fas fa-cloud-rain"></i> Rainfall: <span id="rainfall-value">{rainfall}</span> ml</p>
                    <p id="humidity"><i class="fas fa-tint"></i> Humidity: <span id="humidity-value">{humidity}</span> %</p>
                </div>
                <button onclick="refreshData()">Refresh Data</button>
            </div>

            <script>
                function refreshData() {{
                    fetch('/data')
                    .then(response => response.json())
                    .then(data => {{
                        document.getElementById('rainfall-value').innerText = data.rainfall;
                        document.getElementById('humidity-value').innerText = data.humidity;
                    }});
                }}

                refreshData(); // Load initial data when page loads
            </script>
        </body>
        </html>
    """.format(rainfall=rainfall, humidity=humidity)

@app.get("/data", response_class=JSONResponse)
async def get_data():
    rainfall = generate_random_rainfall()
    humidity = generate_random_humidity()
    return {"rainfall": rainfall, "humidity": humidity}
