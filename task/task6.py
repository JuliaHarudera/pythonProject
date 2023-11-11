from  datetime import  timedelta, date


def date_range(start_date, end_date):
    delta = timedelta(days=1)
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += delta


start_date = date(2023, 1, 1)
end_date = date(2023, 1,10)


for single_date in date_range(start_date, end_date):
    print(single_date)