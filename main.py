from flask import Flask, render_template, request
app = Flask(__name__)
import pickle


# open a file, where you want to store the data
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        # print(request.form)
        myDictionary = request.form
        fever = int(myDictionary['fever'])
        age = int(myDictionary['age'])
        bodyPain = int(myDictionary['bodyPain'])
        runningNose = int(myDictionary['runningNose'])
        diffBreath = int(myDictionary['diffBreath'])
        # Code for inference (for probability)
        inputFeatures = [fever, bodyPain, age, runningNose, diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html', inf=round(infProb*100))
    # return 'Hello World' + str(infProb)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)