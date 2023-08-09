def cash_on_hand_function():
    from pathlib import Path
    import csv

    #--------------- PART 1: Attaining the records --------------# 

    # Modify the file path to cash_on_hand.csv
    fp = Path("PFBGP","csv_reports","cash_on_hand.csv")

    # read the csv file to append Day and CashOnHand from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list to store cash on hand records
        cashOnHandRecords = []

        # append Day and CashOnHand records into the cashOnHandRecords list
        for row in reader:
            cashOnHandRecords.append([int(row[0]), float(row[1])])

    #--------------- PART 2: Check COH trend --------------# 
    # checks if the net profit is increasing more than the previous day everyday or
    # checks if the net profit is decreasing more than the previous day everyday or
    # checks if the net profit is fluctuating up and down everyday
    def check_COH_trend(CashOnHandRecords):
        increasing = decreasing = True
        
        for i in range(1, len(CashOnHandRecords)):
            if CashOnHandRecords[i][1] > CashOnHandRecords[i - 1][1]:
                decreasing = False
            elif CashOnHandRecords[i][1] < CashOnHandRecords[i - 1][1]:
                increasing = False
        result1 = ''
        
        # if increasing everyday, goes to the next function to find highest increase and day
        if increasing:
            #--------------- PART 3: COH increase function --------------#
            def find_highest_increase(data):
                max_increase_day, max_increase_amount = 0, 0
                prev_cash_on_hand = data[0][1] # Set the initial previous cash on hand
                for day, cash_on_hand in data[1:]:
                    increase = cash_on_hand - prev_cash_on_hand
                    if increase > max_increase_amount:
                        max_increase_day, max_increase_amount = day, increase
                    prev_cash_on_hand = cash_on_hand
                return max_increase_day, max_increase_amount

            # Find the day and amount of the highest increase when Cash-on-Hand is always increasing.
            max_increase_day, max_increase_amount = find_highest_increase(cashOnHandRecords)
            # Print the highest increase in Cash-on-Hand in the desired format.
            result1 += ("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            result1 += (f"[HIGHEST CASH SURPLUS] DAY: {max_increase_day}, AMOUNT: USD {max_increase_amount:.2f}\n")
            with open ("Summary_report.txt","a") as file:
                file.write(result1)

        # if decreasing everyday, goes to the next function to find largest deficit and day
        elif decreasing:
