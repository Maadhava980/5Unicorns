def cash_on_hand_function():
    from pathlib import Path
    import csv

    #--------------- PART 1: Attaining the records --------------# 

    # Modify the file path to cash_on_hand.csv
    fp = Path("project_group B","csv_reports","Cash_on_Hand.csv")

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
    def check_COH_trend(CashOnHandRecords):
        """ checks if the net profit is increasing more than the previous day everyday or
            checks if the net profit is decreasing more than the previous day everyday or
            checks if the net profit is fluctuating up and down everyday
            """
        increasing = decreasing = True
        
        # for loop to iterate over the records list. Uses the len function and 
        for i in range(1, len(CashOnHandRecords)): 
            # checks if the cash on hand value at the current index is greater than the previous index 
            if CashOnHandRecords[i][1] > CashOnHandRecords[i - 1][1]:
                decreasing = False
            # checks if the cash on hand value at the current index is lower than the previous index
            elif CashOnHandRecords[i][1] < CashOnHandRecords[i - 1][1]:
                increasing = False
        result1 = '' #result1 as an empty string
        
        # if increasing everyday, goes to the next function to find highest increase and day
        if increasing:
            #--------------- PART 3: COH increase function --------------#
            def find_highest_increase(data):
                """The functions finds finds the highest increase in cash on hand and the day it happened
                given that cash on hand is always increasing"""
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
            #writes the result of this function into the summary report text file in append mode
            with open ("Summary_report.txt","a") as file:
                file.write(result1)

        # if decreasing everyday, this function is  used to find largest deficit and day
        elif decreasing:
            #--------------- PART 4: COH decrease function --------------#
            # Function to find the day and amount of largest decrease 
            def find_largest_deficit(data):
                """This function finds the largest deficit in cash on hand and the day it ocurred given that cash 
                 on hand is always decreasing """
                max_deficit_day, max_deficit_amount = 0, 0
                prev_cash_on_hand = data[0][1] # Set the initial previous cash on hand
                for day, cash_on_hand in data[1:]:
                    deficit = prev_cash_on_hand - cash_on_hand
                    if deficit > max_deficit_amount:
                        max_deficit_day, max_deficit_amount = day, deficit
                    prev_cash_on_hand = cash_on_hand
                return max_deficit_day, max_deficit_amount

            max_deficit_day, max_deficit_amount = find_largest_deficit(cashOnHandRecords)
            # Print the largest decrease in Cash-on-Hand in the desired format.
            result1 += ("\n[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
            result1 += (f"[HIGHEST CASH DEFICIT] DAY: {max_deficit_day}, AMOUNT: USD {max_deficit_amount:.2f}\n")
            #writes the result of this function into the summary report text file in append mode
            with open ("Summary_report.txt","a") as file:
                file.write(result1)

        # If cash on hand is fluctuating everyday, this function finds all the days with deficits
        else:
            #--------------- PART 5: COH fluctuate function --------------#
            def compute_cash_on_hand_difference(data):
                """this function calculates the fluctuations aka all the cash deficits we had. it calculates all the
                differences of the previous day. For each day it prints out the day and the deficit of that specific day
                """
                differences = []
                prev_cash_on_hand = data[0][1] # Set the initial previous cash on hand
                for day, cash_on_hand in data[1:]:
                    if cash_on_hand < prev_cash_on_hand:
                        difference = cash_on_hand - prev_cash_on_hand
                        differences.append((day, difference * -1))
                    prev_cash_on_hand = cash_on_hand
                return differences

            # Calculate the differences in Cash-on-Hand only if it's lower than the previous day.
            differences = compute_cash_on_hand_difference(cashOnHandRecords)
            #for loop to get all the results for each day and amount
            for day, amount in differences: 
                result1 += (f"[ CASH DEFICIT ] DAY: {day:3}, AMOUNT: USD {amount:.2f}\n")
            #writes the result of this function into the summary report text file in append mode
            with open ("Summary_report.txt","a") as file:
                file.write(result1)

            return result1 
        return result1
    # call on the check_COH_trend function and capture its result
    COH_trend_result = check_COH_trend(cashOnHandRecords)
    return COH_trend_result

#call the Cash_on_hand function and capture its result
cash_on_hand_result = cash_on_hand_function()

#print the result
print(cash_on_hand_result)