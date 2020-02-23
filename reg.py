import re
def name():
	a = input("""
	Hello please input $ or %
		""")
	if not re.match("^[$,%]",a):
		print("Please input any signs above!")
		name()
	else:
		print("Thank you")
name()