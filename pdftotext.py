import os
import sys
import argparse
import PyPDF2

# A python script that receives as input through the command line a directory path and converts
# all the pdf files in that directory into plain text files. The name of the output file is the 
# same as the pdf file but replacing .pdf by .txt. The script also allows to include an optional 
# argument -o --output that allows to specify the output folder where the files are stored.


def main():
    # Define command line arguments
    parser = argparse.ArgumentParser(description='Convert PDF files to plain text')
    parser.add_argument('input_path', type=str, help='Path to directory containing PDF files')
    parser.add_argument('-o', '--output', type=str, help='Path to output folder where txt files will be written')

    # Parse command line arguments
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output or input_path  # Use input_path as output_path if not specified


    # If input path does not exist -> stop
    if not os.path.exists(input_path):
        parser.error(f"input_path directory '{input_path}' does not exist.")

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Created  output directory: {output_path}")

    # Iterate over PDF files in directory
    for input_file_name in os.listdir(input_path):
        #print(f'*** {file_name}')
        if input_file_name.endswith('.pdf'):
            # Create input and output file paths
            input_file_path = os.path.join(input_path, input_file_name)
            output_file_name = input_file_name[:-4] + '.txt'
            output_file_path = os.path.join(output_path, output_file_name)
            #print(f'**** input path {input_path} | output_path {output_path} | ofn {output_file_name}')
            # Convert PDF to plain text
            with open(input_file_path, 'rb') as input_file, open(output_file_path, 'w') as output_file:
                reader = PyPDF2.PdfReader(input_file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    output_file.write(text)

            print(f'{input_file_name} converted to {output_file_path}')

if __name__ == '__main__':
    main()
