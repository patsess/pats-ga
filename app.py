
import logging
from flask import Flask, render_template

__author__ = 'psessford'

logging.basicConfig(level=logging.INFO)

"""
note: for details on deploying using Heroku, see 
https://stackabuse.com/deploying-a-flask-application-to-heroku/
"""


app = Flask(__name__)


@app.route('/')
def main_page():
    with open('static/texts/pyt6_course_description.txt', 'r') as f:
        pyt6_description = f.read()

    with open('static/texts/pyt6_course_feedback_scores.txt', 'r') as f:
        pyt6_feedback_scores = f.read()

    pyt6_feedback_scores = _parse_feedback_to_list(
        feedback_text=pyt6_feedback_scores)
    pyt6_feedback_scores = _style_pyt6_feedback_scores(
        pyt6_feedback_scores=pyt6_feedback_scores)

    with open('static/texts/pyt6_course_feedback_quotes.txt', 'r') as f:
        pyt6_feedback_quotes = f.read()

    pyt6_feedback_quotes = _parse_feedback_to_list(
        feedback_text=pyt6_feedback_quotes)

    return render_template(
        'ga_experience.html',
        pyt6_course_description=pyt6_description,
        pyt6_feedback_scores=pyt6_feedback_scores,
        pyt6_feedback_quotes=pyt6_feedback_quotes)


def _parse_feedback_to_list(feedback_text):
    feedback_list = feedback_text.split('\n')
    feedback_list = [f.strip() for f in feedback_list if f]
    return feedback_list


def _style_pyt6_feedback_scores(pyt6_feedback_scores):
    pyt6_feedback_scores = [
        s.replace('AVG', '<br /><strong>AVG') + '</strong>'
        for s in pyt6_feedback_scores]
    return pyt6_feedback_scores


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
