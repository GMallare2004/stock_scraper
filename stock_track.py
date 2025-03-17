import yfinance as yf
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		ticker = request.form['text']
		processed_ticker = ticker.upper()
		return redirect(url_for('result', ticker=processed_ticker)) 
	return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	ticker = request.args.get('ticker', '')
	dat = yf.Ticker(ticker)
	history = pd.DataFrame(dat.history(period='5y', interval='1mo')['Close'])
	if request.method == 'POST':
		history.to_clipboard(index=False)
		return render_template('result.html', ticker=ticker, tables=[history.to_html(classes='data', header='false')], status='Copied to clipboard!')
	return render_template('result.html', ticker=ticker, tables=[history.to_html(classes='data', header='false')], status='')

if __name__ == '__main__':
	app.debug = True
	app.run()