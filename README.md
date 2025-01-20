# Discord Question Answering Bot

This bot is designed to answer questions in a Discord server by using advanced language models. The bot receives a question, retrieves relevant documents from a stored document set, and generates a suitable response using Hugging Face's deepset/roberta-base-squad2, a variant of the RoBERTa model fine-tuned specifically for the SQuAD 2.0 task, which is a question-answering task. Alternatively, you can use Open AI also, if you got enough credits.

## Setup

1. Clone the repository and navigate to its directory in your terminal.
2. Install the required packages with `pip install -r requirements.txt`.

## Environment Variables

Before starting the bot, make sure to set the following environment variables:

- `DISCORD_TOKEN`: Your Discord bot token. You can get this from the [Discord Developer Portal](https://discord.com/developers/applications).
- `OPENAI_API_KEY`: Your OpenAI API key. You can get it here [OpenAI Plattform](https://platform.openai.com/account/api-keys) or
- `HUGGINGFACE_API_KEY`: Your Hugging Face API key.You can get it here[Hugging Face](https://huggingface.co/docs/huggingface_hub).

## Starting the Bot

To start the bot, simply run `python3 bot.py` in your terminal.

## Usage

After inviting the bot to your Discord server, you can ask it a question with the command `@ask <your question here>`. For example:

```
#ask Who is Ayush Pratap Singh?
```

The bot will process your question, retrieve relevant documents, and generate a suitable response using the model.
