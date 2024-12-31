import os
import numpy as np
import nltk
import bs4
import requests

header_text = "*** START OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN; OR, THE MODERN PROMETHEUS ***"
footer_text = "*** END OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN; OR, THE MODERN PROMETHEUS ***"

def download_deps(packages_list):
    print("Checking for dependencies... ")
    
    for pack in packages_list:
        try:
            # Downloading each package quietly (no output to the console)
            nltk.download(pack, quiet=True)
            print(f"Downloaded '{pack}' successfully.")
        except Exception as e:
            print(f"Failed to download '{pack}': {str(e)}")
    
    print("Check complete.")
    
    
# Convert a POS tag for WordNet
def tagtowordnet(postag):
     wordnettag=-1
     if postag[0]=='N':
         wordnettag='n'
     elif postag[0]=='V':
         wordnettag='v'
     elif postag[0]=='J':
         wordnettag='a'
     elif postag[0]=='R':
         wordnettag='r'
     return(wordnettag)
 
    
# Unify the vocabularies.
def unify_vocab(vocabs, quiet):
    if not quiet:
        print("unify the vocabularies")
# First concatenate all vocabularies
    tempvocabulary=[]
    for k in range(len(vocabs[0])):
        tempvocabulary.extend(vocabs[1][k])
    # Find the unique elements among all vocabularies
    uniqueresults=np.unique(tempvocabulary,return_inverse=True)
    unifiedvocabulary=uniqueresults[0]
    wordindices=uniqueresults[1]
    # Translate previous indices to the unified vocabulary.
    # Must keep track where each vocabulary started in
    # the concatenated one.
    vocabularystart=0
    myindices_in_unifiedvocabulary=[]
    for k in range(len(vocabs[0])):
     # In order to shift word indices, we must temporarily
     # change their data type to a Numpy array
         tempindices=np.array(vocabs[2][k])
         tempindices=tempindices+vocabularystart
         tempindices=wordindices[tempindices]
         myindices_in_unifiedvocabulary.append(tempindices)
         vocabularystart=vocabularystart+len(vocabs[1][k])
    return unifiedvocabulary, myindices_in_unifiedvocabulary

# Function to extract unique vocabularies and their indices from lemmatized text
def unique_vocabs(lemmatized_list, quiet):
    if not quiet:
        print("Getting vocab... ")

    vocab = []
    vocab_indices = []

    # For each document, find its unique vocabulary
    for k in range(len(lemmatized_list)):
        temp_text = lemmatized_list[k]  # Lemmatized text
        unique_results = np.unique(temp_text, return_inverse=True)
        unique_words = unique_results[0]  # Unique words in the document
        word_indices = unique_results[1]  # Indices of words in the original text

        vocab.append(unique_words)  # Store unique vocabulary
        vocab_indices.append(word_indices)  # Store word indices
    return [lemmatized_list, vocab, vocab_indices]

# Function to lemmatize tokens (reduce words to their base form)
def lemma_text(tokens, quiet):
    if not quiet:
        print("Lemmanizing all books... ")

    all_lemma_text = []

    for token_word in tokens:
        lemma_processor = nltk.stem.WordNetLemmatizer()  # WordNet lemmatizer
        tagged_text = nltk.pos_tag(token_word)  # POS tagging the text

        lemma_result = []
        for l in range(len(tagged_text)):
            word_to_lemma = tagged_text[l][0]  # Extract the word
            word_net_tag = tagtowordnet(tagged_text[l][1])  # Convert POS tag to WordNet tag

            # Lemmatize the word if a valid WordNet tag exists
            if word_net_tag != -1:
                lemma_word = lemma_processor.lemmatize(word_to_lemma, word_net_tag)
            else:
                lemma_word = word_to_lemma  # Use the original word if no tag is found

            lemma_result.append(lemma_word)  # Store the lemmatized word
        all_lemma_text.append(lemma_result)
    return all_lemma_text

