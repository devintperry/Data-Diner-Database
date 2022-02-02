Data Diner is a demo of utilization of psycopg2 and pgAdmin to implement a Python based UI.
This UI is in the form of a fake restaurant, a "Data Diner." 

This program requires a postgres database to connect to the interface. 
Uploaded alongside the main code is the example database utilized for this purpose, with EER connectivity in Boyde-Codd Normal Form.
This code also serialized transactions and cleanses inputs, aiming to reduce any possible SQL injection.

Transactions include role handling (customer, manager, various employee positions), database verifications, connectivity verification, and an easy to use lightweight UI.
