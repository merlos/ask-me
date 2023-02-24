# Ask me

Ask me is a proof of concept (PoC) of the use of OpenAI GPT that allows you to ask questions based on the content of a particular knowledge base (corpus), for example, your website, your organization regulatory framework, guidance, or a particular set of documents.

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
* [OpenAI account](https://platform.openai.com/), and and [API key](https://platform.openai.com/account/api-keys). You get $18 USD of free credits for testing.


After cloning this repo (`git clone https://github.com/merlos/ask-me/`):

1. Activate the virtual environment 
    ```shell
    source venv/bin/activate
    ```
2. Install requirements
    ```shell
    pip install -r requirements.txt
    ```
3. Set the OpenAI API key environment variable
  
    ```shell

    # OSX and GNU/Linux
    export OPENAI_API_KEY=<your key>

    # Windows
    setenv OPENAI_API_KEY=<your key>
    ```
  
  Then, you can test the API is working by running

  ```shell
  python openai_api_test.py
  ```

### Step 1: Collect/Scrapping the data

Scrap the webpage that will be used as source or your knowledge base from.

```shell
python scrapper.py https://www.merlos.org
```
This will create the folder `text/www.merlos.org/` with the scrapped pages in text format.

Note: This step can be replaced with a conversion of any kind of file into text. For example, a PDF, Word Document, etc. You just need to place the documents converted into plain text (i.e. `.txt`) in the `./text` folder

### Step 2: Process the data.

Run the script with the same domain
```shell
python process.py https://www.merlos.org
```

This will create the files `processed/corpus.csv`, which is just a list of the pages, and `processed/embeddings.csv` that includes the embeddings. 

## Usage

Now it is time to make the questions to the AI. You can use the command line script `ask.py` with the question as argument.

```shell
python ask.py "Who is Juan?"
```

Alternatively you can test the output on a browser, run the script:

```shell
python web.py
```

Then open a browser with the address http://localhost:5000

Finally, you can also query the API of `web.py` manually by making a `POST` at the endpoint http://localhost:5000/api/answers
with a JSON body like this:

```json
{"question": "Who is Juan?"}
```
The response is something like:
```json
{ 
    "question": "Who is Juan?",
    "answer": "The answer provided by OpenAI API"
}
```

## References

* Tutorial to make Q&A using OpenAI API https://platform.openai.com/docs/tutorials/web-qa-embeddings
* Source code of the tutorial https://github.com/openai/openai-cookbook/tree/main/solutions/web_crawl_Q%26A
* A more advanced version using [Dagster](https://dagster.io) and [LangChain](https://github.com/hwchase17/langchain) https://dagster.io/blog/chatgpt-langchain
* A version using [LangChain](https://github.com/hwchase17/langchain) and a Notion DB https://github.com/hwchase17/notion-qa 


## LICENSE MIT

Copyright (c) 2023 Juan M. Merlos @merlos.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
