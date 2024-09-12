import tkinter as tk
import subprocess

# Variáveis globais para processos e entradas
script_process = None

# Função para rodar o script de força bruta com parâmetros
# Função para rodar o script de força bruta com parâmetros
def run_force_bruta(url, username):
    global script_process
    if url and username:
        # Substitui pelo comando correto do script de força bruta
        command = f"python3 InvadeScripts/forca_bruta/forcaBruta.py {url} {username}; exec bash"
        script_process = subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c', command])
    else:
        print("Preencha todos os campos antes de iniciar o script!")

def run_sniffing():
    global script_process
    command = f"sudo python3 InvadeScripts/sniffing/snif.py; exec bash"
    script_process = subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c', command])

def run_DoS():
    global script_process
    command = f"python3 InvadeScripts/DoS/DoS.py; exec bash"
    script_process = subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c', command])

# Função para rodar os outros scripts (como o servidor)
def run_script(script_name):
    global script_process
    # Abre o script em um novo terminal (funciona no Linux e macOS)
    script_process = subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'python3', script_name])
    
    # Se estiver no Windows, use o comando abaixo:
    # script_process = subprocess.Popen(['start', 'cmd', '/k', 'python', script_name + ' & exit'], shell=True)

def DoS():
    # Ocultar elementos da tela principal
    clear_main_screen()

    global texto1, texto2, texto3, texto4
    texto1 = tk.Label(root, text="Esse ataque tem como objetivo deixar algo inoperante")
    texto1.pack(pady=10)
    texto2 = tk.Label(root, text="Abre o servidor web, e comece a abrir abas de ataque")
    texto2.pack(pady=10)
    texto3 = tk.Label(root, text="Quanto mais abas voce abrir mais voce vai notar o servidor enfraquecendo")
    texto3.pack(pady=10)
    texto4 = tk.Label(root, text="Legal voce ir visualizando pelo consele cada novo terminal aberto")
    texto4.pack(pady=10)


    # Botão para iniciar o site/server
    start_button = tk.Button(root, text="Servidor para DoS", command=lambda: run_script('InvadeScripts/DoS/db.py'))
    start_button.pack(pady=10)

    # Botão para iniciar o script
    start_button = tk.Button(root, text="Iniciar DoS (abra quantas vezes quiser)", command=lambda: run_DoS())
    start_button.pack(pady=10)

    # Botão para voltar à tela anterior
    back_button = tk.Button(root, text="Voltar", command=back_to_scripts_screen)
    back_button.pack(pady=10)

def Sniffing():
    # Ocultar elementos da tela principal
    clear_main_screen()

    global texto1, texto2, texto3, texto4
    texto1 = tk.Label(root, text="Esse ataque visa espionar o que o usuario esta fazendo")
    texto1.pack(pady=10)
    texto2 = tk.Label(root, text="Nesse caso voce ira espionar a si mesmo")
    texto2.pack(pady=10)
    texto3 = tk.Label(root, text="Deixei o mesmo servidor/site teste para voce abrir e visualizar espionar nele")
    texto3.pack(pady=10)
    texto4 = tk.Label(root, text="Porem sinta-se livre para abrir outros sites e ver o console te dando informacoes sobre o que voce esta fazendo")
    texto4.pack(pady=10)


    # Botão para iniciar o site/server
    start_button = tk.Button(root, text="Servidor para Sniffing", command=lambda: run_script('InvadeScripts/sniffing/website.py'))
    start_button.pack(pady=10)

    # Botão para iniciar o script
    start_button = tk.Button(root, text="Iniciar Sniffing", command=lambda: run_sniffing())
    start_button.pack(pady=10)

    # Botão para voltar à tela anterior
    back_button = tk.Button(root, text="Voltar", command=back_to_scripts_screen)
    back_button.pack(pady=10)

def SQL_screen():
    # Ocultar elementos da tela principal
    clear_main_screen()

    global texto1, texto2, texto3, texto4
    texto1 = tk.Label(root, text="Se voce ja iniciou o servidor web antes apenas entre la e tente invador")
    texto1.pack(pady=10)
    texto2 = tk.Label(root, text="Deixamos uma falha no codigo que permite a injecao de SQL, portanto tem 2 maneiras de acessar a pagina")
    texto2.pack(pady=10)
    texto3 = tk.Label(root, text="A primeira forma eh tendo o nome de usuario, voce coloca um codigo malicioso apos o nome que te permite logar com uma senha aleatoria")
    texto3.pack(pady=10)
    texto4 = tk.Label(root, text="A Segunda forma eh apenas utilizando o campo de login, sem necessariamente um usuario voce escrever um codigo que te de acesso")
    texto4.pack(pady=10)
    texto4 = tk.Label(root, text="Dica: de uma olhada no codigo de escrita do servidor web")
    texto4.pack(pady=10)


    # Botão para iniciar o script (inicialmente desabilitado)
    start_button = tk.Button(root, text="Servidor para SQL_INJECTION", command=lambda: run_script('InvadeScripts/SQL_Injection/db.py'))
    start_button.pack(pady=10)

    # Botão para voltar à tela anterior
    back_button = tk.Button(root, text="Voltar", command=back_to_scripts_screen)
    back_button.pack(pady=10)

