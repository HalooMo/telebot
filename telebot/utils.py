'''
import openai
import asyncio
import logging
import config

openai.api_key = config.API_KEY

async def text_generate(prompt) -> dict:
    try:
        response = await openai.ChatCompletion.acreate(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"user", "content":prompt}
            ]
        )
        return  response["choises"][0]["message"]["content"], response["usage"]["total_tokens"]
    except Exception as e:
        logging.error(e)


async def image_generate(prompt, size, n) -> list[str]:
    try:
        response = await openai.Image.acreate(
            prompt = prompt,
            n = n,
            size = size
        )
        urls = []
        for i in response["data"]:
            urls.append(i["url"])
    except Exception as e:
        logging.error(e)
        return []
    else:
        return urls


'''