import pandas as pd
import numpy as np
import polars as pl

from datasets import Dataset

from haystack import Document, Pipeline

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

# Major Tasks
# TODO: Create a swarm of stupid bots trained on each member of the book club
# TODO: Create a hivemind bot to poll all of the stupid bots and provide one consensus answer

# Subtasks
# TODO: Create a class construction for the stupid bot
# TODO: Instantiate the class numerous times with different LLMs and RAG models
# TODO: Make the stupid bot class conform to tool usage
# TODO: Make hivemind bot have conversational memory and tool usage
# TODO: Integrate the hivemind bot into a user interface; consider Gradio

# TODO: Create a function that takes in a book club member's name and returns their book club role
# TODO: Create a function that takes in a book club member's name and returns their book club preferences
