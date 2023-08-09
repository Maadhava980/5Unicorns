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
            # Print the highest increase in Net profit in the desired format.
            result2 +=("\n[NET PROFIT DEFICIT] PROFIT ON EACH DAY IS LOWER THE PREVIOUS DAY]")
            result2 +=(f"[LARGEST NET PROFIT DEFICIT] DAY: {max_deficit_day}, AMOUNT: USD {max_deficit_amount:.2f}\n")
            with open ("Summary_report.txt", "a") as file:
                file.write(result2)

        # fluctuate everyday goes to this function that finds the deficits on each day where there were differences
        else:  
            #--------------- PART 5: Profit fluctuate function --------------#   
            def compute_net_profit_difference(data):
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
            for day, amount in differences:
                result2 +=(f"[ NET PROFIT DEFICIT ] DAY: {day:3}, AMOUNT: USD {amount:.2f}\n") 
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