import textstat  # https://pypi.org/project/textstat/

text=("This report will describe current issues facing light pollution and potential solutions"
 "dealing with the UN sustainable goal that “ensures access to affordable, reliable, sustainable"
 "and modern energy for all” [18]. The potential solutions will not only describe the cutting-edge"
 "technology that Electrip Inc. provides but will also include other solutions that can also improve"
 "the electricity consumption through light usage. The document will provide research that will help"
 "convince the user to save electricity by describing the feasibility of doing so. The report will"
 "cover the human involvement and environmental (human health, conditions, corporate and personal"
 "financial significance, atmospheric impact, ecosystems, migration pattern, wildlife life cycles)"
 "involvement in light pollution and excessive consumption. Furthermore, other topics such as simple"
 "solutions that can be achieved form personal initiative (Psychological techniques and energy"
 "efficient light investments), along side smart technology that Electrip Inc. has to offer."
 "Additionally, the mechanism will be described in terms of logistics and technology involved"
 "(Sensor/actuator interface with AI). The scope of the report will mainly cover the need for"
 "Electrip Inc. the personal/home environment as well as workspaces and technicality of the"
 "sensor/actuator interface and how the AI will interact with the currently integrated technology"
 "present in current spaces. It will explore ultra wideband wireless connection, frequency and"
 "concepts of data domains utilized by the AI. The document will not cover the installation"
 "processes and the specific costs for technology integration as technology integration methodology"
 "will vary across different environments due to infrastructure of the building’s circuitry.")

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