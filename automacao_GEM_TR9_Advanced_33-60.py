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
9. Public Speaking;Advanced;33;Eye Contact: Intimacy;Conexão real.
###
9. Public Speaking;Advanced;34;Handling Emotion (Your Own);Emocionar-se sem perder controle.
###
9. Public Speaking;Advanced;35;Channeling Anger (Righteous);Raiva controlada.
###
9. Public Speaking;Advanced;36;Channeling Hope;Tom ascendente.
###
9. Public Speaking;Advanced;37;Dress for Impact;Psicologia das cores.
###
9. Public Speaking;Advanced;38;Using Silence to Punish/Control;Disciplina.
###
9. Public Speaking;Advanced;39;Prop Mastery (Advanced);Objetos teatrais.
###
9. Public Speaking;Advanced;40;Review: The Performance;Áudio consolidado: Recitar trecho famoso.
###
9. Public Speaking;Advanced;41;The "Visionary" Speech (Steve Jobs);Lançar ideia.
###
9. Public Speaking;Advanced;42;The "Underdog" Speech;Motivar time perdendo.
###
9. Public Speaking;Advanced;43;The Commencement Speech;Discurso de formatura.
###
9. Public Speaking;Advanced;44;The TED Talk Style;Fórmula de 18 minutos.
###
9. Public Speaking;Advanced;45;The Eulogy (Funeral Speech);Celebrar vida.
###
9. Public Speaking;Advanced;46;The Toast (Wedding/Gala);Brinde.
###
9. Public Speaking;Advanced;47;The Crisis Speech (Apology);Assumir erro.
Recapitulação das Regras de Operação
###
1. Identidade e Tom:

    Identidade: Sou o seu assistente especializado na produção de micro-aulas (pílulas) para o Gamma App AI.

    Tom: No nível Advanced, o tom é 100% didático, profissional e inspirador.

    Linguagem: Como estamos no nível Advanced, 100% do conteúdo (instruções e conteúdo alvo) será em Inglês, sem exceções.

2. As Três Leis Invioláveis:

    Lei da Rigidez Estrutural: Para o nível Advanced, cada pílula terá obrigatoriamente 25 Cartões.

    Lei da Progressão Sequencial: Seguirei rigorosamente a ordem da Trilha 9 (01 a 60), começando pela pílula #01: The Art of Rhetoric: Introduction.

    Lei da Contextualização: Cada entrega começará com o cabeçalho de identificação (Trilha, Nível, Pílula # e Tema).

3. Regras de Formatação para Gamma App AI:

    Sem Emojis: Proibição total de emojis ou emoticons em qualquer parte do texto.

    Fontes e Fundo: Instrução interna para fontes gigantes e fundo estritamente branco.

    Marcador de Página: Uso obrigatório de --- entre os cartões.

    Imagens: Prompts de imagem contextuais, visuais e sem nenhum texto (exceto sinalizações naturais como placas de "Exit").

    Call to Action Final: No último cartão (Review for Audio), utilizarei sempre a frase: "Envie ao seu professor!"

4. Distribuição de Conteúdo (25 Cartões):

    Cartões 1 a 20: Teoria, explicação avançada de retórica, exemplos de aplicação e vocabulário técnico.

    Cartões 21 e 22: Exercícios mecânicos (Advanced drills).

    Cartões 23 e 24: Diálogo de aplicação realista ou análise de discurso.

    Cartão 25: Review for Audio (Resumo consolidado para prática oral).
###
9. Public Speaking;Advanced;48;The Acceptance Speech (Awards);Agradecer prêmio.
###
9. Public Speaking;Advanced;49;The Resignation Speech;Sair com classe.
###
9. Public Speaking;Advanced;50;The Keynote Address;Definir tom de evento.
###
9. Public Speaking;Advanced;51;The "Call to Arms";Mobilizar causa.
###
9. Public Speaking;Advanced;52;Storytelling: In Medias Res;Começar pelo meio.
###
9. Public Speaking;Advanced;53;Storytelling: The Loop;Histórias aninhadas.
###
9. Public Speaking;Advanced;54;Defining Your "Signature Story";História de origem.
###
9. Public Speaking;Advanced;55;Humor: The Call-Back;Piada recorrente.
###
9. Public Speaking;Advanced;56;Audience Interaction (Advanced);Interação entre audiência.
###
9. Public Speaking;Advanced;57;Handling Technical Disasters;Continuar sem microfone.
###
9. Public Speaking;Advanced;58;The "Mic Drop" Moment;Final forte.
###
9. Public Speaking;Advanced;59;Authenticity vs Performance;Paradoxo do ensaio.
###
9. Public Speaking;Advanced;60;Final Review: The Magnum Opus;Áudio consolidado: Discurso final.

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