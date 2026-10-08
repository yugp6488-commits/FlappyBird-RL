import flappy_bird_gymnasium
import gymnasium
import pygame

env  = gymnasium.make("Flappybird-v0",render_mode = "human",use_lider=True)

obs, _ = env.reset()
done = False

pygame.init()
screen = pygame.display.get_surface()


while not done:
    action = 0
    for event in pygame.eveny.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                action = 1
    state,reward,done,truncated,info = env.step(action)
    env.render()

