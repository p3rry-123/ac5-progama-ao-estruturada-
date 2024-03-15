import random
def main():
    
    #aventureio
    vida_aventureio = 100
    ataque_aventureio = random.randint (10,20)
    defesa_aventureio = random.randint (1,5)
    #monstro
    vida_monstro = random.randint (60,80)
    ataque_monstro = random.randint (20,30)
    #exibir atributos
    print("atributos aventureio")
    print("vida", vida_aventureio)
    print("ataque aventureio ", ataque_aventureio)
    print("defesa aventureio ", defesa_aventureio )
   
    print("\natributos monstro") 
    print("vida", vida_monstro)
    print("ataque", ataque_monstro)

    Rodada=1 
    while vida_aventureio > 0 and vida_monstro > 0 :
        print("\nRodada",Rodada, ":" )
        #Aventureiro ataque do monstro
        dano_aventureio = random.randint (1, ataque_aventureio)
        vida_monstro -= dano_aventureio
        print(" O aventureiro ataca o monstro causando" , dano_aventureio , "de dano")
        if vida_monstro <=0 :
            print(" O monstro morreu! ")
            break
            #monstro ataca aventureio
        dano_monstro= random.randint (1,ataque_monstro) - defesa_aventureio
        
        if dano_monstro < 0 :
            dano_monstro = 0 
        vida_aventureio -= dano_monstro
        print("O monstro ataca o aventureiro causando", dano_monstro, "de dano.")
        
        if vida_aventureio<=0 :
            print("o aventureio morreu",)
            print("vida do monstro", vida_monstro)
            break

        Rodada=Rodada+1
        print("Aventureiro: vida",vida_aventureio, "- att ", ataque_aventureio, "-def", defesa_aventureio)
        print("Monstro: vida", vida_monstro, "- att", ataque_monstro)
        
main()