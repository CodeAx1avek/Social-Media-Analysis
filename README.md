Social Media Performance Analysis - Pre-Hackathon Assignment
Overview

The Social Media Performance Analysis project is a basic analytics tool developed for the Level Supermind Hackathon Pre-Hackathon Assignment. The tool uses Langflow, DataStax Astra DB, and Groq to analyze engagement data from mock social media accounts and provide insights into how different post types (carousel, reels, static images) perform in terms of likes, shares, and comments. The project aims to help users understand how various social media formats impact engagement metrics.
Hackathon Details

    Assignment: Pre-Hackathon Social Media Performance Analysis
    Deadline: January 8th, 2025
    Hackathon Link: Level Supermind Hackathon - Social Media Analysis

Objective

The main objective of this project was to develop an analytics module that:

    Simulates engagement data for social media posts (likes, shares, comments).
    Stores this data in DataStax Astra DB.
    Analyzes post performance based on these metrics.
    Provides insights using Groq based on the analyzed data.

Tools & Technologies Used

    DataStax Astra DB: Cloud-based database used to store and query social media engagement data.
    Langflow: A workflow creation tool that integrates with Groq to generate insights from the data.
    Groq: An AI-powered language model integrated into Langflow to generate insights from engagement data.
    Chart.js: A JavaScript library used to visualize the data in bar charts (for likes, shares, and comments).
    HTML/CSS/JavaScript: Front-end technologies used to build the user interface of the web application.

Features
1. Data Generation & Storage

A small mock dataset was generated representing social media engagement data for different post types (carousel, reels, static images). This dataset includes the following metrics:

    Likes
    Shares
    Comments
    Post Types

The data was then stored in DataStax Astra DB for further analysis.
2. Post Performance Analysis

Using Langflow, a simple workflow was created to:

    Accept different post types as input (carousel, reels, static images).
    Query the dataset in Astra DB to calculate the average engagement metrics (likes, shares, comments) for each post type.

This allows users to analyze and compare how different post types perform in terms of engagement.
3. Insights Generation

With Groq integration via Langflow, insights were generated based on the engagement data. Example insights include:

    "Carousel posts have 20% higher engagement than static posts."
    "Reels drive 2x more comments than static images or carousels."

These insights help users understand the impact of different content types on social media engagement and assist in making data-driven decisions.
How to Use
1. Clone the Repository

Clone the repository to your local machine using the following command:

git clone https://github.com/CodeAx1avek/Social-Media-Analysis.git

2. Install Dependencies

Navigate to the project directory and install the required dependencies:

cd Social-Media-Analysis
pip install -r requirements.txt

3. Set Up DataStax Astra DB

    Create an account at DataStax Astra.
    Set up a new database and download the secure connect bundle.
    Update the database credentials and connection details in your configuration file.
    Use the Langflow API to integrate the database with your workflow.

4. Run the Application

To run the app locally, execute the following command:

    For Flask:

flask run

Or:

python app.py

This will start the app and make it accessible at http://localhost:5000.
5. Interact with the Web Interface

The web interface allows users to:

    View interactive charts that display engagement data for likes, shares, and comments.
    Interact with a chatbot to analyze post performance.
    Receive insights from the chatbot based on the data.

## Demo Video

Here’s a link to the demo video where I explain how the project works:

[Watch the Demo Video](https://youtu.be/mh8OztiQgt8?si=kvvuiI4uTjVFzHo7)

In the video, I explain:
- How Langflow was used to create the workflow.
- How DataStax Astra DB is used for data storage and querying.
- How Groq generates insights from the data.


Project Links

    GitHub Repository
    Google Drive Link (if applicable for code ZIP file)

Conclusion

This project demonstrates the power of combining data storage, workflow automation, and AI insights to help social media managers and content creators optimize their engagement strategies. The analysis and insights generated from this project can guide content creators in making data-driven decisions to boost engagement and grow their social media presence.

Thank you for checking out my project!
