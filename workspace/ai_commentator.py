import openai

_charName = "The Dark Urge. "
_bio = "A character from baldur's gate who embodies a struggle with violent desires, particularly the urge to murder. It is about fighting against those dark thoughts while understanding that succumbing to them could lead to certain consequences."

class AICommentator:
    
    def generate_commentary(self, dialogue, history):
        parameters = {
            'model': 'gpt-4',
            'messages': [
            {
                "role": "system", "content":
                "Your job is to embody a D&D character in an RPG video game and augment the game's dialogue with your 'thoughts' as a role-player. "
                + "You will be provided the current dialogue, followed by a history of past dialogue. "
                + "\nThe character you embody is named " + _charName
                + "\nThe character's bio, in a nutshell: " + _bio
                + "\nNote: The provided text is an OCR conversion from a screenshot. It may have non-applicable text and symbols. "
                },
            {
                "role": "user", "content": "current dialogue: " + dialogue + "\n" + "Dialogue history: " +  history
            }
            ]
        }
    
        response = openai.ChatCompletion.create(**parameters)
    
        return response.choices[0].message.content

    def __init__(self):
        self.openai = openai




    
    
