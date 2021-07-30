import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

script_version = "4.0.0"


def progressBar():
    animation = [
        "[□□□□□□□□□□]",
        "[■□□□□□□□□□]",
        "[■■□□□□□□□□]",
        "[■■■□□□□□□□]",
        "[■■■■□□□□□□]",
        "[■■■■■□□□□□]",
        "[■■■■■■□□□□]",
        "[■■■■■■■□□□]",
        "[■■■■■■■■□□]",
        "[■■■■■■■■■□]",
    ]
    progress_anim = 0
    save_anim = animation[progress_anim % len(animation)]
    percent = 0
    while True:
        for i in range(10):
            percent += 1
            sys.stdout.write(
                f"\r[+] Waiting response...  " + save_anim + f" {percent}%"
            )
            sys.stdout.flush()
            time.sleep(0.075)
        progress_anim += 1
        save_anim = animation[progress_anim % len(animation)]
        if percent == 100:
            sys.stdout.write("\r[+] Request completed... [■■■■■■■■■■] 100%")
            break


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return "".join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return "".join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


def run(referrer):
    url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"
    try:
        install_id = genString(22)
        body = {
            "key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES",
        }
        data = json.dumps(body).encode("utf8")
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print("")
        print(error)


def main(idWarp):
    g = 0
    b = 0
    r = 0
    
    while True:
        z = 0
        while z <= 100: 
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\t\t\tWARP-PLUS-CLOUDFLARE (script)\n")
            print(f"[+] Buff for ID: {idWarp}")
            print(f"[+] Total: {g} Good - {b} Bad")
            print(f"[+] Number of Auto-Restart: {r}\n")
            # print(f"int: {z}")
            print("------------------------------------------------------\n")
            
            sys.stdout.write("\r[+] Sending request...   [□□□□□□□□□□] 0%")
            sys.stdout.flush()
            result = run(idWarp)
            
            if result == 200:
                g += 1
                progressBar()
                print(f"\n[+] {g} GB has been successfully added to your account.")

                for i in range(18, 0, -1):
                    sys.stdout.write(
                        f"\r[*] After {i} seconds, a new request will be sent."
                    )
                    sys.stdout.flush()
                    time.sleep(1)
            else:
                b += 1
                print("[:(] Error when connecting to server.")
                for i in range(20, 0, -1):
                    sys.stdout.write(f"\r[*] Retrying in {i}s...")
                    sys.stdout.flush()
                    time.sleep(1)
            z += 1
            
        for i in range(10, 0, -1):
            sys.stdout.write(f"\r[*] Restart after {i} seconds")
            sys.stdout.flush()
            time.sleep(1)
        r += 1


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]")
    print("[+]                                                         [+]")
    print("[+]             Script get unlimited GB on Warp+            [+]")
    print(f"[+]                       Version: {script_version}\t\t    [+]")
    print("[+]                                                         [+]")
    print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]\n")

    lst_id_key = [
        {
            "id": "1d9d520d-a0ef-4846-99ab-d0d561daf6e1",
            "key": "VZ723kC0-69OJLl87-t48Q1H0V",
        },
        {
            "id": "26f7ea47-ffc2-4776-b30b-4c0408bcf43e",
            "key": "cgs9h603603-5R46mfa0-x852dGU1",
        },
    ]

    print("The available ID of the list:\n")
    for i in range(0, len(lst_id_key)):
        print(
            "[-] ID {2}: {0}\n[-] Key: {1}\n".format(
                lst_id_key[i]["id"], lst_id_key[i]["key"], i
            )
        )

    print("\n[+] Number -1 to enter ID from keyboard")

    select = int(input("[#] Select number ID: "))
    if select == -1:
        os.system("cls" if os.name == "nt" else "clear")
        _id = input("Enter ID: ")
        main(_id)
    else:
        main(lst_id_key[select]["id"])
