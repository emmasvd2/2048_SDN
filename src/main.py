#%%

import pygame
from classEcran import Ecran
from classGrille import Grille
from classJeu import Jeu
#import frontend  # Importer le module frontend

def main():
    FPS = 60
    # Initialisation de Pygame
    pygame.init()
    
    # Créer une instance de l'écran
    ecran = Ecran(800, 600, "2048 SDN")
    
    # Appel de la fonction main du fichier frontend pour l'authentification
    #user = frontend.main()  # Vérifie si l'authentification a réussi
    user = True

    if user:  # Si l'authentification a réussi
        jeu = Jeu(ecran,user)
        clock = pygame.time.Clock()  
        jeu.grille = Grille(4, 4, ecran)
        jeu.dessiner()
        jeu.tuile = jeu.genererTuile()
    
        
        
        # Boucle principale du jeu
        while True:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ecran.eteindre()  # Éteindre l'écran si la fenêtre est fermée
                    return
              
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ecran.eteindre()  # Éteindre l'écran si la touche Échap est pressée
                        return
                    if event.key == pygame.K_LEFT:
                        jeu.move_tiles(clock, "left")
                    if event.key == pygame.K_RIGHT:
                        jeu.move_tiles(clock, "right")
                    if event.key == pygame.K_UP:
                        jeu.move_tiles(clock, "up")
                    if event.key == pygame.K_DOWN:
                        jeu.move_tiles(clock, "down")
                    
               
            jeu.dessiner()

            
            
   
    
    pygame.quit()  # Quitter Pygame à la fin

if __name__ == "__main__":
    main()

# %%
