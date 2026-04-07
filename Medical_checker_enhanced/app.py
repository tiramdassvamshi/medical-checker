from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for medications and their interactions
MEDICATIONS = {
    'medA': {'interactions': ['medB', 'medC']},
    'medB': {'interactions': ['medA']},
    'medC': {'interactions': ['medA', 'medD']},
    'medD': {'interactions': []}
}

@app.route('/check_interactions', methods=['POST'])
def check_interactions():
    data = request.get_json()
    medicines = data.get('medications', [])
    interactions = []

    for med in medicines:
        if med in MEDICATIONS:
            # Check if the medication has interactions
            for interaction in MEDICATIONS[med]['interactions']:
                if interaction in medicines:
                    interactions.append((med, interaction))

    return jsonify({'interactions': interactions})

if __name__ == '__main__':
    app.run(debug=True)