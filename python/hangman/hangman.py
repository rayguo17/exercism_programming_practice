# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

#one guess reveal all exist letter

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING # can be retrieve from remain_guess and guessed arr
        self.guessed=[] #letter given by user
        self.word = word
        
        
    def deduct_remain_chances(self):
           if self.remaining_guesses>=0 and self.get_status() == STATUS_ONGOING:
               self.remaining_guesses-=1
           else:
               raise ValueError("The game has already ended.")

    def guess(self, char):
        if char in self.guessed:
            self.deduct_remain_chances()
            return
        if not char in self.word:
            self.deduct_remain_chances()
        self.guessed.append(char)
        
        

    def get_masked_word(self):
        result=""
        for ch in self.word:
            if ch in self.guessed:
                result = f"{result}{ch}"
            else:
                result = f"{result}_"
        return result

    def get_status(self):
        if self.remaining_guesses>=0 and self.get_masked_word() == self.word:
            return STATUS_WIN
        if self.remaining_guesses>=0:
            return STATUS_ONGOING
        return STATUS_LOSE
    def print_status(self):
        print(self.word)
        print(self.guessed)
        print(self.remaining_guesses)
            
if __name__ =="__main__":
    game = Hangman("hello")
    game.print_status()
    print(game.get_status())
    print(game.get_masked_word())
    game.guess('l')
    print(game.get_status())
    print(game.get_masked_word())
    game.print_status()
    game.guess('l')
    game.print_status()