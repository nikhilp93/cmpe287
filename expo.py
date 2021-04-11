if __name__ == "__main__":
  final_out={1:"storytelling",2:"drawing",3:"quiz",4:"essay writing",5:"rhyming",6:"poetry"}
  while True:
      gender = input("Please enter child's gender for games expo:[boy/girl]: ") 
      age = float(input("Please enter child's age in years: "))

      if gender=="boy":
        if 7<age<10:
          print("can participate in ",final_out[1])
          print("\n-------------------------------------------------------\n")
        elif 11<age<15:
          print("can participate in ",final_out[3])
          print("\n-------------------------------------------------------\n")
        elif age<6:
          print("can participate in ",final_out[5])
          print("\n-------------------------------------------------------\n")
        elif age>20:
          print("can participate in ",final_out[6])
          print("\n-------------------------------------------------------\n")
        else:
          print("invalid age input")
          print("\n-------------------------------------------------------\n")
      elif gender=="girl":
        if 7<age<10:
          print("can participate in ",final_out[2])
          print("\n-------------------------------------------------------\n")
        elif 11<age<15:
          print("can participate in ",final_out[4])
          print("\n-------------------------------------------------------\n")
        elif age<6:
          print("can participate in ",final_out[5])
          print("\n-------------------------------------------------------\n")
        elif age>20:
          print("can participate in ",final_out[6])
          print("\n-------------------------------------------------------\n")
        else:
          print("invalid age input")
          print("\n-------------------------------------------------------\n")
      else:
        print("please enter a valid gender")
        print("\n-------------------------------------------------------\n")
