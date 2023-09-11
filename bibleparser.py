import re, json
# instantiate empty dictionary for the file we're parsing
dictionary = dict()
#
# open the unparsed version of the file
unparsed_file = open('./unparsed/kjv.txt', 'r', encoding='utf-8-sig')

# extract lines from the unparsed file into memory
lines = unparsed_file.readlines()

# iterate over lines
for line_idx, line in enumerate(lines):
    # remove the chapter/verse reference from the line
    text = line.split('\t')[1]
    # remove all special characters, force all letters to lowercase, split into an array of these processed words
    no_spc_text = re.sub(r"('[sS])|[^a-zA-Z]+", ' ', text).lower().split()
    # iterate over each word in the array of processed words, storing the word's first found verse
    for word_idx, word in enumerate(no_spc_text):
        # check if the word is already in the dictionary
        if word not in dictionary:
            # if not, add it to the dictionary as a key
            # it's value is an array that stores the chapter/verse reference
            dictionary.update({word:line_idx})
        # skip words already in dictionary
    # end of line, move to next line
# all lines complete, file parsing complete
# close the unparsed file
unparsed_file.close()

# open the parsed file, erasing all previous contents
with open('./parsed/kjv.js', 'w') as outfile:
    # dump contents of dictionary to file
    outfile.write("var KJV_dict = ")
    json.dump(dictionary, outfile, ensure_ascii=False)
    outfile.write (";\n var KJV_text = ")
    json.dump(lines, outfile)

# file will automatically close
# complete