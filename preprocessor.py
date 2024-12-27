import re
import pandas as pd

def preprocess(data):
    pattern = r'\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}(?:\u202F?[ap]m) - '
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Clean non-breaking space and remove text after the datetime part
    df['message_date'] = df['message_date'].str.replace('\u202f', '', regex=True)
    df['message_date'] = df['message_date'].str.extract(r'(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}(?:am|pm))')[0]

    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M%p')

    # Rename column
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        # Use a raw string for the regex pattern
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # User name is present
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:  # It's a group notification
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['only_date'] = df['date'].dt.date
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    
    period = []
    for hour in df['hour']:
        if hour == 0:
            period.append(f"12AM-1AM")
        elif hour == 11:
            period.append(f"11AM-12PM")
        elif hour == 23:
            period.append(f"11PM-12AM")
        elif hour == 12:
            period.append(f"12PM-1PM")
        elif hour < 12:
            period.append(f"{hour}AM-{hour + 1}AM")
        else:
            period.append(f"{hour - 12}PM-{hour - 11}PM")

    df['period'] = period

    return df
