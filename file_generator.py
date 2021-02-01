'''
This file is going to generate new python files that will speed up the process
of making new files during my time running through the coding problems in
Cracking the Coding Interview.
'''

import argparse
import os
import shutil

if __name__ == "__main__":

    # usage: python file_generator.py <path-to-file>
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file_path", help="The destination of the file to be created")
    args = parser.parse_args()

    output_path = args.output_file_path
    basename = os.path.basename(output_path)
    dirname = os.path.dirname(output_path)
    
    template_path = "./problem_template.py"

    try:
        os.makedirs(dirname, exist_ok=True)
    except OSError as error:
        print("There has been an error creating the directories.")

    # Now make the file that is going to go there
    with open(output_path, 'w') as file:
        shutil.copyfile(template_path, output_path)

