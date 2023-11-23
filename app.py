from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

likes = {
    'song1': 1,
    'song2': 0,
    'song3': 0
}
@app.route('/')
def index():
    return render_template('index.html', likes=likes)

@app.route('/rap')
def rap():
    return render_template('rap.html', likes=likes)

@app.route('/jazz')
def jazz():
    return render_template('jazz.html', likes=likes)

@app.route('/varieteInternational')
def varieteInternational():
    return render_template('varieteInternational.html', likes=likes)


@socketio.on('like')
def handle_like(data):
    song_id = data['song_id']
    likes[song_id] += 1
    emit('update_likes', {'song_id': song_id, 'likes': likes[song_id]}, broadcast=True)

@socketio.on('dislike')
def handle_dislike(data):
    song_id = data['song_id']
    likes[song_id] -= 1
    emit('update_likes', {'song_id': song_id, 'likes': likes[song_id]}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
