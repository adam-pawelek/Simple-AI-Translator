import os

from openai import OpenAI
import json

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_from_language",
            "description": "Retrieve the ISO 639-3 code for a given language",
            "parameters": {
                "type": "object",
                "properties": {
                    "iso639_3": {
                        "type": "string",
                        "description": "The ISO 639-3 code for a language, e.g., 'eng' for English",
                    },
                },
                "required": ["iso639_3"],
            },
        },
    }
]

def get_from_language(iso639_3):
    iso639_3 = iso639_3.lower()
    return iso639_3

def get_one_language_from_text(text):
    # Step 1: send the conversation and available functions to the model
    messages = [
        {"role": "system", "content": "You are a language detector. You should return the ISO 639-3 code to the get_from_language function of user text."},
        {"role": "user", "content": text}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_from_language": get_from_language
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        print(tool_calls)
        tool_call =  tool_calls[0]
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        return function_args.get("iso639_3")


print(get_one_language_from_text("jak ty się nazywasz"))
print(get_one_language_from_text("hvordan har du det kjære"))