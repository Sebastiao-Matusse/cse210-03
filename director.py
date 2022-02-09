from terminal_service import TerminalService
from word import RandomWord
from parachute import Parachute


class Director:

    def __init__(self):
        self._is_playing = True
        self._terminal_service = TerminalService
        self._parachute = Parachute
        self._word = RandomWord
    

    def start_game(self):
        """Start the game by running the main loop"""

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def _get_inputs(self):
        """Display the location of the guessed letter"""
        display_parachute = self._parachute
        letter = self._terminal_service.read_letter("\nGuess a letter")
        new_word = self._terminal_service.read_word(letter)
    
    def _do_updates(self):
        # The parachute class should have a method which 
        # should change break a line on the parachute if they guess
        # incorrectly the letter or do otherwise if they guess correctly
        self._parachute.watch_letter()
        
    def _do_outputs(self):
        display_word = self._terminal_service.write_word()
        if self._parachute.no_parachute():
            self._is_playing = False

