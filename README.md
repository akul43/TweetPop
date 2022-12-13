# Project Description

For this project, I created a Flask app using Python that allows users to search for the most popular tweets for a given keyword. The app uses the Twitter API to search for tweets and displays the results in a web page. The tweets are sorted by relevancy, with the most popular tweets appearing at the top of the page.

To build this app, I used Flask, a popular web framework for Python, to handle the routing and rendering of the web pages. I also used the Twitter API to search for tweets and retrieve their popularity data.

The app is designed to be user-friendly and intuitive. It has a simple and clean user interface, with a search bar at the top of the page where users can enter a keyword to search for tweets. The results are displayed in a grid layout, with each tweet shown as a card that includes the tweet text, the user's profile picture, and the number of likes and retweets.

Overall, this project showcases my skills in web development using Python and Flask, as well as my ability to work with APIs and databases. It provides a useful tool for users to search for popular tweets on a given topic, and it demonstrates my ability to build practical and engaging web applications

# Twitter API

I used the Twitter API to search for tweets and retrieve their popularity data. The Twitter API is a powerful and versatile tool that allows developers to access and interact with data from the Twitter platform. It provides various endpoints for searching, posting, and analyzing tweets, as well as for managing user accounts and interactions.

To use the Twitter API in my Flask app, I first had to register for a Twitter developer account and create an app. This gave me access to the API keys and tokens that I needed to authenticate my app and make API requests. I then used the Python requests library to make HTTP requests to the Twitter API endpoints and retrieve the data I needed.

In my app, I used the search/tweets endpoint to search for tweets that matched a given keyword. This endpoint allows you to specify various parameters, such as the language of the tweets, the date range, and the number of results to return. I used these parameters to fine-tune my search and retrieve the most relevant and popular tweets. I used the tweepy library in Python to implement the Twitter API in my Flask app. tweepy is a popular and easy-to-use library that provides a convenient wrapper for the Twitter API. It simplifies the process of making API requests and handling the data that is returned.

# Flask

This project is a Flask web app that allows users to search for the most popular tweets for a given keyword. Flask is a popular web framework for Python that provides a lightweight and modular way to build web applications. It is known for its simplicity and ease of use, making it a great choice for small and medium-sized projects.

To build the Flask app, I used the Flask framework to handle the routing and rendering of the web pages. I defined routes for the different pages of the app, such as the home page and the search results page.

I also used Flask to handle user input and requests. The app has a search bar at the top of the home page where users can enter a keyword to search for tweets. When the user submits the search form, Flask receives the request and uses the Twitter API to search for tweets that match the keyword. The results are then passed back to Flask, which renders the search results page with the tweets.

Overall, the Flask app provides a simple and intuitive interface for searching for popular tweets on a given topic. It showcases my skills in web development using Python and Flask, and it demonstrates my ability to build practical and engaging web applications.