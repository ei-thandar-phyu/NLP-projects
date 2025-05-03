# Spelling Correction for Myanmar Text Using SymSpell

This project explores the use of [SymSpell](https://github.com/wolfgarbe/SymSpell) algorithm for correcting spelling errors in Myanmar text. It is inspired by the paper titled [SymSpell4Burmese](https://ieeexplore.ieee.org/document/9678171), which applies the Symmetric Delete Spelling Correction technique to the Myanmar language.

We conducted testing on a small set of manually selected sentences containing common spelling errors. The system successfully corrected various typographical errors such as ဟုတိ, ဘူူး, and ဒီေနြ. It also handled some phonetic errors (e.g., correcting ပတ်သတ်), though corrections that require contextual understanding remain challenging. Additionally, the system struggles with informal or non-standard language often found on social media, including slang and abbreviations.

For improved results, consider using context-aware neural models such as BERT-based spell checkers, Seq2Seq models, or Transformer-based approaches that better capture semantics and context in Myanmar text.

## Features

- Spell correction for Myanmar sentences using SymSpell
- Unigram and bigram dictionary support
- Customizable edit distance
- Script for building frequency dictionaries from raw text
- Jupyter Notebook demo included


## Install dependencies:

```
pip install symspellpy
```

## Data Preparation

- Dataset used in this project will be uploaded soon at the following link:

🔗https://github.com/ye-kyaw-thu/mySpell

- Preprocessing includes:
	- Removing extra spaces, punctuation, and emojis.
	- Word segmentation using myWord: Syllable, Word and Phrase Segmenter for Burmese.

## Frequency Dictionary Creation

Use [build_dict.py](https://github.com/ei-thandar-phyu/NLP-projects/blob/main/myanmar-spellcheck-symspell/build_dict.py) to generate unigram and bigram frequency dictionaries.

### Unigram Dictionary

You can optionally include a pre-existing Myanmar dictionary file such as [myG2p](https://github.com/ye-kyaw-thu/myG2P/blob/master/ver2/myg2p.ver2.0.txt).

```
# Without dictionary file
python build_dict.py -i corpus.txt -o unigram_dict.txt -t unigram

# With dictionary file
python build_dict.py -i corpus.txt -o unigram_dict.txt -t unigram -d myg2p.ver2.0.txt
```

### Bigram Dictionary

```
python build_dict.py -i corpus.txt -o bigram_dict.txt -t bigram
```

### Sample Output
Unigram Dictionary
```
မြန်မာ 2446
သူငယ်ချင်း 647
စကြဝဠာ 57
```

Bigram Dictionary
```
မြန်မာ နိုင်ငံ 671
ရှိ ဘူး 495
လူငယ် တွေ 144
```

### Running Spell Correction

- Open the jupyter notebook: [MMSpellCorrect_SymSpell.ipynb](https://github.com/ei-thandar-phyu/NLP-projects/blob/main/myanmar-spellcheck-symspell/MMSpellCorrect_SymSpell.ipynb)
- Load the generated frequency dictionaries
- Perform correction using SymSpellMyanmar 
- View corrected output

# References

1. Mon, E.P.P., et al., SymSpell4Burmese: Symmetric Delete Spelling Correction Algorithm (SymSpell) for Burmese Spelling Checking, in 2021 16th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP). 2021. p. 1-6. DOI: 10.1109/iSAI-NLP54397.2021.9678171.

2. Myanmar Language (Burmese) Grapheme to Phoneme (myG2P) Conversion Dictionary, Version.2.0, Feb 15, 2021: https://github.com/ye-kyaw-thu/myG2P/blob/master/ver2/myg2p.ver2.0.txt

3. myWord: Syllable, Word and Phrase Segmenter for Burmese, Ye Kyaw Thu, Sept 2021, GitHub Link: https://github.com/ye-kyaw-thu/myWord
