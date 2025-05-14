from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline # type: ignore
import os

os.environ['HF_HOME']='D:/huggingface_cache'

llm= HuggingFacePipeline.from_model_id(
    model_id='',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=1.5,
        max_new_tokens=100
    )
)

model= ChatHuggingFace(llm=llm)
result= model.invoke("who I am")
print(result.content)