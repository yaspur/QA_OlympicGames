from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser

from agent.agent import Agent

from logic.tool_validation import ResponseValidation
from logic.result_schema import Data

load_dotenv()

class OlympicGames:

    @classmethod
    def response_process(cls, query: str):
        
        try:
            
            og_validation_chain = cls.__query_validation_chain(query=query)
            
            og_chain = {
                "process": og_validation_chain,
                "query": lambda x: query
            } | RunnableLambda(cls.__route_response)
            
            result = og_chain.invoke({})
            
            return result
            
        except Exception as e:
            
            return f"{e}"
            
        
    
    @staticmethod
    def __route_response(data) -> str:
        
        try:
        
            data = Data(**data)
            
            if "yes" in data.process.resultado:
                
                return Agent.execute_agent_basic(query=data.query)
                
            elif "no" in data.process.resultado:
                
                return "Lo siento, solo puedo procesar preguntas que sean sobre los juegos olimpicos"
        
        except Exception as e:
            
            return f"Ha ocurrido un problema en route response {e}"
        
    @staticmethod
    def __query_validation_chain(query: str):
        
        try:
        
            model  = ChatOpenAI(model="gpt-4-turbo", temperature=0.2)
            
            model_validation = model.bind_tools(tools=[ResponseValidation], tool_choice="ResponseValidation", strict=True)
            
            parser = JsonOutputKeyToolsParser(key_name="ResponseValidation", first_tool_only=True)
            
            system_instructions = """\
            Eres un asistente especializado en los Juegos Olímpicos. Tu tarea es validar si las preguntas son únicamente sobre los Juegos Olímpicos. Si la pregunta no está directamente relacionada con los Juegos Olímpicos, intenta reformularla para que se relacione con los Juegos Olímpicos. Si no es posible reformular la pregunta, responde con "no", si la pregunta trata sobre los juegos olimpicos responde con "yes".
            """
            
            human_instructions = """\
            Aqui tienes algunos ejemplos para saber que responder:
            """
            
            human_first_example = """\
            ¿Quién ganó la medalla de oro en los 100 metros en los últimos Juegos Olímpicos?
            """
            response_first_example = """\
            yes
            """
            
            human_second_example = """\
            ¿Quién es el presidente?
            """
            response_second_example = """\
            puedo reformular la pregunta a "¿quien es el presidente de los juegos olimpicos?", respondo con "yes"
            """
            
            human_third_example = """\
            ¿Cuál es el precio actual del petróleo?
            """
            response_third_example = """\
            no
            """
            
            human_fourth_example = """\
            ¿Cuál es la capital de Italia?
            """
            response_fourth_example = """\
            no
            """
            
            human_indications = """\
            Haz tu pregunta a continuación y, si no está relacionada con los Juegos Olímpicos, trataré de ayudarte a reformularla para que esté relacionada con el tema.
            """
            
            human_question = f"""\
            Esta es la pregunta:
            {query}
            """
            
            messages = [
                SystemMessagePromptTemplate.from_template(template=system_instructions),
                HumanMessagePromptTemplate.from_template(template=human_instructions),
                HumanMessagePromptTemplate.from_template(template=human_first_example),
                AIMessagePromptTemplate.from_template(template=response_first_example),
                HumanMessagePromptTemplate.from_template(template=human_second_example),
                AIMessagePromptTemplate.from_template(template=response_second_example),
                HumanMessagePromptTemplate.from_template(template=human_third_example),
                AIMessagePromptTemplate.from_template(template=response_third_example),
                HumanMessagePromptTemplate.from_template(template=human_fourth_example),
                AIMessagePromptTemplate.from_template(template=response_fourth_example),
                HumanMessagePromptTemplate.from_template(template=human_indications),
                HumanMessagePromptTemplate.from_template(template=human_question)
            ]
            
            chat_prompt = ChatPromptTemplate.from_messages(messages=messages)
            
            
            query_validation_chain = chat_prompt | model_validation | parser
            
            return query_validation_chain

        except Exception as e:
            
            raise f"Ha ocurrido un problema en la validacion de la pregunta {e}"