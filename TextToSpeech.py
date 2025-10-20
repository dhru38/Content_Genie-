import edge_tts
import asyncio
from Reddit_API import get_post 

async def main() : 
    text = get_post()
    if not text :
        print("There is NO Story Right Now!!! ")
    voice = "en-US-AriaNeural"
    output_file = "Story.mp3"
    print(text)

    tts = edge_tts.Communicate(text,voice)
    await tts.save(output_file)

    print("Saved file")

asyncio.run(main())