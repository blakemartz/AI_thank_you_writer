import pandas as pd
from gpt_api import write_thank_you
import time

SIGNATURE = "Love, Your Best Friend"
OCCASION = ""

# the free openai api has a rate limit of 3 requests per minute.
# this sleep value will pause the script between calls to stay within that limit
SLEEP_IN_SECONDS = 20

# initialize dataframe from csv
df = pd.read_csv("guest_list.csv")
# add response column to dataframe
df['response'] = None
# create list of guests and their gifts from dataframe
guest_gift_list = [{"name": row['name'], "gift": row['gift']} for (index, row) in df.iterrows()]

# iterate through list and call for letter
for i in guest_gift_list:
    guest_name = i["name"]
    guest_gift = i["gift"]

    # call API for thank you letter
    thank_you_letter = write_thank_you(guest=guest_name, gift=guest_gift, signature=SIGNATURE, occasion=OCCASION)

    # Find the index of the corresponding guest in df and update 'response' field
    guest_index = df[df['name'] == guest_name].index[0]
    df.loc[guest_index, 'response'] = thank_you_letter

    # print each thank you letter to terminal
    print(thank_you_letter)

    time.sleep(SLEEP_IN_SECONDS)

# Write the updated DataFrame back to guest_list.csv
df.to_csv("guest_list_responses.csv", index=False)
