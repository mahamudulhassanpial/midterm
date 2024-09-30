class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall_OBJECT):
        Star_Cinema._hall_list.append(hall_OBJECT)

    @classmethod
    def get_hall_list(self):
        return self._hall_list

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        Show_details = (show_id, movie_name, time)
        self.__show_list.append(Show_details)

        seat_layout = [['0' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seat_layout

    def book_seats(self, show_id, seat_list):
        if show_id in self.__seats:
            for (row,col) in seat_list:
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if self.__seats[show_id][row][col] == '0':
                        self.__seats[show_id][row][col] = '1'
                        print(f"Seat ({row}, {col}) successfully booked!")
                    else:
                        print(f"Error: Seat ({row}, {col}) is already booked!\n**** Please find an another seat *****")
                else:
                    print(f"Error: Seat ({row}, {col}) is out of Seat area!\n***** We can not provide the seat ****")
        else:
            print(f"This Show is not running")

    def view_show_list(self):
        print("-----------------------------------------------------------------------------------")
        print("*********************** Wellcome TO MUKTI CHENAMA HAll *****************************")
        print(f"Shows Running in Hall no({self.__hall_no}):")
        for show in self.__show_list:
            show_id, movie_name, time = show
            print(f"Movie Name: {movie_name}    Show ID: {show_id}     Time: {time}")
        print("------------------------------------------------------------------------------------")

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            print(f"\nAvailable seats for Show ID {show_id}:")
            for row in self.__seats[show_id]:
                print(' '.join(row))
        else:
            print(f"Show ID {show_id} not found!!\n***** Please try again and Enter the right show id ****")


def Cinema_Service():
    while True:
        print("\n1. View All Shows Today")
        print("2. View Available Seats")
        print("3. Book Ticket")
        print("4. Exit")
        option = input("Enter Option: ")

        if option == '1':
            for hall in Star_Cinema.get_hall_list():
                hall.view_show_list()
        elif option == '2':
            hall_no = input("Enter Hall number: ")
            show_id = input("Enter Show ID: ")
            for hall in Star_Cinema.get_hall_list():
                if hall._Hall__hall_no == hall_no:
                    hall.view_available_seats(show_id)
                    break
            else:
                print("The Hall not found!!!")
        elif option == '3':
            seat = input("Enter number of seats: ")
            hall_no = input("Enter Hall number: ")
            show_id = input("Enter Show ID: ")
            seat_input = input("Enter seats to book (row,col) separated by spaces: ")
            seats = [tuple(map(int, seat.split(','))) for seat in seat_input.split()]

            for hall in Star_Cinema.get_hall_list():
                if hall._Hall__hall_no == hall_no:
                    hall.book_seats(show_id, seats)
                    break
            else:
                print("Error: Hall is not found!")
        elif option == '4':
            print("Thanks For visiting us.\nPlease Come again. Goodbye!!!")
            break
        else:
            print("Please Select the given Option and try again.")


HALl1 = Hall(7, 7, 'A1')
HALl1.entry_show('001', 'Puspa', '02/08/24 6:00 PM')
HALl1.entry_show('002', 'Batman', '04/08/24 10:00 PM')
HALl1.entry_show('003', 'Avenger End Game', '02/08/24 8:00 PM')


Cinema_Service()

