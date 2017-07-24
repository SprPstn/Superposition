#!/usr/bin/env bash

gsjson 1hAT5hBv70fLAPwRCGRBf8DKSXpB68abyfGAfG-allZU dgb_$1.json -b
gsjson 1yBEvI-EUbM2xk7Ul9GE-ZDo81_WBAdraZw3mBDN29DM xrp_$1.json -b
gsjson 1hmB-Mx6J_NxTUUDI4yfYtTd2it92O_su6z9pEaAyyLQ eth_$1.json -b
curl -X POST -H 'Content-type: application/json' --data '{"text":"#DGB #ETH and #XRP JSON updated"}' https://hooks.slack.com/services/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
