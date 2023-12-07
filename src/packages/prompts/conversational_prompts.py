from langchain import PromptTemplate


class ConversationalPromptWithoutMemory:
    template = """Given a ("QUERY") and ("API_DOCS") respond to query ("QUERY") based on the Military Operation 
Simulation capabilities according to the provided documentation ("API_DOCS").
If the query does not match the documentation or Operation Simulation topic, just answer {not_relevant_output}

QUERY: {query}
API_DOCS: {api_docs}
FINAL ANSWER:"""

    PROMPT = PromptTemplate(
        template=template,
        input_variables=['query', 'api_docs', 'not_relevant_output']
    )


class ConversationalPromptWithMemory:
    template = """Given a ("QUERY"), ("API_DOCS") and ("CHAT_HISTORY") respond to query ("QUERY") based on the 
Military Operation Simulation capabilities according to the provided documentation ("API_DOCS") and history of the 
conversation ("CHAT_HISTORY").
If the query does not match the documentation ("API_DOCS") or Operation Simulation topic, just answer {not_relevant_output}

QUERY: {query}
CHAT_HISTORY: {chat_history}
API_DOCS: {api_docs}
FINAL ANSWER:"""

    PROMPT = PromptTemplate(
        template=template,
        input_variables=['query', 'api_docs', 'chat_memory', 'not_relevant_output']
    )
