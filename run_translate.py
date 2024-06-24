import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(
        api_key=os.getenv('GROQAPI_KEY'),
    )
filename = os.path.dirname(__file__) + "/recorded_audio.wav"

with open(filename, "rb") as file:
    translation = client.audio.translations.create(
      file=(filename, file.read()),
      model="whisper-large-v3",
      prompt="",  # Optional
      response_format="json",  # Optional
      temperature=0.0  # Optional
    )
    print(translation.text)