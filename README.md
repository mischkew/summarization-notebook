# Text Summarization Lab

This Jupyter Lab contains several approaches to summarize political news articles of The Telegraph. We combine rules, sentiment analysis and state-of-the-art extraction based summary algorithms. We use different APIs (Google NLP, Aylien, ...) and text corpora (WordNet, Punkt, ... available from NLTK). This environment is used for prototyping our approaches.

## Prerequisites

You will need a python3 development environment. Best to use virtualenv also.

```bash
brew install python3
pip install virtualenv
````

## Installation

Clone the repository.

```bash
git clone https://github.com/mischkew/summarization-notebook
```

Setup a virtualenv.

```bash
virtualenv venv -p python3
source venv/bin/activate
```

Install requirements and activate Jupyter Lab.

```bash
pip install -r requirements.txt
jupyter serverextension enable --py jupyterlab --sys-prefix
```

### API Setup

Before you can use the Google API, you have to setup your Service Account and export the credentials.
Have a look here: https://cloud.google.com/natural-language/docs/common/auth#set_up_a_service_account

## Usage

Run Jupyter Lab or Jupyter Notebook

```bash
jupyter lab
# jupyter notebook
```
