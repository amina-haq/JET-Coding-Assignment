# Just Eat Takeaway Assessment - Restaurant Finder

This is a Flask web application that allows users to search for the restaurants in the UK via postcode.
It fetches data form an API address and displays data such as Name, Cuisines, Rating and Address for each
restaurant. The interface is simple and User-friendly, with a search bar, restaurant cards and responsive 
layout.

## Features

** Enter a UK postcode to display the first 10 restaurants in that area
** Each restaurant card shows name, cuisines, rating, and address
** Clear error message will appear if the postcode is invalid or no restaurants are found
** “Clear Search” button appears after performing a search

## Installation

To build and run the application, follow the outlined steps bellow:

**1) Clone the repository:**
```bash
git clone https://github.com/amina-haq/JET-Coding-Assignment
cd JET-Coding-Assignment
```

**2) Install dependencies:**
```bash
pip install -r requirements.txt
```
Run the above code in the terminal 

**3) Run the Flask app:**
```bash
python app.py
```

**4) Open your browsker and go to:**
```bash
http://127.0.0.1:8000/
```
## Assumptions 
** Only UK postcodes are supported because the Just Eat API does not return results for non-UK addresses
** Users can search any UK postcode, providing flexibility compared to hardcoding a postcode
** If a postcode is invalid or has no restaurants, an error message will be displayed instead of an empty page

## Improvments
** Navigation & Multiple Pages – add a navigation bar with “Home,” “Restaurants,” and “Contact” pages
** Enhanced UI/UX – use a responsive grid layout, larger restaurant cards, and visually appealing design elements
** Mobile Support – implement media queries to ensure the grid collapses properly on smaller screens
** Filtering Options – include filtering by cuisine type, minimum rating, or dietary
** Include filteraruion for dieraty requiremtsnt so only first 1o restutanrs are shown for specific requimrent
** Pagination – add pagination if more than 10 restaurants are returned
** Unit Testing – add automated tests for API integration and restaurant filtering, ensuring everything works as expected

## Technology Used
** Python
** Flask
** HTML/CSS
