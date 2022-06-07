from jumper import Jumper
from word_list import words
from console import Console

class Director:

    def __init__(self):
        self.keep_playing = True
        self.console = Console()
        self.jumper = Jumper()
        self.word = words

    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self.word

    def do_updates(self):
        self.jumper.process()

    def do_outputs(self):
        pass
