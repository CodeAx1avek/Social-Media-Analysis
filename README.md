Social Media Performance Analysis - Pre-Hackathon Assignment
Overview

The Social Media Performance Analysis project is a basic analytics tool I developed as part of the Level Supermind Hackathon pre-hackathon assignment. The tool leverages Langflow, DataStax Astra DB, and Groq to analyze engagement data from mock social media accounts and provide insights into how different post types (like carousel, reels, static images) perform. The project aims to help users understand how various social media formats impact engagement through likes, shares, and comments.
Hackathon Details

    Assignment: Pre-Hackathon Social Media Performance Analysis
    Deadline: January 8th, 2025
    Hackathon Link: Level Supermind Hackathon - Social Media Analysis

Objective

The main objective was to develop an analytics module that:

    Simulates engagement data for social media posts (likes, shares, comments).
    Stores this data in DataStax Astra DB.
    Analyzes post performance based on these metrics.
    Provides insights using Groq based on the data.

Tools & Technologies Used

    DataStax Astra DB: A cloud database service used to store and query social media engagement data.
    Langflow: A tool used to create workflows, allowing integration of Groq for generating insights based on the analyzed data.
    Chart.js: A library used to visualize the data in bar charts (for likes, shares, and comments).
    HTML/CSS/JavaScript: Technologies used for building the web interface.

Features
1. Data Generation & Storage

I generated a small mock dataset representing social media engagement data (such as likes, shares, comments) for different post types (carousel, reels, static images). This dataset was stored in DataStax Astra DB for further analysis. The data includes the following metrics:

    Likes
    Shares
    Comments
    Post Types

2. Post Performance Analysis

Using Langflow, I created a simple workflow that:

    Accepts different post types as input (carousel, reels, static images).
    Queries the dataset in Astra DB to calculate the average engagement metrics (likes, shares, comments) for each post type.

This workflow allows you to analyze and compare how different post types perform in terms of engagement.
3. Insights Generation

With Groq integration via Langflow, I utilized Groq to generate simple insights based on the data. Some example outputs include:

    "Carousel posts have 20% higher engagement than static posts."
    "Reels drive 2x more comments than static images or carousels."

These insights can help users understand the impact of different content types on their social media engagement and make data-driven decisions.
How to Use
1. Clone the Repository

To get started, clone this repository to your local machine:

[git clone https://github.com/your-username/social-media-performance-analysis.git](https://github.com/CodeAx1avek/Social-Media-Analysis.git)

2. Install Dependencies

Install the required dependencies for the project. If you're using Python for the backend (e.g., Flask or Django), you can install the necessary libraries:

cd Social-Media-Analysis 
pip install -r requirements.txt

3. Set Up DataStax Astra DB

    Create an account at DataStax Astra.
    Set up a new database and download the secure connect bundle.
    Update the database credentials and connection details in your configuration file.
    Use langflow api

5. Run the Application

Run the app locally using the following commands:

    For Flask:

flask run

    Or:

python app.py

The app will be accessible at http://localhost:5000.
5. Interact with the Web Interface

The web interface allows users to:

    View interactive charts that display engagement data for likes, shares, and comments.
    Interact with the chatbot to analyze post performance.
    Receive insights from the chatbot based on the data.

Demo Video

Here’s a link to my demo video that walks through the project and explains how it works:

    Watch Demo Video

In the demo, I explain:

    How Langflow was used to create the workflow.
    How DataStax Astra DB is used for data storage and querying.
    How Groq generates insights based on the social media data.

Project Links

    GitHub Repository
    Google Drive Link (if applicable for code ZIP file)
    
Conclusion

This project demonstrates the power of combining data storage, workflow automation, and AI insights to help social media managers and content creators optimize their engagement strategies. The analysis and insights generated from this project can guide content creators in making data-driven decisions to boost engagement and grow their social media presence.

Thank you for checking out my project!
