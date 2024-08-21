from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
    Tool
)
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from tools.internet_search import InternetSearch

from dotenv import load_dotenv

load_dotenv()

api_wrapper = WikipediaAPIWrapper(lang="es", top_k_results=2, doc_content_chars_max=10000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun()

class Agent:
    
    __tools = [
        Tool(
            name="Wikipedia",
            func=wiki.run,
            description="Util cuando necesitas buscar un tema, pais o persona en wikipedia."
        ),
        Tool(
            name="DuckDuckGo Search",
            func=search.run,
            description="Util cuando necesitas realizar una busqueda en internet para encontrar informacion que otra herramienta no puede proporcionar."
        )
    ]
    
    __llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.5)
    
    @classmethod
    def execute_agent_basic(cls, query: str):
        
        try: 
        
            prompt = hub.pull("hwchase17/react")
            
            template = """Eres un experto en deportes, exactamente en los juegos olimpicos.
            Responde la siguiente pregunta en español como un experto del tema.
            **PREGUNTA**: {q}
            """
            
            prompt_template = PromptTemplate.from_template(template)
            
            # Create the ReAct agent using the create_react_agent function
            agent = create_react_agent(
                llm=cls.__llm,
                tools=cls.__tools,
                prompt=prompt
            )

            # Create an agent executor from the agent and tools
            agent_executor = AgentExecutor(
                agent=agent,
                tools=cls.__tools,
                verbose=True,
                handle_parsing_errors=True,
                max_iterations=10
            )
            
            # Run the agent with a test query
            response = agent_executor.invoke({
                "input": prompt_template.format(q=query)
            })
            
            response = response["output"]
            
            return response
        
        except Exception as e:
            
            return f"Ha ocurrido un problema agent execution {e}"
            