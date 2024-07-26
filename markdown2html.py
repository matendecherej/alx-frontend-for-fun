#!/usr/bin/env python3

import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    try:
        with open(markdown_file, 'r') as f:
            markdown_text = f.read()
        html_text = markdown.markdown(markdown_text)
        with open(output_file, 'w') as f:
            f.write(html_text)
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)
