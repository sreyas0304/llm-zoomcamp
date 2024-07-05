import openai
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

# # Set up your OpenAI API key
# openai.api_key = 'ollama'

# # Connect to the running container
# openai.api_base = 'http://localhost:11434/v1'

# Define the prompt
prompt = "What's the formula for energy?"

# Generate the response with temperature set to 0
response = client.chat.completions.create(
    model="gemma:2b",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.0
)

# Print the response and the number of completion tokens
print("Response:", response.choices[0].message.content)
print(response)
