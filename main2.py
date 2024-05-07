from data1 import fetch_data
from injestion import injestion
from qa_chain import get_qa_chain

ticker = input("Company ticker? ")
# fetch_data(ticker=ticker)
# injestion()
qa_chain = get_qa_chain()

query = """
        You are given the following data for {ticker} from 1995 to 2023. Go through it once.
        It contains informations like:
        1. the balance sheet for the company
        2. the income statement
        3. the cash flow statement
        4. the shareholders' equity statement
        The trends of these informations from 1995 to 2023 can be used to do fundamental analysis for this company.
        Analyse these files, and keep in mind the analysis and results you have taken out beforehand, and generate a fundamental analysis report  of the company in the following format:

        1. Company name
        2. About the company in 2 lines.
        3. Display the data and values
        4. Show financial ratios one by one, the value and its implications.
        5. According to the result, what's the sentiment of the stock, whther strong buy or strong sell.

        Use numbers wherever required and make sure to be 100 percent confident with your stance.
        Give me a complete analysis.
        """

result = qa_chain(query)
answer = result['result']
print("=> A BRIEF FUNDAMENTAL ANALYSIS:\n\n" + answer)

while True:
    print("\nType EXIT to exit.\n")
    query = input("What else on your mind: ")
    if query == 'EXIT':
        break
    result = qa_chain(query)
    answer = result['result']
    print(answer)