
# DEBUG
# Informowanie o przebiegających akcjach i aktywowanych funkcjach
# końcowy zapis do Log.data.txt

class DEBUG:
    def __init__(self, enabled=False):
        self.enabled = enabled
        if enabled:
            print(">> DEBUG enabled >> Debug object made")

    def print_elements(self, *args) -> None:
        print(">> Elements")
        for element in args:
            print(element)

    def get_debug_elements(self, *args):
        return args

    #funckja na przenoszenie given printów/stringów into tuple here !!

    def export_to_txt(self, string_tuple : tuple, filename : str = "log.txt" ) -> None:
        try:
            with open(filename, "w") as f:
                f.write("\n".join(string_tuple))
                print(">> Debug log saved to file")  # export docelowy path needed !!
        except Exception as e:
            print("!!! ERR0R !!! \n", e)



#sznycel = DEBUG(enabled=True)
#x = 5
#y = 0
#z = [4,2,1,5,3,6,3]
#sznycel.print_elements(z)
#sznycel.print_elements(x,y,z)
#print(sznycel.get_debug_elements(x, y))