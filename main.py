import textstat  # https://pypi.org/project/textstat/
import os
import glob       # using to read in many files
import docx2txt   # because I'm reading in word docs
# where is the folder with your content?
folderPath = 'C:\\Users\suhas\git\text-stat-example\folder'
# I want to search in all of the folders, so I set recursive=True
docs=[]
docs = glob.glob(folderPath + '/**/*.txt',recursive=True)
docs.extend(glob.glob(folderPath + '/**/*.docx',recursive=True))
#... keep adding whatever types you need
print(docs)
# the language is English by default so no need to set the language
# Loop through my docs
for doc in docs:
    if os.path.isfile(doc):
        text = docx2txt.process(os.path.join(folderPath,doc))
        
        print('Document:                     ' + doc)
        print('Flesch Reading Ease:          ' + str(textstat.flesch_reading_ease(text)))
        print('Smog Index:                   ' + str(textstat.smog_index(text)))
        print('Flesch Kincaid Grade:         ' + str(textstat.flesch_kincaid_grade(text)))
        print('Coleman Liau Index:           ' + str(textstat.coleman_liau_index(text)))
        print('Automated Readability Index:  ' + str(textstat.automated_readability_index(text)))
        print('Dale Chall Readability Score: ' + str(textstat.dale_chall_readability_score(text)))
        print('Difficult Words:              ' + str(textstat.difficult_words(text)))
        print('Linsear Write Formula:        ' + str(textstat.linsear_write_formula(text)))
        print('Gunning Fog:                  ' + str(textstat.gunning_fog(text)))
        print('Text Standard:                ' + str(textstat.text_standard(text)))
        print('*********************************************************************************')
"""Flesch-Kincaid Grade Level = This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document"""
"""Gunning Fog = This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document."""
"""SMOG - for 30 sentences or more  =This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document."""
"""Automated Readability Index = Returns the ARI (Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text."""
""" Coleman Liau Index = Returns the grade level of the text using the Coleman-Liau Formula."""
"""Linsear = Returns the grade level using the Linsear Write Formula."""
""" Dale Chall = Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."""