# Just Eat Takeaway Assessment - Restaurant Finder

This is a Flask web application that allows users to search for the restaurants in the UK via postcode.
It fetches data form an API address and displays data such as Name, Cuisines, Rating and Address for each
restaurant. The interface is simple and User-friendly, with a search bar, restaurant cards and responsive 
layout.

## Features

* Enter a UK postcode to display the first 10 restaurants in that area
* Each restaurant card shows name, cuisines, rating, and address
* Clear error message will appear if the postcode is invalid or no restaurants are found
* “Clear Search” button only appears after performing a search

## How It Works
When the user enters a UK postcode in the search bar, the Flask app sends a request to the API to get restaurant data for that area. The JSON response from the API is parsed to extract only the relevant information: name, cuisines, rating, and address. The first 10 restaurants are displayed as individual cards on the webpage. The interface is designed to be simple and user-friendly, with a “Clear Search” button appearing after a search to allow users to easily start a new query.

## Installation

To build and run the application, follow the outlined steps below:

*1) Clone the repository:*
```bash
git clone https://github.com/amina-haq/JET-Coding-Assignment
cd JET-Coding-Assignment
```

*2) Install dependencies:*
Run the below code in the terminal 
```bash
pip install -r requirements.txt
```

*3) Run the Flask app:*
```bash
python app.py
```

*4) Open your browser and go to:*
```bash
http://127.0.0.1:8000/
```
## Assumptions 
* Only UK postcodes are supported because the Just Eat API does not return results for non-UK addresses
* Users can search any UK postcode, providing flexibility compared to hardcoding a postcode
* If a postcode is invalid or has no restaurants, an error message will be displayed instead of an empty page

## Improvements
* Navigation & Multiple Pages – add a navigation bar with 'Home', 'Restaurants', and 'Contact' pages
* Enhanced UI/UX – use a responsive grid layout, larger restaurant cards, and visually appealing design elements
* Mobile Support – implement media queries to ensure the grid collapses properly on smaller screens
* Filtering Options – include filtering by cuisine type, minimum rating, or dietary
* Include filtering for dietary requirements so only first 10 restaurants are shown for specific requirement
* Pagination – add pagination if more than 10 restaurants are returned
* Unit Testing – add automated tests for API integration and restaurant filtering, ensuring everything works as expected

## Technology Used
* Python
* Flask
* HTML/CSS
