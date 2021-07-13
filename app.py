from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
"""debugtoolbar secretkey can use 'import os' for a random one"""
app.config['SECRET_KEY'] = 'xfd1234'

debug = DebugToolbarExtension(app) 
"""home page decorator and function"""
@app.route("/")
def get_prompts():
    """Get words from form for story prompts"""
    prompts = story.prompts
    return render_template("prompts.html", prompts=prompts)

@app.route("/story")
def story():
    """Generate story output from user input"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
