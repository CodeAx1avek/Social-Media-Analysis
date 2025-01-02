Social Media Performance Analysis
Objective

The Social Media Performance Analysis project is a basic analytics module designed to evaluate the performance of social media posts using data from mock social media accounts. The project utilizes Langflow for workflow creation, DataStax Astra DB for storing engagement data, and GPT for generating insights based on the data.
Submission Details

    Pre-Hackathon Assignment: Social Media Performance Analysis
    Submission Deadline: January 8th, 2025
    Hackathon Link: Level Supermind Hackathon - Social Media Analysis

Tools & Technologies Used

    Langflow: Used to create a workflow to analyze engagement data and integrate GPT for insights.
    DataStax Astra DB: Used for storing and querying the social media engagement data.
    GPT Integration: Used for generating insights based on post performance.
    Chart.js: Used to visualize the data in bar charts (Likes, Shares, Comments).
    JavaScript/HTML/CSS: For building the user interface and displaying results interactively.

Task Overview

    Data Generation & Storage:
        A mock dataset simulating social media engagement data (likes, shares, comments, post types) was created.
        The data was stored in DataStax Astra DB for querying and analysis.

    Post Performance Analysis:
        A simple workflow was constructed in Langflow that:
            Accepts different post types (e.g., carousel, reels, static images).
            Queries the dataset from Astra DB to calculate average engagement metrics for each post type.

    Insights Generation:
        GPT was integrated into the workflow to generate insights based on engagement data, such as:
            Carousel posts have 20% higher engagement than static posts.
            Reels drive 2x more comments than static images or carousels.

How to Use
1. Clone the Repository

To run the project locally, start by cloning this repository:

git clone https://github.com/your-username/social-media-performance-analysis.git

2. Install Dependencies

Navigate to the project directory and install the required dependencies:

cd social-media-performance-analysis
# Install Python dependencies
pip install -r requirements.txt

3. Set Up DataStax Astra DB

    Create an account on DataStax Astra.
    Set up a new database and download the secure connect bundle.
    Update the configuration in the code (usually in a config.py or environment variables) with your Astra DB credentials and database URL.

4. Run the Application

For Flask (if you're using Flask as the backend):

flask run

For Django:

python manage.py runserver

The app should now be accessible locally at http://localhost:5000 (or the Django equivalent).
5. Interact with the Chatbot and View Analytics

    The web interface allows users to interact with the chatbot to analyze post performance.
    Charts for likes, shares, and comments will be displayed using Chart.js.
    The chatbot will provide insights based on the data stored in DataStax Astra DB.

Demo Video

    Link to Demo Video

In the demo video, I explain:

    How Langflow is used to create the workflow.
    How DataStax is used to store and query social media engagement data.
    How GPT is leveraged to generate insights based on the engagement metrics.

Project Links

    GitHub Repository
    Google Drive (Code ZIP) (if applicable)

Project Description

This project aims to showcase how data-driven insights can be leveraged to optimize social media content. By analyzing engagement data such as likes, shares, and comments, the tool provides key insights into which types of posts (carousel, reels, static images) perform the best, helping users make more informed decisions about their content strategy.
