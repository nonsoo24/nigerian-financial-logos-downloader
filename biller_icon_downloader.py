import requests
import os
import json
import re # Import regex for advanced filename cleaning

# Define the path to the JSON data file
DATA_FILE = 'biller_data.json'

# Base directory for all downloaded images
BASE_DOWNLOAD_DIR = 'downloaded_biller_icons'

def sanitize_filename(name):
    """
    Cleans up a string to be safe for use as a filename or folder name.
    Removes invalid characters and replaces spaces with underscores.
    """
    s = str(name).strip()
    s = re.sub(r'[\\/:*?"<>|]', '', s)  # Remove invalid characters
    s = re.sub(r'\s+', '_', s)          # Replace spaces with single underscores
    s = re.sub(r'[^a-zA-Z0-9_.-]', '', s) # Remove any remaining non-alphanumeric, non-underscore, non-dot, non-hyphen chars
    s = s.strip('_.') # Remove leading/trailing underscores or dots
    return s

def download_image(url, folder_path, filename):
    """
    Downloads an image from a given URL to a specified folder.
    """
    if not url:
        print(f"Skipping download: No URL provided for {filename}")
        return

    full_path = os.path.join(folder_path, filename)
    os.makedirs(folder_path, exist_ok=True) # Ensure the category folder exists

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # Raise an exception for bad status codes

        with open(full_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {filename} to {folder_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url} for {filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {url} ({filename}): {e}")
    return False

def main():
    """
    Main function to load biller data, categorize, and download icons.
    """
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            biller_data = json.load(f)
        print(f"Successfully loaded biller data from {DATA_FILE}")
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' not found. Please create this file with your JSON biller data.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{DATA_FILE}'. Please check the file's format.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading '{DATA_FILE}': {e}")
        return

    download_summary = {}

    print(f"\nStarting biller icon download into '{BASE_DOWNLOAD_DIR}'...")

    for category_item in biller_data:
        category_name = category_item.get("category", "UnknownCategory")
        biller_list = category_item.get("billerList", [])

        sanitized_category_name = sanitize_filename(category_name)
        category_folder_path = os.path.join(BASE_DOWNLOAD_DIR, sanitized_category_name)

        if sanitized_category_name not in download_summary:
            download_summary[sanitized_category_name] = {"downloaded": 0, "skipped": 0}

        for biller in biller_list:
            biller_name = biller.get("billerName", "UnknownBiller")
            biller_icon_url = biller.get("billerIcon")

            if not biller_icon_url:
                print(f"Skipping '{biller_name}' in category '{category_name}': No icon URL found.")
                download_summary[sanitized_category_name]["skipped"] += 1
                continue

            # Generate a unique and safe filename for the icon
            # Use billerName + a portion of the URL or a unique ID to avoid conflicts
            # Extract file extension from the URL, handling potential query parameters
            url_path = biller_icon_url.split('?')[0] # Remove query parameters
            file_extension = os.path.splitext(url_path)[1]
            if not file_extension:
                file_extension = ".png" # Default if no extension found

            # Create a unique filename for the biller icon
            safe_biller_name = sanitize_filename(biller_name)
            filename = f"{safe_biller_name}{file_extension}"

            # Download the image
            if download_image(biller_icon_url, category_folder_path, filename):
                download_summary[sanitized_category_name]["downloaded"] += 1
            else:
                download_summary[sanitized_category_name]["skipped"] += 1

    print("\nDownload process complete.")
    print("Summary of downloads by category:")
    for category, counts in download_summary.items():
        print(f"  {category}: Downloaded {counts['downloaded']} icons, Skipped {counts['skipped']} icons.")

if __name__ == "__main__":
    main()