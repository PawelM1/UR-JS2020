import sys
from datetime import date

dateFromTerminal = date.fromisoformat(sys.argv[1])
today = date.today()
    
datediff = today - dateFromTerminal
    
print(abs(datediff.days))