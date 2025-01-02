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
