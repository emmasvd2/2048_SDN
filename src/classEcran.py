import pygame

from classGrille import Grille

class Ecran:
    

    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        
        pygame.font.init()
        pygame.display.set_caption(self.titre)

    
    
    def afficherGrille(grille, ecran):
        grille.draw_grid(ecran)


        


    """
    Fonction Clear
        Elle permet d'enlver ce qui est afficher à l'écran
    Paramètres : 

    """

    """
    Fonction mettreAJour
        Elle permet de mettre à jour l'écran
    Paramètres:
    - aucun
    """
    def mettreAJour(self):
        pygame.display.update()
    
    """
    Fonction eteindre
        Elle permet d'éteindre l'écran
    Paramètres:
    - aucun
    """
    def eteindre(self):
        pygame.quit()