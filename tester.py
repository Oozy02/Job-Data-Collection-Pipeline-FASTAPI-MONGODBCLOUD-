import json
from h11 import Data
import requests

# data = {"data":[{"Role": "SrReactJSDeveloper", "Comapany": "DaynilGroupSolutionsPvtLtd", "Location": "India", "Type": "Remote"}, {"Role": "MERNSTACKDEVELOPER", "Comapany": "AvestanTechnologies", "Location": "India", "Type": "Remote"}, {"Role": "FullStackDeveloper(NodeJS)", "Comapany": "Solvevolve", "Location": "India", "Type": "Remote"}, {"Role": "Node.jsDeveloper", "Comapany": "well-knowncompany", "Location": "India", "Type": "Remote"}, {"Role": "React.jsDeveloper", "Comapany": "SoftEdgeInfoTechPrivateLimited", "Location": "Ahmedabad,Gujarat,India", "Type": "Hybrid"}, {"Role": "MERNDeveloper", "Comapany": "SoftEdgeInfoTechPrivateLimited", "Location": "Ahmedabad,Gujarat,India", "Type": "Hybrid"}, {"Role": "ReactDeveloper", "Comapany": "WebduraTechnologies", "Location": "India", "Type": "Remote"}]}

datA =[
  {
    "Company": "string",
    "Role": "string",
    "Location": "string",
    "Type": "string"
  },
{
    "Company": "string",
    "Role": "string",
    "Location": "string",
    "Type": "string"
  },
{
    "Company": "string",
    "Role": "string",
    "Location": "string",
    "Type": "string"
  }

]
r= requests.post(url = 'http://127.0.0.1:8000/api/job1', json = datA)
print(r)
print(r.reason)