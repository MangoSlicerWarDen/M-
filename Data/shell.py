import basic
print("M++ Programming Language | Version 0.5 | Created by luisipad#6463")
print("")
print("")
print("For more info please join the discord: https://discord.gg/mcMh97Q")
while True:
		text = input('>>  ')
		result, error = basic.run('<stdin>', text)

		if error:
				print(error.as_string())
		else:
				print(result)


