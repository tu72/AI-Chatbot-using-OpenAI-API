import os
os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # Replace with your actual API key DO NOT SHARE WITH OTHERS!!!

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the AI chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        ai_response = get_ai_response(user_input)
        print("AI:", ai_response)

if __name__ == "__main__":
    main()