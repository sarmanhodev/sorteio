import random
from flask import*

app = Flask(__name__, template_folder='template')



@app.route("/sorteio", methods=['GET', 'POST'])
def sorteio():
    if request.method == "POST":
        
        nome_participante = request.form['nome_participante'].upper()


        lista_participantes_consulta = open('nomes_participantes.txt','r')
        flag = 0
        index= 0

        for line in lista_participantes_consulta:
            index += 1

            if nome_participante in line:
                flag = 1
                break

        if flag == 0:
            lista_nomes = open('lista_nomes.txt', 'r')
            nomes =[]
            for linha in lista_nomes:
                linha = linha.strip()
                nomes.append(linha)
            lista_nomes.close()

            n = random.randrange(0,len(nomes)) #RANDOMIZA A CAPTURA DOS NOMES
            nome_sorteado = nomes[n] #VARIÁVEL QUE CAPTURA O NOME SORTEADO

            if nome_participante == nome_sorteado:
                print("Ops! Parece que você mesmo se sorteou. Tente novamente")
            else:
                #EXCLUINDO REGISTRO DO ARQUIVO TXT
                with open('lista_nomes.txt', 'r') as fr:
                    lines = fr.readlines()
            
                    with open('lista_nomes.txt', 'w') as fw:
                        for line in lines:
                            
                            
                            if line.strip('\n') != nome_sorteado:
                                fw.write(line)
                
                print(f"O(a) participante {nome_participante.upper()} sorteou o nome {nome_sorteado}")
                print(f"Registro deletado: {nome_sorteado}")

            
            lista_participantes = open('nomes_participantes.txt','a')
            lista_participantes.write("\n"+str(nome_participante)+"\n") #salva o nome do participante no arquivo nomes_participantes.txt
            lista_participantes.close()

            resultado = open('resultado_sorteio.txt','a')
            resultado.write("\n"+f"O(a) participante {nome_participante.upper()} sorteou o nome {nome_sorteado}"+"\n") 
            resultado.close()
            resultado_sorteio = f"O(a) participante {nome_participante.upper()} sorteou o nome {nome_sorteado}"
            return render_template("home.html", resultado_sorteio = resultado_sorteio)


        else:
            print(f"{nome_participante} já sorteou um nome")
            participante_repetido = f"{nome_participante} já sorteou um nome"
            return render_template("home.html", participante_repetido = participante_repetido)

        lista_participantes_consulta.close()
        



    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")