# importaciones
from flask import Flask, render_template
from flask_socketio import SocketIO,send
# instancias de flask y socketio
app=Flask(__name__)
app.config['SECRET_KEY']='secret'
socketio= SocketIO(app)

# Renderiza la pagina web con el servidor 
@app.route("/")
def home():
    return render_template("index.html")

# Conexiòn y recepcion de mensaje
@socketio.on('connect')
def handle_message():
    print('Client connected')

@socketio.on('mensaje_entrante')
def handle_message(data):
    print('mensaje_cliente-> ', data)

# Ejecutar la aplicacion 
app.run()
# if __name__ == "__name__":