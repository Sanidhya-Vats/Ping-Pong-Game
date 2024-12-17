
import pygame, sys,random

#Ball Animation
def ball_animation():
	global ball_speed_x, ball_speed_y,player2_score,player_score,score_time
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		pygame.mixer.Sound.play(pong_sound)
		ball_speed_y *= -1
	if ball.left <= 5 :
		pygame.mixer.Sound.play(score_sound)
		player_score +=1
		score_time=pygame.time.get_ticks()
	if ball.right >= screen_width-5:
		pygame.mixer.Sound.play(score_sound)
		player2_score +=1
		score_time=pygame.time.get_ticks()

	if ball.colliderect(player)and ball_speed_x>0:
		pygame.mixer.Sound.play(pong_sound)
		if abs(ball.right - player.left)< 5:
			ball_speed_x *= -1
	elif abs(ball.bottom -player.top)<2 and ball_speed_y> 0:
			ball_speed_y *= -1
	elif abs(ball.top -player.bottom)<2 and ball_speed_y< 0:
			ball_speed_y *= -1

	if ball.colliderect(player2)and ball_speed_x<0:
		pygame.mixer.Sound.play(pong_sound)
		if abs(ball.left - player2.right)< 5:
			ball_speed_x *= -1
	elif abs(ball.bottom -player2.top)<2 and ball_speed_y> 0:
		ball_speed_y *= -1
	elif abs(ball.top -player2.bottom)<2 and ball_speed_y< 0:
			ball_speed_y *= -1

#Player Animation
def player_animation():
	player.y += player_speed

	if player.top <= 10:
		player.top = 10
	if player.bottom >= screen_height-15:
		player.bottom = screen_height-15
def player2_animation():
	player2.y += player2_speed

	if player2.top<= 10:
		player2.top = 10
	if player2.bottom >= screen_height-15:
		player2.bottom = screen_height-15
  
# Counter 
def ball_start():
    global ball_speed_x,ball_speed_y,score_time
    
    current_time= pygame.time.get_ticks()
    if 2100<current_time <2700:
        pygame.mixer.Sound.play(pong_sound)
        start_text =game_font2.render("Start",False,blue)
        screen.blit(start_text,(screen_width/2-95,screen_height/2-45))
    ball.center= (screen_width/2,screen_height/2)
    ball_speed_x = 8* random.choice((1,-1))
    ball_speed_y = 8* random.choice((1,-1))    
    if current_time-score_time <700:
        pygame.mixer.Sound.play(score_sound)
        number_three =game_font2.render("3",False,red)
        screen.blit(number_three,(screen_width/2-20,screen_height/2-35)) 
    if 700<current_time-score_time <1400:
        pygame.mixer.Sound.play(score_sound)
        number_three =game_font2.render("2",False,red)
        screen.blit(number_three,(screen_width/2-20,screen_height/2-35))   
    if 1400<current_time-score_time <2100:
        pygame.mixer.Sound.play(score_sound)
        number_three =game_font2.render("1",False,red)
        screen.blit(number_three,(screen_width/2-20,screen_height/2-35))
    if current_time-score_time <2700:
        ball_speed_x,ball_speed_y=0,0
    else:
        ball_speed_x = 8 * random.choice((1,-1))
        ball_speed_y = 8 * random.choice((1,-1))
        score_time = None
    

# General setup
pygame.mixer.pre_init(44100,-16,8,4096)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1500
screen_height = 760
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong')

# Colors
white = (255,255,255)
greenmat = (61, 86, 86)
red=(255,0,0)
blue=(0,0,255)


# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 40, screen_height / 2 - 70, 20,140)
player2 = pygame.Rect(20, screen_height / 2 - 70, 20,140)

# Game Variables
ball_speed_x = 8 *random.choice((1,-1))
ball_speed_y = 8 *random.choice((1,-1))
player_speed = 0
player2_speed = 0

# Text Variable
player_score = 0
player2_score =0
game_font =pygame.font.Font("freesansbold.ttf",40)
game_font2 =pygame.font.Font("freesansbold.ttf",80)

# Timer
score_time= True

# Sound
pong_sound =pygame.mixer.Sound("pong.ogg")
score_sound =pygame.mixer.Sound("score.ogg")

# Game Logic
 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 8
			if event.key == pygame.K_DOWN:
				player_speed += 8
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 8
			if event.key == pygame.K_DOWN:
				player_speed -= 8
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player2_speed -= 8
			if event.key == pygame.K_s:
				player2_speed += 8
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player2_speed += 8
			if event.key == pygame.K_s:
				player2_speed -= 8
	
	ball_animation()
	player_animation()
	player2_animation()
	

	# Visuals
	screen.fill(greenmat)
	pygame.draw.rect(screen, red, player)
	pygame.draw.rect(screen, blue, player2)
	pygame.draw.ellipse(screen, white, ball)
	pygame.draw.line(screen, white, (screen_width / 2, 0),(screen_width / 2, screen_height),width=6)
	pygame.draw.circle(screen, white, (screen_width/2,screen_height/2),100,width=6)
	pygame.draw.line(screen, white, (2,0),(2, screen_height),width=6)	
	pygame.draw.line(screen, white, (screen_width,2),(0,2 ),width=6)	
	pygame.draw.line(screen, white, (0,screen_height-5),(screen_width-5,screen_height-5),width=6)	
	pygame.draw.line(screen, white, (screen_width-4,0),(screen_width-4,screen_height-4),width=6)	
 
	if score_time:
		ball_start()
  
	player_text =game_font.render(f"{player_score}",False,white)
	screen.blit(player_text,(screen_width/2-55,screen_height/2-20))
	player_text =game_font.render(f"{player2_score}",False,white)
	screen.blit(player_text,(screen_width/2+35,screen_height/2-20))
# Update the Window
	pygame.display.flip()
	clock.tick(60)
