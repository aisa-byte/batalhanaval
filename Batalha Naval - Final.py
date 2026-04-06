import pygame as pg   
import cores    

def main():
    pg.init()   

    tela = pg.display.set_mode((301, 631))       
    pg.display.set_caption("Batalha Naval")     
    tela.fill(cores.roxo)
    fonte = pg.font.SysFont("Comic Sans MS", 14)    

    cursor_img = pg.image.load('shipk.png').convert_alpha()
    cursor_img = pg.transform.smoothscale(cursor_img, (87, 27))
    sink_img = pg.image.load('sink.png').convert_alpha()
    sink_img = pg.transform.smoothscale(sink_img, (87, 27))
    bomb_img = pg.image.load('boom.png').convert_alpha()
    bomb_img = pg.transform.smoothscale(bomb_img, (28, 28))
    splash_img = pg.image.load('splash.png').convert_alpha()
    splash_img = pg.transform.smoothscale(splash_img, (28, 28))

    cursor = pg.cursors.Cursor((15, 15), cursor_img)
    pg.mouse.set_cursor(cursor)

    rodando = True
    p1rdy = False
    p2rdy = False
    tamcel = 30
    linhas = 10
    navios = [7, 7]
    turno = 0

    for linha in range(10):
        for coluna in range(10):
            pg.draw.rect(tela, cores.azulbb, ((coluna * 30) + 1, (linha * 30) + 1, 28, 28))
    for linha in range(10):
        for coluna in range(10):
            pg.draw.rect(tela, cores.azulbb, ((coluna * 30) + 1, (linha * 30) + 331, 28, 28))

    texto = fonte.render("^ Jogador 1, posicione os navios! ^",True,cores.rosabb)
    tela.blit(texto,(39, 305))

    pg.display.update()

    tab1 = [[None for i in range(linhas)] for j in range(linhas)]
    tab2 = [[None for i in range(linhas)] for j in range(linhas)]

    while rodando:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
    
            if navios[0] > 0 and navios[1] == 7 and turno == 0:
                mx,my = pg.mouse.get_pos()
                
                if mx >= 240 or my >= 300:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_NO)
                else:
                    pg.mouse.set_cursor(cursor)

                if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                    pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                    texto = fonte.render("^ Jogador 1, posicione os navios! ^",True, cores.rosabb)
                    tela.blit(texto,(39, 305))

                    cel_x = mx // tamcel
                    cel_y = my // tamcel
                    
                    if cel_x >= 8 or cel_y >= 10:
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("Posição inválida! Tente outro lugar!" ,True, cores.rosabb)
                        tela.blit(texto,(39, 305))
                        break 

                    if tab1[cel_y][cel_x] == tab1[cel_y][cel_x + 1] == tab1[cel_y][cel_x + 2] == None:
                        navios[0] -= 1
                        tab1[cel_y][cel_x] = "head"
                        tab1[cel_y][cel_x + 1] = "mid"
                        tab1[cel_y][cel_x + 2] = "tail"
                    
                    x, y = cel_x, cel_y

                    if (tab1[y][x] == "head" and tab1[y][x+1] == "mid" and tab1[y][x+2] == "tail" and tab1[y][x - 1] != "head" and tab1[y][x - 1] != "mid"):
                        tela.blit(cursor_img, (30*x + 1, 30*y + 1))

            elif navios[0] == 0 and navios[1] > 0 and not p1rdy:
                tela.fill(cores.roxo)
                texto = fonte.render("v Agora é a vez do 2º Jogador! v",True, cores.rosabb)
                tela.blit(texto,(39, 305))
            
                for linha in range(10):
                    for coluna in range(10):
                        pg.draw.rect(tela, cores.azulbb, ((coluna * 30) + 1, (linha * 30) + 1, 28, 28))
                for linha in range(10):
                    for coluna in range(10):
                        pg.draw.rect(tela, cores.azulbb, ((coluna * 30) + 1, (linha * 30) + 331, 28, 28))
            
                p1rdy = True
            
            if navios[0] == 0 and navios[1] > 0 and p1rdy:
                mx,my = pg.mouse.get_pos()

                if mx >= 240 or my <= 330:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_NO)
                else:
                    pg.mouse.set_cursor(cursor)

                if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                    pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                    texto = fonte.render("v Agora é a vez do 2º Jogador! v",True, cores.rosabb)
                    tela.blit(texto,(39, 305))

                    cel_x = mx // tamcel
                    cel_y = my // tamcel
                    
                    if cel_x >= 8 or cel_y <= 10:
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("Posição inválida! Tente outro lugar!" ,True, cores.rosabb)
                        tela.blit(texto,(39, 305))
                        break

                    if tab2[cel_y - 11][cel_x] == tab2[cel_y - 11][cel_x + 1] == tab2[cel_y - 11][cel_x + 2] == None:   
                        navios[1] -= 1

                        tab2[cel_y - 11][cel_x] = "head"
                        tab2[cel_y - 11][cel_x + 1] = "mid"
                        tab2[cel_y - 11][cel_x + 2] = "tail"
                    
                    x, y = cel_x, (cel_y - 11)
                    
                    if (tab2[y][x] == "head" and tab2[y][x+1] == "mid" and tab2[y][x+2] == "tail" and tab2[y][x - 1] != "head" and tab2[y][x - 1] != "mid"):
                        tela.blit(cursor_img, (30*x + 1, 30*(y + 11) + 1))
              
            elif navios[0] == navios[1] == turno == 0:
                tela.fill(cores.roxo)
                texto = fonte.render("v 1º Jogador, hora de atacar! v",True,cores.rosabb)
                tela.blit(texto,(52, 304))

                cursor = pg.cursors.Cursor((15, 15), bomb_img)
                pg.mouse.set_cursor(cursor)

                for linha in range(10):
                    for coluna in range(10):
                        pg.draw.rect(tela, cores.azulbb, ((coluna * 30) + 1, (linha * 30) + 1, 28, 28))
                for linha in range(10):
                    for coluna in range(10):
                        pg.draw.rect(tela, cores.azulbb, ((coluna * 30) + 1, (linha * 30) + 331, 28, 28)) 

                p2rdy = True
                navios = [7, 7]
                turno = 1

            if navios[1] > 0 and turno == 1:
                mx,my = pg.mouse.get_pos()

                if my < 300:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_NO)
                else:
                    pg.mouse.set_cursor(cursor)

                if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                    mx, my = evento.pos
                
                    cel_x = mx // tamcel
                    cel_y = my // tamcel

                    if cel_y <= 10 and turno == 1:
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("Posição inválida! Tente outro lugar!" ,True, cores.rosabb)
                        tela.blit(texto,(39, 305))
                        break

                    x, y = cel_x, (cel_y - 11)
                        
                    if tab2[y][x] == "head":
                        tab2[y][x] = "hit"
                        tab2[y][x + 1] = "hit"
                        tab2[y][x + 2] = "hit"
                        tela.blit(sink_img, (30*x + 1, 30*(y + 11) + 1))

                        pg.mixer.music.load("explosion.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render(f"v Jogue novamente! (Restam {navios[1]} navios!) v",True,cores.rosabb)
                        tela.blit(texto,(23, 305))

                        navios[1] -= 1
                        
                    elif tab2[y][x] == "mid":
                        tab2[y][x] = "hit"
                        tab2[y][x - 1] = "hit"
                        tab2[y][x + 1] = "hit"
                        tela.blit(sink_img, (30*x - 29, 30*(y + 11) + 1))

                        pg.mixer.music.load("explosion.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render(f"v Jogue novamente! (Restam {navios[1]} navios!) v",True,cores.rosabb)
                        tela.blit(texto,(23, 305))

                        navios[1] -= 1
                        
                    elif tab2[y][x] == "tail":
                        tab2[y][x] = "hit"
                        tab2[y][x - 1] = "hit"
                        tab2[y][x - 2] = "hit"
                        tela.blit(sink_img, (30*x - 59, 30*(y + 11) + 1))

                        pg.mixer.music.load("explosion.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render(f"v Jogue novamente! (Restam {navios[1]} navios!) v",True,cores.rosabb)
                        tela.blit(texto,(23, 305))

                        navios[1] -= 1

                    elif tab2[y][x] == None:
                        tab2[y][x] = "miss"
                        tela.blit(splash_img, (30*x, 30*(y + 11)))

                        pg.mixer.music.load("miss.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("^ Errou! Agora é a vez do 2º Jogador! ^",True,cores.rosabb)
                        tela.blit(texto,(22, 305))

                        turno = 2

                    elif tab2[y][x] == "hit" or tab2[y][x] == "miss":
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("v Você já atirou aqui! Tente outro lugar! v",True,cores.rosabb)
                        tela.blit(texto,(15, 305))

            elif navios[1] == 0 and turno == 1:
                pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                texto = fonte.render("v 1º Jogador, Você venceu! v",True,cores.rosabb)
                tela.blit(texto,(60, 305))     

                pg.mixer.music.load("applause.ogg")
                pg.mixer.music.play(1)

                turno = 3

            elif navios[0] > 0 and turno == 2:
                mx,my = pg.mouse.get_pos()

                if my >= 300:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_NO)
                else:
                    pg.mouse.set_cursor(cursor)

                if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                    mx, my = evento.pos
                
                    cel_x = mx // tamcel
                    cel_y = my // tamcel

                    if cel_y >= 10 and turno == 2:
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("Posição inválida! Tente outro lugar!" ,True, cores.rosabb)
                        tela.blit(texto,(39, 305))
                        break

                    x, y = cel_x, cel_y
                        
                    if tab1[y][x] == "head":
                        tab1[y][x] = "hit"
                        tab1[y][x + 1] = "hit"
                        tab1[y][x + 2] = "hit"
                        tela.blit(sink_img, (30*x + 1, 30*y + 1))

                        pg.mixer.music.load("explosion.ogg")
                        pg.mixer.music.play(1)
                        
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render(f"^ Jogue novamente! (Restam {navios[0]} navios!) ^",True,cores.rosabb)
                        tela.blit(texto,(23, 305))

                        navios[0] -= 1

                    elif tab1[y][x] == "mid":
                        tab1[y][x] = "hit"
                        tab1[y][x - 1] = "hit"
                        tab1[y][x + 1] = "hit"
                        tela.blit(sink_img, (30*x - 29, 30*y + 1))

                        pg.mixer.music.load("explosion.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render(f"^ Jogue novamente! (Restam {navios[0]} navios!) ^",True,cores.rosabb)
                        tela.blit(texto,(23, 305))

                        navios[0] -= 1

                    elif tab1[y][x] == "tail":
                        tab1[y][x] = "hit"
                        tab1[y][x - 1] = "hit"
                        tab1[y][x - 2] = "hit"
                        tela.blit(sink_img, (30*x - 59, 30*y + 1))

                        pg.mixer.music.load("explosion.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render(f"^ Jogue novamente! (Restam {navios[0]} navios!) ^",True,cores.rosabb)
                        tela.blit(texto,(23, 305))
                                                
                        navios[0] -= 1

                    elif tab1[y][x] == None:
                        tab1[y][x] = "miss"
                        tela.blit(splash_img, (30*x, 30*y))

                        pg.mixer.music.load("miss.ogg")
                        pg.mixer.music.play(1)

                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("v Errou! Agora é a vez do 1º Jogador! v",True,cores.rosabb)
                        tela.blit(texto,(22, 305))

                        turno = 1

                    elif tab1[y][x] == "hit" or tab1[y][x] == "miss":
                        pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                        texto = fonte.render("^ Você já atirou aqui! Tente outro lugar! ^",True,cores.rosabb)
                        tela.blit(texto,(15, 305))

            elif navios[0] == 0 and turno == 2:
                pg.draw.rect(tela, cores.roxo, (0, 300, 300, 30))
                texto = fonte.render("^ 2º Jogador, Você venceu! ^",True,cores.rosabb)
                tela.blit(texto,(60, 305))

                pg.mixer.music.load("applause.ogg")
                pg.mixer.music.play(1)

                turno = 3

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()