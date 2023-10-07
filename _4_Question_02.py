# 👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

dictionary = {
  "Himachal Pradesh": "Shimla",
  "Jharkhand": "Ranchi",
  "Assam": "Dispur",
  "Gujarat": "Gandhinagar",
  "Karnataka":"Bengaluru",
  "Madhya Pradesh":"Bhopal",
  "Haryana":"Chandigarh "  
}

obj = json.dumps(dictionary, indent=3)
 

with open("F:\PYTHON WORK\__6__JSON_and_OOPS_Assignment\_1_ Assignment_01\_2_Question_02\_1_States_and_Captial.json", "w") as file:
  file.write(obj)

print(obj)
