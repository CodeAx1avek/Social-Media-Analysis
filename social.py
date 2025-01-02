import csv
import random

# Post types with more variety
post_types = [
    "Carousel", 
    "Static", 
    "Reel",
    "Story",
    "Live Video",
    "IGTV",
    "Poll",
    "Quiz",
    "Text Post",
    "Short Video"
]

# Generate mock data
data = [
    {
        "Post_Type": random.choice(post_types),
        "Likes": random.randint(50, 300),
        "Shares": random.randint(10, 100),
        "Comments": random.randint(5, 75),
    }
    for _ in range(500)
]

# Save to CSV
with open("mock_social_media_data.csv", "w", newline="") as csvfile:
    fieldnames = ["Post_Type", "Likes", "Shares", "Comments"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print("Mock dataset created: mock_social_media_data.csv")





import os
import pandas as pd
from django.shortcuts import render
from django.conf import settings
import json

def home(request):
    # Path to the CSV file
    csv_path = os.path.join(settings.BASE_DIR, 'app', 'social_media_data.csv')
    
    # Check if the file exists
    if not os.path.isfile(csv_path):
        return render(request, 'home.html', {"error": f"File not found at {csv_path}"})
    
    # Read the CSV file
    data = pd.read_csv(csv_path)

    # Prepare the data for the chart
    chart_data = {
        "labels": data["Post_Type"].tolist(),
        "datasets": [
            {
                "label": "Likes",
                "data": data["Likes"].tolist(),
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1,
            },
            {
                "label": "Shares",
                "data": data["Shares"].tolist(),
                "backgroundColor": "rgba(255, 159, 64, 0.2)",
                "borderColor": "rgba(255, 159, 64, 1)",
                "borderWidth": 1,
            },
            {
                "label": "Comments",
                "data": data["Comments"].tolist(),
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1,
            },
        ],
    }

    # Pass the chart data to the template
    return render(request, 'home.html', {"chart_data": json.dumps(chart_data)})