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
        help='Path to the file containing the DeepSeek API key.'
    )
    
    parser.add_argument(
        '--input_file', 
        type=str, 
        required=True, 
        help='Path to the input .txt file to be processed.'
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
    # Read the contents of the input file
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
    
    # Read the input file contents
    input_text = read_input_file(args.input_file)
    
    # Initialize the OpenAI client with the provided API key
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )

    # System prompt for parsing the question and answer from text
    system_prompt = """
    The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

    EXAMPLE INPUT: 
    Which is the highest mountain in the world? Mount Everest.

    EXAMPLE JSON OUTPUT:
    {
        "question": "Which is the highest mountain in the world?",
        "answer": "Mount Everest"
    }
    """

    # User prompt based on the input file content
    user_prompt = f"请解析文献并提取：{input_text} 请解析文献并提取：1. 基因组版本（如B73 RefGen_v4）2. 基因ID（仅Zm/Grm开头）3. 基因名称4. 核心功能变异位点（选最主要的一个）5. 调控的性状6. 文章标题.按顺序用制表符分隔，格式：基因组版本\\t基因ID\\t基因名\\t变异位点\\t调控性状\\t标题.不要任何解释和标记"

    # Prepare the messages to send to the DeepSeek API
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]

    # Make the request to the API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={
            'type': 'json_object'
        },
        temperature=0,  
        max_tokens=4096 
    )

    # Get the response content and save it to the output file
    output_content = json.loads(response.choices[0].message.content)

    # Save the response to the output file
    try:
        with open(args.output_file, 'w', encoding='utf-8') as out_file:
            json.dump(output_content, out_file, ensure_ascii=False, indent=4)
        print(f"Parsing completed. Output saved to {args.output_file}.")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        exit(1)

if __name__ == "__main__":
    main()
