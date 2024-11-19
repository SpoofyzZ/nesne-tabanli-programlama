from abc import ABC, abstractmethod
import random

# Abstract sınıf: Player
class Player(ABC):
    @abstractmethod
    def make_move(self):
        """Her oyuncunun bir hamle yapması gerekir."""
        pass

# Concrete sınıf: HumanPlayer
class HumanPlayer(Player):
    def make_move(self):
        move = input("Hamlenizi seçin (taş, kağıt, makas): ").lower()
        while move not in ["taş", "kağıt", "makas"]:
            print("Geçersiz hamle. Lütfen tekrar deneyin.")
            move = input("Hamlenizi seçin (taş, kağıt, makas): ").lower()
        return move

# Concrete sınıf: ComputerPlayer
class ComputerPlayer(Player):
    def make_move(self):
        move = random.choice(["taş", "kağıt", "makas"])
        print(f"Bilgisayarın hamlesi: {move}")
        return move

# Oyun sınıfı
class RockPaperScissorsGame:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self, move1, move2):
        if move1 == move2:
            return "Berabere"
        elif (move1 == "taş" and move2 == "makas") or \
             (move1 == "kağıt" and move2 == "taş") or \
             (move1 == "makas" and move2 == "kağıt"):
            return "Oyuncu 1 kazandı!"
        else:
            return "Oyuncu 2 kazandı!"

    def play_round(self):
        move1 = self.player1.make_move()
        move2 = self.player2.make_move()
        result = self.determine_winner(move1, move2)
        print(f"Sonuç: {result}")

# Oyun başlatma
if __name__ == "__main__":
    print("Taş-Kağıt-Makas Oyununa Hoş Geldiniz!")
    human = HumanPlayer()
    computer = ComputerPlayer()
    game = RockPaperScissorsGame(human, computer)

    play_again = "e"
    while play_again.lower() == "e":
        game.play_round()
        play_again = input("Tekrar oynamak ister misiniz? (e/h): ")
