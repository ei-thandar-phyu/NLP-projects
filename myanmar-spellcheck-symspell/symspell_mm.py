from symspellpy import SymSpell, Verbosity

class SymSpellMyanmar:
    def __init__(self, unigram_path, bigram_path, max_edit_distance=3, prefix_length=7):
        self.symspell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)
        self.unigram_path = unigram_path
        self.bigram_path = bigram_path
        self.max_edit_distance = max_edit_distance
        self._load_dictionaries()

    def _load_dictionaries(self):
        self.symspell.load_dictionary(self.unigram_path, term_index=0, count_index=1)
        self.symspell.load_bigram_dictionary(self.bigram_path, term_index=0, count_index=2)

    def correct(self, sentence):
        sentence = sentence.strip()
        suggestions = self.symspell.lookup_compound(sentence, max_edit_distance=self.max_edit_distance, split_by_space=True)
        return suggestions[0].term if suggestions else sentence

