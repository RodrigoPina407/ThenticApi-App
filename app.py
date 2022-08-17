from flask import Flask, render_template, request, redirect
import requests
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-nft', methods = ['POST'])
def createNft():
    url = 'https://thentic.tech/api/nfts/contract'
    headers = {'Content-Type': 'application/json'}
    
    data = {'key': request.form['apiKey'],
            'chain_id': request.form['chainId'],
            'name': request.form['nftName'], 
            'short_name': request.form['nftSymbol']}
    
    r = requests.post(url, json=data, headers=headers)
    webbrowser.open_new_tab(r.json()['transaction_url'])

    return redirect("/", code=302)

@app.route('/get-nft', methods = ['GET'])
def createNft():

