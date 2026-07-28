# Publications markdown generator for AcademicPages
# 
# Takes a TSV / CSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). 
# Can be called via the command prompt by using `python3 publications.py [filename]`.

# Data format
# 
# The file needs to have the following columns as a header at the top:
# pub_date, title, venue, excerpt, citation, url_slug, paper_url, slides_url
# - `excerpt`, `paper_url`, and slides_url can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. 
#    The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`
import csv
import os
import re
import sys

# Flag to indicate an error occurred
EXIT_ERROR = 0

# The expected layout of the CSV / TSV file
HEADER_LEGACY  = ['pub_date', 'title', 'venue', 'excerpt', 'citation', 'url_slug', 'paper_url', 'slides_url']
HEADER_UPDATED = HEADER_LEGACY + ['category']
HEADER_V3      = HEADER_UPDATED + ['bibtex_url']

# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands)
# with their HTML encoded equivalents. This makes them look not so readable in raw format, but they are parsed and
# rendered nicely.
HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to
# concatenate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then
# does the description for the individual page.
def create_md(lines: list, layout: list):
    for item in lines:
        # Parse the filename information
        md_filename = f"{item[layout.index('pub_date')]}-{item[layout.index('url_slug')]}.md"
        html_filename = str(item[layout.index('pub_date')]) + "-" + item[layout.index('url_slug')]
        
        # Parse the YAML variables
        md = f"---\ntitle: \"{item[layout.index('title')]}\"\n"
        md += "collection: publications"
        if 'category' in layout:
            md += f"\ncategory: {item[layout.index('category')]}"
        else:
            md += "\ncategory: manuscripts"
        md += f"\npermalink: /publications/{html_filename}"
        if len(str(item[layout.index('excerpt')])) > 5:
            md += f"\nexcerpt: '{html_escape(item[layout.index('excerpt')])}'"
        md += f"\ndate: {item[layout.index('pub_date')]}"
        md += f"\nvenue: '{html_escape(item[layout.index('venue')])}'"
        if len(str(item[layout.index('paper_url')])) > 5:
            md += f"\npaperurl: '{item[layout.index('paper_url')]}'"
        if 'slides_url' in layout and len(str(item[layout.index('slides_url')])) > 5:
            md += f"\nslidesurl: '{item[layout.index('slides_url')]}'"
        if 'bibtex_url' in layout and len(str(item[layout.index('bibtex_url')])) > 5:
            md += f"\nbibtexurl: '{item[layout.index('bibtex_url')]}'"
        md += f"\ncitation: '{html_escape(item[layout.index('citation')])}'"
        md += "\n---\n"

        # This script generates FRONT MATTER ONLY. The citation and the download
        # links are rendered from the front matter by _layouts/single.html and
        # _includes/archive-single.html, so writing them into the body too would
        # show them twice.
        #
        # Hand-written body content IS supported and is preserved: anything you
        # add below the closing '---' of a file in _publications/ survives every
        # subsequent run of this script. That is where per-paper prose, figures
        # and equations go. Only the front matter is regenerated from the CSV.
        #
        # NOTE: `excerpt_separator: "\n\n"` is set in _config.yml, so the first
        # paragraph of any body you write would become the listing excerpt. Set
        # the `excerpt` column in the CSV to control that text explicitly.

        os.makedirs("../_publications/", exist_ok=True)
        md_filename = os.path.join("../_publications/", os.path.basename(md_filename))

        body = preserved_body(md_filename)
        with open(md_filename, 'w') as f:
            f.write(md + body)

def preserved_body(path: str) -> str:
    '''Return the hand-written body of an existing generated file, i.e. everything
    after the closing '---' of its front matter. Empty string if the file does not
    exist or has no body. This is what keeps per-paper prose from being clobbered
    when the CSV is regenerated.'''
    if not os.path.exists(path):
        return ''
    with open(path) as f:
        text = f.read()
    match = re.match(r'^---\r?\n.*?\r?\n---[ \t]*\r?\n?', text, re.DOTALL)
    if not match:
        return ''
    return text[match.end():]

def html_escape(text):
    """Produce entities within text."""
    return "".join(HTML_ESCAPE_TABLE.get(c,c) for c in text)

def read(filename: str) -> tuple[list, list]:
    '''Read the contents of the file, check the header and return the parsed line along with the file type.'''

    # Read the contents of the file
    lines = []
    with open(filename, 'r') as file:
        delimiter = ',' if filename.endswith('.csv') else '\t'
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            lines.append(row)

    # Verify the file format makes sense
    if len(lines) <= 1:
        print(f'Not enough lines in the file to process, found {len(lines)}', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    # Verify the header, remove it once checked
    for candidate in (HEADER_V3, HEADER_UPDATED, HEADER_LEGACY):
        if candidate == lines[0]:
            layout = candidate
            break
    else:
        print(lines[0])
        print('The header of the file does not match the expected format', file=sys.stderr)
        sys.exit(EXIT_ERROR)
    lines = lines[1:]
    
    # Return the lines and format
    return lines, layout

if __name__ == '__main__':
    # Make sure a filename was given
    if len(sys.argv) != 2:
        print('Usage: python3 publications.py [filename]', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    # Make sure the filename is TSV or CSV
    filename = sys.argv[1]
    if not (filename.endswith('.csv') or filename.endswith('.tsv')):
        print(f'Expected a TSV or CSV file, got {filename}', file=sys.stderr)
        sys.exit(EXIT_ERROR)    

    # Read and process the lines
    lines, layout = read(filename)
    create_md(lines, layout)
