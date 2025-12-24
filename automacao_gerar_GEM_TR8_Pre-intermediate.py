import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# ==============================================================================
# 1. CONFIGURAÇÕES & DADOS
# ==============================================================================

# IMPORTANTE: No Chromebook (Linux), não usamos "C:\". 
# Usamos o caminho relativo ou absoluto do Linux.
# O perfil será criado na pasta onde o script estiver rodando.
CAMINHO_PERFIL_ROBO = os.path.join(os.getcwd(), "chromebook_profile")

# URL do Gemini
URL_ALVO = "https://gemini.google.com/app"

# --- SEUS TEXTOS (INSIRA AQUI O CONTEÚDO SEPARADO POR ###) ---
lista_conteudos = """
8. Social English;Pre-Intermediate;01;Expanding Likes: "I enjoy...";Usar variações como "I enjoy", "I love".
###
8. Social English;Pre-Intermediate;02;Expanding Dislikes: "I can't stand...";Expressar desagrado forte.
###
8. Social English;Pre-Intermediate;03;Music Genres & Preferences;Discutir tipos de música.
###
8. Social English;Pre-Intermediate;04;Movies & TV Shows Types;Vocabulário de gêneros (Action, Comedy).
###
8. Social English;Pre-Intermediate;05;Discussing a Movie Plot;Descrever a história de um filme.
###
8. Social English;Pre-Intermediate;06;Sports: "Play" vs "Go" vs "Do";Usar o verbo correto.
###
8. Social English;Pre-Intermediate;07;Talking about Gym/Fitness;Vocabulário de exercício.
###
8. Social English;Pre-Intermediate;08;Reading & Books;Falar sobre hábitos de leitura.
###
8. Social English;Pre-Intermediate;09;Video Games & Gaming;Vocabulário básico de jogos.
###
8. Social English;Pre-Intermediate;10;Cooking as a Hobby;Falar sobre cozinhar por prazer.
###
8. Social English;Pre-Intermediate;11;Outdoor Activities;Hiking, Camping, Fishing.
###
8. Social English;Pre-Intermediate;12;Describing Talent: "I am good at...";Falar sobre habilidades naturais.
###
8. Social English;Pre-Intermediate;13;Frequency Adverbs (Position);Colocar "Always", "Often" no lugar certo.
###
8. Social English;Pre-Intermediate;14;"How often do you...?";Perguntar a frequência de atividades.
###
8. Social English;Pre-Intermediate;15;Expression: "Once/Twice a week";Definir frequência numérica.
###
8. Social English;Pre-Intermediate;16;Shopping for Fun;Vocabulário de compras.
###
8. Social English;Pre-Intermediate;17;Eating Out: Types of Restaurants;Fast food, Fine dining.
###
8. Social English;Pre-Intermediate;18;Describing Food Taste;Spicy, Sweet, Salty.
###
8. Social English;Pre-Intermediate;19;Recommending Things;"You should try...", "I recommend...".
###
8. Social English;Pre-Intermediate;20;Review: My Perfect Weekend;Áudio consolidado: Descrever um fim de semana ideal.
###
8. Social English;Pre-Intermediate;21;Making Suggestions: "Let's...";Sugerir uma atividade.
###
8. Social English;Pre-Intermediate;22;Making Suggestions: "Why don't we...?";Propor planos.
###
8. Social English;Pre-Intermediate;23;Inviting Someone: "Do you want to...?";O convite direto informal.
###
8. Social English;Pre-Intermediate;24;Inviting Someone: "Would you like to...?";O convite mais polido.
###
8. Social English;Pre-Intermediate;25;Accepting an Invitation;"Sure, I'd love to!".
###
8. Social English;Pre-Intermediate;26;Refusing Politely;"I'm sorry, I can't".
###
8. Social English;Pre-Intermediate;27;Giving an Excuse;"I have to work".
###
8. Social English;Pre-Intermediate;28;Arranging a Time;"What time shall we meet?".
###
8. Social English;Pre-Intermediate;29;Arranging a Place;"Where should we meet?".
###
8. Social English;Pre-Intermediate;30;Changing Plans (Canceling);Desmarcar ou reagendar.
###
8. Social English;Pre-Intermediate;31;Running Late;Avisar que vai atrasar.
###
8. Social English;Pre-Intermediate;32;At a Party: Introductions;Apresentar um amigo a outro.
###
8. Social English;Pre-Intermediate;33;At a Party: Small Talk;"How do you know the host?".
###
8. Social English;Pre-Intermediate;34;Offering Food/Drink (Host);"Can I get you something?".
###
8. Social English;Pre-Intermediate;35;Asking for the Bathroom;"Where is the restroom?".
###
8. Social English;Pre-Intermediate;36;Complimenting;"I like your dress".
###
8. Social English;Pre-Intermediate;37;Responding to Compliments;"Thank you, I bought it at...".
###
8. Social English;Pre-Intermediate;38;Asking for Contact Info;"What is your Instagram?".
###
8. Social English;Pre-Intermediate;39;Saying Goodbye (Social);"It was nice seeing you".
###
8. Social English;Pre-Intermediate;40;Review: Making Plans;Áudio consolidado: Combinar um jantar.
###
8. Social English;Pre-Intermediate;41;Talking about Last Weekend;Usar o Passado Simples.
###
8. Social English;Pre-Intermediate;42;"How was it?" (Opinions);Perguntar sobre eventos passados.
###
8. Social English;Pre-Intermediate;43;Talking about Holidays;Christmas, New Year.
###
8. Social English;Pre-Intermediate;44;Birthday Vocabulary;Cake, Gift, Party.
###
8. Social English;Pre-Intermediate;45;Describing a Past Trip;"I traveled to...", "I stayed at...".
###
8. Social English;Pre-Intermediate;46;Means of Transport (Travel);By plane, By train.
###
8. Social English;Pre-Intermediate;47;At the Airport: Basic;Check-in, Boarding.
###
8. Social English;Pre-Intermediate;48;At the Hotel: Basic;Check-in, Room key.
###
8. Social English;Pre-Intermediate;49;Sightseeing Vocabulary;Take photos, Visit museums.
###
8. Social English;Pre-Intermediate;50;Souvenirs & Gifts;Comprar lembranças de viagem.
###
8. Social English;Pre-Intermediate;51;Future Plans: "Going to";Falar sobre planos concretos.
###
8. Social English;Pre-Intermediate;52;Future Plans: "Want to";Falar sobre desejos.
###
8. Social English;Pre-Intermediate;53;New Year's Resolutions;Falar sobre metas pessoais.
###
8. Social English;Pre-Intermediate;54;Describing a Friend;Falar sobre a aparência e personalidade.
###
8. Social English;Pre-Intermediate;55;Social Media Vocabulary;Post, Like, Share.
###
8. Social English;Pre-Intermediate;56;Texting Abbreviations;LOL, OMG, BTW.
###
8. Social English;Pre-Intermediate;57;Expressing Feelings: Happy/Sad;"I feel happy when...".
###
8. Social English;Pre-Intermediate;58;Expressing Feelings: Excited/Bored;"I am bored" vs "It is boring".
###
8. Social English;Pre-Intermediate;59;Giving Advice (Simple);Usar "You should...".
###
8. Social English;Pre-Intermediate;60;Final Review: Social Story;Áudio consolidado: Contar o que fez nas férias.
"""

