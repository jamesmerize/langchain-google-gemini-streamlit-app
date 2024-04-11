from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_core.language_models.llms import LLM
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain.chains.sequential import SequentialChain



def googleapi(apikey):
    llm1 = GoogleGenerativeAI(model="gemini-1.0-pro-latest", google_api_key=apikey)
    return llm1

def restNameGen(cusine):
     # Create the language model with your API key
    llm1 = GoogleGenerativeAI(model="gemini-1.0-pro-latest", google_api_key="")

    # Template for suggesting a restaurant name
    Template1 = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} cuisine. Suggest one fancy name for it."
    )

    # Chain for generating a restaurant name
    chain1 = LLMChain(llm=llm1, prompt=Template1, output_key="restaurant_name")

    # Template for suggesting menu items
    Template2 = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest menu items for {restaurant_name}. Return them as comma-separated values."
    )

    # Chain for generating menu items
    chain2 = LLMChain(llm=llm1, prompt=Template2, output_key="menu_items")  # Use "menu_items" for clarity

    # Sequential chain to execute both prompts in order
    ssschain = SequentialChain(
        chains=[chain1, chain2],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]  # Use "menu_items" for clarity
    )

    # Execute the chain with input
    response = ssschain({'cuisine': cusine})
    # print(response)  # Print the complete response

    return response

if __name__=="__main__":
    print(restNameGen("indian"))