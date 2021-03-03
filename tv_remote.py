import os 

class TV():

    def __init__(self, sound = 0, channel_list = ["fox"], current_channel = "fox" ):
        self.sound = sound 
        self.channel_list = channel_list
        self.current_channel = current_channel

    def info(self):
        print(f"\nState of Television\n  sound = {self.sound}\n  channel list = {self.channel_list}\n  current channel = {self.current_channel}") 

    # def __str__(self):
    #     return f"\nState of Television\n  sound = {self.sound}\n  channel list = {self.channel_list}\n  current channel = {self.current_channel}"

    def set_sound(self):

        print("Current sound level : ", self.sound)        

        while(True):
            res = input("\nPress - | + | S(save)\n") 
            
            if res == "-":
                if self.sound >= 10:
                    self.sound -= 10
                    print("Sound level is : ", self.sound)
            
            elif res == "+":
                if self.sound < 100:
                    self.sound += 10
                    print("Sound level is : ", self.sound)
            
            else:
                print("Sound is update : ", self.sound)
                break 

    def add_channel(self):

        print("Current channel list : ", self.channel_list)
        new_ch = input("\nEnter new channel name : ")
        self.channel_list.append(new_ch)
        print("Updated channel list : ", self.channel_list)
    

    def change_channel(self):

        while(True):
            print("_"*20)
            print("\nChannel list :", self.channel_list)
            print("\nCurrent channel :", self.current_channel)
            button = input("\n >  |  <  | channel number | S(save) :  ")
            current_indice = self.channel_list.index(self.current_channel)
            total_channel = len(self.channel_list)

            if button == ">":
                current_indice += 1

                if current_indice > total_channel-1:
                    current_indice = 0
        
                self.current_channel = self.channel_list[current_indice]

                print("\nNow current channel is ",self.current_channel)
        
            elif button == "<":
                current_indice -= 1
                self.current_channel = self.channel_list[current_indice]
                
                if current_indice < 0:
                    current_indice = total_channel

                print("\nNow current channel is ",self.current_channel)
            
            # elif button == "1":
            #     pass

            else:
                print("Save current channel")
                break 

# ==========================================

def main():
    
    tv = TV()

    while(True):
        os.system("clear")
        print("""
        MENU
        [1] -> STATE OF TV 
        [2] -> SOUND SETTING
        [3] -> ADD CHANNEL
        [4] -> CHANGE TO CHANNEL 
        [Q] -> CLOSE TV        """)

        case = input("Enter your process : ")

        # show current state
        if case == "1":
            tv.info()
            # print(tv)
            input("Press enter for menu.")
        
        # sound setting
        if case == "2":
            tv.set_sound()
            input("press enter for menu.")

        # add channel
        if case == "3":
            tv.add_channel()
            input("press enter for menu.")
        
        # change channel
        if case == "4":
            tv.change_channel()
            input("press enter for menu.")
        
        # quit 
        if case == "q" or case == "Q":
            print("closed tv")
            break

if __name__ == ("__main__"):
    main()