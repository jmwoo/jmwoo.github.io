# This is a work in progress
# goal is to convert resume from a markdown file to a html/pdf file

import markdown2
import pdfkit
import os

# Function to convert Markdown file to HTML
def markdown_to_html(markdown_file_path):
    with open(markdown_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    html_content = markdown2.markdown(md_content)
    return html_content

# Function to save HTML content to a file
def save_html(html_content, html_file_path):
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# Function to convert HTML file to PDF
def html_to_pdf(html_file_path, pdf_file_path):
    try:
        pdfkit.from_file(html_file_path, pdf_file_path)
    except OSError as e:
        print(f"Error: {e}")
        print("Make sure 'wkhtmltopdf' is installed and accessible in your PATH.")
        exit(1)

# Paths
markdown_file_path = './resume.md'
html_file_path = './assets/resume.html'
pdf_file_path = './assets/resume.pdf'
assets_path = './assets'

# Read, convert, and save
html_content = markdown_to_html(markdown_file_path)

# Replace relative paths to assets with absolute paths
html_content = html_content.replace('src="assets/', f'src="{os.path.abspath(assets_path)}/')

# Save HTML to a temporary file
save_html(html_content, html_file_path)

# Convert HTML to PDF
html_to_pdf(html_file_path, pdf_file_path)

print(f"PDF generated successfully at: {pdf_file_path}")
