from openai import OpenAI

with open('OpenAIAPIKey.txt', 'r') as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

with open('Prompt.txt', 'r') as f:
    prompt = f.read()

def analyze_misinformation_and_bias(article):
    """
    This function will take a string article as input and return a dictionary with the following keys:
    
    'misinformation_rating': an whole number indicating the level of misinformation in the article (0-10, 0 for no misinformation, 10 for completely fictional)
    'misinformation_sentences': a list of strings, the top 3 sentences in the article that contain the most misinformation
    'misinformation_explanation': a list of strings, an explanation for the misinformation in each of the sentences in misinformation_sentences
    'political_bias_rating': an integer whole number indicating the political bias of the article (0-10,
    'political_bias_sentences': a list of strings, the top 3 sentences in the article that contain the most political bias
    'political_bias_explanation': a list of strings, an explanation for the political bias in each of the sentences in political_bias_sentences
    
    This will all be determines using OpenAI's GPT-3.5-turbo model
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Analyze the article: {article}"}
        ]
    )

    result = completion['choices'][0]['message']['content']
    return result
    