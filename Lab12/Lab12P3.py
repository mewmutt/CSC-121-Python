# Myles Joubert
# 4/11/23

from datetime import datetime

def main():
    now = datetime.now()
    
    format1 = now.strftime("%m/%d/%y %I:%M:%S %p")
    format2 = now.strftime("%a, %b %d, %Y")
    format3 = now.strftime("%A, %B %d, %Y")
    
    print("The current date/time is:")
    print(format1)
    print(format2)
    print(format3)
    
    date_string = input("Enter a date (e.g. 04-01-1989): ")
    
    try:
        date = datetime.strptime(date_string, "%m-%d-%Y")
        
        weekday = date.strftime("%A")
        
        print("That date was on a", weekday + ".")
    except ValueError:
        print("Date in wrong format.")
        
if __name__ == '__main__':
    main()