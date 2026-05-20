This project is based on agentic ai system using langgraph.

It's a chatbot with multiple tools like research , websearch , or llm based research tool.

It's based on react architecture - (Reasoning and act)

It uses Anthropic and groq api for llm.

It also uses tavily api for websearch.

It also uses arxiv and wikipedia for research 

Our chatbot is based upon agents which will decide which tool to use based upon the query.

Chatbot workflow :-
user --> agent --> tool --> agent --> tool --> agent --> respond to user.

Model :- claude sonnet 4.5

Start - AI assistant(llm) -> decide wheter to go for tool call for the query - if yes then which tool cool is decided -> tool output --> llm -> react to user --> end


