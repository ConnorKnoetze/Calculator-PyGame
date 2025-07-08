import pygame
import infixtopostfix
import postfixprocess
import os
import sys

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (20,20,20)
grey = (34,34,34)

sys.path.append(os.path.dirname(__file__))

class button():
    def __init__(self, symbol, coords):
        super().__init__()
        self.b_size = (125, 111.25)
        self.coords = coords
        self.symbol = symbol
        self.rect = pygame.Rect(coords[0]+5, coords[1] + 5, self.b_size[0] - 5, self.b_size[1] - 5)
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    return self.symbol
    
    def draw(self, win):
        font = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'fonts', 'FreeSansBold.ttf'), 32)
        M_text = font.render("{}".format(self.symbol), True, white, grey)
        M_textRect = M_text.get_rect()
        M_textRect.center = (self.coords[0]+(self.b_size[0] // 2 + 5), self.coords[1]+(self.b_size[1] // 2 + 5))
        pygame.draw.rect(win, grey, self.rect, 0,5)
        win.blit(M_text, M_textRect)

# Draw text
def draw_text(win, text):
    font = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'fonts', 'FreeSansBold.ttf'), 50)
    M_text = font.render(f"{text}", True, white, black)
    M_textRect = M_text.get_rect()
    M_textRect = (10,50)
    win.blit(M_text, M_textRect)

# Draw Display background
def b_display(win):
    t_rect = pygame.Rect((5,5),(490,145))
    b_rect = pygame.Rect((0,155), (500, 445))
    pygame.draw.rect(win,(black),t_rect, 0, 5)
    pygame.draw.rect(win,black,b_rect, 0, 5)

def init_buttons():
    symbols = ['0','1','2',
               '3','4','5',
               '6','7','8',
               '9','/','*',
               '-','+', 'C',
               '=']
    coords = [(125, 488.75),(0,377.5),(125,377.5),
              (250,377.5),(0,266.25),(125,266.25),
              (250, 266.25),(0, 155),(125, 155),
              (250, 155),(375,155),(375,266.25),
              (375,377.5),(375,488.75), (0,488.75),
              (250,488.75)]
    
    b_list = [button(symbols[i], coords[i]) for i in range(16)]
    return b_list

def process_op(equ):
    s = infixtopostfix.infixToPostfix(equ)
    final = postfixprocess.process(s)
    return final

win = pygame.display.set_mode((500, 600))
buttons_list = init_buttons()
running = True

input_string = ""
input_list = []
inp_stack = []
shift = False

while running:
    win.fill((0,0,0))
    b_display(win)
    if input_string != "":
        draw_text(win, input_string)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                shift = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                input_string = ""
                s = "".join([n for n in inp_stack])
                input_list.append(s)
                result = process_op(input_list)
                input_list = []
                inp_stack = []
                inp_stack.append(result)
                input_string = result
            elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                input_string += "0"
                inp_stack.append("0")
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                input_string += "1"
                inp_stack.append("1")
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                input_string += "2"
                inp_stack.append("2")
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                input_string += "3"
                inp_stack.append("3")
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                input_string += "4"
                inp_stack.append("4")
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                input_string += "5"
                inp_stack.append("5")
            elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                input_string += "6"
                inp_stack.append("6")
            elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                input_string += "7"
                inp_stack.append("7")
            elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                input_string += "8"
                inp_stack.append("8")
            elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                input_string += "9"
                inp_stack.append("9")
            elif event.key == pygame.K_MINUS:
                input_string += " {} ".format(" - ")
                s = "".join(inp_stack)
                input_list.append(s)
                input_list.append("-")
                inp_stack = []
            elif event.key == pygame.K_SLASH:
                input_string += " {} ".format(" / ")
                s = "".join(inp_stack)
                input_list.append(s)
                input_list.append("/")
                inp_stack = []
            elif shift and event.key == pygame.K_EQUALS:
                input_string += "{}".format(" + ")
                s = "".join(inp_stack)
                input_list.append(s)
                input_list.append("+")
                inp_stack = []
            elif shift and event.key == pygame.K_8:
                input_string += " {} ".format(" * ")
                s = "".join(inp_stack)
                input_list.append(s)
                input_list.append("*")
                inp_stack = []
            elif event.key == pygame.K_c:
                input_list = []
                inp_stack = []
                input_string = ""
            elif event.key == pygame.K_LSHIFT:
                shift = False
            elif event.key == pygame.K_BACKSPACE:
                if len(inp_stack) > 0:
                    input_string = input_string[:len(input_string)-1]
                    inp_stack.pop()
                else:
                    input_string = input_string[:len(input_string)-3]
                    input_list.pop()


    for but in buttons_list:
        but.draw(win)

    for but in buttons_list:
        ops = "-+*/"
        inp = but.update(events)
        if inp != None:
            if inp in ops:
                input_string += " {} ".format(inp)
            else:
                input_string += inp
        if inp != None and inp not in ops and inp != 'C' and inp != "=":
            inp_stack.append(inp)
        
        elif inp != None and inp in ops:
            s = "".join(inp_stack)
            input_list.append(s)
            input_list.append(inp)
            inp_stack = []
        
        elif inp != None and inp == 'C':
            input_list = []
            inp_stack = []
            input_string = ""
        elif inp != None and inp == "=":
            input_string = ""
            s = "".join([n for n in inp_stack])
            input_list.append(s)
            result = process_op(input_list)
            input_list = []
            inp_stack = []
            inp_stack.append(result)
            input_string = result


    pygame.display.update()

pygame.quit()