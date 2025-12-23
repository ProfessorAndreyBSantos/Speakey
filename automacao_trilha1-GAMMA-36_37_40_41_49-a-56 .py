import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ==============================================================================
# 1. CONFIGURAÇÕES
# ==============================================================================
CAMINHO_PERFIL_ROBO = r"C:\ChromeAutomacao"
URL_ALVO = "https://gamma.app/create"

# --- SEUS TEXTOS ---
lista_conteudos = 
"""

"""
projetos = [bloco.strip() for bloco in lista_conteudos.split('###') if bloco.strip() != '']



# ==============================================================================
# 2. INICIALIZAÇÃO (CORRIGIDA PARA CHROMEBOOK)
# ==============================================================================
def get_driver():
    print("⚙️ Configurando Robô no Chromebook...")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    # Detecção automática de ambiente para definir os caminhos
    # Se estiver no Linux (Chromebook), usa os caminhos do sistema
    if os.name == 'posix': 
        CAMINHO_PERFIL_ROBO = os.path.join(os.getcwd(), "chromebook_profile")
        options.binary_location = "/usr/bin/chromium"
        service = Service("/usr/bin/chromedriver") # <--- O PULO DO GATO ESTÁ AQUI
    else:
        # Fallback para Windows (caso você rode no PC depois)
        CAMINHO_PERFIL_ROBO = r"C:\ChromeAutomacao"
        service = Service(ChromeDriverManager().install())

    options.add_argument(f"user-data-dir={CAMINHO_PERFIL_ROBO}")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") # Essencial para Chromebook
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    return webdriver.Chrome(service=service, options=options)

# ==============================================================================
# 3. AUTOMAÇÃO
# ==============================================================================
def run_automation():
    print("🚀 Iniciando Automação...")
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    for i, texto_aula in enumerate(projetos):
        print(f"\n🔹 --- PROJETO {i+1} de {len(projetos)} ---")
        
        try:
            # Garante que está na tela de criação
            if "create" not in driver.current_url:
                driver.get(URL_ALVO)
                time.sleep(3)
            
            # ---------------------------------------------------------
            # PASSO 1: CLICAR EM "RECOMBINAR UM MODELO"
            # Classe: css-x01ui3 | Texto: "Recombinar um modelo"
            # ---------------------------------------------------------
            print("   📍 Passo 1: Procurando 'Recombinar um modelo'...")
            try:
                # Tenta primeiro pelo TEXTO (Mais seguro e humano)
                botao_recombinar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Recombinar um modelo')]")))
                botao_recombinar.click()
                print("      ✅ Cliquei pelo Texto!")
            except:
                print("      ⚠️ Texto não achado, tentando pela Classe (.css-x01ui3)...")
                # Se falhar, tenta pela CLASSE específica que você passou
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-x01ui3"))).click()
                print("      ✅ Cliquei pela Classe!")

            # ---------------------------------------------------------
            # PASSO 2: SELECIONAR MODELO ESPECÍFICO
            # Classe: css-p9a4jz | Nome: "Modelo - Trilhas - Primeiro Modelo"
            # ---------------------------------------------------------
            print("   📍 Passo 2: Buscando 'Modelo - Trilhas - Primeiro Modelo'...")
            time.sleep(2)
            try:
                # Pega todos os cartões de modelo
                modelos = driver.find_elements(By.CSS_SELECTOR, ".css-p9a4jz")
                clicado = False
                
                # Procura qual deles tem o nome certo
                for modelo in modelos:
                    if "Trilhas" in modelo.text or "Primeiro Modelo" in modelo.text:
                        modelo.click()
                        clicado = True
                        print("      ✅ Modelo encontrado e selecionado!")
                        break
                
                # Plano B: Clica no primeiro disponível se não achar o nome
                if not clicado and len(modelos) > 0:
                    modelos[0].click()
                    print("      ⚠️ Nome exato não achado. Cliquei no 1º modelo disponível.")
                elif not clicado:
                    # Tenta clicar direto no seletor (se só houver um)
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-p9a4jz"))).click()
            
            except Exception as e:
                print(f"      ❌ Erro no Passo 2: {e}")


            # ---------------------------------------------------------
            # PASSO 3: COLAR TEXTO (OTIMIZADO COM JAVASCRIPT)
            # Classe: ProseMirror
            # ---------------------------------------------------------
            print("    📝 Passo 3: Colando texto (Modo Turbo)...")
            try:
                # 1. Localiza o editor
                editor = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ProseMirror")))
                editor.click()
                time.sleep(0.5)

                # 2. INJEÇÃO DIRETA DE JAVASCRIPT (Instantâneo)
                # Isso substitui o send_keys que estava travando seu Chromebook
                driver.execute_script("""
                    arguments[0].innerText = arguments[1];
                    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                """, editor, texto_aula)
                
                # 3. "Acordar" o site
                # Enviamos apenas um ESPAÇO físico para garantir que o Gamma perceba a mudança
                time.sleep(1)
                editor.send_keys(" ") 
                
                print("       ✅ Texto colado com sucesso!")

            except Exception as e:
                print(f"       ❌ Erro no Passo 3: {e}")            

            # ---------------------------------------------------------
            # PASSO EXTRA: GERAR
            # ---------------------------------------------------------
            print("   🚀 Clicando em Gerar...")
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1w21vqj"))).click()
            except:
                print("      (Botão Gerar já foi acionado ou não existe)")

            # ---------------------------------------------------------
            # PASSO 4: ESPERAR 3 MINUTOS
            # ---------------------------------------------------------
            print("   ⏳ Passo 4: Aguardando 3 minutos...")
            time.sleep(180)
            
            print("   🔄 Reiniciando ciclo...")
            driver.get(URL_ALVO)
            time.sleep(5)

        except Exception as e:
            print(f"❌ Erro crítico no projeto {i+1}: {e}")
            driver.get(URL_ALVO)
            time.sleep(5)
            continue

    print("\n✅ Finalizado!")

if __name__ == "__main__":
    run_automation()