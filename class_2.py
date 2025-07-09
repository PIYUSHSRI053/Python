def recta(rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if (i == 1 or i == rows or j == 1 or j == cols):
                print("*", end="")
            else:
                print(end=" ")
        print()

rows = int(input("Enter the no. of Rows: "))
cols = int(input("Enter the no. of Columns: "))
recta(rows, cols)


# def Pattern(rows, cols):
# 	for i in range(1, rows + 1):
# 		for j in range(1, i):
# 			print(end = " ")
# 		for j in range(1, cols + 1):
# 			if (i == 1 or i == rows or
# 				j == 1 or j == cols):
# 				print("*", end = "")
# 			else:
# 				print(end = " ")
		
# 		print()
# rows=int(input("Enter the no. of Rows: "))
# cols=int(input("Enter the no of col.: "))
# Pattern(rows, cols)

