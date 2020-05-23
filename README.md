# COVID-19 Infection Probability Detector
A Machine Learning Model that do predict you the probability of having the infection.
At first the model predict the probability of having the infection by the Logistic Regression.
Keep in mind that the data is NOT real and I have assume data's features and label.

In backend, I've run the flask server, which recieves data features by GET method from an HTML form which I've designed beautifully and sends data by POST to the form which shows the resultant probability.

At first the HTML + CSS form send the data to the flask server and then the ML model, which is in "myTraining" file, predicts the infection's probability.

Then by PSOT method the server sends the probability's value to form and it shows.

# The Data
Here the I didn't find any relevent data set that can actually do this job for me. So that's why I've just assumed and created this data set on my own.

## Features of Data
1. bodyPain
2. Age
3. runningNose
4. diffBreath

## Label of Data
The label or this attribute which our model is said to predict is the "infectionProb".
