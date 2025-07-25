import datetime
def calculate_future_date():

    days_to_add = int(input("Enter the number of days to add to the current date: "))

    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)


    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)

calculate_future_date()
