import datetime

def solution(a, b):
    week = {
            'Monday':"MON",
            'Tuesday':"TUE",
            'Wednesday':"WED",
            'Thursday':"THU",
            'Friday':"FRI",
            'Saturday':"SAT",
            'Sunday':"SUN"}
    answer = datetime.date(2016, a, b)
    return week[answer.strftime("%A")]