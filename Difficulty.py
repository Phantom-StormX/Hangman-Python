import random
import Welcome
import sys

easy_words = ['earth','hello','apple','chicken','space','fire','wood','water','hair','duck']
medium_words = ['ally','complex','cornucopia','pumpkin','python','believe','holster','available','nugget','fish']
hard_words = ['erudite','incomprehensibility','foe','oak','zinc','humpback','wolfhound','doubtfully','xenon','hiking']
SUPERHARD_WORDS = ['pneumonoultramicroscopicsilicovolcanoconiosis','supercalifragilisticexpialidocious','hippopotamophobia','xenotransplantation','sly','rutabaga','dinosaur','oleszewski','TV']

easy = random.sample(easy_words, 1)[0]
medium = random.sample(medium_words, 1)[0]
hard = random.sample(hard_words, 1)[0]
super_hard = random.sample(SUPERHARD_WORDS, 1)[0]



