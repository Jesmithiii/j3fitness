from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/')
def home():
    return "J3Fitness AI Coaching App is running."

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    data = request.get_json()
    goal = data.get('goal')
    weight = data.get('weight')
    height = data.get('height')
    experience = data.get('experience')

    prompt = f"""
    Build a customized bodybuilding plan for a client. 
    Goal: {goal}
    Weight: {weight} lbs
    Height: {height} inches
    Experience Level: {experience}
    Provide: Macros, Meal Plan, Weekly Training Split, Supplement Suggestions.
    """

    response = openai.Completion.create(
        engine="gpt-4o",  # adjust depending on your API access
        prompt=prompt,
        max_tokens=500
    )

    return jsonify({'plan': response['choices'][0]['text'].strip()})

if __name__ == '__main__':
    app.run(debug=True)
