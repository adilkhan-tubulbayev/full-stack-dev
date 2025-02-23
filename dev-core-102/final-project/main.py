class Game:
	def __init__(self):
		pass

	def start(self):
		return '''Игрок — путешественник во времени, которому поручено исправить критическую ошибку в прошлом, 
которая привела к разрушительному парадоксу и угрозе будущего. Каждое принятое решение влияет на временную 
линию: правильный выбор приближает к восстановлению баланса, а неправильный — усиливает парадокс, приводя к 
катастрофическим последствиям.'''

	def make_choice(self):
		choice = input()
		return f"Ur choice: {choice}"

	def trigger_paradox():
		pass
	


story = Game()
print(story.start())
print(story.make_choice())