import os
from dotenv import load_dotenv
from openai import OpenAI




def main():
    load_dotenv()
    try:
        api_key = os.environ.get("OPENROUTER_API_KEY")
    except Exception as e:
        raise RuntimeError("could not fetch the API_KEY")
    client = OpenAI(base_url = "https://openrouter.ai/api/v1", api_key = api_key,)
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = [
            {
                "role" : "user",
                "content" : "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            }
        ],
    )
    print(response.choices[0].message.content)

    


if __name__ == "__main__":
    main()
