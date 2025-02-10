import requests
import re
from bs4 import BeautifulSoup

def fetch_google_doc(url):
    # Fetch the content from the Google Doc URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to fetch the document.")

def parse_grid_data(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Get the text content from the document
    text = soup.get_text(separator=' ', strip=True)
    
    # Extract the relevant lines from the text
    pattern = r'(\d+)\s+(\S)\s+(\d+)'
    lines = re.findall(pattern, text)
    # Prepare to parse the coordinates and characters
    grid_data = []
    
    for line in lines:
        x, char, y = line
        grid_data.append((int(x), char, int(y)))
    
    return grid_data

def build_grid(grid_data):
    if not grid_data:
        print("Grid data is empty.")
        return None
    # Determine the grid size based on the coordinates
    max_x = max([x for x, _, _ in grid_data])
    max_y = max([y for _, _, y in grid_data])
    
    # Initialize an empty grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill the grid with characters at the specified coordinates
    for x, char, y in grid_data:
        grid[y][x] = char
    return grid

def print_grid(grid):
    if grid is None:
        print("Grid is empty, nothing to print.")
        return
    # Print the grid row by row
    for row in reversed(grid):
        print(''.join(row))

def main(url):
    html_content = fetch_google_doc(url)
    grid_data = parse_grid_data(html_content)
    grid = build_grid(grid_data)
    print_grid(grid)

# Example usage
google_doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
main(google_doc_url)
