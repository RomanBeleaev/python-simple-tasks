x = -10
#             return False
#                  |
#       +----- falsy (or) -----+
#       |                      |
#   falsy (and)            falsy (and)
#       |     doesn't check    |     doesn't check
#       V           V          V           V
r  = x >= -5 and x <= -3 or x >= 10 and x <= 20
print(r)