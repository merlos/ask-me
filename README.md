# Ask me

Ask me is a proof of concept (PoC) of the use of OpenAI GPT that allows you to ask questions based on the content of a particular knowledge base.

It is based on the OpenAI tutorial that explains how to make a [Q&A for a web content](https://platform.openai.com/docs/tutorials/web-qa-embeddings)


## How does it work?

First you need to format the data into something that can be used by the API.

1) **Gather the content you want to use** This can be defining the set of webpages that can be browsed, a set of PDF, markdown, word files that have the content.

2) **Convert the content of txt files**. Convert those files into plain text. We need this step because the model that generates the answer needs plain text as input.

3) **Create a set of embeddings**. Embeddings is a way to translate information into a format (usually a vector of numbers) that machine learning algorithms can use to make predictions or decisions. In our case the embeddings are used to find the documents that most probably have the information that can be used to generate the answer to our question. To create the embeddings the text files will be broken in chunks and create embeddings for each chunk.


### What happens behind the scenes when you ask a question?

1) The first thing that will be done is to try to find the chunks of text that most probably have the answer to the question. To do that we'll pass the embeddings and the question to one of the OpenAI endpoints API.

2) Once we have the text that most likely have the answer, we'll ask the AI behind ChatGPT (i.e GPT) to build an answer based on the chunks of text attached. 

## Setup

Pre-requisites:

* Python (it was tested with v3.9)
* Open API account, and the creation of an [API key](https://platform.openai.com/account/api-keys). You get $18 USD of free credits for testing.

Clone this repo:

1. Activate the virtual environment 
    ```shell
    source venv/bin/activate
    ```
2. Install requirements

  ```shell
  pip install -r requirements.txt
  ```
3. Set the API key env
  
  ```shell
  
  # OSX and GNU/Linux
  export OPENAI_API_KEY=<your key>

  # Windows
  setenv OPENAI_API_KEY=<your key>
  ```
  Then, tou can test the API is working by running

  ```shell
  python openai_api_test.py
  ```

## Step 1: Collect/Scrapping the data


First scrap the webpage you want to create the knowledge base from.

Edit the file scrapper.py and update the domains to get the data from.

```python
# Define root domain to crawl
domain = "www.merlos.org"
full_url = "https://www.merlos.org"
```

```shell
python scrapper.py
```

This will create a folder `text/<domain>/` with the scrapped pages as well as `processed/scrapped.csv`

Them run process

```shell
python process.py
```
This will create the file `processed/embeddings.csv`

Lastly, to test the results you can use the script `ask.py`

```shell
python ask.py "Who is Juan?"
```

# Web interface

You can also test the solution on a browser. To do that you can run the script:

```
python web.py
```

It will launch a server at http://localhost:5000

You can also query the API manually by making a POST at the endpoint http://localhost:5000/api/answers
with a JSON body like this

```json
{"question": "Who is Juan?"}
```

The response is
```json
{ 
    "question": "Who is Juan?",
    "answer": "The answer provided by OpenAI API"
}
```


References:
* Tutorial to make Q&A using OpenAI API https://platform.openai.com/docs/tutorials/web-qa-embeddings
* Source code of the tutorial https://github.com/openai/openai-cookbook/tree/main/solutions/web_crawl_Q%26A


# LICENSE MIT
