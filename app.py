from flask import Flask, render_template, url_for, request
import scraper #Import our scraper python script

#Flask is used to communicate between python code and html page

app = Flask(__name__) #Create Flask App

 

@app.route('/') #Initial lode
@app.route('/home') #First page to be loaded
def home():
    #First html to open when link is loaded
    return render_template("index.html") #HTML file with our form


#Runs when Submit a text
@app.route('/result',methods=['POST', 'GET'])
def result():
    return render_template('index.html') #Send result to html page which will display the tweet text and link
    # !!! Possibly send another html page populated with tweets. 



if __name__ == "__main__":
    app.run(use_reloader = True, debug=True) #App running settings