# Função para a tela de Força Bruta
def forca_bruta_screen():
    # Ocultar elementos da tela principal
    clear_main_screen()

    global texto1, texto2, texto3
    texto1 = tk.Label(root, text="Insira o nome de usuario que deseja Hackear")
    texto1.pack(pady=10)
    texto2 = tk.Label(root, text="Insira o url da pagina exata de login")
    texto2.pack(pady=10)
    texto3 = tk.Label(root, text="Nao se esqueca de ativar o servidor de login no primeiro menu")
    texto3.pack(pady=10)

    # Criar novo layout da tela de Força Bruta
    url_label = tk.Label(root, text="URL:")
    url_label.pack(pady=5)
    url_entry = tk.Entry(root, width=40)
    url_entry.pack(pady=5)

    username_label = tk.Label(root, text="Username:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(root, width=40)
    username_entry.pack(pady=5)

    # Função interna para habilitar/desabilitar o botão de iniciar
    def check_entries(*args):
        if url_entry.get() and username_entry.get():
            start_button.config(state=tk.NORMAL)  # Habilita o botão
        else:
            start_button.config(state=tk.DISABLED)  # Desabilita o botão

    # Monitorar mudanças nas entradas
    url_entry.bind("<KeyRelease>", check_entries)
    username_entry.bind("<KeyRelease>", check_entries)

    # Botão para iniciar o script (inicialmente desabilitado)
    start_button = tk.Button(root, text="Area de login para testar o hack", command=lambda: run_script('InvadeScripts/forca_bruta/app.py'))
    start_button.pack(pady=10)

    # Botão para iniciar o script (inicialmente desabilitado)
    start_button = tk.Button(root, text="Iniciar Força Bruta", state=tk.DISABLED, command=lambda: run_force_bruta(url_entry.get(), username_entry.get()))
    start_button.pack(pady=10)

    # Botão para voltar à tela anterior
    back_button = tk.Button(root, text="Voltar", command=back_to_scripts_screen)
    back_button.pack(pady=10)

# Função para exibir os scripts
def forward():
    global script1_btn, script2_btn, script3_btn, script4_btn, button_back, label_text

    button_forward.pack_forget()  # Oculta o botão de avançar
    button_exit.pack_forget()  # Oculta o botão de sair

    # Adiciona o rótulo e os novos elementos da segunda tela
    label_text = tk.Label(root, text="Selecione um script para rodar:")
    label_text.pack(pady=10)

    script1_btn = tk.Button(root, text="Força Bruta", command=forca_bruta_screen)
    script1_btn.pack(pady=5)

    script2_btn = tk.Button(root, text="SQL Injection", command=SQL_screen)
    script2_btn.pack(pady=5)

    script3_btn = tk.Button(root, text="Sniffing", command=Sniffing)
    script3_btn.pack(pady=5)

    script4_btn = tk.Button(root, text="DoS (denial of service)", command=DoS)
    script4_btn.pack(pady=5)

    button_back = tk.Button(root, text="Voltar para tela inicial", command=back_to_main)
    button_back.pack(pady=5)

# Função para voltar à tela de seleção de scripts
def back_to_scripts_screen():
    clear_main_screen()
    forward()  # Retorna à tela de seleção de scripts

# Função para voltar à tela inicial
def back_to_main():
    clear_main_screen()
    show_main_screen()

# Função para limpar a tela atual
def clear_main_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

# Função para exibir a tela inicial
def show_main_screen():
    button_exit.pack(pady=5)
    button_forward.pack(pady=5)

# Criando a janela principal
root = tk.Tk()
root.title("Teste Ataques Insanos")
root.geometry("950x500")

# Botão para sair
button_exit = tk.Button(root, text="Sair", command=root.quit)
button_exit.pack(pady=5)

# Botão para avançar para a tela de scripts
button_forward = tk.Button(root, text="Ver Scripts maliciosos", command=forward)
button_forward.pack(pady=5)

# Exibindo a tela principal
show_main_screen()

# Iniciando o loop da interface
root.mainloop()
