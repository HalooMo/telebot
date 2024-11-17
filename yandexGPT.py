import requests



def get_words(reque):

    prompt = {
    "modelUri": "gpt://b1gvhu764bb4n87tus35/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты ассистент девушка Enid, способный помочь в поддержании разговора."
        },
        {
            "role": "user",
            "text": reque
        },
        {
            "role": "assistant",
            "text": "Привет!"
        },
    ]
}


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVNz4wGVr8GP5uSVLOq0hArWp9Iq_YnlDb1hHSG"
}

    response = requests.post(url, headers=headers, json=prompt)
    result = response.text
    result = result.replace("**", "")
    result = result.replace("/", "")
    result = result.replace("\\", "")
    result = result.replace(".", ",")
    result = result.replace("nn", ",")
    result = result.replace("n", ",")
    print(len(result))
    if len(result) > 250:
        try:
            text = result.split(r'es":[{"message":{"role":"assistant","text":"')[1].split(r'"},"status":"ALTERNATIVE_STATUS_FINAL"}],"usage":')[0]
            return text
        except Exception:
            return " "
    else:
        return " "