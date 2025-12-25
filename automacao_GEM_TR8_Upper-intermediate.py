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
8. Social English;Upper-Intermediate;01;Slang vs Jargon vs Dialect;Entender quando usar gíria.
###
8. Social English;Upper-Intermediate;02;Modern Slang: Positive Vibes;"Lit", "Fire", "Dope".
###
8. Social English;Upper-Intermediate;03;Modern Slang: Negative Vibes;"Shady", "Salty", "Cringe".
###
8. Social English;Upper-Intermediate;04;Slang for Agreement;"Bet", "For real".
###
8. Social English;Upper-Intermediate;05;Texting Slang (Advanced);"TL;DR", "IMO", "FOMO".
###
8. Social English;Upper-Intermediate;06;Dating Slang;"Ghosting", "Catfishing".
###
8. Social English;Upper-Intermediate;07;Friendship Slang;"Bestie", "Squad".
###
8. Social English;Upper-Intermediate;08;Idioms: The Body;"Cold shoulder", "Play it by ear".
###
8. Social English;Upper-Intermediate;09;Idioms: Food;"Piece of cake", "Spill the beans".
###
8. Social English;Upper-Intermediate;10;Idioms: Animals;"Elephant in the room".
###
8. Social English;Upper-Intermediate;11;Phrasal Verbs: Socializing;"Catch up", "Hang out".
###
8. Social English;Upper-Intermediate;12;Phrasal Verbs: Emotions;"Freak out", "Crack up".
###
8. Social English;Upper-Intermediate;13;Shortening Words;"Sec", "Fav", "Prob".
###
8. Social English;Upper-Intermediate;14;Filler Words (Native-like);"Like", "You know".
###
8. Social English;Upper-Intermediate;15;Vague Language (Advanced);"Thingy", "Ish".
###
8. Social English;Upper-Intermediate;16;Euphemisms (Polite Society);Falar de morte ou demissão suavemente.
###
8. Social English;Upper-Intermediate;17;Hyperbole in Daily Life;"It took forever".
###
8. Social English;Upper-Intermediate;18;Understatement (British Style);Dizer "It's a bit warm" no calor extremo.
###
8. Social English;Upper-Intermediate;19;Swearing & Taboo Language (Awareness);Entender níveis de ofensa.
###
8. Social English;Upper-Intermediate;20;Review: Slang Translator;Áudio consolidado: Traduzir frases para gíria.
###
8. Social English;Upper-Intermediate;21;Humor: The Pun (Wordplay);Entender jogos de palavras.
###
8. Social English;Upper-Intermediate;22;Humor: Dad Jokes;A estrutura da piada simples.
###
8. Social English;Upper-Intermediate;23;Humor: Self-Deprecation;Rir de si mesmo.
###
8. Social English;Upper-Intermediate;24;Humor: Delivery & Timing;A importância da pausa.
###
8. Social English;Upper-Intermediate;25;Humor: "Roasting" Friends;Insultar amigos como afeto.
###
8. Social English;Upper-Intermediate;26;Anecdotes: The "Embarrassing Story";Contar um mico.
###
8. Social English;Upper-Intermediate;27;Responding to a Joke;"That's hilarious".
###
8. Social English;Upper-Intermediate;28;When a Joke Fails (Awkward);O que dizer quando ninguém ri.
###
8. Social English;Upper-Intermediate;29;"Just kidding" / "Pulling your leg";Avisar que era brincadeira.
###
8. Social English;Upper-Intermediate;30;Observational Humor;"Have you ever noticed that...?".
###
8. Social English;Upper-Intermediate;31;Sarcasm Detection: Tone;Identificar tom sarcástico.
###
8. Social English;Upper-Intermediate;32;Sarcasm: "Yeah, right";Expressões de descrença.
###
8. Social English;Upper-Intermediate;33;Sarcasm: "Thanks a lot";Diferenciar gratidão de ironia.
###
8. Social English;Upper-Intermediate;34;Being Passive-Aggressive;Identificar frases como "Whatever you want".
###
8. Social English;Upper-Intermediate;35;The "Backhanded Compliment";Elogio que é insulto.
###
8. Social English;Upper-Intermediate;36;Subtext: The "Polite Refusal";Entender "Let's do coffee sometime" como Não.
###
8. Social English;Upper-Intermediate;37;Subtext: "It's interesting";Entender "Interesting" como estranho.
###
8. Social English;Upper-Intermediate;38;Subtext: Asking without Asking;"It's cold in here" = Feche a janela.
###
8. Social English;Upper-Intermediate;39;Cultural References (Pop Culture);Entender memes e filmes.
###
8. Social English;Upper-Intermediate;40;Review: The Comedy Club;Áudio consolidado: Contar uma história engraçada.
###
8. Social English;Upper-Intermediate;41;Double Entendre;Frases com duplo sentido.
###
8. Social English;Upper-Intermediate;42;Irony: Situational;Quando o oposto do esperado acontece.
###
8. Social English;Upper-Intermediate;43;Mocking (Playful vs Mean);Imitar alguém.
###
8. Social English;Upper-Intermediate;44;Banter (Witty Conversation);Troca rápida de provocações.
###
8. Social English;Upper-Intermediate;45;Handling Compliments (Modesty);"Oh, this old thing?".
###
8. Social English;Upper-Intermediate;46;Gossiping: The Code;"Keep it under your hat".
###
8. Social English;Upper-Intermediate;47;Ventilating / Ranting;Reclamar apaixonadamente.
###
8. Social English;Upper-Intermediate;48;Expressing Indifference;"I couldn't care less".
###
8. Social English;Upper-Intermediate;49;Expressing Skepticism;"Likely story".
###
8. Social English;Upper-Intermediate;50;Nuance: "Quiet" vs "Silent";Diferenças sutis de vocabulário.
###
8. Social English;Upper-Intermediate;51;Nuance: "Job" vs "Career";Diferenças de peso nas palavras.
###
8. Social English;Upper-Intermediate;52;Trigger Warnings & Sensitivity;Introduzir tópicos pesados.
###
8. Social English;Upper-Intermediate;53;Political Correctness (PC);Vocabulário inclusivo.
###
8. Social English;Upper-Intermediate;54;Cancel Culture Vocabulary;Termos como "Woke", "Call out".
###
8. Social English;Upper-Intermediate;55;Navigating Awkward Silences;Frases para quebrar o gelo.
###
8. Social English;Upper-Intermediate;56;Exit Strategies (Social);Sair de uma conversa chata.
###
8. Social English;Upper-Intermediate;57;The "Irish Goodbye";Sair sem se despedir.
###
8. Social English;Upper-Intermediate;58;Reading the Room;Perceber o clima social.
###
8. Social English;Upper-Intermediate;59;Code Switching;Mudar o jeito de falar.
###
8. Social English;Upper-Intermediate;60;Final Review: The Roast;Áudio consolidado: Discurso engraçado para um amigo.
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