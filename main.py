import datetime

def count_down(target_date):
    now  = datetime.datetime.now()
    delta = target_date - now
    return delta

def main():
    year = int(input("Enter the Target Year -> "))
    month = int(input("Enter the Target Month -> "))
    day = int(input("Enter the Target Day -> "))

    target_date = datetime.datetime(year, month, day)
    delta = count_down(target_date)

    print(f"Time Left Until {target_date}: {delta}")

if __name__ == "__main__":
    main()