from os import system 
import random 
class Churn:
    def __init__(self, no, name, password):
        self.no = no
        self.name = name
        self.password = password
        self.total = 0

class Bank:
    def __init__(self):
        self.churn_list = list()

    def be_churn(self, no, name, password):
        self.churn_list.append(Churn(no, name, password))

def main():
    bank = Bank()
    while True:
        system("clear")
        print ("""
        [0] -> I HAVE ALREADY CHURN
        [1] -> I WANT TO BE A CHURN
        """)
        
        case = input("please enter your status : ")
        if case == "0":
            no_lst = [ i.no for i in bank.churn_list ]   # only s list
            print("current ids : ", no_lst)
            no = input("id no : ")

            if no in no_lst:
                for c in bank.churn_list:
                    if no == c.no:
                        print(f"welcome {c.name} :)")
                        pwd = input("password : ")

                        if pwd == c.password:
                            print("enter success !")
                        
                            while True:
                                system("clear")
                                print ("""
                                [1] -> ask total money            
                                [2] -> investment me      
                                [3] -> investment another
                                [4] -> withdraw money
                                [Q] -> quit
                                """)

                                choose = input("please enter your status : ")

                                if choose == "1":
                                    print(f"total money : {c.total}")
                                    input("press enter for menu.")

                                elif choose == "2":
                                    money = int(input("enter your invest money that you want : "))
                                    c.total += money                        
                                    input("press enter for menu.")
                                 
                                elif choose == "3":
                                    send_id = input("enter id that you want send : ")

                                    if send_id in no_lst:
                                        for send_churn in bank.churn_list:
                                            if send_id == send_churn.no:
                                                send_money = int(input("enter your send money that you want : "))
                                                if send_money <= c.total:
                                                    print(f"sended money : {send_money} sended churn : {send_churn}")
                                                    c.total -= send_money
                                                    send_churn.total += send_money 
                                                else:
                                                    print("not enough money !")
                                                    input("press enter for menu.")

                                    else:
                                        print("id not founded")
                                        input("press enter for menu.")

                                elif choose == "4":
                                    get_money = int(input("enter your send money that you want : "))

                                    if get_money <= c.total:
                                        c.total -= get_money
                                        print("done. get money !")
                                        input("press enter for menu.")

                                    else:
                                        print("not enough money !")
                                        input("press enter for menu.")

                                elif choose == "q" or choose == "Q":    
                                    print("quitting..")                                               
                                    break
                                
                        else:
                            print("invalid password.try again")
                            input("press enter for menu.")
                            break        

            else:
                print("id is not in id list. ")
                input("press enter for menu.")
                
        if case == "1":
            id_no = input("enter id : ")
            name = input("name : ")
            password = input("password : ")
            bank.be_churn(id_no, name, password)


if __name__ == ("__main__"):
    main()