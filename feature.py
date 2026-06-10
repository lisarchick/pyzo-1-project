class all_Feature:
    def __init__(self,feature):
        feature = feature
    def open_file(self):
        with open ('feature.txt',"w") as file:
            file.write(self.feature)
open = all_Feature("Tested")
open.open_file()