# import requests
# import os
# import sys
import pandas as pd
import numpy as np
import polars as pl
from datasets import Dataset

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    ServiceContext,
    Document,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import PandasCSVReader
from llama_index.core.memory import ChatMemoryBuffer

# Token counting
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler

# Unused imports from testing
# from llama_index.schema import Document
# from llama_index.node_parser import PandasDataFrameParser
# from llama_index.core.node_parser import PandasDataFrameParser

# from llama_index import PandasQueryEngine
# from llama_index.indices.struct_store import GPTStructuredStoreIndex


# Start program
url = "https://docs.google.com/spreadsheets/d/1HWaiuL5zxgSZaBi4fLgIUnesntcmFvOGj9PAQcITRJI/export?gid=1503492484&format=csv"

# response = requests.get(url)

# print(response.content)

# if response.status_code == 200:
#     filepath = os.path.join("./", "data.csv")
#     with open(filepath, "wb") as f:
#         f.write(response.content)
#         print("CSV file saved to: {}".format(filepath))
# else:
#     print(f"Error downloading Google Sheet: {response.status_code}")
#     sys.exit(1)


# url = "https://docs.google.com/spreadsheets/d/1HWaiuL5zxgSZaBi4fLgIUnesntcmFvOGj9PAQcITRJI/edit?gid=1503492484#gid=1503492484/export?format=csv"

df = pd.read_csv(
    url,
    skiprows=1,
    usecols=np.append(np.arange(1, 14), 17),
    nrows=32,
    na_values=["DNF"],
)
df.rename(columns={"Reader": "Book"}, inplace=True)
# print(df)
df.to_csv("./data.csv")

# dataset = Dataset.from_pandas(df)

# Didn't work:
# pl.read_csv(url, skip_rows=1, columns=np.append(np.arange(1, 14), 17), n_rows=32, null_values=["DNF"])
df1 = pl.from_dataframe(df)

# #Example usage
# df1.filter(pl.col("Kevin").is_null()).select("Book")
# df1.filter(pl.col("Kevin").is_not_null()).select("Book")

# # Direct read of the csv file:
# parser = PandasCSVReader(concat_rows=False)
# file_extractor = {".csv": parser}  # Add other CSV formats as needed
# documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

## This didn't work:
# parser = PandasDataFrameParser()
# documents = parser.parse_dataframe(df)

##AttributeError: 'str' object has no attribute 'get_doc_id'
# documents = []
# for index, row in df.iterrows():
#     text = f"Row {index}: {row.to_dict()}"
#     documents.append(text)
# index = VectorStoreIndex.from_documents(documents)

# documents = [
#     Document(description=row["Book"], metadata={"Kevin": row["Kevin"]})
#     for _, row in df.iterrows()
# ]

# Pandas version
# documents = []
# meta = {}
# for index, row in df.iterrows():
#     des = row["Book"]
#     text = f"Kevin read {row["Book"]}. Kevin rated {row["Book"]} at {row["Kevin"]} out of 5."
#     for column in df:
#         meta[column] = row[column]
#     documents.append(Document(description=des, text=text, metadata=meta))

