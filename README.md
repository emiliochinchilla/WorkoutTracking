Workout Tracker with Nutritionix & Sheety Integration

This project is a simple Workout Tracker that allows you to log exercises using the Nutritionix API to calculate calorie burn and the Sheety API to store the workout data in a Google Spreadsheet.
Features

    User Input: The app accepts user input about exercises and processes them through the Nutritionix API to calculate the duration and calories burned.
    Google Spreadsheet Logging: Logs the workout data (exercise name, duration, and calories burned) into a Google Sheet via the Sheety API.
    Error Handling: Proper error handling for API requests to ensure the application does not crash on failures.

Technologies

    Python: Main programming language.
    Nutritionix API: To process exercises and calculate calorie burn.
    Sheety API: To log the exercises into a Google Spreadsheet.
    dotenv: For managing environment variables securely.

Prerequisites

To run this project, you will need:

    A Nutritionix account to access their API:
        Sign up at Nutritionix Developer and get your x-app-id and x-app-key.

    A Sheety account to access their API:
        Sign up at Sheety and create a new project. Set up a Google Spreadsheet for logging the workout data and get your API URL and Bearer token.

    Python 3.x installed on your system.

    dotenv to handle environment variables. You can install it using the following command:

    bash

    pip install python-dotenv

Setup Instructions

    Clone the repository:

    bash

git clone https://github.com/yourusername/workout-tracker.git
cd workout-tracker

Install the required Python packages:

bash

pip install requests python-dotenv

Create a .env file in the root directory with your API keys:

bash

touch .env

Inside .env, add your API credentials:

bash

NUTRI_APPLICATION_ID=your_nutritionix_app_id
NUTRI_API_KEY=your_nutritionix_api_key
SHEETY_TOKEN=your_sheety_bearer_token

Update the SHEETY_ENDPOINT in the Python file to match your Sheety API endpoint. This endpoint will look something like:

bash

https://api.sheety.co/your_project_id/myWorkouts/workouts

Run the Python script:

bash

    python main.py

    Enter the exercises you performed when prompted, and the workout data will be logged to your Google Spreadsheet automatically!

Usage

When running the script, you will be prompted to enter the exercises you performed:

bash

Tell me which exercises you did: 

You can enter exercises in a natural language format (e.g., "ran 3 miles", "swam for 30 minutes"), and the program will process them, calculate the calories burned, and log the data in your Google Spreadsheet.
Example

    Input:

    bash

Tell me which exercises you did:
ran 3 miles

Output:

json

    {"workout": {"date": "18/10/2024", "time": "12:30:45", "exercise": "ran 3 miles", "duration": 30, "calories": 350}}

The workout will be added to your Google Sheet with the current date, time, exercise, duration, and calories burned.
Error Handling

    If there's an issue with the Nutritionix API, the script will display an error message and skip logging that entry.
    If there's an issue posting data to Sheety, it will also handle the error and provide a message without crashing the script.
