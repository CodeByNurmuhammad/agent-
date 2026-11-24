import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable is not set")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


def print_usage(response) -> None:
    usage = getattr(response, "usage", None)
    if usage is None:
        return

    prompt_tokens = getattr(usage, "prompt_tokens", None)
    completion_tokens = getattr(usage, "completion_tokens", None)
    if prompt_tokens is not None:
        print(f"Prompt tokens: {prompt_tokens}")
    if completion_tokens is not None:
        print(f"Completion tokens: {completion_tokens}")


messages = [
    {"role": "system", "content": system_prompt},
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

max_iterations = 20

for iteration in range(max_iterations):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    message = response.choices[0].message
    messages.append(message)

    tool_calls = getattr(message, "tool_calls", None)
    if tool_calls:
        for tool_call in tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if not isinstance(result_message, dict):
                raise RuntimeError("Function returned an invalid result")
            content = result_message.get("content")
            if content is None or content == "":
                raise RuntimeError("Function returned an empty result")
            if args.verbose:
                print(f"-> {content}")
            messages.append(result_message)
    else:
        print(message.content)
        if args.verbose:
            print_usage(response)
        break

    if args.verbose:
        print_usage(response)
else:
    print("Error: Maximum of 20 iterations reached without a final response.")
    raise SystemExit(1)
