import pygame
import sys
import time

length = 20
tile_size = 30

pygame.init()

game_display = pygame.display.set_mode(((tile_size+2)*(length), (tile_size+2)*(length)))
pygame.display.set_caption("maze")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

x=2
y = 2

sqs = []
reds = []
sabz = []
wall = []
walls = []
start=[]
end=[]


for radif in range(length):
    x = 2
    for soton in range(length):
        sq= pygame.Rect(x, y, tile_size, tile_size)
        sqs.append(sq)
        x += tile_size + 2
    y += tile_size + 2


def show():
    for  sq in sqs:
        pygame.draw.rect(game_display, white, sq)


game_display.fill(black)
show()


def maze_solver(width, height, start, end, walls):

    maze = [[0] * width for _ in range(height)]

    for wall in walls:
        x, y = wall
        maze[y][x] = 1
    
    stack = [(start, [start])]
    
    while stack:
        (x, y), path = stack.pop()
        

        if (x, y) == end:
            return path
        
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx= x + dx
            ny =y + dy
            
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                maze[ny][nx] = 1
                

                stack.append(((nx, ny), path + [(nx, ny)]))
    print(path)

    return "not found....! error 404 "


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            for sq in sqs:
                if sq.collidepoint(pos):
                    if not reds:
                        start_sq=pygame.draw.rect(game_display,red,sq)
                        reds.append(sqs.index(sq))
                    elif not sabz:
                        end_sq=pygame.draw.rect(game_display,green,sq)
                        sabz.append(sqs.index(sq))
                    else:
                       
                        pygame.draw.rect(game_display,black,sq)
                        wall.append(sqs.index(sq))

                    
        if event.type == pygame.KEYDOWN:


            for e in reds:
                x=e%length
                y= int(e/length)
                start.append((x,y))
            for e in sabz:
                x=e%length
                y= int(e/length)
                end.append((x,y)) 
            for e in wall:
                x=e%length
                y= int(e/length)
                walls.append((x,y))       
            
            start = start[0]
            end = end[0]
            walls=walls
            path=maze_solver(length,length,start,end,walls)

            print('start is {0}'.format(start))
            print('end is {0}'.format(end))
            print('walls are {0}'.format(walls))
            print('path is {0}'.format(path))

            if type(path)!= str:
                for p in path:

                    if 0<path.index(p)<len(path)-1:
                        
                        time.sleep(0.1)
                        x1=path[path.index(p)][0]
                        y1=path[path.index(p)][1]
                        x=(tile_size+2)*( x1)+2
                        y=(tile_size+2)*( y1)+2
                        
                        p= pygame.Rect(x, y,tile_size, tile_size)
                        pygame.draw.rect(game_display,yellow,p)

                       
                        pygame.display.update()


    pygame.display.update()