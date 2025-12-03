"""""
def worker(ip:str,id:int):
    ping_reussi=0
    total_ping=0

    cmd = os.popen(f"ping -c 2 {ip}")
    res = cmd.read()
    matchs = ping_regex.search(res)
    if int(matchs.group("res")) == 2:
        ping_reussi+=1
    else:
        total_ping+=1
    calcul=ping_reussi/total_ping
    proba={id:calcul}

    with open("dispo.json","a")as f:
        json.load(proba,f)
    """