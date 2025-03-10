import argparse
import json
from openai import OpenAI

def parse_arguments():
    # Setup argparse to handle input arguments
    parser = argparse.ArgumentParser(description="Interact with the DeepSeek API for text extraction.")
    
    parser.add_argument(
        '--api_key_file', 
        type=str, 
        required=True, 
        help='Path to the file containing the API key.'
    )
    
    parser.add_argument(
        '--input_file', 
        type=str, 
        required=True, 
        help='Path to the input markdown file to be processed.'
    )
    
    parser.add_argument(
        '--output_file', 
        type=str, 
        required=True, 
        help='Path to save the output results.'
    )
    
    return parser.parse_args()

def read_api_key(api_key_file):
    # Read the API key from the specified file
    try:
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
            if not api_key:
                raise ValueError("API key is empty.")
            return api_key
    except Exception as e:
        print(f"Error reading API key from file: {e}")
        exit(1)

def read_input_file(input_file):
    # Read the contents of the input file (markdown)
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading input file: {e}")
        exit(1)

def main():
    # Parse arguments
    args = parse_arguments()
    
    # Read the API key from the file
    api_key = read_api_key(args.api_key_file)
    
    # Read the input file contents (markdown)
    input_text = read_input_file(args.input_file)
    
    # Initialize the OpenAI client with the provided API key
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.siliconflow.cn/v1"
    )

    # System prompt for setting up the assistant
    system_prompt = """
    You are a helpful assistant with 10 year in maize genetic biology.
    """

    # Prepare the user prompt (use the content from the markdown file)
    user_prompt = f"请解析文献并提取：{input_text} 按顺序用制表符分隔，格式：基因组版本\\t基因ID\\t基因名\\t变异位点\\t调控性状\\t标题.不要任何解释和标记"

    # Prepare the messages for the API call
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    # Make the API call to get the response
    response = client.chat.completions.create(
        model="Pro/deepseek-ai/DeepSeek-V3",
        messages=messages,
        response_format={"type": "text"}
    )

    # Extract the content from the response
    response_content = response.choices[0].message.content

    # Save the response as plain text to the output file
    try:
        with open(args.output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(response_content)
        print(f"Parsing completed. Output saved to {args.output_file}.")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        exit(1)

if __name__ == "__main__":
    main()
