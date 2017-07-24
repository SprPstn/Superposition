Twitter - IFTTT -> @{{UserName}} ||| {{Text}} ||| {{LinkToTweet}} ||| {{CreatedAt}}  Google Sheet JSON 


Adaptors (key: Value)

 CreatedAt => "July 05, 2017 at 02:50AM" [%b %d, %Y at %H:%M%p] > 

 2PACX-1vRrVw6mrRuubgrBiXjnBIRl3WGq0rgWIMMww5sFlp_NgR_T0sYhdCoXGd4Rl89suTNvCsNoNJRZHLWL

 https://docs.google.com/spreadsheets/d/e/2PACX-1vQcXSz5dVS-mRxf3Dsu9h-mQVgVv1U3Gl6qqCOjPIqXbDrdtvmWb71ZxRyg5QypGTLZnkaqx8R6-voI/pubhtml
https://docs.google.com/spreadsheets/d/e/2PACX-1vQcXSz5dVS-mRxf3Dsu9h-mQVgVv1U3Gl6qqCOjPIqXbDrdtvmWb71ZxRyg5QypGTLZnkaqx8R6-voI/pubhtml

2PACX-1vQcXSz5dVS-mRxf3Dsu9h-mQVgVv1U3Gl6qqCOjPIqXbDrdtvmWb71ZxRyg5QypGTLZnkaqx8R6-voI


>>> from time import gmtime, strftime
'Thu, 28 Jun 2001 14:17:15 +0000'
>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
sprintf strptime() 


Scrap -> Scrub -> Store -> Recall





naming convention ideas ->> twitter
adaptor convertning JSON

   PANDAS_JSON (WWWWHASH)


builder --> mysql 
    
    create table [UserName, tText, LinkToTweet, CreatedAt, why[message], hashlocation]

  Usage: gsjson <spreadsheet-id> <file> [options]


  Options:

    -V, --version                output the version number
    -u, --user [user]            User to login
    -p, --password [password]    Password to login
    -t, --token [token]          Auth token acquired externally
    -y, --tokentype [tokentype]  Type of the informed token (defaults to Bearer)
    -w, --worksheet <n>          Worksheet index
    -c, --hash [column]          Column to hash the final JSON
    -i, --vertical               Use the first column as header
    -l, --list-only              Ignore headers and just list the values in arrays
    -b, --beautify               Beautify final JSON
    -h, --help                   output usage information


[
    {
        "@kaspers75": "@MrBadGuy5270",
        "rt@tagesspiegel:#dgbChef#hoffmannZumWahlprogrammVon#cdu&amp;#csu:\"gerechtGehtAnders\"Https://t.co/c2z9iysfba#btw17Https://t.co/rbubqazchk": "RT @Harald70199: Kopfwäsche für verwirrte #Linke Terroristen und deren Schutztruppen bestehend aus #Verdi #DGB #Grüne #SPD Anhänger… https://t.co/UR2h4pyw1x",
        "http://twitter.com/kaspers75/status/882491411094016000": "http://twitter.com/MrBadGuy5270/status/882491944169070592",
        "july05,2017At02:48am": "July 05, 2017 at 02:50AM"

    },

########################################################################3
pandas



import json
import pandas as pd

df = pd.DataFrame.from_records(map(json.loads, json_lst))


#digibyte
gsjson 1hAT5hBv70fLAPRCGRBf8DKSXpB68abyfGAfG-allZU [pair].json -b

#eth
1MQtl18A_u-PyzdXsFsQrYRIQn_VBAbeAFRDwtd29m2o




