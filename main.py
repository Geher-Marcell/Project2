from tkinter import ttk
import customtkinter
from PIL import Image
import pygame
import pygame.locals
import random

customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.resizable(False, False)

window_height = 450
window_width = 450

root.geometry(f"{window_height}x{window_width}")

root.title("Tamagotchi")

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(padx=20, pady=10, fill="both", expand=True)

my_image = customtkinter.CTkImage(Image.open("tamagotchi1.png"), size=(100, 100))
my_image2 = customtkinter.CTkImage(Image.open("tamagotchi2.png"), size=(100, 100))
my_image3 = customtkinter.CTkImage(Image.open("tamagotchi3.png"), size=(100, 100))
my_image4 = customtkinter.CTkImage(Image.open("hamburger.jpg"), size=(100, 100))
my_image5 = customtkinter.CTkImage(Image.open("halfHamburger.jpg"), size=(100, 100))


def tab1():
    def tab2(text1: str):
        label1.destroy()
        label2.destroy()
        text.destroy()
        button1.destroy()

        # 36. sor
        def tab3(karakter: str):
            label3.destroy()
            labelanyad.destroy()
            bbutton.destroy()
            bbutton1.destroy()
            bbutton2.destroy()

            def tab4(Ehseg: ttk.Progressbar):
                label_karakter.destroy()
                label_elet.destroy()
                Elet.destroy()
                label_ehseg.destroy()
                label_kedv.destroy()
                Kedv.destroy()
                buttonElet.destroy()
                buttonEhseg.destroy()
                buttonKedv.destroy()

                karakter1 = customtkinter.CTkLabel(master=frame1, text="" + karakter, font=("Roboto", 30))
                karakter1.pack(padx=10, pady=10)
                kaja = customtkinter.CTkButton(master=frame1, text="", image=my_image4, font=("Roboto", 30), command=lambda: Ehseg.step(19))
                Ehseg.step(19)
                kaja.pack(padx=10, pady=10)
                if True:
                    kaja.destroy()
                    jolLakott = customtkinter.CTkLabel(master=frame1, text="Tele vagyok!", font=("Roboto", 30))
                    jolLakott.pack(padx=10, pady=10)

            if karakter == "kutya":
                label_karakter = customtkinter.CTkLabel(master=frame1, image=my_image, text="", font=("Roboto", 30))
                label_karakter.pack(padx=10, pady=10)
            elif karakter == "macska":
                label_karakter = customtkinter.CTkLabel(master=frame1, image=my_image2, text="", font=("Roboto", 30))
                label_karakter.pack(padx=10, pady=10)
            elif karakter == "anyud":
                label_karakter = customtkinter.CTkLabel(master=frame1, image=my_image3, text="", font=("Roboto", 30))
                label_karakter.pack(padx=10, pady=10)
            label_elet = customtkinter.CTkLabel(master=frame1, text="Élet: ", font=("Roboto", 15))
            label_elet.pack(padx=10, pady=3)
            Elet = ttk.Progressbar(master=frame1, length=100)
            Elet.step(22)
            Elet.pack(padx=10, pady=10)

            label_ehseg = customtkinter.CTkLabel(master=frame1, text="Éhség: ", font=("Roboto", 15))
            label_ehseg.pack(padx=10, pady=3)
            Ehseg = ttk.Progressbar(master=frame1, length=100)
            Ehseg.step(22)
            Ehseg.pack(padx=10, pady=10)

            label_kedv = customtkinter.CTkLabel(master=frame1, text="Kedv: ", font=("Roboto", 15))
            label_kedv.pack(padx=10, pady=3)
            Kedv = ttk.Progressbar(master=frame1, length=100)
            Kedv.step(22)
            Kedv.pack(padx=10, pady=10)
            print(Kedv["value"])

            buttonElet = customtkinter.CTkButton(master=frame1, text="Simogatás", width=120, height=30, command=lambda: Elet.step(19))
            buttonElet.pack(padx=10, pady=5, side="left")
            buttonEhseg = customtkinter.CTkButton(master=frame1, text="Megetetés", width=120, height=30, command=lambda: tab4(Ehseg))
            buttonEhseg.pack(padx=10, pady=5, side='right')
            buttonKedv = customtkinter.CTkButton(master=frame1, text="Játék állatoddal", width=120, height=30, command=lambda: auto(Kedv))
            buttonKedv.pack(padx=10, pady=5, side="right")

        label3 = customtkinter.CTkLabel(master=frame1, text="Az állatod neve: " + text1, font=("Roboto", 30))
        label3.pack(padx=10, pady=10)
        labelanyad = customtkinter.CTkLabel(master=frame1, text="Válaszd ki a karaktered: ", font=("Roboto", 30))
        labelanyad.pack(padx=10, pady=10)

        bbutton = customtkinter.CTkButton(master=frame1, image=my_image, text="", width=30, fg_color="transparent", command=lambda: tab3("kutya"))
        bbutton.pack(padx=10, pady=10, side="left")
        bbutton1 = customtkinter.CTkButton(master=frame1, image=my_image2, text="", width=30, fg_color="transparent", command=lambda: tab3("macska"))
        bbutton1.pack(padx=10, pady=10, side="right")
        bbutton2 = customtkinter.CTkButton(master=frame1, image=my_image3, text="", width=30, fg_color="transparent", command=lambda: tab3("anyud"))
        bbutton2.pack(padx=10, pady=10, side="right")

    label1 = customtkinter.CTkLabel(master=frame1, text="Szia, üdv a játékunkban!", font=("Roboto", 30))
    label1.pack(padx=10, pady=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Nevezd el az állatod!", font=("Roboto", 30))
    label2.pack(padx=10, pady=10)

    text = customtkinter.CTkEntry(master=frame1, width=200, justify="center", font=("Roboto", 15))
    text.pack(padx=10, pady=10)

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30, command=lambda: tab2(text.get()))
    button1.pack(padx=10, pady=5)


