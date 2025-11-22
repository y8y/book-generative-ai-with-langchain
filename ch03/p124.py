from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.language_models import FakeListChatModel
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import trim_messages, HumanMessage


class PrintOutputCallback(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print(f"Amount of input messages: {len(messages)}")


sessions = {}
handler = PrintOutputCallback()
llm = FakeListChatModel(responses=["ai1", "ai2", "ai3"])


def get_session_history(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = InMemoryChatMessageHistory()
    return sessions[session_id]


trimmer = trim_messages(
    max_tokens=1,
    strategy="last",
    token_counter=len,
    include_system=True,
    start_on="human",
)
raw_chain = trimmer | llm
chain = RunnableWithMessageHistory(raw_chain, get_session_history)

config = {"callbacks": [PrintOutputCallback()], "configurable": {"session_id": "1"}}

_ = chain.invoke(
    [HumanMessage("Hi!")],
    config=config,
)
print(f"History length: {len(sessions['1'].messages)}")

_ = chain.invoke(
    [HumanMessage("How are you?")],
    config=config,
)
print(f"History length: {len(sessions['1'].messages)}")
