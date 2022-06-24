import textstat  # https://pypi.org/project/textstat/
import docx2txt

text = docx2txt.process("text.docx")

print(textstat.flesch_reading_ease(text))
print(textstat.flesch_kincaid_grade(text))
print('*********************************************************************************')

"""Flesch-Kincaid Grade Level = This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document"""
"""Gunning Fog = This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document."""
"""SMOG - for 30 sentences or more  =This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document."""
"""Automated Readability Index = Returns the ARI (Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text."""
""" Coleman Liau Index = Returns the grade level of the text using the Coleman-Liau Formula."""
"""Linsear = Returns the grade level using the Linsear Write Formula."""
""" Dale Chall = Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."""