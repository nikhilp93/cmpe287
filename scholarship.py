if __name__ == "__main__":
  final_out={1:"student is eligible for scholarship",0:"student is NOT eligible for scholarship", "Dean":"Dean for consideration"}
  while True:   
      age = float(input("Please enter student's age in years: "))
      cal_dur = float(input("Please enter the number of months the student lived in california: "))
      part_time = float(input("Please enter the number of months student worked part time in relevant field of study: "))
      parents_ca_tax = float(input("Please enter the number of months student's parents paid california taxes: "))
      student_vol = input("Did the student volunteer for a cause and has valid proof for the same [yes/no]:")
      house_inc = float(input("Please enter the annual income in US dollars: "))

      if 18 <= age <=24: 
        if cal_dur>=24:
          if part_time >=6:
            if parents_ca_tax >=12 and student_vol == "yes" :
              print(final_out[1])
              print("\n-------------------------------------------------------\n")
            else:
              print(final_out[0])
              print("\n-------------------------------------------------------\n")
          #Has household income less than 5000$ per annum then one need not satisfy criteria C, he will be redirected to "Dean for consideration"
          elif age >=18 and age <=24 and cal_dur>=24 and parents_ca_tax >=12 and student_vol == "yes" and house_inc <=5000:
            print(final_out["Dean"])
            print("\n-------------------------------------------------------\n") 
          #Has worked part time for at least for 6 months in the relevant field of study, if he fails this criterion, check if satisfies E
          elif part_time < 6 and student_vol == "yes":
            print(final_out[1])
            print("\n-------------------------------------------------------\n")
          else:
            print(final_out[0])
            print("\n-------------------------------------------------------\n")
        #Student has lived in California for last 2 years, if he fails this criterion, check if satisfies D.
        elif cal_dur<24 and parents_ca_tax >=12 and student_vol == "yes":
          print(final_out[1])
          print("\n-------------------------------------------------------\n")
        else:
          print(final_out[0])
          print("\n-------------------------------------------------------\n")
      else:
          print(final_out[0])
          print("\n-------------------------------------------------------\n")

"""
      if age >=18 and age <=24:
        cal_dur = float(input("Please enter the number of months the student lived in california: "))
        if cal_dur>=24 :
          part_time = float(input("Please enter the number of months student worked part time in relevant field of study: "))
          if part_time >=6 :
            parents_ca_tax = float(input("Please enter the number of months student's parents paid california taxes: "))
            if parents_ca_tax >=12 :
              student_vol = input("Did the student volunteer for a cause and has valid proof for the same [yes/no]:")
              if student_vol == "yes" :
                print(final_out[1])
                print("\n#########################################################\n")
              else:
                print(final_out[0])
                print("\n#########################################################\n")
            else:
              print(final_out[0])
              print("\n#########################################################\n")
          else:
            print(final_out[0])
            print("\n#########################################################\n")
        else:
          print(final_out[0])
          print("\n#########################################################\n") 
      #if household income less than 5k, no need 
      elif age >=18 and age <=24 and cal_dur>=24 and parents_ca_tax >=12 and student_vol == "yes" and house_inc <=5000:
          print(final_out["Dean"])
          print("\n#########################################################\n")
      else:
          print(final_out[0])
          print("\n#########################################################\n")
"""   
