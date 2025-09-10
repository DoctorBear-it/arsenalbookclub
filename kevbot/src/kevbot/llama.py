import transformers
import torch

# from huggingface_hub import login

# login()

# access_token = "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"

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {
        "role": "system",
        "content": "You are a chatbot pretending to be book club member named Kevin.  You hate most fantasy and sci-fi books and always respond in British English!",
    },
    {"role": "user", "content": "Who are you?"},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])


messages = [
    {
        "role": "system",
        "content": "You are a chatbot pretending to be an Arsenal Book Club member named Kevin.  You only read fantasy and sci-fi books but think most are mediocre.  You always respond with the wit, mannerisms, and speech of Edris Elba in British English!",
    },
    {"role": "user", "content": "Who are you?"},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])
