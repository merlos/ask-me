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
    parser.add_argument('dir_path', type=str, help='Path to directory containing PDF files')
    parser.add_argument('-o', '--output', type=str, help='Path to output directory')

    # Parse command line arguments
    args = parser.parse_args()
    dir_path = args.dir_path
    output_base_path = args.output or dir_path  # Use dir_path as output_path if not specified

    # Iterate over PDF files in directory
    for file_name in os.listdir(dir_path):
        #print(f'*** {file_name}')
        if file_name.endswith('.pdf'):
            # Create input and output file paths
            input_path = os.path.join(dir_path, file_name)
            output_file_name = file_name[:-4] + '.txt'
            output_path = os.path.join(output_base_path, output_file_name)
            #print(f'**** dir path {dir_path} | output_path {output_path} | ofn {output_file_name}')
            # Convert PDF to plain text
            with open(input_path, 'rb') as input_file, open(output_path, 'w') as output_file:
                reader = PyPDF2.PdfReader(input_file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    output_file.write(text)

            print(f'{file_name} converted to {output_path}')

if __name__ == '__main__':
    main()
