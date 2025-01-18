import os
# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"]= OPENAI_API_KEY

llm = OpenAI(temperature=0.6)
def generate_restaurant_name_and_items(cuisine):
    
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
    )
    name_chain = LLMChain(llm = llm,prompt = prompt_template_name,output_key="restaurant_name")

     # Chain 2: Food Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template = """Suggest some menu items for {restaurant_name}. Return it as a comman separated string. Note: Please return it only once and without numbering"""
    )

    food_items_chain = LLMChain(llm = llm,prompt = prompt_template_items,output_key="menu_items")


    chain = SequentialChain(
        chains=[name_chain,food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name","menu_items"]
    )
    response = chain({'cuisine': cuisine})
    print(response)
    return response



if __name__=='__main__':
    print(generate_restaurant_name_and_items("Italian"))

