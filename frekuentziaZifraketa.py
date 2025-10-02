from collections import Counter

frekuentziaNormala= ['E', 'A', 'O', 'S', 'R', 'N', 'I', 'D', 'L', 'C', 'U', 'T', 'M', 'P', 'B', 'V', 'G', 'H', 'F', 'Q', 'Y', 'Z', 'J', 'Ñ', 'X', 'K', 'W']

def frekuentziaBilatu (mezua):
    mezua = mezua.upper()
    letrak = [letra for letra in mezua if letra.isalpha()]
    frekuentzia= Counter(letrak)
    return frekuentzia

def mezuaDeszifratu(mezua, frekuentziaNormala, frekuentziaBerria):
    aldaketak={}
    for i in range(0,len(frekuentziaBerria)):
        aldaketak[frekuentziaBerria[i]]=frekuentziaNormala[i]
    mezuDeszifratua=[]
    for letra in mezua:
        if letra in aldaketak:
            letraBerria=aldaketak[letra]
            mezuDeszifratua.append(letraBerria)
        else:
            mezuDeszifratua.append(letra)
    return "".join(mezuDeszifratua)

def main():
    archivo=input("mezu zifratuaren .txt izena sartu \n")
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            mezua= f.read()
    except FileNotFoundError:
        print(f"{archivo} ez da aurkitu.")
        return
    frekuentzia=frekuentziaBilatu(mezua)
    print(frekuentzia)
    frekuentziaBerria=[par[0] for par in frekuentzia.most_common()]
    mezuDeszifratua=mezuaDeszifratu(mezua,frekuentziaNormala,frekuentziaBerria)
    print("\n Mezua: \n"+mezuDeszifratua)
    aldatzekoa=input("Sartu aldatu nahi duzun letra. Beztela enter sakatu \n").upper()
    while aldatzekoa!="":
        berria=input("Sartu zein letrarekin aldatu nahi duzun. Beztela enter sakatu \n").upper()
        if berria=="":
            break
        for i in range(0,len(frekuentziaNormala)):
            if frekuentziaNormala[i]==aldatzekoa:
                frekuentziaNormala[i]=berria
            elif frekuentziaNormala[i]==berria:
                frekuentziaNormala[i]=aldatzekoa
        mezuDeszifratua=mezuaDeszifratu(mezua,frekuentziaNormala,frekuentziaBerria)
        print("\n Mezua: \n"+mezuDeszifratua)
        aldatzekoa=input("Sartu aldatu nahi duzun letra. Beztela enter sakatu \n").upper()

if __name__ == "__main__":
    main()
