from unittest import case


# Klasa Kryterium
# Przechwyci i zapisze wybrane kryterium w zmiennej,
# Funkcje do zarządzania kryrerium

class Kryterium:
    def __init__(self, year_toggle = False, month_toggle = False, extension_toggle = False):
        self.year_toggle : bool = year_toggle
        self.month_toggle : bool = month_toggle
        self.extension_toggle : bool = extension_toggle

        self.kryterium_case_list : list = []
        self.toggles_list : list = [self.year_toggle, self.month_toggle, self.extension_toggle]

        for element in self.toggles_list:
            if element == self.year_toggle and self.year_toggle is True:
                self.kryterium_case_list.append("year")

            elif element == self.month_toggle and self.month_toggle is True:
                self.kryterium_case_list.append("month")

            elif element == self.extension_toggle and self.extension_toggle is True:
                self.kryterium_case_list.append("extension")

    def get_toggles(self):
        return self.toggles_list

    def get_kryterium_case_list(self):
        return self.kryterium_case_list

    def get_current_kryterium(self):

        for element in self.get_kryterium_case_list:
            match element:
                case "year":
                    print("current kryterium = year")
                    return "year"

                case "month":
                    print("current kryterium = month")
                    return "month"

                case "extension":
                    print("current kryterium = extension")
                    return "extension"

                case default:
                    print("!!! no kryterium detected !!!")
                    return "ERR0R"




        #if year_toggle == True:
        #    year = True
        #elif month_toggle == True:
        #    month = True
        #elif extension_toggle == True:
        #    extension = True


        #def get_kryterium(self):
        #    return


        #TODO: trza wincy / funkcje jakies