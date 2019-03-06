'''

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

'''
def minion_game(string):
    vCount=0
    cCount=0
    stringValue = string
    vowels =['A','E','I','O','U']
    for i in range(0,len(stringValue)):
        if stringValue[i] in vowels:
            vCount = vCount + (len(stringValue)-i)

        else:
            cCount = cCount + (len(stringValue)-i)

    if vCount > cCount:
        print('Kevin '+str(vCount))
    elif vCount < cCount:
        print('Stuart '+str(cCount))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
