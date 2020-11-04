"""
Name:  CompoundInterest.py
Author:  Lee Brown
Created:  11/02/2020
Last Updated:  11/02/2020
Purpose:  Practice recursion by making a function that solves compound interest problems.
Description:  This function is going to use recursion to solve compound interest
            problems.  I got the idea from the following website:
            https://hackernoon.com/recursion-vs-looping-in-python-9261442f70a5
Outline:

I will start with a function that only works for whole year compounding.

function(principal, rate, years):
    principal = principal + (rate * principal)
    years = years - 1
    if years == 0:
        return principal
    else:
        function(principal, rate, years)
        return that value


Now, I will try for n compounding periods in a year.

function(principal, rate, compounds_per_year, years, _total_time_units_ = (compounds_per_year * years))
    _total_time_units -= 1
    principal = principal + (principal * (rate/compounds_per_year))

    if _total_time_units == 0:
        return principal
    else:
        function(principal, rate, years)
        return that value

"""
def CompoundAnnually(principal, rate, years):
    new = principal + (rate * principal)
    time_left = years - 1
    if time_left == 0:
        return new
    else:
        recur = CompoundAnnually(new, rate, time_left)
        return recur

#print(CompoundAnnually(2, 0.5, 5))

def CompoundN(principal, rate, comps_per_year, years, _time_units_ = None):
    if _time_units_ == None:
        _time_units_ = years * comps_per_year
    principal = principal + (principal * (rate/comps_per_year))
    _time_units_ -= 1
    if _time_units_ == 0:
        return principal
    else:
        recur = CompoundN(principal, rate, comps_per_year, years, _time_units_)
        return recur
print(CompoundN(2, 0.1, 12, 5))
