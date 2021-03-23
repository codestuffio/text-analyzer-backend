from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pos


class Payload(BaseModel):
    text: str
    description: Optional[str] = None
    tagging: Optional[bool] = True
    word_freq_dist: Optional[bool] = True
    tag_freq_dist: Optional[bool] = True


app = FastAPI()


def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


@app.get("/")
async def read_item():
    return 'Welcome to the textual api. Please POST data to the endpoint /api to analyze text'


@app.post("/api")
async def read_item(payload: Payload):
    res = {
        'original': payload.text,
        'description': payload.description
    }

    res['tagging'] = pos.tags(payload.text) if payload.tagging else None

    res['word_freq_dist'] = pos.word_frequency_distribution(
        payload.text) if payload.word_freq_dist else None

    res['tag_freq_dist'] = pos.tag_frequency_distribution(
        payload.text) if payload.tag_freq_dist else None

    return del_none(res)


@app.post("/api/test")
async def read_item(text: str):
    return text
