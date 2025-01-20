import os
import discord
from discord.ext import commands
from transformers import pipeline
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the model for question-answering using a robust model for Q&A tasks
chat_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", device="mps", token=os.getenv("HUGGINGFACE_API_KEY"))

# Create the bot instance with required intents and '@' as the command prefix
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

bot = commands.Bot(command_prefix="#", intents=intents)

# Function to read content from youtube.txt file and return it as context
def load_file_content(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"

# Function to get the answer based on the uploaded file content and a question
def get_answer(question, context):
    formatted_prompt = {
        'question': question,
        'context': context
    }
    try:
        result = chat_pipeline(formatted_prompt)
        return result['answer']
    except Exception as e:
        return f"Error: {e}"

# Command to upload a file and ask a question
@bot.command(name="uploadfile")
async def upload_file(ctx):
    # Prompt the user to upload a .txt file containing the context data
    await ctx.send("Please upload a .txt file named 'data.txt' containing the context data.")

# Command to handle the uploaded file
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename == "data.txt":
                # Download the file and read its content
                file_path = f"./data.txt"
                await attachment.save(file_path)
                context = load_file_content(file_path)
                await message.channel.send("File uploaded successfully. You can now ask questions!")

    await bot.process_commands(message)

# Command to ask a question, now using @ask
@bot.command(name="ask")
async def ask_question(ctx, *, question: str):
    # Check if the data.txt file has been uploaded
    context = load_file_content("./data.txt")
    if context:
        answer = get_answer(question, context)
        await ctx.send(f"Answer: {answer}")
    else:
        await ctx.send("Please upload a valid 'data.txt' file first.")

# Run the bot with the provided token from environment variables
bot.run(os.getenv("DISCORD_TOKEN"))

