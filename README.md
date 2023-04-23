# AI_thank_you_writer
This is a simple thank you letter assistant that uses the OpenAI API.
It takes a csv with names and gifts and outputs a csv file with custom thank you letters.

Enter your OpenAI API key in the text file "openai_api_key.txt".
Only enter the API key. Do not use any quotes or variables.

In the main.py file, customize the variables OCCASION and SIGNATURE. 
For example:
OCCASION = "Wedding"
SIGNATURE = "Love, John and Jessie"

Make sure to replace "guest_list.csv" with your own file.
Make sure your "guest_list.csv" has two columns titled "name", and "gift"

To generate your thank you letters, run main.py and the script will generate "thank_you_letters.csv". 
Letters will print in the terminal as they are generated. The output csv will be generated once all letters are complete.

Hints:
1. Customize the names in your csv with their relationship to get more personal responses.
Example:
"My sister Sandra"

2. Add details to the OCCASION to get more specific responses. 
Example: OCCASION = "My wedding, which was almost a year ago"


*Using the free OpenAI API, the script will take approximately 20 seconds per guest. You can customize the timer as you see fit.
