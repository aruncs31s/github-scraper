def get_full_description(readme_contents: str)  -> str: 
    # TODO: Check if this is neccessory.
    """Extracts the full description from the README contents.

    Args:
        readme (str): The contents of the README file.
    
    Returns:
        str: The extracted full description.
    """
    h1_start = readme_contents.find("# ")
    # This gets just before the newline
    h1_end = readme_contents.find("\n", h1_start)
    # print(f"Heading:  {readme_contents[h1_start:h1_end].strip()} ")
    # Assume first one will be a picture 
    h2_start = readme_contents.find("## ", h1_end)
    h2_end = readme_contents.find("\n" , h2_start)
    # The description is in between h1_end and h2_start
    h1_contents = readme_contents[h1_end:h2_start].strip()

    # Remove The Pictures from the description
    def remove_all_images(texts):
        count = 0 
        while(texts.find("imgs/") > 0):
            # print(texts.find("imgs/"))
            count += 1
            picture_start = texts.find("![")
            picture_end = texts.find("\n",picture_start)
            texts = texts[:picture_start].strip() + "" +  h1_contents[picture_end:].strip()
            # avoid recursion
            if count > 5:
                return None 
        return texts
    h1_contents = remove_all_images(h1_contents)
    return h1_contents

if __name__ == "__main__":
    with open("test/readme.md" , 'r') as f:
        get_full_description(f.read())