# Simple Shopping Application
A web application that emulates an online shopping experience.

# Motivation
Applying what I learned in class, in attempts, to explore different types of applications that have been used before.

# Tech Stack/Programming languages
 - Main: Python- Flask
 - Others: HTML, CSS
 - Database: PostgreSQL

# Build Details

I started with the homepage to visualize how everything would fall into place:

 - 
 
Next, I added a shopping cart tab with functionality to ensure each item appears in the cart:

 - 
 
I made a dictionary that held "dummy data" to create the logic that sums the total in the shopping cart. After completing the logic, I went back and added a database through "PostgreSQL" that held the same data shown on the website (and the dictionary I used). Additionally, I adjusted the logic to fit the database methods in the "repository/shopping_repo.py" file that fetches data utilizing "psycopg":

 - 
 
Lastly, I added a connection pool using psycopg's connectionPool() method to access the database and the connection() method for traffic flow.

# Things that I will attempt to do in the future
Next on my list is writing test cases to make sure that the website is functioning properly.

I may apply a quantity section in the "shopping cart" tab so that items are not repeated!