# Function to tokenize book content into words
def tokenize(book_content_list, quiet):
    if not quiet:
        print("Tokenizing all books... ")

    mycrawled_nltktexts = []

    for k in range(len(book_content_list)):
        temp_nltktext = nltk.Text(nltk.word_tokenize(book_content_list[k].lower()))  # Tokenizing text to lowercase
        mycrawled_nltktexts.append(temp_nltktext)  # Store tokenized text
    return mycrawled_nltktexts

# Function to download book content from the Gutenberg site
def download_book_content(book_details, download, host_name, quiet):
    if not quiet:
        print("Downloading book ", book_details)

    download_directory = 'downloads'
    book_content = []

    # Create download directory if not present
    if download and not os.path.exists(download_directory):
        os.makedirs(download_directory)

    for book_detail in book_details:
        link = book_detail['link']
        title = book_detail['title']
        key = link.split('/')[-1]  # Extract book ID from URL

        print("Name: ", title, " Address: ", link, " Id:", key)
        r = requests.get(host_name + link + '.txt.utf-8')  # Download the book in UTF-8 format

        text = remove_start_and_end_labels(r)  # Remove the Gutenberg headers
        book_content.append(text)  # Store the cleaned book content

        if download:
            with open(os.path.join(download_directory, key + '.txt'), 'wb') as fd:
                fd.write(bytes(text, 'utf-8'))  # Save content to disk
    return book_content

# Function to remove Gutenberg-specific start and end labels from text
def remove_start_and_end_labels(r):
    text = r.text  # Get the raw text from the HTTP response
    header_index = text.find(header_text)  # Find start label
    footer_index = text.find(footer_text)  # Find end label
    return text[header_index + len(header_text):footer_index].strip()  # Return cleaned text

# Function to get book details (link and title) from Gutenberg's "Top Books" section
def get_book_details(path, max_books, quiet):
    if not quiet:
        print("Crawling for books at ", path)

    top_book_list = []
    pagetocrawl_html = requests.get(path)  # Request the webpage
    pagetocrawl_parsed = bs4.BeautifulSoup(pagetocrawl_html.content, 'html.parser')  # Parse the HTML

    # Find the top books from the last 30 days section
    top_books_last_30_days_li = pagetocrawl_parsed.find('h2', {'id': 'books-last30'}).find_next_sibling('ol').findAll('li')

    book_counter = 0
    for book_li in top_books_last_30_days_li:
        if book_counter >= max_books:
            break

        book_link = book_li.find('a')  # Find the book link
        top_book_list.append({'link': book_link['href'], 'title': book_link.text})  # Store book link and title

        book_counter += 1
    return top_book_list

# Main function to crawl, download, and process books from Project Gutenberg
def gutenberg_book_crawler(max_books=20, download_file=False, quiet=True):
    host_name = 'https://www.gutenberg.org'  # Base URL for Project Gutenberg
    books_home_path = '/browse/scores/top'  # Path to the "Top Books" section

    # Get book details (URLs and titles)
    book_details = get_book_details(host_name + books_home_path, max_books, quiet)
    # Download book content
    downloaded_content = download_book_content(book_details, download_file, host_name, quiet)
    # Tokenize the downloaded book content
    tokenized_words = tokenize(downloaded_content, quiet)
    # Lemmatize the tokenized words
    lemma_words = lemma_text(tokenized_words, quiet)
    # Get unique vocabularies and their indices for each book
    vocab_list = unique_vocabs(lemma_words, quiet)
    # Unify all vocabularies into one
    unified_vocab = unify_vocab(vocab_list, quiet)

    return unified_vocab  # Return the unified vocabulary


if __name__ == '__main__':
    download_deps(['punkt', 'wordnet', 'omw-1.4', 'punkt_tab', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng'])
    result = gutenberg_book_crawler(20, False, quiet=False)
    print(result[0][:100])
    