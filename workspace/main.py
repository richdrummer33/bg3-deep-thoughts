from screen_reader import ScreenReader
from dialogue_history import DialogueHistory
from ai_commentator import AICommentator
import time

def main():
    screen_reader = ScreenReader()
    dialogue_history = DialogueHistory()
    ai_commentator = AICommentator()

    while True:
        dialogue = screen_reader.read_screen()
        dialogue_history.add_dialogue(dialogue)
        history = dialogue_history.get_history()
        commentary = ai_commentator.generate_commentary(dialogue, history)
        print(commentary)
        time.sleep(1)

if __name__ == "__main__":
    main()
