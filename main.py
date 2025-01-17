def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	return len(text)
	
def count_sentences(text):
	text = text.replace ("!",".")
	text = text.replace ("?",".")
	sentences = text.split(".")
	return len(sentences)

def count_most_common_words(text):
	words = text.lower().split()
	total_words = len(words)
	word_counts = {}
	stop_words = {"the", "a", "and", "of", "to", "in", "i", "was", "that", "he", "you", "my"}

	for word in words:
		if word not in stop_words:
			if word in word_counts:
				word_counts[word] += 1
			else:
				word_counts[word] = 1

	word_frequencies = []
	for word,count in word_counts.items():
		percentage = (count/total_words)*100
		word_frequencies.append((word,count,percentage))

	return sorted(word_frequencies, key=lambda x: x[1], reverse=True)[:5]

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	word_count = count_words(file_contents)
	character_count = count_characters(file_contents)
	sentences_count = count_sentences(file_contents)
	average_word_length = round(character_count / word_count)
	average_word_per_sentences = round(word_count/sentences_count)
	most_common = count_most_common_words(file_contents)
	print("---Book Report---")
	print(f"Qty of Words {word_count}")
	print(f"Qty of Characters {character_count}")
	print(f"Qty of Sentences {sentences_count}")
	print(f"Average word length: {average_word_length} characters")
	print(f"Average words per sentence {average_word_per_sentences}")
	print("Most common words")
	for word, count, percentage in most_common:
		print(f"'{word}': {count} times ({percentage:.2f}% of text)")
		

main()
