# Nigerian Financial Logos Downloader

This repository contains Python scripts designed to download and categorize bank logos and biller icons related to Nigerian financial services. The scripts fetch image URLs from external JSON data files and organize the downloaded images into structured folders based on predefined categories.

## ✨ Features

* **Categorized Downloads:** Automatically sorts downloaded bank logos into "Commercial Banks," "Microfinance Banks (MFBs)," "Mortgage Banks," "Payment Service Banks (PSBs)," "Merchant Banks," "Finance Companies," "Wallets/Digital Services," and "Others" directories.
* **Biller Icon Organization:** Organizes biller icons into folders corresponding to their respective service categories (e.g., "Internet Data", "Betting", "CableTV", "Electricity", "Transport and Tolls", "Education", "Solar", "eSIM").
* **External Data Source:** Reads bank and biller data from external JSON files (`bank_data.json` and `biller_data.json`), ensuring a clean separation of code and data.
* **Placeholder Image Exclusion:** Intelligently skips downloading generic "Default-Bank.png" placeholder images for bank logos.
* **Robust File Naming:** Sanitizes bank/biller names to create valid and unique filenames, preventing issues with special characters.

## 🚀 Getting Started

Follow these instructions to set up and run the scripts on your local machine.

### Prerequisites

* Python 3.x installed on your system.
* `pip` (Python package installer), which usually comes with Python.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourGitHubUsername/nigerian-financial-logos-downloader.git](https://github.com/YourGitHubUsername/nigerian-financial-logos-downloader.git)
    cd nigerian-financial-logos-downloader
    ```
    (Replace `YourGitHubUsername` with your actual GitHub username)

2.  **Create a Virtual Environment (Recommended):**
    It's best practice to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install requests
    ```

5.  **Prepare Your Data Files:**
    The scripts expect two JSON files in the root directory of the project:

    * **`bank_data.json`**: This file should contain the JSON array of bank data.
        * Create a new file named `bank_data.json` in the `nigerian-financial-logos-downloader` directory.
        * Paste your entire bank JSON data into this file.

    * **`biller_data.json`**: This file should contain the JSON array of biller data.
        * Create a new file named `biller_data.json` in the `nigerian-financial-logos-downloader` directory.
        * Paste your entire biller JSON data into this file.

    **Example `bank_data.json` structure (truncated):**
    ```json
    [
        {
            "bankName": "Fidelity Bank",
            "bankCode": "000007",
            "imageUrl": "imageUrl"
        },
        {
            "bankName": "Access Bank",
            "bankCode": "000014",
            "imageUrl": "imageUrl"
        }
        // ... more bank data
    ]
    ```

    **Example `biller_data.json` structure (truncated):**
    ```json
    [
        {
            "category": "Internet Data",
            "billerList": [
                {
                    "billerName": "MTN NG DATA",
                    "billerIcon": "billerIcon"
                }
                // ... more biller data
            ]
        }
        // ... more categories and billers
    ]
    ```

## 🏃 Usage

Once the setup is complete, you can run the scripts from your activated virtual environment.

### Downloading and Categorizing Bank Logos

To download and categorize bank logos:

```bash
python categorized_bank_downloader.py
```

This script will create a downloaded_bank_logos directory in the project root, containing subfolders for each bank category (e.g., Commercial_Banks, Microfinance_Banks_(MFBs), Others), with the respective bank logos inside.

Downloading and Categorizing Biller Icons
To download and categorize biller icons:

```bash
python biller_icon_downloader.py
```

This script will create a downloaded_biller_icons directory in the project root, containing subfolders for each biller category (e.g., Internet_Data, Betting, CableTV), with the respective biller icons inside.

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, feel free to:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📄 Credits

All bank and biller data, including associated icons and URLs, were sourced from publicly accessible information provided by [Kuda Bank](https://kuda.com/).