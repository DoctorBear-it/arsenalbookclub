import pandas as pd
import numpy as np
import polars as pl

from datasets import Dataset

from haystack import Document, Pipeline
# from haystack import document_stores
from haystack.document_stores.types import DuplicatePolicy
# from haystack.components import TableReader
# from haystack.components.retrievers import BM25Retriever
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore

from haystack_integrations.components.generators.ollama import OllamaGenerator

from haystack.dataclasses import ChatMessage

from haystack_integrations.components.generators.ollama import OllamaChatGenerator

import time
import gradio as gr

url = "https://docs.google.com/spreadsheets/d/1HWaiuL5zxgSZaBi4fLgIUnesntcmFvOGj9PAQcITRJI/export?gid=1503492484&format=csv"
df = pd.read_csv(
    url,
    skiprows=1,
    usecols=np.append(np.arange(1, 14), 17),
    # nrows=32,
    na_values=["DNF"],
)
df.rename(columns={"Reader": "Book"}, inplace=True)
df1 = pl.from_dataframe(df)
# print(df)
# df.to_csv("./data.csv")
dataset = Dataset.from_pandas(df)
documents = [Document(dataframe=df)]  # , content_type="table", meta={}

members = {
    "Timothy": "Tim",
    "Michael P": "Mike P",
    "Michael Y": "Yankel",
    "Matthew": "Matt",
    "Kevin": "Kev",
    "Justin": "Cozy",
    "Andrew": "Andrew",
}
# documents = []
for row in df1.iter_rows(named=True):
    des = row["Book"]
    documents.append(
        Document(
            meta={"book": des},
            content=f"The Arsenal Book Club average rating for {des} was {row["Average"]} cannons out of 5 cannons. 1 cannon is lowest rating and is the worst.  5 cannons is the highest rating and is the best rating. Books that recieve a rating between 2.5 and 3.5 are considered average.",
        )
    )
    documents.append(
        Document(
            meta={"book": des},
            content=f"The Arsenal Book Club gave {des} a 'Tot or Not' rating of {row["Tot or Not"]}. The 'Tot or Not' rating is a scale from Tottenham to not-Tottenham.  Tottenham is equal to shit.  When you think of Tottenham, you think of shit.  When you think of shit, you think of Tottenham.  A 'Tot' rating means the book was shit.  A 'Not' rating means the book was not shit.",
        )
    )
    documents.append(
        Document(
            meta={"book": des},
            content=f"The Arsenal Book Club awarded {des} a 'Three Lions' score of {row["Lions"]}.  The Three Lions award is named for the England National football team.  The score is judged and awarded to each book and is based on {des} similarity to each of the three main story acts of Disney's movie The Lion King.  The Lion King is in fact the best movie ever made and has the best story ever told.  The Three Lions award is the hardest and most prestigous award given by The Arsenal Book Club.",
        )
    )
    for member, nickname in members.items():
        if row[member] is not None:
            content = f"{member} is a member of The Arsenal Book Club. {member} also goes by the nickname or alias {nickname}. {member} read {row["Book"]}. {member} rated {row["Book"]} at {row[member]} cannons out of 5 cannons.  1 cannon is lowest rating and is the worst.  5 cannons is the highest rating and is the best rating. Books that recieve a rating between 2.5 and 3.5 are considered average."
        else:
            content = f"{member} is a member of The Arsenal Book Club. {member} also goes by the nickname or alias {nickname}. {member} has not yet read {row["Book"]}. {member} currently rates {row["Book"]} at {row[member]} cannons out of 5 cannons. 1 cannon is lowest rating and is the worst.  5 cannons is the highest rating and is the best rating. Books that recieve a rating between 2.5 and 3.5 are considered average."
        documents.append(Document(content=content, meta={"book": des, "member": row}))

