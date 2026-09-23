from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi SQLite (Flask otomatis menyimpan file ini di dalam folder instance/)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mohair.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODEL DATABASE (Contoh Lead Generation) ---
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_instansi = db.Column(db.String(100), nullable=False)
    jumlah_pesanan = db.Column(db.Integer, nullable=False)

# --- BAGIAN INI YANG MEMBUAT FOLDER instance/ OTOMATIS ---
with app.app_context():
    db.create_all()  # Otomatis membuat instance/mohair.db jika belum ada

@app.route('/')
def home():
    return "Website Mohair Tailor Siap!"

if __name__ == '__main__':
    app.run(debug=True)