import re, json
# instantiate empty dictionary for the file we're parsing
dictionary = dict()
# open the unparsed version of the file
unparsed_file = open('./unparsed/kjv.txt', 'r', encoding='utf-8-sig')

# extract lines from the unparsed file into memory
lines = unparsed_file.readlines()

# iterate over lines
for line in lines:
    # extract and store the chapter/verse reference
    chapter_verse = line.split('\t')[0]
    # remove the chapter/verse reference from the line
    text = line.split('\t')[1]
    # remove all special characters, force all letters to lowercase, split into an array of these processed words
    no_spc_text = re.sub(r"[^a-zA-Z0-9]+", ' ', text).lower().split()
    # iterate over each word in the array of processed words, storing the word's index in the line
    for index, word in enumerate(no_spc_text):
        # check if the word is already in the dictionary
        if word not in dictionary:
            # if not, add it to the dictionary as a key
            # it's value is an array that stores the chapter/verse reference, and the word's index in that verse's line
            dictionary.update({word:(chapter_verse, index)})
        # skip words already in dictionary
    # end of line, move to next line
# all lines complete, file parsing complete
# close the unparsed file
unparsed_file.close()

# open the parsed file, erasing all previous contents
with open('./parsed/kjv.json', 'w') as outfile:
    # dump contents of dictionary to file
    json.dump(dictionary, outfile, ensure_ascii=False)
# file will automatically close
# complete