class Sol:
    def nim_game(self,num):
        return num%4!=0
if __name__ == '__main__':
    p1=Sol()
    print(p1.nim_game(3))
