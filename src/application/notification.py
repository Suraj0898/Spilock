import requests


def http_post():
    r = requests.post('https://maker.ifttt.com/trigger/wrong_tap/with/key/bTL_QCxVgaPxfLFfpLPtl0',
                      params={"value1": "none", "value2": "none", "value3": "none"})
