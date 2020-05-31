import pandas as pd
import re

# Raw text from archive:
# [4/29/19, 12:25:49 PM] Bilal Hashmi: Yes exactly

# Goal is to break down to raw text into four tokens
# {Date}, {Time} - {Author}: {Message}

def isDateAndTime(raw_text):
    sample = "[4/29/19, 12:25:49 PM] Bilal Hashmi: Yes exactly"
    # Learn how REGEX works: https://medium.com/tech-tajawal/regular-expressions-the-last-guide-6800283ac034
    pattern = '^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)(\d{2}|\d{4}), ([0-9][0-9]):([0-9][0-9]) -'

    result = re.match(pattern, sample)
    if result:
        print("WHAY")
        return True
    print("PAKISTAN WHAT")
    return False



def isAuthor(text):
    patterns = [
        '([\w]+):',                        # First Name
        '([\w]+[\s]+[\w]+):',              # First Name + Last Name
        '([\w]+[\s]+[\w]+[\s]+[\w]+):',    # First Name + Middle Name + Last Name
        '([+]\d{2} \d{5} \d{5}):',         # Mobile Number (Pakistan)
        '([+]\d{2} \d{3} \d{3} \d{4}):',   # Mobile Number (US)
        '([+]\d{2} \d{4} \d{7})'           # Mobile Number (UK/Europe)
    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, text)
    if result:
        return True
    return False


def parseData(line_in):    
    split = line_in.split(" - ")
    dateTime = split[0]

    date, time = dateTime.split(", ")

    #todo 
    message = ' '.join(split[1:])

    if isAuthor(message):
        splitMessage = message.split(': ')
        author = splitMessage[0] 
        message = ' '.join(splitMessage[1:])
    
    # Author will return null for all raw text similar to "Bilal Hashmi created the group"
    else:
        author = None
    return date, time, author, message

def main():
    processedData = []
    path = '_chat.txt'

    line = "[4/29/19, 12:25:49 PM] Bilal Hashmi: Yes exactly"
    data = parseData(line)
    for elt in data:
        print(elt)
    # with open(path, encoding="utf-8") as file:
    #     # Ignore first line of the conversation ("...Messages to this group are now secured with end-to-end encryption.")
    #     file.readline()

    #     # For multi-line messages
    #     buffer = []
    #     date, time, author = None, None, None 
        
    #     while True:
    #         line = file.readline()
            
    #         # EOF reached
    #         if not line:
    #             break
            
    #         # Remove random leading and trailing whitespaces
    #         line = line.strip()

    #         # New message
    #         if isDateAndTime(line):
    #             print("in here mate")
    #             # If buffer full from previous iteration, append
    #             if len(buffer) > 0:
    #                 processedData.append([date, time, author, ' '.join(buffer)])

    #             # Clear the buffer
    #             buffer.clear()

    #             date, time, author, message = parseData(line)
    #             buffer.append(message)
    #         else:
    #             # At this point, if its not date And Time, its part of a multi-line message, so append to message buffer
    #             buffer.append(line)
    

    # dataframe = pd.DataFrame(processedData, columns=['Date', 'Time', 'Author', 'Message'])
    


if __name__ == "__main__":
    main()