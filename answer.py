print("answer")


number = 42


while True:
	answer = input("11111?")
	if not answer or answer == "exit":
		break
	if not answer.isdigit():
		print("Another one?")
		continue

	user_answer = int(answer)
	if user_answer > number:
		print("Number is more")
	elif user_answer < number:
		print("Number is less")
	else:
		print("Congratulations")
		break
input()