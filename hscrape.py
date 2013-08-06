# This is the beginning of the end.
import json
from operator import itemgetter

# Now actually scraping the content...for a specific string
def phraseCount(convo):
    strCounter = 0
    wantNext = False # Generally want line right after since I add the enter key a ton..

    for chat in convo:
        chat_meat = chat["chat_message"]["message_content"]
        if ("segment" in chat_meat):
            chat_meat = chat_meat["segment"]
            for c in chat_meat:
                if (c["type"] == "TEXT"):
                    # Making the string purty
                    chatText = (c["text"]).encode('utf-8').strip()
                    if (stringOfChoice in str.lower(chatText)):
                        wantNext = True
                        strCounter += 1
                        print chatText
                    elif (wantNext):
                        wantNext = False
                        print chatText
    return strCounter

# count ALL the words!
def wordCount(convo, minWordLen, topBlah):
    totWord = 0
    wordCountArray = {}

    for chat in convo:
        chat_meat = chat["chat_message"]["message_content"]
        if ("segment" in chat_meat):
            chat_meat = chat_meat["segment"]
            for c in chat_meat:
                if (c["type"] == "TEXT"):
                    # Making the string purty
                    chatText = (c["text"]).encode('utf-8').strip()

                    # Need to go word by word...
                    for word in chatText.split(' '):
                        totWord += 1
                        word = word.lower()
                        if (word in wordCountArray):
                            wordCountArray[word] += 1
                        else:
                            # doesn't exist, sadface ):
                            wordCountArray[word] = 1
                            # so add it! :D
    print totWord

    # Ideally want to sort this monstrosity..
    newArray = sorted(wordCountArray.items(), key=itemgetter(1), reverse=True)

    topBlah = 10
    for w in newArray:
        if (topBlah > 0 and len(w[0]) >= minWordLen):
            print w
            # print wordCountArray[w]
            # print w + ': ' + str(wordCountArray[w])
            topBlah -= 1

    # print wordCountArray


# beginning of other silly things
filename = "Hangouts.json"
name = str.lower("David Diciurcio")
stringOfChoice = str.lower("is it bad")

# Starting to compute variables
fileObj = json.loads(open(filename).read())

counter = 1
convo = None

for metadata in fileObj:
    if (metadata == 'conversation_state'):
        for convo in fileObj[metadata]:
            convodata = convo["conversation_state"]
            participants = convodata["conversation"]["participant_data"]
            fallbackNameSet = False
            for p in participants:
                if ("fallback_name" in p and str.lower(str(p["fallback_name"])) == name):
                    # Cool beans, finally found the convo with person X
                    fallbackNameSet = True
                    break
            if (fallbackNameSet):
                print p["fallback_name"]
                convo = convodata["event"]
                break
            counter += 1


print 'length of convo you are scraping: ' + str(len(convo))

print '-----results!------'
# strCounter = phraseCount(convo)
# print strCounter
# print str((strCounter/float((len(convo)))) * 100) + '%'

wordCount(convo, 16, 10)


