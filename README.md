# OpenAI's Chatbot for STM

This is a simple web-based chatbot application that uses OpenAI's GPT-3.5-turbo model to generate responses in a conversation with users with custom knowledge. The chatbot can engage in interactive conversations, respond to user input, and provide helpful information based on the given context.

## Features

- Custom knowledge
- Engage in natural language conversations with users.
- Utilize OpenAI's GPT-3.5-turbo model for generating responses.
- Interactive web interface for easy user interaction.

## Installation and Setup

1. Clone this repository to your local machine.

```bash
git clone https://github.com/ServiceToMankind/openapi_chatbot
```

2. Install the required dependencies using pip.

```bash
pip install -r requirements.txt
```

3. export OPENAI_API_KEY

```bash
export OPENAI_API_KEY='your-api-key-here'
```

4. Run the Flask application.

```python
python app.python
```

5. Open your web browser and navigate to http://localhost:5000 to use the chatbot.

## Usage

1. Enter your message in the input field and click "Send."
2. The chatbot will respond with relevant information based on the context of the conversation.

## Customization

- You can customize the chatbot's behavior and appearance by modifying the HTML, CSS, and JavaScript files in the templates and static directories.

## Credits

- This project is based on OpenAI's GPT-3 API.
- The front-end interface is created using Bootstrap and jQuery.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ServiceToMankind/openapi_chatbot/blob/main/LICENSE) file for details.
