from fastapi import FastAPI
import pos

app = FastAPI()


@app.get("/api")
async def read_item(text: str):
    return {
        "tagging": pos.tags(text),
        "word_freq_dist": pos.word_frequency_distribution(text),
        "tag_freq_dist": pos.tag_frequency_distribution(text)
    }
