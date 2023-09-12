$(document).ready(function(){
    $("#entry-form").submit(function(e){
        e.preventDefault(); // this will prevent the submit
        // load the selected translation
        // let's just stick with mandatory KJV for now
        const dict = KJV_dict;
        // fetch the textarea's contents
        var contents = $("#entry-field").val();
        // split up words from any non-alphanumeric characters
        var word_arr = contents.split(/([^A-Za-z']+)/);
        // iterate over each word in the text block
        for (let word_idx in word_arr) {
            var word = word_arr[word_idx].toLowerCase();
            // check if the word is alphabetical characters
            if (/^[A-Za-z']+$/.test(word)) {
                // search word in dictionary
                if (dict[word] != undefined) {
                    // word found
                    // highlight green
                    word_arr[word_idx] = "<span class=\"tooltip highlight-found\">".concat(word_arr[word_idx]);
                    // isolate the reference of the verse
                    var tooltip_title = "<b>" + KJV_text[dict[word]].split("\t")[0] + "</b><hr>";
                    // isolate the text of the verse
                    var tooltip_text = KJV_text[dict[word]].split("\t")[1];
                    // split the text into words and non-words, so we can accurately highlight the target word, regardless of punctuation
                    // we're not using lookaheads/lookbehinds for things like parentheses or punctiation, because not all browsers support lookbehinds
                    // so instead we're doing this like cavemen
                    var split_text = tooltip_text.split(/([^A-Za-z']+)/);
                    // now iterate over all that shit until we find our target word
                    for (let tooltip_idx in split_text) {
                        if (split_text[tooltip_idx].toLowerCase() === word) {
                            // highlight word in reference tooltip 
                            split_text[tooltip_idx] = split_text[tooltip_idx].concat("</span>");
                            split_text[tooltip_idx] = "<span class=\"highlight-found\">".concat(split_text[tooltip_idx]);
                            // only need the first instance, break out of the loop
                            break;
                        }
                    }
                    // reassemble the verse text
                    tooltip_text = split_text.join("");
                    // now cram that all into a tooltip that's going to be shown as a hover-box over the target word
                    word_arr[word_idx] = word_arr[word_idx].concat("<span class=\"tooltiptext\">" + tooltip_title + tooltip_text +"</span></span>");
                } else {
                        // word not found
                        // highlight red
                        word_arr[word_idx] = word_arr[word_idx].concat("</span>");
                        word_arr[word_idx] = "<span class=\"highlight-notfound\">".concat(word_arr[word_idx]);
                }
            } else {
              word_arr[word_idx] = word.replace(/\n\r?/g, "<br/>");  
            }
        }
        // dump new, highlighted text to results box
        var output = word_arr.join("");
        $('#processed-block').html(output);         
    });
});

