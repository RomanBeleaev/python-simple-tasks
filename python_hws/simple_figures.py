figure = input("what figure to draw? ")

if figure == "line":
  print("-----")
elif figure == "square":
  print("-----","|   |","|   |","-----",sep='\n')
elif figure == "parallel horizontal lines":
  print("-----","-----",sep='\n')
elif figure == "parallel vertical lines":
  print("|   |","|   |",sep='\n')
else:
  print("CAN'T DRAW SUCH FIGURE!")  