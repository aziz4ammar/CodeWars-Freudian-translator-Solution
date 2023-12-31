def to_freud(sentence):
    words = sentence.split()
    translated_sentence = ' '.join(['sex' for _ in words])
    return translated_sentence