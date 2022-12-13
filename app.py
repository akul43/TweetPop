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
    #Take input and run tweets query
    output = request.form.to_dict() #User Input
    keyword = scraper.run_query(output['keyword']) #Run Tweet Search with given keyword
    return render_template('index.html', len = len(keyword), keyword = keyword) #Send result to html page which will display the tweet text and link



if __name__ == "__main__":
    app.run(use_reloader = True, debug=True) #App run settings