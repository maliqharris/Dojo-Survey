from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
app = Flask(__name__) 
app.secret_key = "any string dawg"   # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response


@app.route('/handle_form', methods = ['post'])
def create():
    
    # code to processs data from form
    print(request.form)
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['dojolocation'] = request.form['dojolocation']
    session['comment'] = request.form['comment']
    return redirect('/result')



 
@app.route('/result')
def result():

    # if request.form["change"] == "goback":
    #     return redirect("/")
    # else:
    


        return render_template("result.html")







if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.