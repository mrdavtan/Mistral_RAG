from langchain_core.prompts import PromptTemplate

_template = """
[INST]
Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language, that can be used to query a FAISS index. This query will be used to retrieve documents with additional context.

Let me share a couple examples that will be important.

If you do not see any chat history, you MUST return the "Follow Up Input" as is:

```
Chat History:

Follow Up Input: How is Lawrence doing?
Standalone Question:
How is Lawrence doing?
```

If this is the second question onwards, you should properly rephrase the question like this:

```
Chat History:
Human: How is Lawrence doing?
AI:
Lawrence is injured and out for the season.

Follow Up Input: What was his injurt?
Standalone Question:
What was Lawrence's injury?
```

Now, with those examples, here is the actual chat history and input question.

Chat History:
{chat_history}

Follow Up Input: {question}
Standalone question:
[your response here]
[/INST]
"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

def generate_standalone_question(question, conversation_history, llm):
    prompt = CONDENSE_QUESTION_PROMPT.format(question=question, chat_history=conversation_history)
    standalone_question = llm.generate_text(prompt).strip()
    return standalone_question