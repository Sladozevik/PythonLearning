def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    words = s.split()
    word_string_count = []
    for word in words:
    	if word in s:
    		count = words.count(word)
    		word_string_count.append((word, count))
    	else:
    		word_string_count.append((word, 0))

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    word_string_count = list(set(word_string_count))
    
    # sort=sorted(zip_l.iteritems(),key=lambda(k,v):(-v,k)) -removed due below is better

    word_string_count.sort(key=lambda tup: (-tup[1], tup[0]))

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return word_string_count[:n]

def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
