'''
Part 1:

Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. 
The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, 
the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
'''

from enum import Enum

class Months(Enum):
    JAN =1
    FEB =2
    MAR =3
    APR =4
    MAY =5
    JUN =6
    JUL=7
    AUG=8
    SEP=9
    OCT=10
    NOV=11
    DEC=12 
    
class Rainfall:
    num_years: int
    
    def __init__(self, num_years: int):
        self.num_years = num_years
    
    def cal_avg_ranfall(self, monthly_data: dict):
        total_months = self.num_years * len(Months)
        
        total_rain_fall = 0
        for year, monthly_data in monthly_data.items():
            total_rain_fall += sum(monthly_data.values())
        
        avg_rain_fall = round(total_rain_fall / total_months , 2)
        print(f"Total number of months: {total_months}")
        print(f"Total inches of rain: {total_rain_fall}")
        print(f"Average rain fall per month: {avg_rain_fall}")
    
    
    def load_rainfall_data(self) -> dict:
        user_data = {}
        
        for year in range(1, (self.num_years+1)):
            user_data[year] = {}
            for month in Months:
                user_input = input(f"Enter rain fall for year: {year} {month.name} month: ")
                if (user_input != None and user_input != ''):
                    rain_fall = round(float(user_input), 2)
                    user_data[year][month.name] = rain_fall
                else:
                    user_data[year][month.name] = 0
                    
        
        return user_data
        

if __name__ == "__main__":
    
    print("Program to calculate the average rain fall, please enter the few years of data")
    
    num_year = int(input("Please enter the number of years: "))
    rainfall_calc = Rainfall(num_years=(num_year))
    
    monthly_data = rainfall_calc.load_rainfall_data()
    rainfall_calc.cal_avg_ranfall(monthly_data)

    
    
    