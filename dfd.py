import pygame 
print("Start up")

pygame.init()
pygame.key.set_repeat(500,500) #키보드 반응 대기 시간
#처음 키보드 입력 후 500ms 대기
# 가로 640, 세로 480
surface = pygame.display.set_mode((640,480))
# 게임의 초당 프레임 수를 조절하기 위한 시계 객체를 생성
clock = pygame.time.Clock()

image = pygame.image.load("assets/images/fighter.png")
scale_up_image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height()* 2))
x = 640/2 - scale_up_image.get_width() / 2
y = 480 - scale_up_image.get_width() - 10
#메인 게임 루프
while True: 
    print("Update") # 루프가 정상적으로 돌아가는 지 확인
    # 사용자의 입력을 받아 처리하는 코드
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Shutdow")
            pygame.quit()
            exit()
            break
        print("render") #화면 그리기 출력

        surface.fill((0,0,0))
        #pygame.draw.rect(surface, (0,0,225),(10,10,100,100))
        surface.blit(scale_up_image, (x,y))
        pygame.display.update() #화면을 업데이트
        clock.tick(30)
