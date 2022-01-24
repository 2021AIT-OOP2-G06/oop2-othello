from flask import Flask, render_template, request, jsonify
from othello import *
import othello
from cpu import *
import cpu

app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/othello')
def index():
    title = 'Othello'
    score = 'Score'
    return render_template('index.html', title= title, score = score)

@app.route('/getPosition', methods=['POST'])
def getPosition():
    
    row = request.json['row']
    col = request.json['col']
    player = request.json['player']
    sms = othello.selectCell(row, col,player)
    print(sms)
    return jsonify( grid=othello.grid, message=sms)

@app.route('/start', methods=['POST'])
def start():
    return jsonify( grid=othello.grid)

@app.route('/reset', methods=['POST'])
def reset():
    othello.grid = request.json['respaldo']
    return jsonify( grid=othello.grid)

@app.route('/')
def top():
    return render_template('toppage.html')

@app.route('/cpu')
def cpu_battle():
    return render_template('cpu.html')

@app.route('/cpugetPosition', methods=['POST'])
def cpugetPosition():
    
    row = request.json['row']
    col = request.json['col']
    player = request.json['player']
    sms = cpu.selectCell(row, col,player)
    print(sms)
    return jsonify( grid=cpu.grid, message=sms)

@app.route('/cpustart', methods=['POST'])
def cpustart():
    return jsonify( grid=cpu.grid)

@app.route('/cpureset', methods=['POST'])
def cpureset():
    cpu.grid = request.json['respaldo']
    return jsonify( grid=cpu.grid)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)