# members = ["Timothy", "Michael P", "Michael Y", "Matthew", "Kevin", "Justin", "Andrew"]
members = {
    "Timothy": "Tim",
    "Michael P": "Mike P",
    "Michael Y": "Yankel",
    "Matthew": "Matt",
    "Kevin": "Kev",
    "Justin": "Cozy",
    "Andrew": "Andrew",
}
documents = []
for row in df1.iter_rows(named=True):
    des = row["Book"]
    documents.append(
        Document(
            description=des,
            text=f"The Arsenal Book Club average rating for {des} was {row["Average"]} cannons out of 5 cannons. 1 cannon is lowest rating and is the worst.  5 cannons is the highest rating and is the best rating. Books that recieve a rating between 2.5 and 3.5 are considered average.",
        )
    )
    documents.append(
        Document(
            description=des,
            text=f"The Arsenal Book Club gave {des} a 'Tot or Not' rating of {row["Tot or Not"]}. The 'Tot or Not' rating is a scale from Tottenham to not-Tottenham.  Tottenham is equal to shit.  When you think of Tottenham, you think of shit.  When you think of shit, you think of Tottenham.  A 'Tot' rating means the book was shit.  A 'Not' rating means the book was not shit.",
        )
    )
    documents.append(
        Document(
            description=des,
            text=f"The Arsenal Book Club awarded {des} a 'Three Lions' score of {row["Lions"]}.  The Three Lions award is named for the England National football team.  The score is judged and awarded to each book and is based on {des} similarity to each of the three main story acts of Disney's movie The Lion King.  The Lion King is in fact the best movie ever made and has the best story ever told.  The Three Lions award is the hardest and most prestigous award given by The Arsenal Book Club.",
        )
    )
    for member, nickname in members.items():
        if row[member] is not None:
            text = f"{member} is a member of The Arsenal Book Club. {member} also goes by the nickname or alias {nickname}. {member} read {row["Book"]}. {member} rated {row["Book"]} at {row[member]} cannons out of 5 cannons.  1 cannon is lowest rating and is the worst.  5 cannons is the highest rating and is the best rating. Books that recieve a rating between 2.5 and 3.5 are considered average."
        else:
            text = f"{member} is a member of The Arsenal Book Club. {member} also goes by the nickname or alias {nickname}. {member} has not yet read {row["Book"]}. {member} currently rates {row["Book"]} at {row[member]} cannons out of 5 cannons. 1 cannon is lowest rating and is the worst.  5 cannons is the highest rating and is the best rating. Books that recieve a rating between 2.5 and 3.5 are considered average."
        documents.append(Document(description=des, text=text, metadata=row))

for member, nickname in members.items():
    read = df1.filter(pl.col(member).is_not_null()).select("Book").to_series().to_list()
    documents.append(
        Document(
            text=f"{member} has read the following list of books: {read}."  # but {member} has not yet read {not_read}
        )
    )

    not_read = df1.filter(pl.col(member).is_null()).select("Book").to_series().to_list()
    documents.append(
        Document(text=f"{member} has not read the following list of books: {not_read}.")
    )

    ratings = (
        df1.filter(pl.col(member).is_not_null())
        .select(["Book", member])
        .to_numpy()
        .tolist()
    )
    documents.append(
        Document(
            text=f"The list of books that {member} has read and the associated ratings are {ratings}.  These are the same ratings as before where the scale is from 1.0 to 5.0 cannons where 1.0 cannon is the lowest and worst, 5.0 cannons is the highest and best.  A score of 4.0 or more cannons suggests that {member} liked the book.  A score of 2.0 or lower suggests that {member} did not like the book."
        )
    )

documents.append(
    Document(text=f"The members of The Arsenal Book Club are: {list(members.keys())}")
)

documents.append(
    Document(
        text="A book club member's favorite book is judged by three criteria.  The first criteria is the book with the highest rating in cannons.  The second criteria is the highest number of Lions in the Three Lions ratings from the club.  The Third criteria is if the book is rated Not in the Tot or Not rating.  A book with a Tot rating can never be a favorite book."
    )
)

# kev_no_read = df1.filter(pl.col("Kevin").is_null()).select("Book").to_series().to_list()
# kev_read = (
#     df1.filter(pl.col("Kevin").is_not_null()).select("Book").to_series().to_list()
# )
# # kev_no_read_meta = df1.filter(pl.col("Kevin").is_null()).select("Book").to_dict()
# documents.append(
#     Document(text=f"Kevin did not read the following list of books: {kev_no_read}.")
# )
# documents.append(
#     Document(text=f"Kevin did read the following list of books: {kev_read}.")
# )

# documents.append(
#     Document(
#         text='The members of The Arsenal Book Club are "Timothy" who goes by "Tim", "Michael P" who goes by "Mike P", "Michael Y" who goes by "Yankel", "Matthew" who goes by "Matt", "Kevin" who goes by "Kev", and "Justin" who goes by "Cozy".'
#     )
# )

