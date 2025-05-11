import chainlit as cl
from shared_lib import common_function

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Welcome to the Chainlit app! Type something to get started.").send()

@cl.on_message
async def on_message(message: cl.Message):
    # Process the message using a common function
    response = common_function(message.content)
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()