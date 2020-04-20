# COVID-19_Infection_Probability_Dectector
A Machine Learning Model that do predict you the probability of having the infection.
At first the model predict the probability of having the infection by the Logistic Regression.
Keep in mind that the data is NOT real and I have assume data's features and label. 
In back, I've run the flask server, which recieves data features by GET method and sends data by POST.
The HTML+CSS form send the data to the flask server and the ML model, the "myTraining" file predict the infection's probability.
By PSOT method the server sends the probability's value to form and it shows.
