'''
Part 2:

The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

    If a customer purchases 0 books, they earn 0 points.
    If a customer purchases 2 books, they earn 5 points.
    If a customer purchases 4 books, they earn 15 points.
    If a customer purchases 6 books, they earn 30 points.
    If a customer purchases 8 or more books, they earn 60 points.

Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
'''

class Bookstore:
    award_points = {0: 0, 2: 5, 4: 15, 6: 30, 8: 60}
    
    def __init__(self):
        pass
    
    def points_awarded(self, numbooks: int):
        sorted_award_points = dict(sorted(self.award_points.items()))
        
        awarded_pints = 0
        for key in sorted_award_points.keys():
            if key <= numbooks:
                awarded_pints = sorted_award_points[key]
            else:
                print(f"Number of points awarded: {awarded_pints}")
                return
        

if __name__ == "__main__":
    bookstore = Bookstore()
    num_books = int(input("Please Enter the Number of books student purchased: "))
    
    bookstore.points_awarded(numbooks=num_books)
    