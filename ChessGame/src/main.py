import os
import pygame

# Print the current working directory
print(os.getcwd())

# List all files in the assets directory
assets_path = 'C:/Users/Benja/OneDrive/Skole/DevRepos/Applications/ChessGame/assets'
print("Files in assets directory:", os.listdir(assets_path))

# Load the board image
board_img = pygame.image.load(os.path.join(assets_path, 'board.jpg'))
