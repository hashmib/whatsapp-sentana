import pandas as pd
import re

# Raw text from archive:
# [4/29/19, 1:03:21 PM] Talal Siddiqui: What's mine


# Goal is to break down to raw text into four tokens
# {Date}, {Time} - {Author}: {Message}


# todo: primitive implementation, needs regex for proper handling
def isDateTime(raw_text):
    return "[" in raw_text and "]" in raw_text



def parseData(line_in):
    #line_in = "‎[5/31/20, 19:20:23] ‪+92 321 2287108‬: ‎image omitted" 
    
    split_str = line_in.split("] ")
    dateTime = split_str[0].split("[")[1]

    date, time = dateTime.split(", ")
    remainder = ' '.join(split_str[1:])

    checkAuthorChar = ':'

    # Messages without an author (:) are ignored (eg - [4/29/19, 12:06:20] ‎Adeel Khalique created this group)
    if checkAuthorChar in remainder:
        split_remainder = remainder.split(': ')
        author = split_remainder[0] 
        message = ' '.join(split_remainder[1:])
        message = message.strip('\u200e')
    
    # Author will return null for all raw text similar to "Bilal Hashmi created the group"
    else:
        author = None
        message = None
    return date, time, author, message


def main():
    processedData = []
    path = '_chat.txt'

    with open(path, encoding="utf-8") as file:
        # Ignore first line of the conversation ("...Messages to this group are now secured with end-to-end encryption.")
        file.readline()

        # For multi-line messages
        buffer = ""
        date, time, author = None, None, None
        
        while True:
            line = file.readline()
            
            # EOF reached
            if not line:
                break
            
            # Remove random leading and trailing whitespaces
            line = line.strip()

            # New message
            if isDateTime(line):
                # If buffer has data from previous iteration, append
                if len(buffer) > 0:
                    processedData.append([date, time, author, buffer])

                # Clear the buffer
                buffer = ""

                date, time, author, message = parseData(line)
                if message:
                    buffer += message
            else:
                # At this point, if its not date time, its part of a multi-line message, so append to message buffer
                buffer += line

        processedData.append([date, time, author, buffer])    
    
    dataframe = pd.DataFrame(processedData, columns=['Date', 'Time', 'Author', 'Message'])
    return dataframe
    
    


if __name__ == "__main__":
    main()