from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Serve HTML file
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to retrieve snake game state
@app.route('/game_state')
def game_state():
    # Replace this with your snake game logic to compute game state
    game_data = {
        'snake': [
            {'x': 10, 'y': 10},
            {'x': 20, 'y': 10},
            {'x': 30, 'y': 10}
        ],
        'food': {'x': 50, 'y': 50},
        'score': 0
    }
    return jsonify(game_data)

if __name__ == '__main__':
    app.run(debug=True)
