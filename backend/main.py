from flask import Flask, render_template
from db import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)
app = Flask(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()