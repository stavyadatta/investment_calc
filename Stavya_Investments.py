import xlwings as xw
import numpy_financial as npf

@xw.func
def final_calculator(interest_rate, sip, number_of_years, principal_amount=0):
    months = int(number_of_years * 12)
    monthly_interest = interest_rate / 12
    
    # Calculating the final amount
    invested_amt = (sip * (((1 + monthly_interest) ** months) - 1) / monthly_interest) \
                    + (principal_amount * (1 + monthly_interest) ** months)
    return invested_amt

print(final_calculator(0.12, 1, 1, 10))

@xw.func
def irr_personal(sip, number_of_years, final_amount, principal_amount):
    months = int(number_of_years * 12)
    initial_investment = principal_amount
    cash_flow = [initial_investment * -1] + [sip * -1] * months + [final_amount]
    print(cash_flow)
    # Calculating IRR
    irr = npf.irr(cash_flow)
    return irr * 12 * 100

    
    
    