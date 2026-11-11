import random

easy_words = ['earth','hello','apple','chicken','space','fire','wood','water','hair','duck']
medium_words = ['ally','complex','cornucopia','pumpkin','python','believe','holster','available','nugget','fish']
hard_words = ['erudite','incomprehensibility','foe','oak','zinc','humpback','wolfhound','doubtfully','xenon','hiking']
SUPERHARD_WORDS = ['pneumonoultramicroscopicsilicovolcanoconiosis','supercalifragilisticexpialidocious','hippopotamophobia','xenotransplantation','sly','rutabaga','dinosaur','oleszewski','tv','luxembourg']


def choose_random(difficulty):
    if difficulty == '1':
        return random.choice(easy_words)
    elif difficulty == '2':
        return random.choice(medium_words)
    elif difficulty == '3':
        return random.choice(hard_words)
    elif difficulty == '4':
        return random.choice(SUPERHARD_WORDS)
    else:
        print("yo that's not a valid response")