# Separa os blocos e remove vazios
projetos = [bloco.strip() for bloco in lista_conteudos.split('###') if bloco.strip() != '']

# ==============================================================================
# 2. INICIALIZAÇÃO DO CHROMIUM
# ==============================================================================
def get_driver():
    print("⚙️ Configurando Chromium no Chromebook...")
    
    options = Options()
    # Mantém o navegador aberto após o script (opcional, mas bom para debug)
    options.add_experimental_option("detach", True)
    
    # Configura o perfil de usuário para salvar login (se necessário futuramente)
    options.add_argument(f"user-data-dir={CAMINHO_PERFIL_ROBO}")
    
    # Ajustes para rodar liso no ambiente Linux/Container
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # --- PONTO CRÍTICO PARA CHROMEBOOK ---
    # O Selenium precisa saber onde está o executável do Chromium.
    # Geralmente em: /usr/bin/chromium ou /usr/bin/google-chrome
    # Se der erro, verifique rodando 'which chromium' no terminal.
    options.binary_location = "/usr/bin/chromium" 

    try:
        # Tenta usar o gerenciador automático
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"⚠️ Erro no Manager, tentando driver padrão do sistema Linux: {e}")
        # Fallback para o driver instalado via apt (sudo apt install chromium-driver)
        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

    return driver

# ==============================================================================
# 3. AUTOMAÇÃO
# ==============================================================================
def run_automation():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    # 1. Abrir o site (Chromium já abriu no get_driver)
    print(f"🌍 Navegando para {URL_ALVO}...")
    driver.get(URL_ALVO)

    # 2 e 3. Esperar interação do usuário
    print("\n" + "="*50)
    print("🛑 PAUSA DE 1 MINUTO")
    print("👉 Por favor, faça login (se necessário) e selecione a conversa alvo.")
    print("⏳ Aguardando 60 segundos...")
    print("="*50 + "\n")
    
    time.sleep(60) # Pausa solicitada de 1 minuto

    print("🚀 Iniciando envio dos prompts...")

    for i, texto in enumerate(projetos):
        print(f"\n🔹 Enviando Prompt {i+1} de {len(projetos)}...")
        
        try:
            # 4. Encontrar a caixa de texto
            # O seletor abaixo busca pela DIV editável (role="textbox") que é mais estável que classes dinâmicas
            caixa_texto = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='textbox']")))
            
            # Limpa (por segurança) e Cola o texto
            # Nota: send_keys direto costuma funcionar melhor que CTRL+V em containers Linux, 
            # mas se o texto for muito grande, o script colará caractere por caractere.
            caixa_texto.send_keys(texto)
            
            # 5. Esperar 2 segundos e Apertar Enter
            time.sleep(2)
            caixa_texto.send_keys(Keys.ENTER)
            print("   ✅ Texto enviado (Enter pressionado).")

            # Nota sobre o botão: Você forneceu o seletor do botão, mas pediu para apertar ENTER.
            # O Enter é mais seguro. Se preferir clicar, descomente as linhas abaixo:
            # botao_enviar = driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Envi']")
            # botao_enviar.click()

            # 6. Esperar 65 segundos para a resposta
            if i < len(projetos) - 1: # Só espera se não for o último
                print("   ⏳ Aguardando 65 segundos para a resposta do Gemini...")
                time.sleep(65)
            else:
                print("   🏁 Último prompt enviado.")

        except Exception as e:
            print(f"❌ Erro ao processar o item {i+1}: {e}")
            continue

    print("\n✅ Automação Finalizada!")

if __name__ == "__main__":
    run_automation()