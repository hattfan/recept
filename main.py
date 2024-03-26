import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from waitress import serve

app = Flask(__name__)
scheduler = BackgroundScheduler()

def job():
    print("Scheduled job executed")

scheduler.add_job(job, 'interval', seconds=10)
scheduler.start()

@app.route("/")
def home():
    return "Hello, World!"
    
# if __name__ == "__main__":
#     app.run(debug=False)
port = int(os.environ.get('PORT', 5000))

serve(app, listen=f'*:{port}')