# GeorgiaTech_task

<p>This is a basic system that takes a company's ticker from the user, downloads 10-K filling from 1995 to 2023 using SEC EDGAR API, pre-processes it, creates a vector database using CHROMA, and then using RAG, an open-source GPT4ALL LLM model gives fundamental analysis of that company, and suggests whether to buy or sell a stock of that company, along with an option to interact with the documents.</p>

-------------------------

## Steps to follow:
1. Clone this repository.
  
   ```
   git clone https://github.com/ArghaKamalSamanta/GeorgiaTech_task.git
   ```
2. Get your SEC EDGAR API key from <a href=https://sec-api.io/>here</a>, and paste it in the  `.env` file.

   ```.env
   SEC_API_KEY = "<YOUR_API_KEY>"
   ```
3. Now, you can either wait for the code to download the model or download it manually. To download it manually, visit <a href=https://gpt4all.io/index.html>here</a>, download  `mistral-7b-instruct-v0.1.Q4_0.gguf`,  place it in a subfolder, and name it  `GPT4All_models` .
4. Run  `app.py` .

   ```
   python app.py
   ```
5. Visit the link where the UI is hosted, something like  `http://127.0.0.1:5000/`

----------------------------

## Results:

![Screenshot (908)](https://github.com/ArghaKamalSamanta/GeorgiaTech_task/assets/97786651/13a9c01f-0943-49c6-b042-7a5c1600458d)

![Screenshot (909)](https://github.com/ArghaKamalSamanta/GeorgiaTech_task/assets/97786651/4dbf2b34-b36e-4c15-9f6e-7bce8f81c823)



*N.B.: The model used is about 3.8 GB in size. Thus, it may take time to generate a response if you don't have a GPU core.*

