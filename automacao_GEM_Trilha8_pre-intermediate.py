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
8. Social English;Basic;01;Greetings & Farewells;Cumprimentar e se despedir informalmente.
###
8. Social English;Basic;02;"How are you?" Variations;Responder além do "I'm fine".
###
8. Social English;Basic;03;Introducing Yourself (Social);Dizer nome, idade e origem.
###
8. Social English;Basic;04;Immediate Family: Parents;Falar sobre pai e mãe.
###
8. Social English;Basic;05;Immediate Family: Siblings;Falar sobre irmãos e irmãs.
###
8. Social English;Basic;06;Immediate Family: Children;Falar sobre filhos.
###
8. Social English;Basic;07;Extended Family: Grandparents;Falar sobre avós.
###
8. Social English;Basic;08;Extended Family: Relatives;Falar sobre tios, tias e primos.
###
8. Social English;Basic;09;Marital Status;Dizer se é solteiro, casado ou divorciado.
###
8. Social English;Basic;10;Describing Appearance: Height/Weight;Usar adjetivos simples (Tall, Short).
###
8. Social English;Basic;11;Describing Appearance: Hair/Eyes;Descrever cor de cabelo e olhos.
###
8. Social English;Basic;12;Describing Personality: Positive;Usar adjetivos como Funny, Nice.
###
8. Social English;Basic;13;Describing Personality: Negative;Usar adjetivos como Shy, Lazy.
###
8. Social English;Basic;14;"How old are they?";Falar a idade de familiares.
###
8. Social English;Basic;15;Review: My Family Tree;Áudio consolidado: Apresentar 3 membros da família.
###
8. Social English;Basic;16;Days of the Week;Pronunciar corretamente de Monday a Sunday.
###
8. Social English;Basic;17;Parts of the Day;Morning, Afternoon, Evening, Night.
###
8. Social English;Basic;18;Telling Time: O'clock / Half past;Dizer as horas de forma simples.
###
8. Social English;Basic;19;Morning Routine verbs;Wake up, Get up, Shower.
###
8. Social English;Basic;20;Breakfast Vocabulary;Coffee, Bread, Eggs.
###
8. Social English;Basic;21;Commuting Verbs;Go to work, Drive, Take the bus.
###
8. Social English;Basic;22;Work/School Routine;Start work, Have lunch, Finish work.
###
8. Social English;Basic;23;Evening Routine verbs;Cook dinner, Watch TV.
###
8. Social English;Basic;24;Night Routine verbs;Go to bed, Sleep.
###
8. Social English;Basic;25;Weekends vs Weekdays;Diferenciar o que faz na semana e no fim de semana.
###
8. Social English;Basic;26;Frequency: Always / Usually;Dizer o que faz sempre ou geralmente.
###
8. Social English;Basic;27;Frequency: Sometimes / Never;Dizer o que faz às vezes ou nunca.
###
8. Social English;Basic;28;Connectors: Before / After;Organizar a sequência.
###
8. Social English;Basic;29;Connectors: Then / And then;Conectar ações.
###
8. Social English;Basic;30;Review: My Daily Routine;Áudio consolidado: Narrar sua rotina completa.
###
8. Social English;Basic;31;My House: Type;House vs Apartment.
###
8. Social English;Basic;32;Rooms: Living Room;Sofa, TV, Carpet.
###
8. Social English;Basic;33;Rooms: Kitchen;Fridge, Stove, Table.
###
8. Social English;Basic;34;Rooms: Bedroom;Bed, Wardrobe, Lamp.
###
8. Social English;Basic;35;Rooms: Bathroom;Shower, Toilet, Sink.
###
8. Social English;Basic;36;Prepositions of Place;In, On, Under, Next to.
###
8. Social English;Basic;37;Household Chores: Cleaning;Clean the house, Sweep.
###
8. Social English;Basic;38;Household Chores: Kitchen;Wash the dishes, Cook.
###
8. Social English;Basic;39;Household Chores: Laundry;Wash clothes, Iron.
###
8. Social English;Basic;40;"I have to..." (Obligation);Falar de deveres.
###
8. Social English;Basic;41;Food: Fruits & Vegetables;Vocabulário básico de feira.
###
8. Social English;Basic;42;Food: Meat & Carb;Chicken, Beef, Rice.
###
8. Social English;Basic;43;Meals of the Day;Breakfast, Lunch, Dinner.
###
8. Social English;Basic;44;"I am hungry / thirsty";Expressar necessidades físicas.
###
8. Social English;Basic;45;Review: My Home;Áudio consolidado: Descrever sua casa e comida.
###
8. Social English;Basic;46;Verb: Like / Don't like;Expressar gostos simples.
###
8. Social English;Basic;47;Verb: Love / Hate;Expressar gostos fortes.
###
8. Social English;Basic;48;Hobbies: Sports;Play soccer, Go to the gym.
###
8. Social English;Basic;49;Hobbies: Arts & Music;Listen to music, Watch movies.
###
8. Social English;Basic;50;"My favorite...";Falar sobre favoritos.
###
8. Social English;Basic;51;Weather: Hot / Cold;Descrever a temperatura.
###
8. Social English;Basic;52;Weather: Sunny / Rainy;Descrever o estado do céu.
###
8. Social English;Basic;53;Seasons of the Year;Summer, Winter, Fall, Spring.
###
8. Social English;Basic;54;Clothes: Summer;T-shirt, Shorts, Sandals.
###
8. Social English;Basic;55;Clothes: Winter;Coat, Jeans, Boots.
###
8. Social English;Basic;56;"I am wearing...";Descrever o que está vestindo.
###
8. Social English;Basic;57;Colors;Red, Blue, Green, Black.
###
8. Social English;Basic;58;Numbers: Age & Price;Revisão de números em contexto social.
###
8. Social English;Basic;59;Pets;Dog, Cat, Bird.
###
8. Social English;Basic;60;Final Review: Who Am I?;Áudio consolidado: Apresentação completa.
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
