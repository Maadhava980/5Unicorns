import overheads, cash_on_hand, profit_loss

def main():
    overhead_result = overheads.overhead_func()
    cash_result = cash_on_hand.cash_on_hand_function()
    profit_result = profit_loss.profit_loss_function()

    return overhead_result, cash_result, profit_result
