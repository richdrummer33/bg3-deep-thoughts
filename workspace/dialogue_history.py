class DialogueHistory:
    def __init__(self):
        self.history = ""

    def add_dialogue(self, dialogue):
        self.history += dialogue
        if len(self.history) > 500:
            self.history = self.history[-500:]

    def get_history(self):
        return self.history
