import aiohttp
import asyncio
import json
import random
from colorama import Fore, Style, init
from pystyle import Colors, Center, Colorate, Write
import os
import ctypes
import re

init(autoreset=True)

def title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def repo(link):
    match = re.match(r"https://github\.com/([^/]+)/([^/]+)/issues", link)
    if match:
        owner, repo = match.groups()
        return f"https://api.github.com/repos/{owner}/{repo}/issues"
    else:
        return None

async def create(session, url, headers, payload):
    async with session.post(url, headers=headers, json=payload) as response:
        if response.status == 201:
            data = await response.json()
            number = data.get("number")
            print(
                f'{Fore.YELLOW}Successfully Created Issue Named: {Fore.BLUE + payload["title"]} '
                f"{Fore.RED}| {Fore.YELLOW}Issue Number: {Fore.GREEN + str(number)}"
            )
        else:
            print(
                f'{Fore.LIGHTRED_EX}Failed to create issue. Status Code: "{Fore.RED + str(response.status)}"'
            )
            print(await response.text())

async def spam(target, total):
    if "\x61\x73\x74\x72\x61\x70\x79" in target:
        return

    with open("config.json") as config_file:
        config = json.load(config_file)
    names = config.get("names", ["default"])
    tokens = config.get("tokens", ["token"])

    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(total):
            name = random.choice(names)
            token = random.choice(tokens)

            if target.startswith("https://github.com"):
                url = repo(target)
            else:
                url = target
            if url is None:
                print(f"{Fore.LIGHTRED_EX}Invalid GitHub link: {Fore.RED + target}")
                return
            payload = {"title": name, "body": "Issue created using GitHub API"}

            headers = {
                "Authorization": f"Token {token}",
                "Accept": "application/vnd.github.v3+json",
            }

            print(
                f"{Fore.CYAN}Creating Issue With Name: {Fore.BLUE + name} {Fore.RED}| {Fore.CYAN}Token Using: {Fore.BLUE + token}"
            )

            tasks.append(create(session, url, headers, payload))
        await asyncio.gather(*tasks)
    print(
        f"\n{Fore.GREEN}Successfully Opened {Fore.MAGENTA}[{total}] {Fore.GREEN}Issues For: {Fore.MAGENTA}{target}\n"
    )

if __name__ == "__main__":
    clear_console()
    title("Astra Github Issuer Spam")
    banner = Center.XCenter(
        """
    _______       _____                   ________                                 
    ___    |________  /_____________ _    ____  _/_________________  ______________
    __  /| |_  ___/  __/_  ___/  __ `/     __  / __  ___/_  ___/  / / /  _ \_  ___/
    _  ___ |(__  )/ /_ _  /   / /_/ /     __/ /  _(__  )_(__  )/ /_/ //  __/  /    
    /_/  |_/____/ \__/ /_/    \__,_/      /___/  /____/ /____/ \__,_/ \___//_/     
                                                                               
                    Made By astra.py | Discord discord.gg/A5XW5RwMM4
                        Use Multiple Tokens To Be More Effective\n      
    """
    )
    print(Colorate.Vertical(Colors.red_to_purple, banner, 2))
    target = input(
        f"{Fore.MAGENTA}┌──({Fore.BLUE}Astra@Root{Fore.MAGENTA}) ~ {Fore.MAGENTA}[{Fore.RED}Ϟ{Fore.MAGENTA}]\n"
        f"{Fore.MAGENTA}|{Fore.CYAN}[{Fore.MAGENTA}GitHub Target{Fore.CYAN}]\n"
        f"{Fore.MAGENTA}└─> {Fore.WHITE}"
    )

    clear_console()
    title("Astra Github Issuer Spam")
    banner = Center.XCenter(
        """
    _______       _____                   ________                                 
    ___    |________  /_____________ _    ____  _/_________________  ______________
    __  /| |_  ___/  __/_  ___/  __ `/     __  / __  ___/_  ___/  / / /  _ \_  ___/
    _  ___ |(__  )/ /_ _  /   / /_/ /     __/ /  _(__  )_(__  )/ /_/ //  __/  /    
    /_/  |_/____/ \__/ /_/    \__,_/      /___/  /____/ /____/ \__,_/ \___//_/     
                                                                               
                    Made By astra.py | Discord discord.gg/A5XW5RwMM4
                        Use More Tokens To Be More Effective\n      
    """
    )
    print(Colorate.Vertical(Colors.red_to_purple, banner, 2))

    total = int(
        input(
            f"{Fore.MAGENTA}┌──({Fore.BLUE}Astra@Root{Fore.MAGENTA}) ~ {Fore.MAGENTA}[{Fore.RED}Ϟ{Fore.MAGENTA}]\n"
            f"{Fore.MAGENTA}|{Fore.CYAN}[{Fore.MAGENTA}Issues To Create{Fore.CYAN}]\n"
            f"{Fore.MAGENTA}└─> {Fore.WHITE}"
        )
    )

    asyncio.run(spam(target, total))

# Any suggestion, join the discord an create an /suggestion: https://discord.gg/baMAyb4jeG
