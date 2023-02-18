
def calculate_investment_value(initial_value, percentage, years):
    result=initial_value*(1+percentage/100)**years
    print(f"Po {years} latach Twoja lokata będzie warta {result:.2f}")

print("Kalkulator wartości lokaty z roczną kapitalizacją")
initial_value_input=input("Jaką kwotę wpłaciłaś na lokatę?")
initial_value= int(initial_value_input)
percentage_input=input("Jakie jest oprocentowanie (%) ")
percentage=int(percentage_input)
years_input=input("Ile lat trwa lokata?")
years=int(years_input)

calculate_investment_value(initial_value,percentage,years)