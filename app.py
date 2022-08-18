from flask import Flask, render_template, request
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

    return render_template('index.html', value = "Execute Transaction", transaction = r.json()['transaction_url'])

@app.route('/get-contracts', methods = ['POST'])
def getContracts():
    url = 'https://thentic.tech/api/contracts'
    headers = {'Content-Type': 'application/json'}
    data = {'key': request.form['apiKey'],
            'chain_id': request.form['chainId']
            }

    r = requests.get(url, json=data, headers=headers)

    contractList = []

    for c in r.json()['contracts']:
      if c['contract'] != None:
        contractList.append({'address': c['contract'], 'name':c['name']})

    return render_template('index.html', contracts= contractList)

@app.route('/mint-nft', methods = ['POST'])
def mintNft():
    url = 'https://thentic.tech/api/nfts/mint'
    headers = {'Content-Type': 'application/json'}
    
    data = {'key': request.form['apiKey'],
            'chain_id': request.form['chainId'],
            'contract': request.form['nftContract'],
            'nft_id': request.form['nftId'], 
            'nft_data': request.form['nftData'],
            'to': request.form['to']
            }
    
    r = requests.post(url, json=data, headers=headers)

    return render_template('index.html', value = "Execute Transaction", transaction = r.json()['transaction_url'])

@app.route('/get-nfts', methods = ['POST'])
def getNft():
    url = 'https://thentic.tech/api/nfts'
    headers = {'Content-Type': 'application/json'}
    
    data = {'key': request.form['apiKey'],
            'chain_id': request.form['chainId'],
            }
    r = requests.get(url, json=data, headers=headers)
    nftList = []

    for nft in r.json()['nfts']:
      if nft['status'] == 'success':
        nftList.append(
        {   'address': nft['contract'], 
            'name':nft['name'],
            'data':nft['data'],
            'id':nft['id'],
            'symbol':nft['short_name']
        })

    return render_template('index.html', nfts= nftList)


@app.route('/transfer-nft', methods = ['POST'])
def transferNft():
    url = 'https://thentic.tech/api/nfts/transfer'
    headers = {'Content-Type': 'application/json'}
    
    data = {'key': request.form['apiKey'],
            'chain_id': request.form['chainId'],
            'contract': request.form['nftContract'],
            'nft_id': request.form['nftId'], 
            'from': request.form['from'],
            'to': request.form['to']
            }
    
    r = requests.post(url, json=data, headers=headers)

    return render_template('index.html', value = "Execute Transaction", transaction = r.json()['transaction_url'])
