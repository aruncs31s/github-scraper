from readme_extractor import parse_arguments,get_readme
from required_props import rProps
from yaml_helper import yProps
from readme_helper import get_full_description
import re , yaml


# Later generate id , from database 
id = 1 
agrs = parse_arguments()

readme = get_readme(file=agrs.input,repo_url=None)



# This will only extract the frontmatter
yaml_helper = yProps(readme)

# now extract Contents after font matter
newProps = rProps()
newProps.main['content'] = get_full_description(readme_contents=readme)


print(newProps.main['content']) 

# Save to a new md file 

output_file = agrs.output if agrs.output else 'output.md'


with open(output_file, 'w') as file:
    file.write(f"---\n")
    file.write(f"title: {yaml_helper.title}\n")
    file.write(f"description: {yaml_helper.description}\n")
    file.write("main:\n")
    file.write(f"  id: {id}\n")
    file.write("  " + "content: |\n")
    file.write("    " + newProps.main['content'])
    file.write(f"\n---\n")


