# text_data_crawling
# DATA.STAT.840 Statistical Methods for Text Data Analysis Exercises for Lecture 2: Basic text processing

This exercise we will process top-downloaded public domain ebooks from Project Gutenberg.
(a) Create a variant of the web crawler which is intended to download the top-k most
downloaded ebooks of the last 30 days from Project Gutenberg in .TXT format.
(b) Using the crawler, download the top-20 ebooks (k=20). Report the names and addresses of
the books.
(c) Use the processing pipeline described on the lecture to tokenize and lemmatize the
downloaded books.
(d) Create a unified vocabulary from the ebooks; report the top-100 words.

# The output for b question: The output for the top 20 ebookd with their names and addresses
1. Name:  呻吟語 by Kun Lü (259762)  Address:  /ebooks/25558  Id: 25558
2. Name:  Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley (107767)  Address:  /ebooks/84  Id: 84
3. Name:  A Christmas Carol in Prose; Being a Ghost Story of Christmas by Charles Dickens (93151)  Address:  /ebooks/46  Id: 46
4. Name:  Moby Dick; Or, The Whale by Herman Melville (72220)  Address:  /ebooks/2701  Id: 2701
5. Name:  Romeo and Juliet by William Shakespeare (67995)  Address:  /ebooks/1513  Id: 1513
6. Name:  歸蓮夢 by active 18th century Su'anzhuren (59082)  Address:  /ebooks/27104  Id: 27104
7. Name:  二刻拍案惊奇 by Mengchu Ling (53521)  Address:  /ebooks/24162  Id: 24162
8. Name:  The Complete Works of William Shakespeare by William Shakespeare (51713)  Address:  /ebooks/100  Id: 100
9. Name:  Middlemarch by George Eliot (50930)  Address:  /ebooks/145  Id: 145
10. Name:  A Room with a View by E. M.  Forster (50091)  Address:  /ebooks/2641  Id: 2641
11. Name:  Little Women; Or, Meg, Jo, Beth, and Amy by Louisa May Alcott (48100)  Address:  /ebooks/37106  Id: 37106
12. Name:  The Blue Castle: a novel by L. M.  Montgomery (43981)  Address:  /ebooks/67979  Id: 67979
13. Name:  Alice's Adventures in Wonderland by Lewis Carroll (43939)  Address:  /ebooks/11  Id: 11
14. Name:  The Enchanted April by Elizabeth Von Arnim (43526)  Address:  /ebooks/16389  Id: 16389
15. Name:  Pride and Prejudice by Jane Austen (41640)  Address:  /ebooks/1342  Id: 1342
16. Name:  The Adventures of Ferdinand Count Fathom — Complete by T.  Smollett (40696)  Address:  /ebooks/6761  Id: 6761
17. Name:  Cranford by Elizabeth Cleghorn Gaskell (40460)  Address:  /ebooks/394  Id: 394
18. Name:  The Expedition of Humphry Clinker by T.  Smollett (39988)  Address:  /ebooks/2160  Id: 2160
19. Name:  History of Tom Jones, a Foundling by Henry Fielding (39585)  Address:  /ebooks/6593  Id: 6593
20. Name:  The Adventures of Roderick Random by T.  Smollett (39581)  Address:  /ebooks/4085  Id: 4085
Tokenizing all books... 
Lemmanizing all books... 
Getting vocab... 
d. unify the vocabularies with top-100 words
['!' '#' '$' '%' '&' "'" "''" "'76" "'_dolce" "'_ein" "'_go_" "'_hail"
 "'_parley" "'_route" "'advice" "'after" "'ah" "'aisy" "'alas" "'all"
 "'altered" "'amy" "'an" "'an't" "'and" "'are" "'ariadne" "'as" "'at"
 "'authors" "'ay" "'aye" "'bacheldore" "'be" "'begging" "'behold" "'being"
 "'birds" "'blarneystone" "'bless" "'blessed" "'bosen" "'bosom" "'brother"
 "'bundle" "'bus" "'but" "'by" "'cabbages" "'calf-skin" "'call" "'calm"
 "'captain" "'catch" "'change" "'charge" "'charmingly" "'chowder"
 "'christopher" "'clinker" "'codicils" "'cold" "'come" "'compose"
 "'concerning" "'constant" "'could" "'cousin" "'cutlasses" "'d" "'damn"
 "'das" "'dawdle" "'dead" "'dear" "'degenerate" "'delectable" "'dem"
 "'demi" "'did" "'die" "'dis" "'dite" "'dorothy" "'dunghill" "'effalunt"
 "'either" "'em" "'en" "'envy" "'especially" "'exert" "'father" "'femme"
 "'fess" "'fessor" "'finish" "'fire" "'first" "'flowers"]
