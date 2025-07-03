import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

"""
load_dotenv() find  .env file and set grok api key as environment variable.

"""

load_dotenv()

class Chain:

    def __init__(self):
        self.llm = ChatGroq( temperature=0, groq_api_key = os.getenv('GROQ_API_KEY'),model_name='llama3-70b-8192')

    def extract_jobs(self, cleaned_text):

        prompt_extract = PromptTemplate.from_template(

        """
        ###SCRAP TEXT FROM WEBSITE:
        {page_data}
        ###INSTRUCTIONS:
        The scrap text is from careers page of a  website.
        Your job is to extract the job posting and return them in json format containing the following fields:
        `role`, `experience`, `description`, `skills`.
        Only return the valid json.
        ### VALID JSON (NO PREAMBLE):
        """)
        
        #prompt chaining

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
            
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs")
        
        return res if isinstance(res, list) else [res]
    
    def Write_Mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Rohit, a business development executive at CodeNest. CodeNest is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of CodeNestest 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase CodeNest's portfolio: {link_list}
        Remember you are Rohit, BDE at CodeNest. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv('GROQ_API_KEY'))





    
