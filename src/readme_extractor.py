"""
Author: Arun CS
date: 2025:07:10    
"""

import argparse 
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Github README.md Extractor'
    )
    
    parser.add_argument(
        '-r', '--repo',
        type=str,
        required=False,
        help='GitHub repository URL'
    )
    parser.add_argument(
        '-i', '--input',
        type=str,
        required=False,
        default='',
        help='Input file path'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='output.json',
        help='Output file path (default: output.json)'
    )
    return parser.parse_args()


def get_readme(repo_url,file):
    if repo_url:
        readme_url = f"{repo_url}/raw/main/README.md"
        response = requests.get(readme_url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch README.md from {repo_url}. Status code: {response.status_code}")
    elif file:
        try:
            with open(file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise Exception(f"File {file} not found.")
def save_readme_to_file(readme_content, output_file):
    with open(output_file, 'w') as file:
        file.write(readme_content)
    print(f"README.md content saved to {output_file}")
    



if __name__ == "__main__":
    args = parse_arguments()
    readme = get_readme(args.repo)
    save_readme_to_file(readme, args.output)

# - python readme_extractor.py --repo