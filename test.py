class tic_tak_tok:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.a = [x for x in range(0,9)]
        self.visited = ['']*9

    def game_check(self):
        a=self.a
        #horizontal
        if a[0] == a[1] and a[1] == a[2]:
            return False
        if a[3]== a[4] and a[4]== a[5]:
            return False
        if a[6]==a[7]and a[7]==a[8]:
            return False
        #vertical
        if a[0] == a[3]and a[3] == a[6]:
            return False
        if a[1]==a[4]and a[4]==a[7]:
            return False
        if a[2]==a[5]==a[8]:
            return False
        #digonal
        if a[0] == a[4] and a[4] == a[8]:
            return False
        if a[2] == a[4] and a[4] == a[6]:
            return False
        else:
            return True

    def layout(self):
        a=self.a
        print(f' {a[0]}|{a[1]}|{a[2]}')
        print('-------')
        print(f' {a[3]}|{a[4]}|{a[5]}')
        print('-------')
        print(f' {a[6]}|{a[7]}|{a[8]}')

    def input_play(self,charcter,pos):
        self.a[pos]=charcter
        
    def play(self):
        p1=self.p1
        p2=self.p2
        i=0
        pos=-1
        while self.game_check():
            pos = int(input(f'Enter position for p{(i%2)+1}:'))
            if (pos not in self.visited) and (pos<9):
                if i%2==0:
                    self.input_play(p1,pos)
                else:
                    self.input_play(p2,pos)
                self.visited[pos]=pos
                i+=1
            if i==9: 
                break
            self.layout()
        print('GAME OVER')


if __name__=='__main__':
    p1 = input('Enter symbol for p1 ')
    p2 = input('Enter symbol for p2 ')
    game = tic_tak_tok(p1,p2)
    
    game.play()

