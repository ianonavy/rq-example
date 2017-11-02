"""Background tasks for application.

Just simple functions. Can be entirely separate library or repo
if needed. Needs to be picklable.
"""
import time


def evaluate_bidder(bidder_job_id):
    # TODO: actually implement logic here instead of faking
    # how long it takes to run
    time.sleep(5)
    return 'Bidder evaluation for {}'.format(bidder_job_id)
