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

 - ![image](https://github.com/user-attachments/assets/972e4c86-1ddd-49fb-9878-a6b75237f1d6)

 
Next, I added a shopping cart tab with functionality to ensure each item appears in the cart:

 - ![image](https://github.com/user-attachments/assets/1bb06288-384c-48d5-9d1c-68d63fb4c11f)

 
I made a dictionary that held "dummy data" to create the logic that sums the total in the shopping cart. After completing the logic, I went back and added a database through "PostgreSQL" that held the same data shown on the website (and the dictionary I used). Additionally, I adjusted the logic to fit the database methods in the "repository/shopping_repo.py" file that fetches data utilizing "psycopg":

 - ![image](https://github.com/user-attachments/assets/db61c619-dda5-4272-863c-4d72dfcf918d)

 
Lastly, I added a connection pool using psycopg's connectionPool() method to access the database and the connection() method for traffic flow.
 - ![image](https://github.com/user-attachments/assets/b1cc8575-f323-4923-9460-c55a91c56e25)
 - And right before each Database task there is a "get_pool()":
      - ![image](https://github.com/user-attachments/assets/d36318fb-0582-42c6-8d9a-4689884ed77b)



# Things that I will attempt to do in the future
Next on my list is writing test cases to make sure that the website is functioning properly.

I may apply a quantity section in the "shopping cart" tab so that items are not repeated!
