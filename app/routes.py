from app import app
from flask import render_template, request
import sqlite3

# PÁGINA HOME

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# PÁGINA ANIMAL

@app.route('/animal_form')
def animalForm():
    return render_template('animal_form.html')

@app.route('/identify_animal', methods=['POST'])
def indentifyAnimal():
    color = request.form['color']
    size = request.form['size']
    sound = request.form['sound']

    if color == 'marrom' and size == 'médio' and sound == 'latido':
        animal = 'cachorro'
    elif color == 'cinza' and size == 'pequeno' and sound == 'miado':
        animal = 'gato'
    else:
        animal = 'desconhecido'
    
    # CONFIGURAÇÃO DO SQLITE3
    conn1 = sqlite3.connect('table.db')
    cursor1 = conn1.cursor()
    
    cursor1.execute('INSERT INTO animal VALUES (?, ?, ?, ?)', (color, size, sound, animal))
    conn1.commit()

    return render_template('animal_result.html', animal=animal)
    
# PÁGINA CONTAMINAÇÃO

@app.route('/contamination_form')
def contaminadoForm():
    return render_template('contamination_form.html')

@app.route('/detect_contamination', methods=['POST'])
def detect_contamination():
    temperature = request.form['temperature']
    has_mold = request.form['has_mold']
    expired_food = request.form['expired_food']

    if temperature == 'high':
        result = 'Temperatura alta. Risco de contaminação!'
    elif has_mold == 'yes':
        result = 'Presença de mofo detectada. Ação necessária!'
    elif expired_food == 'yes':
        result = 'Alimentos fora da validade. Risco de contaminação!'
    else:
        result = 'A geladeira está limpa. Nenhuma contaminação detectada.'
        
        # CONFIGURAÇÃO DO SQLITE3
    conn1 = sqlite3.connect('table.db')
    cursor1 = conn1.cursor()
    
    cursor1.execute('INSERT INTO geladeira VALUES (?, ?, ?, ?)', (temperature, has_mold, expired_food, result))
    conn1.commit()

    return render_template('contamination_result.html', result=result)

# PÁGINA PERSONALIDADE

@app.route('/personality_form')
def personalidadeForm():
    return render_template('personality_form.html')

@app.route('/analyze_personality', methods=['POST'])
def analyze_personality():
    name = request.form['name']
    age = int(request.form['age'])
    movie_genre = request.form['movie_genre']
    likes_studying = request.form['likes_studying']
    programming_language = request.form['programming_language']
    likes_beach = request.form['likes_beach']

    # Lógica para analisar a personalidade com base nas respostas

    personality = ''

    if movie_genre in ['comédia', 'ação'] and programming_language == 'Python' and likes_studying == 'sim' and likes_beach == 'sim':
        personality = 'positiva'
    elif movie_genre in ['comédia', 'ação'] and programming_language == 'Python' and likes_studying == 'não' and likes_beach == 'não':
        personality = 'sem sal'
    else:
        personality = 'mal humorada'
        
    conn1 = sqlite3.connect('table.db')
    cursor1 = conn1.cursor()
    
    cursor1.execute('INSERT INTO personalidade VALUES (?, ?, ?, ?, ?, ?, ?)', (name, age, movie_genre, likes_studying, programming_language, likes_beach, personality))
    conn1.commit()

    return render_template('personality_result.html', name=name, personality=personality)

if __name__ == '__main__':
    app.run()