
from asyncflows import AsyncFlows

writing_sample = """
Hullo mai neyms Kruubi Duubi, aI'm hear to rite yu a stowy abowt enyting yu want. 
"""

# Load the flow
flow = AsyncFlows.from_file("text_style_transfer.yaml").set_vars(
   writing_sample=writing_sample,
)

# Run the flow
while True:
   # Get the user's query via CLI interface (swap out with whatever input method you use)
   try:
      message = input("Write about: ")
   except EOFError:
      break

   # Set the query and conversation history
   topic_flow = flow.set_vars(
      topic=message,
   )

   # Run the flow and get the result
   result =asyncio.await_for(topic_flow).run()
   print(result)