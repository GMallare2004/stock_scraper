import yfinance as yf
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		tickers = request.form['text']
		processed_tickers = tickers.upper()
		return redirect(url_for('result', tickers=processed_tickers)) 
	return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	tickers = request.args.get('tickers', '')
	tickers = tickers.replace('+', ' ')
	print(f'Pre-processed tickers: {tickers}')
	dat = yf.Tickers(tickers)
	print(f'Processed tickers: {dat}')
	d = {}
	if len(tickers) > 1:
		for ticker in dat.tickers:
			d[ticker] = dat.tickers[ticker].history(period='5y', interval='1mo')['Close'].to_frame(ticker)
			print(f'{ticker}: {d[ticker]}')
		history = pd.concat(d.values(), axis=1)
		print(f'Total number of tickers: {len(d)}')
		print(f'Total result: {history}')
	else:
		for ticker in dat.tickers:
			history = dat.tickers[ticker].history(period='5y', interval='1mo')['Close'].to_frame(ticker)
		print(f'Total result: {history}')
	if request.method == 'POST':
		history.to_clipboard(index=False)
		return render_template('result.html', tickers=tickers, tables=[history.to_html(classes='data', header='false')], status='Copied to clipboard!')
	return render_template('result.html', tickers=tickers, tables=[history.to_html(classes='data', header='false')], status='')

if __name__ == '__main__':
	app.debug = True
	app.run()