This project is for practicing web development as well as using flask.

This part is for design planning. It is like a checklist.

I first started with the homepage to visualize how everything will fall into place.
Next I added a shopping cart tab with functionality making sure that each item will appear in the cart. 
I made a dictionary that held "dummy data" so that I can create the logic that sums the total in the shopping cart. After completing the logic, I went back and added a database through "PostgreSQL" that held the same data shown on the website (and the dictionary I used). Additionally, I adjusted the logic to fit the database methods in the "repository/shopping_repo.py" file that fetches data utilizing "psycopg". Lastly, I added a connection pool using psycopg's connectionPool() method to access the database and the connection() method for traffic flow.

I may apply a quantity section in the "shopping cart" tab so that items are not repeated!
