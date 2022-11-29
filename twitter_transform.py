import re
import pandas as pd
from twitter_extract import run_twitter_extract

raw = run_twitter_extract()

def run_twitter_transform(data):
    def remove_emoji(data):
        emoj = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002500-\U00002BEF"  # chinese char
                          u"\U00002702-\U000027B0"
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          u"\U0001f926-\U0001f937"
                          u"\U00010000-\U0010ffff"
                          u"\u2640-\u2642"
                          u"\u2600-\u2B55"
                          u"\u200d"
                          u"\u23cf"
                          u"\u23e9"
                          u"\u231a"
                          u"\ufe0f"  # dingbats
                          u"\u3030"
                          "]+", re.UNICODE)
        result = re.sub(emoj, '', data)
        return result

    def remove_user_and_link(data):
        result = ' '.join(
            re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data).split())
        return result

    message_list = []
    for d in data['text']:
        no_emoji_message = remove_emoji(d)

        clean_message = remove_user_and_link(no_emoji_message)

        final_message = {
            'text': clean_message
        }
        message_list.append(final_message)

    df = pd.DataFrame(message_list)
    return df

run_twitter_transform(raw)