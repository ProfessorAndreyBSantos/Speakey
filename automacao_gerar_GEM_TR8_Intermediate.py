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
8. Social English;Intermediate;01;Asking for Opinions;"What do you reckon?".
###
8. Social English;Intermediate;02;Giving an Opinion: Weak;"I guess...", "I suppose...".
###
8. Social English;Intermediate;03;Giving an Opinion: Strong;"I’m convinced that...".
###
8. Social English;Intermediate;04;Agreeing: Total Agreement;"Absolutely!", "I couldn't agree more".
###
8. Social English;Intermediate;05;Agreeing: Partial Agreement;"You have a point, but...".
###
8. Social English;Intermediate;06;Disagreeing Politely;"I see what you mean, but...".
###
8. Social English;Intermediate;07;Disagreeing Strongly (Friends);"No way!", "You must be joking!".
###
8. Social English;Intermediate;08;The Phrase "It depends";Explicar que a resposta varia.
###
8. Social English;Intermediate;09;Clarifying Your Opinion;"What I meant was...".
###
8. Social English;Intermediate;10;Checking Understanding;"Does that make sense?".
###
8. Social English;Intermediate;11;Interrupting a Friend;"Can I just say something?".
###
8. Social English;Intermediate;12;Holding the Floor;Impedir interrupção ("Let me finish").
###
8. Social English;Intermediate;13;Changing the Subject;"By the way...".
###
8. Social English;Intermediate;14;Returning to the Topic;"Anyway, as I was saying...".
###
8. Social English;Intermediate;15;Ending a Topic;"Let's agree to disagree".
###
8. Social English;Intermediate;16;Expressing Surprise;"No kidding!", "Really?".
###
8. Social English;Intermediate;17;Expressing Disbelief;"I don't buy it".
###
8. Social English;Intermediate;18;Expressing Sympathy;"What a pity".
###
8. Social English;Intermediate;19;Expressing Relief;"Thank goodness".
###
8. Social English;Intermediate;20;Review: The Debate;Áudio consolidado: Discutir "Cães vs Gatos".
###
8. Social English;Intermediate;21;Talking about the News;"Did you hear about...?".
###
8. Social English;Intermediate;22;Headlines vs Articles;Entender a linguagem das manchetes.
###
8. Social English;Intermediate;23;Fake News & Rumors;Discutir veracidade ("Clickbait").
###
8. Social English;Intermediate;24;Social Media Trends;Falar sobre virais.
###
8. Social English;Intermediate;25;Celebrity News (Gossip);Falar sobre famosos.
###
8. Social English;Intermediate;26;Reporting Speech (Social);Contar o que alguém disse.
###
8. Social English;Intermediate;27;Discussing Movies (Reviews);Dar sua crítica de filme.
###
8. Social English;Intermediate;28;Discussing Series (Spoilers);Avisar antes de contar o final.
###
8. Social English;Intermediate;29;Discussing Music (Concerts);Falar sobre shows.
###
8. Social English;Intermediate;30;Discussing Podcasts;Recomendar conteúdo de áudio.
###
8. Social English;Intermediate;31;Topic: Climate Change (Social);Opiniões básicas sobre clima.
###
8. Social English;Intermediate;32;Topic: Technology Addiction;Opiniões sobre uso de celular.
###
8. Social English;Intermediate;33;Topic: Remote Work (Lifestyle);Discutir vantagens de trabalhar de casa.
###
8. Social English;Intermediate;34;Topic: Cost of Living;Reclamar de preços.
###
8. Social English;Intermediate;35;Topic: Healthy Living;Discutir dietas da moda.
###
8. Social English;Intermediate;36;Topic: Travel Experiences (Bad);Contar perrengues de viagem.
###
8. Social English;Intermediate;37;Topic: Generations;Gen Z vs Boomers.
###
8. Social English;Intermediate;38;Topic: Artificial Intelligence (Fears);Conversa sobre robôs e empregos.
###
8. Social English;Intermediate;39;Topic: Urban Living vs Countryside;Onde é melhor morar.
###
8. Social English;Intermediate;40;Review: Current Affairs;Áudio consolidado: Opinar sobre notícia recente.
###
8. Social English;Intermediate;41;Storytelling: Setting the Scene;"It was a dark night...".
###
8. Social English;Intermediate;42;Storytelling: Building Suspense;"And then, suddenly...".
###
8. Social English;Intermediate;43;Storytelling: The Climax;O ponto alto da história.
###
8. Social English;Intermediate;44;Storytelling: The Resolution;"In the end...".
###
8. Social English;Intermediate;45;Exaggeration (Hyperbole);"I told you a million times".
###
8. Social English;Intermediate;46;Vague Language;"And stuff like that".
###
8. Social English;Intermediate;47;Softening Criticism;"He's a bit...".
###
8. Social English;Intermediate;48;Giving Compliments (Personality);"You have such a great vibe".
###
8. Social English;Intermediate;49;Responding to Bad News;"That must be tough".
###
8. Social English;Intermediate;50;Encouraging Someone;"Hang in there".
###
8. Social English;Intermediate;51;Asking for Favors;"Could you do me a huge favor?".
###
8. Social English;Intermediate;52;Borrowing vs Lending;Pedir emprestado vs Emprestar.
###
8. Social English;Intermediate;53;Apologizing (Social);"My bad".
###
8. Social English;Intermediate;54;Forgiving;"No worries".
###
8. Social English;Intermediate;55;Dealing with misunderstandings;"We got crossed wires".
###
8. Social English;Intermediate;56;Discussing Plans (Hypothetical);"If I won the lottery...".
###
8. Social English;Intermediate;57;Regrets (Social);"I should have gone...".
###
8. Social English;Intermediate;58;Speculating about others;"They must be dating".
###
8. Social English;Intermediate;59;Gossip (Neutral);"Have you heard about...?".
###
8. Social English;Intermediate;60;Final Review: The Dinner Party;Áudio consolidado: Conversa de 3 minutos.
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