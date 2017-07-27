#!/usr/bin/env python
import json
import logging
import requests
import signal
import sys

from config import config

from pygtail import Pygtail



# If there is not something passed to python then assume the default

if len(sys.argv) > 1:
    log = sys.argv[1]
else:
    log = config.get('eth.json')

signal.signal(signal.SIGINT, lambda s,f: sys.exit(0))

for line in Pygtail(log):
    sys.stdout.write(line)
    data = json.dumps({'text': line})

    ## This could be more general
    r = requests.post(config.get('https://hooks.slack.com/services/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'), data = data)

    logging.debug(r.text)