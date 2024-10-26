import wordreference as wr

translations, audio_links = wr.define_word("programmer", "enfr")
print(audio_links)
print("translations", translations)

"""
    [
        'https://www.wordreference.com/audio/en/us/us/en1068804.mp3',
        'https://www.wordreference.com/audio/en/uk/general/en1068804.mp3',
        'https://www.wordreference.com/audio/en/uk/rp/en1068804.mp3',
        'https://www.wordreference.com/audio/en/uk/Yorkshire/en1068804-55.mp3',
        'https://www.wordreference.com/audio/en/Irish/en1068804.mp3',
        'https://www.wordreference.com/audio/en/scot/en1068804.mp3',
        'https://www.wordreference.com/audio/en/us/south/en1068804.mp3',
        'https://www.wordreference.com/audio/en/Australian/en1068804.mp3',
        'https://www.wordreference.com/audio/en/Jamaica/en1068804.mp3'
    ]

translations
{
    1:
    {
        'word': 'programmer n',
        'definition': '(computer: [sb] who writes programs) (Informatique)',
        'meanings': ['programmeur, programmeuse nm, nf'],
        'examples': [
                        [
                            'The department employs programmers to develop.',
                            'Le département emploie programmeurs pour développer.' ]
                        ]
                    ]
    },
    2:
    {
        'word': 'programmer n',
        'definition': '(TV, radio: [sb] who plans schedules) (TV, Radio)',
        'meanings': ['programmateur, programmatrice nm, nf'],
        'examples': [
                        ['BBC programmers defended their decision to air the show at 8pm.', "Les programmateurs de la BBC ont défendu leur décision de diffuser l'émission à 20h."]
                    ]
    },
    3
    {
    ...
    }
"""
