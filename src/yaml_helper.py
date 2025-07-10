import re , yaml

class yProps:
    def __init__(self,readme_content):
        self.yaml_contents = self.get_yaml_content(readme_content)
        self.parsed_data =  yaml.safe_load(self.yaml_contents)
        # print(self.parsed_data)
        self.title = self.parsed_data.get('title',"")
        self.description  = self.parsed_data.get('description' , "")
        self.allowed_project_types =  ["electronics" , "ai/ml", "robotics" , "web" , "software"]
        self.tags = self.parsed_data.get('tags',"")
        self.project_type = self.get_project_type()
    def get_yaml_content(self,readme_content):
        yaml_start = readme_content.find('---')
        yaml_end = readme_content.find('---', yaml_start + 3)
        yaml_content = readme_content[yaml_start + 3:yaml_end].strip()
        return yaml_content
    def get_project_type(self):
        for tag in self.tags:
            if tag in self.allowed_project_types:
                return tag
        return None


if __name__ == "__main__":
    try: 
        with open('./test/readme.md','r') as f:
            readme = f.read()
    except FileNotFoundError:
        with open('./readme.md','r') as f:
            readme = f.read()
    props = yProps(readme)
    print(f"Title: {props.title}")
    print(f"Description: {props.description}")
    print(f"Project Type: {props.project_type}")
    print(f"Tags: {props.tags}")