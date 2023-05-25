import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Get CPU and memory metrics using psutil library
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    
    # Check if CPU or memory usage exceeds 80%
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    
    # Render the index.html template and pass metrics and message to the template
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

if __name__=='__main__':
    # Run the Flask application in debug mode on all network interfaces
    app.run(debug=True, host='0.0.0.0')
