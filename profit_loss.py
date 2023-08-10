def profit_loss_function():
    from pathlib import Path
    import csv

    #--------------- PART 1: Attaining the records --------------#

    # Modify the file path to the "Profit & Loss csv" file
    fp = Path("PFBGP","csv_reports","Profits-and-loss.csv")

    # read the csv file to append Day and Net Profit from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list to store net profit records
        netProfitRecords = []

        # append Day and Net Profit records into the netProfitRecords list
        for row in reader:
            netProfitRecords.append([int(row[0]), float(row[4])])

    #--------------- PART 2: Check profit function --------------#
    def check_profit_trend(netProfitRecords):
        """ checks if the net profit is increasing more than the previous day everyday or
            checks if the net profit is decreasing more than the previous day everyday or
            checks if the net profit is fluctuating up and down everyday
        """
        increasing = decreasing = True
        
        for i in range(1, len(netProfitRecords)):
            if netProfitRecords[i][1] > netProfitRecords[i - 1][1]:
                decreasing = False
            elif netProfitRecords[i][1] < netProfitRecords[i - 1][1]:
                increasing = False
        result2 = ""

        # if increasing everyday, goes to the next function that finds the highest increase and day
        if increasing: 
            #--------------- PART 3: Profit increase function --------------#
            def find_highest_increase(data):
                max_increase_day, max_increase_amount = 0, 0
                prev_net_profit = data[0][1] # Set the initial previous net profit
                for day, net_profit in data[1:]:
                    increase = net_profit - prev_net_profit
                    if increase > max_increase_amount:
                        max_increase_day, max_increase_amount = day, increase
                    prev_net_profit = net_profit
                return max_increase_day, max_increase_amount

            # Find the day and amount of the highest increase when net profit is always increasing.
            max_increase_day, max_increase_amount = find_highest_increase(netProfitRecords)
            # Print the highest increase in Net profit in the desired format.
            result2 += ("\n[NET PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN EACH DAY]")
            result2 += (f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_increase_day}, AMOUNT: USD {max_increase_amount:.2f}\n")
            #writes the result of this function into the summary report text file in append mode
            with open ("Summary_report.txt", "a") as file:
                file.write(result2)

        # if decreasing everyday, goes to the next function that finds the largest deficit and day
        elif decreasing:
            #--------------- PART 4: Profit decrease function --------------#
            def find_largest_deficit(data):
                max_deficit_day, max_deficit_amount = 0, 0
                prev_net_profit = data[0][1] # Set the initial previous net profit
                for day, net_profit in data[1:]:
                    deficit = prev_net_profit - net_profit
                    if deficit > max_deficit_amount:
                        max_deficit_day, max_deficit_amount = day, deficit
                    prev_net_profit = net_profit
                return max_deficit_day, max_deficit_amount

            max_deficit_day, max_deficit_amount = find_largest_deficit(netProfitRecords)
            # Print the largest decrease in Net profit in the desired format.
            result2 +=("\n[NET PROFIT DEFICIT] PROFIT ON EACH DAY IS LOWER THE PREVIOUS DAY]")
            result2 +=(f"[LARGEST NET PROFIT DEFICIT] DAY: {max_deficit_day}, AMOUNT: USD {max_deficit_amount:.2f}\n")
            #writes the result of this function into the summary report text file in append mode
            with open ("Summary_report.txt", "a") as file:
                file.write(result2)

        # fluctuate everyday goes to this function that finds the deficits on each day where there were differences
        else:  
            #--------------- PART 5: Profit fluctuate function --------------#   
            def compute_net_profit_difference(data):
                """This function calculates all the differences from the previous day (deficits). It gets
                all the results for each specific day and amount.
                """
                differences = []
                prev_net_profit = data[0][1] # Set the initial previous net profit
                for day, net_profit in data[1:]:
                    if net_profit < prev_net_profit:
                        difference = net_profit - prev_net_profit
                        differences.append((day, difference * -1))
                    prev_net_profit = net_profit
                return differences

            # Calculate the differences in net profit only if it's lower than the previous day.
            differences = compute_net_profit_difference(netProfitRecords)
            # for loop to get all the results for each day and amount
            for day, amount in differences:
                result2 +=(f"[ NET PROFIT DEFICIT ] DAY: {day:3}, AMOUNT: USD {amount:.2f}\n") 
            #writes the result of this function into the summary report text file in append mode
            with open ("Summary_report.txt", "a") as file:
                file.write(result2)
                
            return result2
        return result2
    profit_trend_result=check_profit_trend(netProfitRecords)
    return profit_trend_result

# Call the profit_loss_function() and capture its result
profit_loss_result = profit_loss_function()

# Print the result
print(profit_loss_result)