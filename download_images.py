import requests
import os

IMAGE_DATA = 'bank_data.json'

output_folder = "downloaded_bank_logos"
os.makedirs(output_folder, exist_ok=True)

for item in IMAGE_DATA:
    image_url = item.get("imageUrl")
    bank_name = item.get("bankName", "unknown_bank").replace(" ", "_").replace("/", "_")

    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status() # Raise an exception for bad status codes

            # Extract file extension from the URL
            file_extension = os.path.splitext(image_url)[1]
            if not file_extension: # Fallback if no extension in URL
                file_extension = ".png" # Assume PNG based on your data

            # Create a unique filename
            filename = f"{bank_name}_{item.get('bankCode')}{file_extension}"
            filepath = os.path.join(output_folder, filename)

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {image_url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {image_url}: {e}")

print("Download process complete.")