for member, nickname in members.items():
    read = df1.filter(pl.col(member).is_not_null()).select("Book").to_series().to_list()
    documents.append(
        Document(
            meta={"member": member},
            content=f"{member} has read the following list of books: {read}.",  # but {member} has not yet read {not_read}
        )
    )

    not_read = df1.filter(pl.col(member).is_null()).select("Book").to_series().to_list()
    documents.append(
        Document(
            meta={"member": member},
            content=f"{member} has not read the following list of books: {not_read}.",
        )
    )

    ratings = (
        df1.filter(pl.col(member).is_not_null())
        .select(["Book", member])
        .to_numpy()
        .tolist()
    )
    documents.append(
        Document(
            content=f"The list of books that {member} has read and the associated ratings are {ratings}.  These are the same ratings as before where the scale is from 1.0 to 5.0 cannons where 1.0 cannon is the lowest and worst, 5.0 cannons is the highest and best.  A score of 4.0 or more cannons suggests that {member} liked the book.  A score of 2.0 or lower suggests that {member} did not like the book."
        )
    )

documents.append(
    Document(
        content=f"The members of The Arsenal Book Club are: {list(members.keys())}"
    )
)

documents.append(
    Document(
        content="A book club member's favorite book is judged by three criteria.  The first criteria is the book that the member gave the highest rating in cannons.  The second criteria is the overall club rating for the highest number of Lions in the Three Lions ratings (individuals do not score this, it is only given at the club consensus).  The Third criteria is if the club rated the book as Not in the Tot or Not rating (individuals do not score this, it is only given at the club consensus).  A book with a Tot rating can never be a favorite book."
    )
)


document_store = InMemoryDocumentStore()

# #delete old documents; unsure why this started throwing an error on 4/5/2025 usage
docs = document_store.filter_documents()
ids = [d.id for d in docs]
document_store.delete_documents(ids)

#now re-add the docs
document_store.write_documents(documents, policy=DuplicatePolicy.OVERWRITE)

prompt_template = """
Given only the following information, answer the question and cite your source and provide the data points for the answer using Chicago Style (Notes and Bibliography).
You are a chatbot pretending to be an Arsenal Book Club member Kevin or 'Kev'.  You only read fantasy and sci-fi books but think most are mediocre.  You always respond with the wit, mannerisms, and speech like Edris Elba in British English! You perfectly remember all of the books you've read and the rating you gave them.  You also know all of the books you haven't read yet.  You also perfectly remember all of the book ratings from all members of the club.  You always check to verify the accuracy of your answer and update your answer if necessary.


Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{ query }}?
"""

retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = PromptBuilder(template=prompt_template)

llm = OllamaGenerator(model="hf.co/unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF:Q6_K_XL", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="hf.co/unsloth/Qwen3-30B-A3B-GGUF:Q6_K_XL", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="qwen3:30b-a3b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="qwen3:8b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="granite3.3:8b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="hf.co/bartowski/google_gemma-3-12b-it-qat-GGUF:Q4_0", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="cogito:8b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="gemma3:12b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="gemma3:4b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="deepseek-r1:8b", url="http://localhost:11434", timeout=600)
# llm = OllamaGenerator(model="llama3.1", url="http://localhost:11434", timeout=600)
# llm = OllamaChatGenerator(model="llama3.1", url="http://localhost:11434")

pipe = Pipeline()
pipe.add_component("retriever", retriever)
pipe.add_component("prompt_builder", prompt_builder)
pipe.add_component("llm", llm)
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")  # change to llm.messages for chat generator usage

# query = "List the books and ratings Kevin has read"

# response = pipe.run({"prompt_builder": {"query": query}, "retriever": {"query": query}})

# print(response["llm"]["replies"])


def ask_question(question):
    response = pipe.run(
        {"prompt_builder": {"query": question}, "retriever": {"query": question}}
    )
    return response["llm"]["replies"][0]


# demo = gr.Interface(fn=ask_question, inputs="text", outputs="text")
# demo.launch()


def chat(message, history):
    # for i in range(len(message)):
    #     time.sleep(0.05)
    #     yield ask_question(message)
    return ask_question(message)


demo = gr.ChatInterface(chat, type="messages")
demo.launch(auth=("abc", "big books"))  # share=True
