import os
import subprocess
import argparse

def convert_pdfs_to_markdown():
    # Ensure the markdown directory exists
    if not os.path.exists("markdown"):
        os.makedirs("markdown")
    
    # Loop through all PDF files in the input directory
    input_folder = "input"
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            # Define the output filename in the markdown folder
            output_filename = f"markdown/{filename[:-4]}.md"
            
            # Check if the markdown file already exists
            if os.path.exists(output_filename):
                print(f"Skipping {filename} as it is already converted.")
                continue
            
            # Convert PDF to markdown using pdftomd.py
            print(f"Converting {filename} to markdown...")
            subprocess.run(["python", "pdftomd.py", os.path.join(input_folder, filename), "-o", output_filename], check=True)
            print(f"{filename} converted to {output_filename}")

def call_deepseek_api_on_markdown():
    # Ensure the answer directory exists
    if not os.path.exists("answer"):
        os.makedirs("answer")
    
    # Loop through all markdown files in the markdown directory
    for filename in os.listdir("markdown"):
        if filename.endswith(".md"):
            input_file = f"markdown/{filename}"
            output_file = f"answer/{filename[:-3]}.txt"
            
            # Check if the answer file already exists
            if os.path.exists(output_file):
                print(f"Skipping {filename} as it has already been processed.")
                continue
            
            print(f"Processing {filename} with DeepSeek API...")

            # Run deepseek_parse.py to get the answer and save it to output_file
            subprocess.run([
                "python", "deepseek_parse.py", 
                "--api_key_file", "apikey.txt", 
                "--input_file", input_file, 
                "--output_file", output_file
            ], check=True)
            print(f"Answer for {filename} saved to {output_file}")

def main():
    # Call both functions
    convert_pdfs_to_markdown()
    call_deepseek_api_on_markdown()

if __name__ == "__main__":
    main()
