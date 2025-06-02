"""
Downloader script because urls would be too long
"""

import os
import requests

urls_dir: str = 'urls'
output_dir: str = 'svgs'

os.makedirs(output_dir, exist_ok=True)

for url_file_name in os.listdir(urls_dir):

    url_file_path = os.path.join(urls_dir, url_file_name)

    with open(url_file_path, 'r') as f:
        url = f.read().strip()

        try:
            r = requests.get(url)
            r.raise_for_status()
            
            svg_file_name = os.path.splitext(url_file_name)[0] + '.svg'
            svg_file_path = os.path.join(output_dir, svg_file_name)

            with open(svg_file_path, 'wb') as svg_file:
                svg_file.write(r.content)

            print(f"Downloaded: {svg_file_name}")

        except Exception as e:
            print(f"Failed to download from {url}: {e}")
