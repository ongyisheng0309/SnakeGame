import tkinter
import random


row = 25
column = 25
tile_size = 25

window_height = column * tile_size
window_width = row * tile_size

#Tile(intialize)

class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False,False)

canvas = tkinter.Canvas(window,bg="black",width=window_width,height=window_height,borderwidth= 0,highlightthickness = 0)
canvas.pack()
window.update()


#center the window

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height  = window.winfo_screenheight()

window_x  = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


#intiliaze game
Snake = Tile(5*tile_size,5*tile_size) # Born at tile 5,5
Snake_body = [] 
Food = Tile(random.randint(1, 24)*tile_size,random.randint(1, 24)*tile_size)
velocity_x = 0
velocity_y = 0
gameover = False
score = 0

def change_direction(e):
    global velocity_x,velocity_y
    #print(e) print the event
    #print(e.keysym) print the event key
    if(gameover):
        return

    if (e.keysym == "Up" and velocity_y != 1): # cause if like u are going down u cannot go up
        velocity_x = 0
        velocity_y = -1

    elif (e.keysym == "Down" and velocity_y != -1):
        velocity_x = 0
        velocity_y = 1

    elif (e.keysym == "Right" and velocity_x != -1):
        velocity_x = 1
        velocity_y = 0

    elif (e.keysym == "Left" and velocity_x != 1):
        velocity_x = -1
        velocity_y = 0


    
def move():
    global Snake, Snake_body,gameover,score

    if(gameover):
        return

    if(Snake.x < 0 or Snake.x > window_width or Snake.y < 0 or Snake.y > window_height):
        gameover = True
        return
    
    for tile in Snake_body:
        if(Snake.x == tile.x and Snake.y == tile.y):
            gameover = True
            return
    #Eat Food
    if(Snake.x == Food.x and Snake.y == Food.y):
        Snake_body.append(Tile(Food.x,Food.y))
        Food.y = random.randint(1, 24)*tile_size
        Food.x = random.randint(1, 24)*tile_size
        score += 1


    # update body
    for i in range (len(Snake_body)-1 ,-1,-1):
        tile = Snake_body[i]
        if(i == 0):
            tile.x = Snake.x
            tile.y = Snake.y
        else:
            prev_tile = Snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    Snake.x += velocity_x *tile_size
    Snake.y += velocity_y*tile_size

def draw():
    global Snake


    move()
    canvas.delete("all")
    # first x and y is define the the left side , then behind should add the tile seize because our one tile seze equal = 25 need fill up all
    
    canvas.create_rectangle(Food.x,Food.y,Food.x +tile_size , Food.y +tile_size, fill=("RED")) 
    canvas.create_rectangle(Snake.x,Snake.y,Snake.x +tile_size , Snake.y +tile_size, fill=("white")) 

    for tile in Snake_body:
        canvas.create_rectangle(tile.x , tile.y , tile.x + tile_size, tile.y +tile_size,fill=("white"))


    if(gameover):
        canvas.create_text(window_width/2,window_height/2,font= "Arial 20", text= f"   GameOver \n Your Score : {score}",fill="Green")
    else:
        canvas.create_text(30,20,font= "Arial 10", text= f"Score : {score}", fill = "Green")

    window.after(100,draw)


draw()
window.bind("<Key>", change_direction)
window.mainloop()