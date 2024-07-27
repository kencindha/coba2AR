from flask import Flask, jsonify, request, send_from_directory, render_template
import os

app = Flask(__name__)

recipes = {
    'apple': {'ingredients': ['Apple', 'Sugar', 'Cinnamon'], 'steps': ['Cut apple', 'Add sugar and cinnamon', 'Bake']},
    'banana': {'ingredients': ['Banana', 'Honey'], 'steps': ['Peel banana', 'Drizzle with honey']}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-recipe', methods=['GET'])
def get_recipe():
    ingredient = request.args.get('ingredient')
    recipe = recipes.get(ingredient.lower())
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Recipe not found'}), 404

# Route for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
