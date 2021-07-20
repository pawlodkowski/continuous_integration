"""
This is the *C*ontroller part of the MVC

(the templates are the *V*iew part of the MVC)

If we had a database, that would be the *M*odel part
"""
from flask import Flask, render_template, request, jsonify
from simple_recommender import get_recommendations, movies, dummy_rec, DummyRecommender


# TODO: drop-down menu where you can find movies
# TODO: text field that autocompletes movie names

app = Flask(__name__)

  
@app.route('/')
def index():
    names = '["Titanic", "Das Boot", "Star Wars", "Pulp Fiction"]'
    return render_template('index.html', movienames=names)


@app.route('/recommender')
def recommender():
    print(request.args)  # variables from the URL arrive here

    name = request.args['movie']
    rating = request.args['rating']
    # TODO: allow user to enter 2+ movies

    top1 = dummy_rec.recommend()  # example only, does nothing

    top3 = get_recommendations(name, rating)
    numbers = [1, 7, 42]   #                      vvvv transport data from a Python function to HTML vvvvv
    return render_template('recommendation.html', movies=top3, title='Your Recommendations', numbers=numbers)  # Jinja2 template
    # a variable 'movies' is available in the template


@app.route('/movielist')
def movielist():
    """We have an API!!!"""
    return jsonify(movies)



if __name__ == "__main__":
    # this block of code is only executed when we exeute this file explicitly.
    
    # if you have this, you can run the development server with `python application.py`
    app.run(debug=True, port=5000)