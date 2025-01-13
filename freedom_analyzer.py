# File name: freedom_analyzer.py
# This program calculates the relative frequency of freedom-related words/terms in books
# Author: Valerio Smit
# Date: 5-1-2025

# List of freedom-related keywords
freedom_keywords = [
    'liberty', 'freedom', 'independence', 'autonomy', 'oppression', 'justice'
]

# Clean and tokenize text
def preprocess_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # Convert text to lowercase
    text = text.lower()
    
    # Remove non-alphabetic characters (retain spaces and letters only)
    clean_text = ""
    for char in text:
        if char.isalpha() or char.isspace():
            clean_text += char
    
    # Split into words
    words = clean_text.split()
    return words

# Count total relative frequency of all keywords combined (per 1000 words)
def count_total_relative_frequency(words, keywords):
    total_words = len(words)
    total_keyword_count = 0

    # Count occurrences of keywords manually
    for word in words:
        if word in keywords:
            total_keyword_count += 1
    
    # Calculate relative frequency per 1000 words
    relative_frequency = (total_keyword_count / total_words) * 1000
    return relative_frequency

# Preprocess and analyze both books
kim_words = preprocess_text('kim.txt')
trial_words = preprocess_text('the_trial.txt')

kim_relative_frequency = count_total_relative_frequency(kim_words, freedom_keywords)
trial_relative_frequency = count_total_relative_frequency(trial_words, freedom_keywords)

# Print results
print(f"Total relative frequency of freedom-related terms in 'Kim' (pre-war book) (per 1000 words): {kim_relative_frequency:.2f}")
print(f"Total relative frequency of freedom-related terms in 'The Trial' (post-war book) (per 1000 words): {trial_relative_frequency:.2f}")
