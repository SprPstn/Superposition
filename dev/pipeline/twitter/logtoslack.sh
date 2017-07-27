#!/bin/bash
 
tail -n0 -F "$1" | while read LINE; do
  (echo "$LINE" | grep -e "$3") && curl -X POST --silent --data-urlencode \
    "payload={\"text\": \"$(echo $LINE | sed "s/\"/'/g")\"}" "$2";
done

#To use this script, save it as an executable script and simply pass the path to the log file and a webhook url to this script.


#./tail-slack.sh "file.log" "https://hooks.slack.com/services/...";
#1
#./tail-slack.sh "file.log" "https://hooks.slack.com/services/...";