import os
import requests

def hex_to_ansi(hex_color: str, is_bg=False) -> str:
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"\033[{48 if is_bg else 38};2;{r};{g};{b}m"

RESET = "\033[0m"
WHITE = "\033[38;2;255;255;255m"
HEADER = hex_to_ansi("#b03030")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    deco = f"{HEADER}{'━' * 50}{RESET}"
    print(deco)
    print(f"{HEADER}Webhook Utilities V3{RESET}".center(50))
    print(deco)
    print(f"{WHITE}Original     @ Cattyn{RESET}")
    print(f"{WHITE}Improvements @ Simon{RESET}")
    print(f"{WHITE}Dedicated    @ DVRKZ{RESET}")
    print(deco)

def check_webhook(hook):
    try:
        resp = requests.get(hook)
        return None if resp.status_code == 404 or "Unknown Webhook" in resp.text else resp.json()
    except requests.RequestException:
        return None

def display_webhook_info(info):
    if not info:
        print(f"{HEADER}Invalid webhook{RESET}")
        return
    print(f"\n{HEADER}Webhook Information{RESET}")
    print(f"{HEADER}Name >{RESET} {WHITE}{info.get('name', '?')}{RESET}")
    print(f"{HEADER}Channel ID >{RESET} {WHITE}{info.get('channel_id', '?')}{RESET}")
    print(f"{HEADER}Server >{RESET} {WHITE}{info.get('guild_name', '?')}{RESET}")
    print(f"{HEADER}Server ID >{RESET} {WHITE}{info.get('guild_id', '?')}{RESET}\n")

def silent_takedown(url):
    try:
        requests.delete(url)
        print(f"{HEADER}Webhook silently deleted{RESET}")
    except requests.RequestException:
        print(f"{HEADER}[-] Silent delete failed{RESET}")

def obvious_spam(url, name, message, delay, amount):
    counter = 0
    while amount == "inf" or counter < int(amount):
        try:
            resp = requests.post(url, json={
                "content": message,
                "username": name,
                "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg"
            })
            status = f"{HEADER}[+] Sent{RESET}" if resp.status_code == 204 else f"{HEADER}[-] Fail{RESET}"
            print(status)
        except requests.RequestException:
            print(f"{HEADER}[-] Error{RESET}")
        counter += 1
 

def main_menu():
    banner()
    print(f"\n{HEADER}1.{RESET} {WHITE}Silent Takedown{RESET}")
    print(f"{HEADER}2.{RESET} {WHITE}Obvious Spam{RESET}")
    choice = input(f"\n{HEADER}Select mode >{RESET} {WHITE}").strip()
    print(RESET, end="")
    return choice

def main():
    mode = main_menu()
    webhook = input(f"\n{HEADER}Webhook URL >{RESET} {WHITE}").strip()
    print(RESET, end="")
    if not (info := check_webhook(webhook)):
        print(f"{HEADER}Invalid webhook{RESET}")
        return

    display_webhook_info(info)

    if mode == "1":
        silent_takedown(webhook)

    elif mode == "2":
        name = input(f"{HEADER}Webhook name >{RESET} {WHITE}").strip()
        message = input(f"{HEADER}Message >{RESET} {WHITE}").strip()
        delay = input(f"{HEADER}Delay >{RESET} {WHITE}").strip()
        amount = input(f"{HEADER}Amount [int/inf] >{RESET} {WHITE}").strip()
        delete_after = input(f"{HEADER}Delete webhook afterwards? (y/n) >{RESET} {WHITE}").strip().lower()
        print(RESET, end="")

        obvious_spam(webhook, name, message, delay, amount)

        if delete_after == "y":
            silent_takedown(webhook)

    else:
        print(f"{HEADER}Invalid mode selection{RESET}")
        return

    print(f"{HEADER}Operation completed{RESET}")


if __name__ == '__main__':
    main()
