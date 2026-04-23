from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Dummy Data for Google Cloud Technologies Conference
schedule = [
    {
        "id": 1,
        "title": "Keynote: The Future of Google Cloud",
        "speakers": [
            {"first_name": "Sundar", "last_name": "Pichai", "linkedin": "https://linkedin.com/in/sundarpichai"}
        ],
        "category": ["Keynote", "Strategy"],
        "description": "Join our CEO for a look at the future of cloud computing and how Google is innovating to empower organizations worldwide.",
        "time": "09:00 AM - 10:00 AM",
        "is_lunch": False
    },
    {
        "id": 2,
        "title": "Scaling AI with Vertex AI",
        "speakers": [
            {"first_name": "Jeff", "last_name": "Dean", "linkedin": "https://linkedin.com/in/jeffdean"}
        ],
        "category": ["AI/ML", "Data"],
        "description": "Discover how Vertex AI helps machine learning practitioners build, deploy, and scale ML models faster.",
        "time": "10:00 AM - 11:00 AM",
        "is_lunch": False
    },
    {
        "id": 3,
        "title": "Cloud Native Architecture with Kubernetes",
        "speakers": [
            {"first_name": "Kelsey", "last_name": "Hightower", "linkedin": "https://linkedin.com/in/kelseyhightower"}
        ],
        "category": ["Containers", "Architecture"],
        "description": "Learn the best practices for running microservices reliably on Google Kubernetes Engine (GKE).",
        "time": "11:00 AM - 12:00 PM",
        "is_lunch": False
    },
    {
        "id": 4,
        "title": "Lunch Break",
        "speakers": [],
        "category": [],
        "description": "Take a 60-minute break to recharge, grab some food, and network with other attendees.",
        "time": "12:00 PM - 01:00 PM",
        "is_lunch": True
    },
    {
        "id": 5,
        "title": "Serverless Computing with Cloud Run",
        "speakers": [
            {"first_name": "Chloe", "last_name": "Condon", "linkedin": "https://linkedin.com/in/chloecondon"}
        ],
        "category": ["Serverless", "Compute"],
        "description": "Develop and deploy highly scalable containerized applications on a fully managed serverless platform.",
        "time": "01:00 PM - 02:00 PM",
        "is_lunch": False
    },
    {
        "id": 6,
        "title": "Modern Data Engineering with BigQuery",
        "speakers": [
            {"first_name": "Felipe", "last_name": "Hoffa", "linkedin": "https://linkedin.com/in/felipehoffa"}
        ],
        "category": ["Data", "Analytics"],
        "description": "Harness the power of serverless data warehousing to analyze petabytes of data using BigQuery.",
        "time": "02:00 PM - 03:00 PM",
        "is_lunch": False
    },
    {
        "id": 7,
        "title": "Zero Trust Security in the Cloud",
        "speakers": [
            {"first_name": "Parisa", "last_name": "Tabriz", "linkedin": "https://linkedin.com/in/parisatabriz"}
        ],
        "category": ["Security", "Networking"],
        "description": "Learn how to adopt a zero trust security model to protect your infrastructure and data on GCP.",
        "time": "03:00 PM - 04:00 PM",
        "is_lunch": False
    },
    {
        "id": 8,
        "title": "Hybrid Cloud Strategies with Anthos",
        "speakers": [
            {"first_name": "Thomas", "last_name": "Kurian", "linkedin": "https://linkedin.com/in/thomaskurian"}
        ],
        "category": ["Hybrid Cloud", "Strategy"],
        "description": "Manage applications consistently across on-premises and public cloud environments with Anthos.",
        "time": "04:00 PM - 05:00 PM",
        "is_lunch": False
    },
    {
        "id": 9,
        "title": "Closing Panel: Ask the Experts",
        "speakers": [
            {"first_name": "Jeff", "last_name": "Dean", "linkedin": "https://linkedin.com/in/jeffdean"},
            {"first_name": "Kelsey", "last_name": "Hightower", "linkedin": "https://linkedin.com/in/kelseyhightower"}
        ],
        "category": ["Panel", "Q&A"],
        "description": "An open Q&A session where you can ask our Google Cloud experts anything.",
        "time": "05:00 PM - 06:00 PM",
        "is_lunch": False
    }
]

@app.route('/')
def index():
    # Fetch current date dynamically
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    return render_template('index.html', schedule=schedule, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
