# Importing the random method to select random words for the poem generation
import random


def generate_poem(filepath):
    # List of common words that will be used to randomly replace words in the poem
    word_list = [
        "Sun", "so", "bright", "shining", "high", "In", "the", "vast", "and", "endless", "sky", "I'm",
        "looking", "for", "a", "rhyme", "and", "I'm", "running", "out", "of", "time", "Birds", "in",
        "flight", "above", "the", "trees", "Carried", "by", "the", "gentle", "breeze", "This", "poem",
        "makes", "some", "sense", "in", "past", "or", "present", "tense", "poem", "rhyme", "time", "try",
        "die", "cry", "dry", "goodbye", "deny", "butterfly", "bonsai", "crime", "climb", "sublime", "dime",
        "stories", "please", "fence", "commence", "offense", "intense", "defence",
        "suspense", "expense", "lie", "sky", "high", "buy", "fly", "guy", "spy", "tie", "shy", "pie", "thigh",
        "why", "try", "guy", "sly", "ply", "tense", "dense", "sense", "expense", "immense", "intense", "fence",
        "commence", "offense", "suspense", "defense", "recompense", "dispense", "preference", "inference"
    ]

    # Defining a template for the poem structure (8 verses, rhyming scheme)
    poem_structure = [
        "Sun so bright shining high,",
        "In the vast and endless sky,",
        "I'm looking for a rhyme,",
        "And I'm running out of time,",
        "Birds in flight, above the trees,",
        "Carried by the gentle breeze",
        "This poem makes some sense,",
        "In past or present tense"

    ]

    # Write the poem to the specified file in write (w) mode
    with open(filepath, 'w') as poem_file:
        for line in poem_structure:
            # Split each line into words and randomly replace some words
            words_in_line = line.split()
            for i in range(len(words_in_line)):
                if random.random() < 0.2:  # Replace 20% of the words
                    random_word = random.choice(word_list)
                    words_in_line[i] = random_word

            # Reconstruct the modified line and write it to the file
            modified_line = ' '.join(words_in_line)
            poem_file.write(modified_line + "\n")


# Call the function with the file path
generate_poem("poem.txt")
