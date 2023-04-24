
import os
import openai
openai.organization = "org-v5UcpkhQE2ztnDHORYp0GO1N"
openai.api_key = ""
modellist=openai.Model.list()
print(modellist)