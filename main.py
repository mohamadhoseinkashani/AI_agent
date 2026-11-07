import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
import sys
from prompts import system_prompt
from call_function import available_functions
from call_function import call_function
import json




def main() -> None:
    load_dotenv()
    try:                                                                            #trying to fetch an API key from open router
        api_key = os.environ.get("OPENROUTER_API_KEY")
    except Exception as e:
        raise RuntimeError("could not fetch the API_KEY")

    
    client = OpenAI(base_url = "https://openrouter.ai/api/v1", api_key = api_key,)  #calling the API from OpenRouter's

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type = str, help = "User Prompt")            #taking prompts from CLI and useing it as a variable called content to feed to the AI model
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [ 
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
        ]

    response = client.chat.completions.create(                                      #taking responses from the AI model
        model = "openrouter/free",
        messages = messages,
        temperature = 0,
        tools = available_functions
    )

    message = response.choices[0].message
    Usage = response.usage
    if args.verbose:                                                               #calculating the tokens
        print(f"User prompt: {messages[0]['content']}")
        print(f"Prompt tokens: {Usage.prompt_tokens}")
        print(f"Response tokens: {Usage.completion_tokens}")
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            if not result_message["content"]:
                raise ValueError("Error: no content available")
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print("Response:")
        print(message.content)
        


    

    # print("Response:")
    # print(response.choices[0].message.content)

    


if __name__ == "__main__":
    main()
