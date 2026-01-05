# Data Engineering Techniques: Reddit Sentiment Analysis

| Name                    | Responsibility                        | GitHub                                                 |
| :---------------------- | :------------------------------------ | :----------------------------------------------------- |
| **Clemens Hafenscher**  | Data Engineering / Retrieval          | [@MrNobdy-T](https://github.com/MrNobdy-T)             |
| **Julia Tuka**          | Machine Learning / Sentiment Analysis | [@juliatuka](https://github.com/juliatuka)             |
| **Michael M. Werfring** | Data Visualization / Analysis         | [@MichaelWerfring](https://github.com/MichaelWerfring) |

## Getting Started

```bash
# Pull latest code:
git pull

# Install packages:
pip install -r requirements.txt

# Activate environment (Windows)
.venv\Scripts\activate

# Activate environment (Mac/Linux)
On Mac/Linux: `source .venv/bin/activate`
```

## Before Pushing Code

To ensure all contributors have the same libraries, update the requirements file before pushing.

```bash
pip freeze > requirements.txt
```

# Project Structure

Please place your files in the correct directories to keep the repository organized:

-   `/notebooks` - Jupyter notebooks
-   `/src` - Larger utility functions (e.g., utils.py)
-   `/test` - Unit tests and validation scripts
-   `/data` - Local data files (this folder is ignored by Git)
