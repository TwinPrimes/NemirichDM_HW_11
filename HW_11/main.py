from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = get_candidates_list()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id_>')
def candidate_page(id_):
    candidates = load_candidates_from_json()
    return render_template('card.html', candidates=candidates, id=id_)


@app.route('/search/<name>')
def candidates_search_page(name):
    candidates = get_candidates_by_name(name)
    candidates_number = len(candidates)
    return render_template('search.html', candidates_number=candidates_number, candidates=candidates)


@app.route('/skill/<skill_name>')
def candidates_skill_page(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    candidates_number = len(candidates)
    return render_template('skill.html', candidates_number=candidates_number,
                           candidates=candidates, skill_name=skill_name)


app.run()
