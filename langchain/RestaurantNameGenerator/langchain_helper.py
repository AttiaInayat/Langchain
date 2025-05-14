from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain
import os
from secret_key import HUGGINGFACEHUB_API_TOKEN

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
llm= HuggingFaceHub(
    repo_id="t5-base",
    model_kwargs={"temperature": 1.5, "max_length": 100}
)



def generate_restaurant_name_and_cusines(cuisine):

    #Chain 1: For restaurant name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.",
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="restaurant_name")

    #Chain 2: For menu items
    cuisine_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string""",
    )

    cuisine_chain=LLMChain(llm=llm, prompt=cuisine_prompt,output_key='menu_items')

    chain=SequentialChain(
        chains=[name_chain,cuisine_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items']
    )

    response=chain({'cuisine':cuisine})

    return response
