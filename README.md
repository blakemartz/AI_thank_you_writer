# AI Thank You Writer
This repo uses a simple python script to write thank you letters for gifts based on user csv file. Uses OpenAI's ChatGPT API.

# // Get Started //

## Clone the Repo:
Clone the repository. 
```shell
git clone https://github.com/blakemartz/AI_thank_you_writer.git
```

## Environment Setup
In order to set your environment up to run the code here, first navigate to the AI_thank_you_writer directory and install all requirements:

```shell
pip install -r requirements.txt
```

## OpenAI API Key 
You will need the OpenAI API key to run this, get your OpenAI key from [here](https://platform.openai.com/account/api-keys)

Enter your OpenAI API key in the text file "openai_api_key.txt".
Only enter the API key. Do not use any quotes or variables.

*Using the free OpenAI API, the script will take approximately 20 seconds per guest. You can customize the timer as you see fit.

## Customize the script:
In the main.py file, customize the variables OCCASION and SIGNATURE. 

For example:
OCCASION = "Wedding"
SIGNATURE = "Love, John and Jessie"

## Update local files
Make sure to replace "guest_list.csv" with your own file.
Make sure your "guest_list.csv" has two columns titled "name", and "gift"

To generate your thank you letters, run main.py
The script will generate "thank_you_letters.csv". 
Letters will print in the terminal as they are generated. The output csv will be generated once all letters are complete.

## Hints:
1. Customize the names in your csv with their relationship to get more personal responses.
Example:
"My sister Sandra"

2. Add details to the OCCASION to get more specific responses. 
Example: OCCASION = "My wedding, which was almost a year ago"




