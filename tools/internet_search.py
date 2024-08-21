from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

class InternetSearch:
    
    @staticmethod
    def search_wikipedia():
        """Searches Wikipedia and returns the summary of the first result."""

        api_wrapper = WikipediaAPIWrapper(lang="es", top_k_results=2, doc_content_chars_max=10000)
        wiki = WikipediaQueryRun(api_wrapper)
        
        
    @staticmethod
    def search_duckduckgo():
        """Searches Internet and returns the summary of the first result."""
        
        return DuckDuckGoSearchRun()
        