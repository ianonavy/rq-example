"""Serve main application.

Defer actual job execution to background worker using RQ.
"""

import flask
from flask import redirect
from flask import request
from flask import url_for
from redis import Redis
from rq import Queue

from tasks import evaluate_bidder


app = flask.Flask(__name__)
q = Queue(connection=Redis())  # connect to localhost redis


@app.route('/')
def index():
    job_id = request.args.get('job_id')
    if job_id is None:
        return 'Please pass ?job_id=XXXX'
    job = q.enqueue(evaluate_bidder, job_id)
    redirect_url = url_for('results', job_id=job.id)
    app.logger.info("Redirecting to %s", redirect_url)
    return redirect(redirect_url)


@app.route('/results/<job_id>')
def results(job_id):
    job = q.fetch_job(job_id)
    if job.result is None:
        response = 'Still waiting! Please refresh.'
    else:
        response = str(job.result)
    return response



if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)
