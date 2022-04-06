import xlwings as xw
import numpy_financial as npf

@xw.func
def final_calculator(interest_rate, sip, number_of_years, principal_amount=0):
    months = int(number_of_years * 12)
    invested_amt = principal_amount
    monthly_interest = interest_rate / 12
    
    for month in range(months):
        invested_amt = invested_amt + invested_amt * monthly_interest
        invested_amt  += sip
    return invested_amt

@xw.func
def irr_personal(sip, number_of_years, final_amount, principal_amount):
    months = int(number_of_years * 12)
    initial_investment = principal_amount
    cash_flow = [initial_investment * -1] + [sip * -1] * months + [final_amount]
    print(cash_flow)
    # Calculating IRR
    irr = npf.irr(cash_flow)
    return irr * 12 * 100

irr_personal(217857, 1, 5844763.294, 2594585)
    
    
    