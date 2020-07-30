from flask import Flask, abort, jsonify, request # importing Flask Lib. into the Python program as flask

import random

## API code starts from here##

app = Flask(__name__) # initialize the Flask APP

@app.route('/hello', methods=['GET'])
def makeRequest():
    
    return jsonify("response","Hello")

@app.route('/quotes', methods=['GET'])
def getQuote():
    QuoteList = ["I have always believed that each man makes his own happiness and is responsible for his own problems. It is a simple philosophy",
                 
    "When we have respect for ourselves and others, we gravitate towards connections that encourage that.",
                 
    "A man should have the aim and the determination to be honest and upright and sincere in all that he undertakes. If he adds persistency to this he can hardly help being successful ",
    "The fact is that grief today is a family matter as much a s it is an individual",
    "Children really brighten up a household. They never turn the lights off." ]

    n = random.randint(0,4)
    
    quote = QuoteList[n]

    return jsonify("response",quote)

@app.route('/getSpecifiedQuote', methods=['POST'])
def getSpecifiedQuote():
    data = request.get_json(force=True)

    num = data.get("number")

    QuoteList = ["I have always believed that each man makes his own happiness and is responsible for his own problems. It is a simple philosophy",
                 
    "When we have respect for ourselves and others, we gravitate towards connections that encourage that.",
                 
    "A man should have the aim and the determination to be honest and upright and sincere in all that he undertakes. If he adds persistency to this he can hardly help being successful ",
    
    "The fact is that grief today is a family matter as much a s it is an individual",
    
    "Children really brighten up a household. They never turn the lights off." 
    ]
    quote = QuoteList[num]
    
    dit = { "Quote":quote, "Position":num}
    
    return jsonify("response",dit)

if __name__ == "__main__":
    app.run(debug=True)