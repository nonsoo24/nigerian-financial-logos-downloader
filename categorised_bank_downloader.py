import requests
import os
import json

# Define the path to the JSON data file
DATA_FILE = 'bank_data.json'

# Base directory for all downloaded images
BASE_DOWNLOAD_DIR = 'downloaded_bank_logos'

# Define categories and their corresponding keywords/suffixes
# This list can be expanded or refined based on more detailed bank data
CATEGORIES = {
    "Commercial Banks": ["bank", "plc", "commercial"], # General commercial banks
    "Microfinance Banks (MFBs)": ["mfb", "microfinance bank", "kuda"], # Microfinance banks
    "Mortgage Banks": ["mortgage bank", "mortgage"], # Mortgage banks
    "Payment Service Banks (PSBs)": ["psb", "payment service bank"], # Payment service banks
    "Merchant Banks": ["merchant bank", "merchant"], # Merchant banks
    "Finance Companies": ["finance company", "finance limited", "finance", "credit"], # Finance companies
    "Wallets/Digital Services": ["wallet", "digital services", "pay", "money", "xpress account", "mobile", "app", "pocket"], # Digital wallets/services
}

# List of image URLs to ignore (case-insensitive)
IGNORE_IMAGE_URLS = [
    "Default-Bank.png",
    "DEFAULT-BANK.PNG",
    "Default-Bank.png", # Added for consistency, though already covered
    "DEFAULT-BANK.PNG"  # Added for consistency, though already covered
]

def get_bank_category(bank_name):
    """
    Determines the category of a bank based on its name.
    """
    bank_name_lower = bank_name.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in bank_name_lower for keyword in keywords):
            return category
    return "Others" # Default category if no match is found

def download_image(url, folder_path, filename):
    """
    Downloads an image from a given URL to a specified folder.
    """
    if not url:
        print(f"Skipping download: No URL provided for {filename}")
        return

    # Check if the URL is in the ignore list
    if any(ignore_url.lower() in url.lower() for ignore_url in IGNORE_IMAGE_URLS):
        print(f"Skipping download: {filename} uses a default placeholder image.")
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
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url} for {filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {url} ({filename}): {e}")

def main():
    """
    Main function to load bank data, categorize, and download images.
    """
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            bank_data = json.load(f)
        print(f"Successfully loaded bank data from {DATA_FILE}")
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' not found. Please create this file with your JSON bank data.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{DATA_FILE}'. Please check the file's format.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading '{DATA_FILE}': {e}")
        return

    total_skipped = 0
    total_downloaded = 0

    for bank in bank_data:
        bank_name = bank.get("bankName", "UnknownBank")
        image_url = bank.get("imageUrl")
        bank_code = bank.get("bankCode", "NoCode")

        # Clean up bank name for filename
        safe_bank_name = bank_name.replace(" ", "_").replace("/", "_").replace(".", "").replace("(", "").replace(")", "").replace("&", "and")
        # Ensure filename is unique and has a proper extension
        file_extension = os.path.splitext(image_url)[1] if image_url else ".png"
        if not file_extension or len(file_extension) > 5: # Basic check for valid extension
            file_extension = ".png" # Default to png if extension is missing or looks odd

        filename = f"{safe_bank_name}_{bank_code}{file_extension}"

        # Determine category and create subfolder path
        category = get_bank_category(bank_name)
        category_folder = os.path.join(BASE_DOWNLOAD_DIR, category)

        # Check if the image URL is one of the default placeholders
        if image_url and any(ignore_url.lower() in image_url.lower() for ignore_url in IGNORE_IMAGE_URLS):
            print(f"Skipping '{bank_name}' due to default placeholder image.")
            total_skipped += 1
            continue

        if image_url:
            download_image(image_url, category_folder, filename)
            total_downloaded += 1
        else:
            print(f"Skipping '{bank_name}': No image URL found.")
            total_skipped += 1

    print(f"\nDownload process complete. Downloaded {total_downloaded} images, skipped {total_skipped} images.")

if __name__ == "__main__":
    main()
