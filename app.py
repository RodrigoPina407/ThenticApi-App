from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-nft', methods = ['POST'])
def createNft():
    print("teste")
    url = 'https://thentic.tech/api/nfts/contract'
    headers = {'Content-Type': 'application/json'}
    
    data = {'key': request.form['apiKey'],
            'chain_id': request.form['chainId'],
            'name': request.form['nftName'], 
            'short_name': request.form['nftSymbol']}
    
    ##r = requests.post(url, json=data, headers=headers)

    return request.form['apiKey']

