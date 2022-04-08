from fileinput import filename
import json
import os
# filename = "policy_assignments_definitions/policies/assignments/policy1.json"
filename = os.environ.get('COMMITED_FILES')
with open(filename) as f:
    data = json.load(f)

print(data)