# index = VectorStoreIndex.from_documents(documents)
##AttributeError: 'str' object has no attribute 'get_doc_id'
# documents = []
# for index, row in df.iterrows():
#     row_str = row.to_string()
#     documents.append(Document(text=row_str, metadata={"index": index}))
# index = VectorStoreIndex.from_documents(documents)

# query_engine = PandasQueryEngine(df)
# index = GPTStructuredStoreIndex.from_documents(documents)

# service_context = VectorStoreIndex.from_defaults()

# Token counter
# TODO: needs a tokenizer to work.  Stopped caring.
# token_counter = TokenCountingHandler(
#     tokenizer=tiktoken.encoding_for_model("llama3.1").encode
# )
# Settings.callback_manager = CallbackManager([token_counter])

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
# llm = Ollama(
#     model="llama3.1",
#     request_timeout=360.0,
# )

llm = Ollama(
    model="qwen2.5",
    request_timeout=360.0,
)

Settings.llm = llm


# Custom text splitting
text_splitter = SentenceSplitter(chunk_size=2048, chunk_overlap=512)
Settings.text_splitter = text_splitter

index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter]
)  # , service_context=service_context

query_engine = index.as_query_engine(
    response_mode="refine",  # "refine" "tree_summarize"
    verbose=True,
    streaming=True,
)
# prompt_key=,

response = query_engine.query("What's Kev's favorite book so far?")
response.print_response_stream()
print("\n")

# response = query_engine.query("What books has Kev not read?")
# response.print_response_stream()
# print("\n")

# response = query_engine.query("Who are the members of The Arsenal Book Club?")
# response.print_response_stream()
# print("\n")

# response = query_engine.query("What book did Cozy like most?")
# response.print_response_stream()
# print("\n")

# streaming_response = query_engine.query("What book did Tim like the least?")
# streaming_response.print_response_stream()

# # Talk to the plain LLM:
# response = llm.complete("Is Dune Tot or Not?")
# print(response)


# "Compare Kevin's ratings to all of Goodreads.  What book do you recommend Kevin read next?"

# chat_engine = index.as_chat_engine()
# response = chat_engine.chat("What did Kevin rate Dune?")
# print(response)

# TODO: check out the new ChatSummaryMemoryBuffer
memory = ChatMemoryBuffer.from_defaults(token_limit=80000)  # 3090

# # Condense plus context
# chat_engine = index.as_chat_engine(
#     chat_mode="condense_plus_context",
#     memory=memory,
#     llm=llm,
#     context_prompt=(
#         "You are a chatbot pretending to be an Arsenal Book Club member Kevin or 'Kev'.  You only read fantasy and sci-fi books but think most are mediocre.  You always respond with the wit, mannerisms, and speech like Edris Elba in British English!"
#         "Here are the relevant documents for the context:\n"
#         "{context_str}"
#         "\nInstruction: Based on the above documents and Kevin's book club ratings, provide a detailed answer for the user question below."
#     ),
# )


# response = chat_engine.stream_chat("What's your favorite book so far?")
# for token in response.response_gen:
#     print(token, end="")

# To reset the convo:
chat_engine.reset()

# Context only
chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    llm=llm,
    similarity_top_k=10,
    system_prompt=(
        "You are a chatbot pretending to be an Arsenal Book Club member Kevin or 'Kev'.  You only read fantasy and sci-fi books but think most are mediocre.  You always respond with the wit, mannerisms, and speech like Edris Elba in British English! You perfectly remember all of the books you've read and the rating you gave them.  You also know all of the books you haven't read yet."
    ),
)

response = chat_engine.stream_chat("What's your highest rated book so far?")
for token in response.response_gen:
    print(token, end="")

# print(
#     "Embedding Tokens: ",
#     token_counter.total_embedding_token_count,
#     "\n",
#     "LLM Prompt Tokens: ",
#     token_counter.prompt_llm_token_count,
#     "\n",
#     "LLM Completion Tokens: ",
#     token_counter.completion_llm_token_count,
#     "\n",
#     "Total LLM Token Count: ",
#     token_counter.total_llm_token_count,
#     "\n",
# )
