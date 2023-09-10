import re, csv
# instantiate empty dictionary for the file we're parsing
dictionary = dict()
# open the unparsed version of the file
unparsed_file = open('./unparsed/kjv.txt', 'r')
# open and erase a file for the parsed version of the dataset
with open('./parsed/kjv.csv', 'w', newline='') as file:
    writer =  csv.writer(file)
    
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
                # print it for our benefit
                #print(word, ",", chapter_verse, ",", index)
                # write it to the target text file
                # encase the chapter/verse reference in quotes for easy parsing as a csv
                writer.writerow([word, chapter_verse, index])
# end of writing, parsed file will automatically close

# close the unparsed file
unparsed_file.close()