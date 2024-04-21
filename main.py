import os
import requests
import subprocess


def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def change_registry(reg_file_path):
    subprocess.run(['regedit', '/s', reg_file_path], check=True)
    os.remove(reg_file_path)


def launch_game(steam_path, game_path):
    if os.path.exists(steam_path):
        subprocess.Popen([steam_path, '-applaunch', '1568590'])
    else:
        subprocess.Popen(game_path)


def main():
    # Измените значения steam_path и game_folder_path на расположение
    # директорий Steam'а и игры "Goose Goose Duck" соответственно
    steam_path = r'C:\Program Files (x86)\Steam\steam.exe'
    game_folder_path = r'E:\SteamLibrary\steamapps\common\Goose Goose Duck'

    game_path = os.path.join(game_folder_path, 'GooseGooseDuck.exe')
    reg_file_url = (r'https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export'
                    r'=download&authuser=0&confirm=t&uuid=bbfd56aa-0434-431c-8f5c-f87a6fe991e3&at=APZUnTU'
                    r'-snZPlITAuTFIRZDbO9P5%3A1713175933486')
                    
    reg_file_path = os.path.join(game_folder_path, 'settings.reg')
    download_file(reg_file_url, reg_file_path)

    change_registry(reg_file_path)

    launch_game(steam_path, game_path)


if __name__ == '__main__':
    main()
