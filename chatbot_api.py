import openai
import os
from system_text import system_text
from chat_functions import *
from available_functions import functions
import json

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key="OPENAI_API_KEY"

# load system text
system_text = system_text()

def call_function(function_name, function_args):
    if function_name == "total_donations":
        return total_donations()
    elif function_name == "donations_list":
        return donations_list(**function_args)
    # Add more functions here as needed

def get_chatbot_response(user_message, conversation=[]):
    # Append the new user message to the existing conversation
    conversation.append({"role": "user", "content": user_message})

    # Prepend the system message to the conversation
    messages = [{"role": "system", "content": system_text}] + conversation

    # Request gpt-3.5-turbo for chat completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )

    # Get the response message from GPT-3.5 Turbo
    response_message = response["choices"][0]["message"]

    # Check if GPT-3.5 Turbo wants to call a function
    if response_message.get("function_call"):
        # Extract function call details
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])

        # Call the function and get the result
        function_result = call_function(function_name, function_args)
        # if not function_result:
        #     function_result = "Sorry, I couldn't find that information."
        if function_result is None:
            function_result = "Sorry, I couldn't find that information."

        # Append the function call and response to the conversation
        conversation.append({"role": "assistant", "content": response_message["content"]})
        conversation.append({"role": "function", "name": function_name, "content": function_result})

        # Request a second response from GPT with the extended conversation
        messages.append(response_message)  # Extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_result,
            }
        )  # Extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        return second_response["choices"][0]["message"]["content"]

    # If no function call, return the chatbot's response
    chat_message = response_message["content"]
    conversation.append({"role": "assistant", "content": chat_message})
    return chat_message
