import urllib.request
import os

def download_dataset():
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "Telco-Customer-Churn.csv")
    
    print(f"Downloading dataset from:\n{url}")
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"Successfully downloaded and saved to: {output_path}")
        # Print basic file info
        file_size = os.path.getsize(output_path)
        print(f"File size: {file_size / 1024:.2f} KB")
    except Exception as e:
        print(f"Error downloading dataset: {e}")

if __name__ == "__main__":
    download_dataset()
