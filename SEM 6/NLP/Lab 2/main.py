import nltk
from nltk.corpus import gutenberg, reuters, webtext, genesis, brown
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from collections import Counter

# Download required NLTK data
nltk.download('punkt_tab')
nltk.download('gutenberg')
nltk.download('reuters')
nltk.download('webtext')
nltk.download('genesis')
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def print_corpus_stats():
    # Gutenberg corpus
    print("\nGutenberg Corpus Statistics:")
    for file_id in gutenberg.fileids():
        print(f"File: {file_id}")
        print(f"Num of words: {len(gutenberg.words(file_id))}")
        print(f"Num of sentences: {len(gutenberg.sents(file_id))}")
        print("-" * 50)
    
    # Reuters corpus
    print("\nReuters Corpus Statistics:")
    print(f"Total files: {len(reuters.fileids())}")
    print(f"Categories: {reuters.categories()}")
    
    # Webtext corpus
    print("\nWebtext Corpus Statistics:")
    for file_id in webtext.fileids():
        print(f"File: {file_id}")
        print(f"Num of words: {len(webtext.words(file_id))}")
        print("-" * 50)
    
    # Genesis corpus
    print("\nGenesis Corpus Statistics:")
    for file_id in genesis.fileids():
        print(f"File: {file_id}")
        print(f"Num of words: {len(genesis.words(file_id))}")
        print("-" * 50)
    
    # Brown corpus
    print("\nBrown Corpus Statistics:")
    print(f"Total categories: {len(brown.categories())}")
    print(f"Categories: {brown.categories()}")
    print(f"Tagged: {'tagged' in dir(brown)}")

def process_text(text):
    # Word tokenization
    words = word_tokenize(text)
    print(f"\nNumber of words: {len(words)}")
    
    # Sentence tokenization
    sentences = sent_tokenize(text)
    print(f"Number of sentences: {len(sentences)}")
    
    # File size before removing stop words
    original_size = len(words)
    print(f"File size (in words) before removing stop words: {original_size}")
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words_no_stop = [word.lower() for word in words 
                     if word.lower() not in stop_words 
                     and word not in string.punctuation]
    
    # File size after removing stop words
    processed_size = len(words_no_stop)
    print(f"File size (in words) after removing stop words: {processed_size}")
    
    # Count unique words
    unique_words = set(words_no_stop)
    print(f"Number of unique words: {len(unique_words)}")
    
    # POS Tagging
    pos_tags = nltk.pos_tag(words)
    print("\nPOS Tagging (first 10 words):")
    print(pos_tags[:10])
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words_no_stop]
    print("\nStemming (first 10 words):")
    print(list(zip(words_no_stop[:10], stemmed_words[:10])))

def main():
    # Print corpus statistics
    print_corpus_stats()
    
    # Process a sample text from Gutenberg corpus
    print("\nProcessing sample text from Gutenberg corpus:")
    sample_text = gutenberg.raw('shakespeare-hamlet.txt')
    process_text(sample_text)

if __name__ == "__main__":
    main()