

## Discussion

# Data Analysis

    - Sentence Segmentation
        - the higher the ratings the shorter  the sentences
         (average)
         Average
            30.490909090909092
            Average
            25.916666666666668
            Average
            23.953488372093023
            Average
            25.08695652173913
            Average
            24.333333333333332

    - Tokenization and Stemming
        '''
        Most common tokens:  
        [('food', 4342), ('place', 4201), ('good', 3946), ('great', 3120), ('service', 2974), ('like', 2805), ('get', 2701), ('time', 2558), ('one', 2549), ('would', 2524), ('back', 2395), ('go', 2091), ('really', 1920), ('also', 1667), ("'ve", 1612), ('got', 1531), ('us', 1481), ('even', 1424), ('``', 1405), ('could', 1396)]
        Most common stems:  
        [('place', 4797), ('food', 4416), ('good', 4009), ('get', 3309), ('time', 3281), ('like', 3166), ('servic', 3138), ('great', 3121), ('go', 2996), ('order', 2979), ('one', 2666), ('would', 2524), ('back', 2409), ('tri', 2029), ('realli', 1920), ('come', 1915), ('love', 1714), ('also', 1667), ("'ve", 1612), ('even', 1551)]
        '''
        - the number of of unique tokens with steming is lower than the ones without stemming 
        - Porter's stemming very aggressive e.g . ('servic', 3138),

        e.g. 
        ('food', 4342) - without stemming
        ('food', 4416) -  with stemming)
        
        - figures


    - POS Tagging
        -
        '''
        The bubble tea was excellent! The service however, was not. I found it pushy, rushed, abrasive, and incredibly rude. Their way of dealing with English speaking customers is to bark at them until they leave with their order. 
        You certainly won't be receiving any of my money ever again.
        parts of speech: [('The', 'DT'), ('bubble', 'JJ'), ('tea', 'NN'), ('was', 'VBD'), ('excellent', 'JJ'), ('!', '.'), ('The', 'DT'), ('service', 'NN'), ('however', 'RB'), (',', ','), ('was', 'VBD'), ('not', 'RB'), ('.', '.'), ('I', 'PRP'), ('found', 'VBD'), ('it', 'PRP'), ('pushy', 'VBZ'), (',', ','), ('rushed', 'VBD'), (',', ','), ('abrasive', 'JJ'), (',', ','), ('and', 'CC'), ('incredibly', 'RB'), ('rude', 'VB'), ('.', '.'), ('Their', 'PRP$'), ('way', 'NN'), ('of', 'IN'), ('dealing', 'VBG'), ('with', 'IN'), ('English', 'NNP'), ('speaking', 'VBG'), ('customers', 'NNS'), ('is', 'VBZ'), ('to', 'TO'), ('bark', 'VB'), ('at', 'IN'), ('them', 'PRP'), ('until', 'IN'), ('they', 'PRP'), ('leave', 'VBP'), ('with', 'IN'), ('their', 'PRP$'), ('order', 'NN'), ('.', '.'), ('You', 'PRP'), ('certainly', 'RB'), ('wo', 'MD'), ("n't", 'RB'), ('be', 'VB'), ('receiving', 'VBG'), ('any', 'DT'), ('of', 'IN'), ('my', 'PRP$'), ('money', 'NN'), ('ever', 'RB'), ('again', 'RB'), ('.', '.')]

        
        I love the sketch comedy nights! Food is not so great. Drinks are average prices. Good venue.
        parts of speech: [('I', 'PRP'), ('love', 'VBP'), ('the', 'DT'), ('sketch', 'NN'), ('comedy', 'NN'), ('nights', 'NNS'), ('!', '.'), ('Food', 'NNP'), ('is', 'VBZ'), ('not', 'RB'), ('so', 'RB'), ('great', 'JJ'), ('.', '.'), ('Drinks', 'NNS'), ('are', 'VBP'), ('average', 'JJ'), ('prices', 'NNS'), ('.', '.'), ('Good', 'JJ'), ('venue', 'NN'), ('.', '.')]


        I used to love Jukebox but after today's meal, all I can say is "it was nice while it lasted".

        That was the dryest, most flavorless burger I've ever had. The cook didn't even bother getting the patty all on the bun, but just slapped everything together in a sloppy, careless mess.

        The fries were way overcooked (it used to come with curly but those are now an extra $$).

        The bun was plain, untoasted and there was no tomato (there was supposed to be).

        $18 for overpriced cardboard.


        parts of speech: [('I', 'PRP'), ('used', 'VBD'), ('to', 'TO'), ('love', 'VB'), ('Jukebox', 'NNP'), ('but', 'CC'), ('after', 'IN'), ('today', 'NN'), ("'s", 'POS'), ('meal', 'NN'), (',', ','), ('all', 'DT'), ('I', 'PRP'), ('can', 'MD'), ('say', 'VB'), ('is', 'VBZ'), ('``', '``'), ('it', 'PRP'), ('was', 'VBD'), ('nice', 'RB'), ('while', 'IN'), ('it', 'PRP'), ('lasted', 'VBD'), ("''", "''"), ('.', '.'), ('That', 'DT'), ('was', 'VBD'), ('the', 'DT'), ('dryest', 'JJS'), (',', ','), ('most', 'JJS'), ('flavorless', 'JJ'), ('burger', 'NN'), ('I', 'PRP'), ("'ve", 'VBP'), ('ever', 'RB'), ('had', 'VBN'), ('.', '.'), ('The', 'DT'), ('cook', 'NN'), ('did', 'VBD'), ("n't", 'RB'), ('even', 'RB'), ('bother', 'VB'), ('getting', 'VBG'), ('the', 'DT'), ('patty', 'NN'), ('all', 'DT'), ('on', 'IN'), ('the', 'DT'), ('bun', 'NN'), (',', ','), ('but', 'CC'), ('just', 'RB'), ('slapped', 'VBD'), ('everything', 'NN'), ('together', 'RB'), ('in', 'IN'), ('a', 'DT'), ('sloppy', 'JJ'), (',', ','), ('careless', 'JJ'), ('mess', 'NN'), ('.', '.'), ('The', 'DT'), ('fries', 'NNS'), ('were', 'VBD'), ('way', 'NN'), ('overcooked', 'VBN'), ('(', '('), ('it', 'PRP'), ('used', 'VBD'), ('to', 'TO'), ('come', 'VB'), ('with', 'IN'), ('curly', 'JJ'), ('but', 'CC'), ('those', 'DT'), ('are', 'VBP'), ('now', 'RB'), ('an', 'DT'), ('extra', 'JJ'), ('$', '$'), ('$', '$'), (')', ')'), ('.', '.'), ('The', 'DT'), ('bun', 'NN'), ('was', 'VBD'), ('plain', 'RB'), (',', ','), ('untoasted', 'JJ'), ('and', 'CC'), ('there', 'EX'), ('was', 'VBD'), ('no', 'DT'), ('tomato', 'NN'), ('(', '('), ('there', 'EX'), ('was', 'VBD'), ('supposed', 'VBN'), ('to', 'TO'), ('be', 'VB'), (')', ')'), ('.', '.'), ('$', '$'), ('18', 'CD'), ('for', 'IN'), ('overpriced', 'VBN'), ('cardboard', 'NN'), ('.', '.')]
        
        
        This place is inside Baiz Supermarket.
        If you are in mood of middle eastern food, this is the place. They have the most popular dishes. I highly recommend this place!
        parts of speech: [('This', 'DT'), ('place', 'NN'), ('is', 'VBZ'), ('inside', 'JJ'), ('Baiz', 'NNP'), ('Supermarket', 'NNP'), ('.', '.'), ('If', 'IN'), ('you', 'PRP'), ('are', 'VBP'), ('in', 'IN'), ('mood', 'NN'), ('of', 'IN'), ('middle', 'JJ'), ('eastern', 'JJ'), ('food', 'NN'), (',', ','), ('this', 'DT'), ('is', 'VBZ'), ('the', 'DT'), ('place', 'NN'), ('.', '.'), ('They', 'PRP'), ('have', 'VBP'), ('the', 'DT'), ('most', 'RBS'), ('popular', 'JJ'), ('dishes', 'NNS'), ('.', '.'), ('I', 'PRP'), ('highly', 'RB'), ('recommend', 'VBP'), ('this', 'DT'), ('place', 'NN'), ('!', '.')]
        
        
        Scheduled manicure and pedicure one day. Came in, was seated and was told to wait. Waited for over 30 minutes, went back to the front desk, they said they forgot about me. I was nice about it, I guess that happenes (not at the good places, but still happens). At the end wasn't even offered a discount... pretty shitty move.
        parts of speech: [('Scheduled', 'VBN'), ('manicure', 'NN'), ('and', 'CC'), ('pedicure', 'NN'), ('one', 'CD'), ('day', 'NN'), ('.', '.'), ('Came', 'NN'), ('in', 'IN'), (',', ','), ('was', 'VBD'), ('seated', 'VBN'), ('and', 'CC'), ('was', 'VBD'), ('told', 'VBN'), ('to', 'TO'), ('wait', 'VB'), ('.', '.'), ('Waited', 'VBN'), ('for', 'IN'), ('over', 'IN'), ('30', 'CD'), ('minutes', 'NNS'), (',', ','), ('went', 'VBD'), ('back', 'RB'), ('to', 'TO'), ('the', 'DT'), ('front', 'NN'), ('desk', 'NN'), (',', ','), ('they', 'PRP'), ('said', 'VBD'), ('they', 'PRP'), ('forgot', 'VBD'), ('about', 'IN'), ('me', 'PRP'), ('.', '.'), ('I', 'PRP'), ('was', 'VBD'), ('nice', 'JJ'), ('about', 'IN'), ('it', 'PRP'), (',', ','), ('I', 'PRP'), ('guess', 'VBP'), ('that', 'IN'), ('happenes', 'NNS'), ('(', '('), ('not', 'RB'), ('at', 'IN'), ('the', 'DT'), ('good', 'JJ'), ('places', 'NNS'), (',', ','), ('but', 'CC'), ('still', 'RB'), ('happens', 'VBZ'), (')', ')'), ('.', '.'), ('At', 'IN'), ('the', 'DT'), ('end', 'NN'), ('was', 'VBD'), ("n't", 'RB'), ('even', 'RB'), ('offered', 'VBN'), ('a', 'DT'), ('discount', 'NN'), ('...', ':'), ('pretty', 'RB'), ('shitty', 'JJ'), ('move', 'NN'), ('.', '.')]
        '''
        - haven't found any mistakes  so far
        - may be interesting for more informmal comments (LoL, xD, :D)
        - very well written sample

    - Most Frequent Adjectivesfor each Rating
        -
        '''

            1.0 star(s) top 10 most used adjectives: [
            ['good' 'other' 'bad' 'first' 'new' 'last' 'horrible' 'few' 'same' 'next']
            2.0 star(s) top 10 most used adjectives: 
            ['good' 'other' 'great' 'bad' 'nice' 'first' 'much' 'little' 'few' 'small']
            3.0 star(s) top 10 most used adjectives: 
            ['good' 'other' 'great' 'nice' 'little' 'small' 'bad' 'few' 'decent' 'hot']
            4.0 star(s) top 10 most used adjectives:
            ['good' 'great' 'nice' 'other' 'little' 'delicious' 'fresh' 'friendly', 'small' 'first']
            5.0 star(s) top 10 most used adjectives: ['great' 'good' 'friendly' 'delicious' 'nice' 'other' 'amazing' 'fresh'
            'first' 'new']

            1.0 star(s) top 10 most indicative adjectives: 
            ['horrible' 'terrible' 'bad' 'rude' 'poor' 'awful' 'last' 'unprofessional' 'same' 'wrong']
            2.0 star(s) top 10 most indicative adjectives: 
            ['bad' 'same' 'dry' 'other' 'second' 'decent' 'chinese' 'slow' 'empty' 'ok']
            3.0 star(s) top 10 most indicative adjectives: 
            ['good' 'decent' 'other' 'small' 'ok' 'little' 'average' 'bad' 'large' 'fine']
            4.0 star(s) top 10 most indicative adjectives: 
            ['good' 'little' 'delicious' 'nice' 'tasty' 'small' 'fresh' 'great' 'busy' 'large']
            5.0 star(s) top 10 most indicative adjectives: 
            ['great' 'delicious' 'happy' 'friendly' 'wonderful' 'excellent' 'professional' 'helpful' 'fantastic' 'awesome']
        '''

        - results for the indicative adjectives are more descriptive for a rating system where 1 stars are the worst rating.
        - ia gives more weight to specific words (terrible, horrible, unprofessional) which appear only in their specific rating
        - counting adjectives only is less descriptive since it also counts observations like ('not good')
    
    - Noun Adjective Pair Summarizer
        -
        '''
        Results oLb3-eXUFtCFJl2DuBhcvA
        [(('front', 'desk'), 20), (('free', 'wifi'), 5), (('clean', 'room'), 5), (('next', 'day'), 5), (('next', 'door'), 4), (('light', 'sleeper'), 4), (('clean', 'rooms'), 4), (('rental', 'car'), 3), (('friendly', 'staff'), 3), (('comfortable', 'bed'), 3), (('great', 'breakfast'), 3), (('hot', 'food'), 3), (('free', 'breakfast'), 3), (('continental', 'breakfast'), 3), (('new', 'room'), 3), (('next', 'morning'), 3), (('complimentary', 'breakfast'), 3), (('free', 'shuttle'), 3), (('first', 'night'), 3), (('first', 'day'), 2)]



        Results S6apFS5ghsQg69rcBvm2Qg
        [(('cole', 'slaw'), 5), (('hot', 'peppers'), 4), (('good', 'sandwich'), 4), (('good', 'sub'), 3), (('russian', 'dressing'), 3), (('favorite', 'sub'), 3), (('delicious', 'sandwich'), 3), (('quick', 'meal'), 3), (('cranberry', 'sauce'), 3), (('next', 'time'), 3), (('first', 'time'), 3), (('vegetarian', 'options'), 3), (('fresh', 'bread'), 2), (('other', 'sandwiches'), 2), (('other', 'place'), 2), (('best', 'subs'), 2), (('new', 'favorite'), 2), (('soft', 'meat'), 2), (('ok', '-pron-'), 2), (('stuffing', 'sauce'), 2)]



        Results xvjkhS2PXajDniDzP1-hdA
        [(('last', 'week'), 5), (('happy', '-pron-'), 5), (('worse', 'condition'), 4), (('friendly', 'staff'), 4), (('able', '-pron-'), 3), (('fine', '-pron-'), 3), (('last', 'time'), 3), (('next', 'morning'), 3), (('nice', '-pron-'), 3), (('clean', 'facility'), 3), (('few', 'minutes'), 3), (('human', 'being'), 2), (('first', 'time'), 2), (('little', 'pricey'), 2), (('allergic', 'reaction'), 2), (('nice', 'staff'), 2), (('lone', 'hospital'), 2), (('grateful', '-pron-'), 2), (('such', 'as'), 2), (('printed', 'paper'), 2)]



        Results RyaCGkXRXxXNeJhbnioz1Q
        [(('white', 'chocolate'), 6), (('white', 'mocha'), 5), (('busy', '-pron-'), 4), (('long', 'line'), 4), (('friendly', 'staff'), 4), (('hot', 'chocolate'), 4), (('right', '-pron-'), 3), (('bad', 'service'), 2), (('other', 'locations'), 2), (('great', 'coffee'), 2), (('fast', '-pron-'), 2), (('nice', 'employees'), 2), (('slow', '-pron-'), 2), (('quick', 'service'), 2), (('classic', 'syrup'), 2), (('perfect', 'order'), 2), (('other', 'starbucks'), 2), (('great', 'tea'), 2), (('white', 'defense'), 2), (('helpful', 'lynette'), 2)]



        Results c0t81YxNqZQuTJrTfn3QYA
        [(('new', 'tires'), 12), (('great', 'service'), 9), (('free', 'for'), 5), (('loyal', 'customer'), 5), (('able', '-pron-'), 4), (('new', 'tire'), 4), (('many', 'years'), 3), (('new', 'one'), 3), (('friendly', '-pron-'), 3), (('last', 'week'), 3), (('third', 'time'), 2), (('amazing', 'service'), 2), (('other', 'places'), 2), (('bad', '-pron-'), 2), (('sure', '-pron-'), 2), (('run', 'tire'), 2), (('flat', 'tire'), 2), (('best', 'experience'), 2), (('other', 'vehicle'), 2), (('multiple', 'times'), 2)]
        '''

        - identifying the facilities / what kind of business (hotel  -> rental car, complimentary breakfast, clean room -> yes)
        - identifying good and bad things ('quick', 'meal')
        - some of the pairs are not important for businesses


    - Application
        - since we got very descriptive results for the indicative adjectives, we can connect the Adjective Noun Summarizer with this. 
        - Restaurant owners and costumers can see the good and the bad things in the restuarants (e.g. ('bad', 'service'), ('best', 'burgers'))
        - with more data, the results are becoming more precise