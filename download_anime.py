from pathlib import Path
from dotenv import load_dotenv
import os

# 1. Tell python-dotenv to look for a .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# 2. Now the Kaggle API will read these env vars automatically
from kaggle.api.kaggle_api_extended import KaggleApi

def download_anime_dataset(
    dataset="CooperUnion/anime-recommendations-database",
    dest="data",
    unzip=True,
    force=False
):
    """
    Fetches the latest dataset from Kaggle.
      - dataset: user/dataset-slug on Kaggle
      - dest: output folder
      - unzip: whether to extract .zip
      - force: re-download even if files exist
    """
    api = KaggleApi()
    api.authenticate()

    out = Path(dest)
    out.mkdir(parents=True, exist_ok=True)

    api.dataset_download_files(
        dataset,
        path=str(out),
        unzip=unzip,
        force=force
    )
    return out

if __name__ == "__main__":
    path = download_anime_dataset(force=False)
    print(f"Dataset ready in: {path}")