def auto(Kedv: ttk.Progressbar):
    pygame.init()

    # create the window
    width = 500
    height = 500
    screen_size = (width, height)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Car Game')

    # colors
    gray = (100, 100, 100)
    green = (76, 208, 56)
    red = (200, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 232, 0)

    # road and marker sizes
    road_width = 300
    marker_width = 10
    marker_height = 50

    # lane coordinates
    left_lane = 150
    center_lane = 250
    right_lane = 350
    lanes = [left_lane, center_lane, right_lane]

    # road and edge markers
    road = (100, 0, road_width, height)
    left_edge_marker = (95, 0, marker_width, height)
    right_edge_marker = (395, 0, marker_width, height)

    # for animating movement of the lane markers
    lane_marker_move_y = 0

    # player's starting coordinates
    player_x = 250
    player_y = 400

    # frame settings
    clock = pygame.time.Clock()
    fps = 120

    # game settings
    gameover = False
    speed = 2
    score = 0

    class Vehicle(pygame.sprite.Sprite):

        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)

            # scale the image down so it's not wider than the lane
            image_scale = 45 / image.get_rect().width
            new_width = image.get_rect().width * image_scale
            new_height = image.get_rect().height * image_scale
            self.image = pygame.transform.scale(image, (new_width, new_height))

            self.rect = self.image.get_rect()
            self.rect.center = [x, y]

    class PlayerVehicle(Vehicle):

        def __init__(self, x, y):
            image = pygame.image.load('images/car.png')
            super().__init__(image, x, y)

    # sprite groups
    player_group = pygame.sprite.Group()
    vehicle_group = pygame.sprite.Group()

    # create the player's car
    player = PlayerVehicle(player_x, player_y)
    player_group.add(player)

    # load the vehicle images
    image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
    vehicle_images = []
    for image_filename in image_filenames:
        image = pygame.image.load('images/' + image_filename)
        vehicle_images.append(image)

    # load the crash image
    crash = pygame.image.load('images/crash.png')
    crash_rect = crash.get_rect()

    # game loop
    running = True
    while running:

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # move the player's car using the left/right arrow keys
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and player.rect.center[0] > left_lane:
                    player.rect.x -= 100
                elif event.key == pygame.K_RIGHT and player.rect.center[0] < right_lane:
                    player.rect.x += 100

                # check if there's a side swipe collision after changing lanes
                for vehicle in vehicle_group:
                    if pygame.sprite.collide_rect(player, vehicle):

                        gameover = True

                        # place the player's car next to other vehicle
                        # and determine where to position the crash image
                        if event.key == pygame.K_LEFT:
                            player.rect.left = vehicle.rect.right
                            crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                        elif event.key == pygame.K_RIGHT:
                            player.rect.right = vehicle.rect.left
                            crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

        # draw the grass
        screen.fill(green)

        # draw the road
        pygame.draw.rect(screen, gray, road)

        # draw the edge markers
        pygame.draw.rect(screen, yellow, left_edge_marker)
        pygame.draw.rect(screen, yellow, right_edge_marker)

        # draw the lane markers
        lane_marker_move_y += speed * 2
        if lane_marker_move_y >= marker_height * 2:
            lane_marker_move_y = 0
        for y in range(marker_height * -2, height, marker_height * 2):
            pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

        # draw the player's car
        player_group.draw(screen)

        # add a vehicle
        if len(vehicle_group) < 2:

            # ensure there's enough gap between vehicles
            add_vehicle = True
            for vehicle in vehicle_group:
                if vehicle.rect.top < vehicle.rect.height * 1.5:
                    add_vehicle = False

            if add_vehicle:

                # select a random lane
                lane = random.choice(lanes)

                # select a random vehicle image
                image = random.choice(vehicle_images)
                vehicle = Vehicle(image, lane, height / -2)
                vehicle_group.add(vehicle)

        # make the vehicles move
        for vehicle in vehicle_group:
            vehicle.rect.y += speed

            # remove vehicle once it goes off screen
            if vehicle.rect.top >= height:
                vehicle.kill()

                # add to score
                score += 1

                # speed up the game after passing 5 vehicles
                if score > 0 and score % 5 == 0:
                    speed += 1

        # draw the vehicles
        vehicle_group.draw(screen)

        # display the score
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Score: ' + str(score), True, white)
        text_rect = text.get_rect()
        text_rect.center = (50, 400)
        screen.blit(text, text_rect)

        # check if there's a head on collision
        if pygame.sprite.spritecollide(player, vehicle_group, True):
            gameover = True
            crash_rect.center = [player.rect.center[0], player.rect.top]

        # display game over
        if gameover:
            screen.blit(crash, crash_rect)

            pygame.draw.rect(screen, red, (0, 50, width, 100))

            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render('Game over. Play again? (Enter Y or N)', True, white)
            text_rect = text.get_rect()
            text_rect.center = (width / 2, 100)
            screen.blit(text, text_rect)

        pygame.display.update()

        # wait for user's input to play again or exit
        while gameover:

            clock.tick(fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameover = False
                    running = False

                # get the user's input (y or n)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        # reset the game
                        gameover = False
                        speed = 2
                        score = 0
                        vehicle_group.empty()
                        player.rect.center = [player_x, player_y]
                    elif event.key == pygame.K_n:
                        # exit the loops
                        gameover = False
                        running = False
                    if Kedv["value"] + score > 100:
                        Kedv["value"] = 100
                    else:
                        Kedv["value"] += score
                        score = 0

    pygame.quit()


tab1()
root.mainloop()
