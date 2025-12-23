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
lista_conteudos = """
Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 36 Tema Central: Resolving Misunderstandings
Resolving Misunderstandings: "Let me clarify"

Objetivo: Aprender a corrigir mal-entendidos sem ser rude. Você descobrirá como dizer "não foi isso que eu quis dizer", como reformular frases confusas e como usar expressões idiomáticas para descrever falhas de comunicação.

Falar uma segunda língua gera confusões. O segredo não é evitar erros, mas saber consertá-los rapidamente e com elegância.
The Core Phrase: "That's not what I meant"

Esta é a frase mais direta e útil quando a outra pessoa interpreta algo totalmente diferente do que você falou.

Estrutura:

    "Sorry, that's not what I meant." (Desculpe, não foi isso que eu quis dizer).

    "Actually, that's not exactly what I meant." (Mais suave).

Use isso imediatamente para interromper a confusão.
The Fix: "Let me rephrase"

Depois de dizer que houve um erro, você precisa explicar de novo, mas com outras palavras.

Frases:

    "Let me rephrase that." (Deixe-me reformular isso).

    "Let me put it another way." (Deixe-me colocar de outra forma).

Isso mostra que você está se esforçando para ser claro, tirando a culpa do ouvinte.
Identifying the Issue: "A Misunderstanding"

Evite dizer "You didn't understand" (Soa como "Você é burro"). Use a forma substantiva para culpar a situação.

Frase:

    "I think there has been a misunderstanding." (Acho que houve um mal-entendido).

    "There seems to be a mix-up." (Informal, bom para reservas/horários).

Idiom: Crossed Wires / Mixed Up

Usado quando duas pessoas têm informações diferentes sobre o mesmo evento (horários, locais).

    To get wires crossed: Confundir as informações.

    To get mixed up: Confundir-se.

Exemplo:

    "Sorry I missed the meeting. I think we got our wires crossed about the time." (Desculpe, perdi a reunião. Acho que trocamos as bolas sobre o horário).

Idiom: The Wrong End of the Stick

Uma expressão muito comum no Reino Unido para quando alguém entende o oposto total da verdade.

To get the wrong end of the stick: Entender tudo errado.

Exemplo:

    "No, I'm not firing you! You got the wrong end of the stick. I'm promoting you!" (Não estou te demitindo! Você entendeu tudo errado. Estou te promovendo!).

Correcting Tone: "I didn't mean to..."

Às vezes, a tradução direta soa rude sem querermos. Se você ofender alguém, corrija rápido.

Frases:

    "I didn't mean to sound rude." (Não tive a intenção de soar rude).

    "I didn't mean to offend you."

Exemplo:

    "When I said 'Go away', I meant 'You can leave early'. I didn't mean to be impolite."

Checking Understanding: "Does that make sense?"

Depois de explicar de novo, verifique se a mensagem chegou.

Evite: "Do you understand?" (Pode soar condescendente/professoral). Use: "Does that make sense?" (Faz sentido?).

Isso pergunta se a sua explicação foi boa, não se a inteligência da pessoa é boa.
Vocabulary: To Clarify / To Clear up

Verbos úteis para resolver a situação.

    To clarify: Esclarecer (dar detalhes).

    To clear up: Resolver (uma confusão/mistério).

Exemplo:

    "I want to clear up any confusion about the bill." (Quero resolver qualquer confusão sobre a conta).

Situation: The False Friend Correction

Quando você usa uma palavra errada (falso cognato) e cria uma situação engraçada ou constrangedora.

Exemplo:

    "I said 'Parents' but I meant 'Relatives'. Sorry, my mistake." (Disse 'Pais' mas quis dizer 'Parentes'. Desculpe, erro meu).

Assumir o erro com "My mistake" encerra o assunto rapidamente.
Strategy: Blame the Language

Se o seu inglês falhar, use isso a seu favor para ganhar simpatia.

Frase:

    "Sorry, English is not my first language. I might be using the wrong word." (Desculpe, inglês não é minha primeira língua. Posso estar usando a palavra errada).

As pessoas tendem a ser muito mais pacientes quando você diz isso.
Scenario: The Hotel Date Confusion

Em datas, americanos usam Mês/Dia e europeus Dia/Mês. Isso gera caos.

Frase:

    "Wait, let's clarify the date. Is 10/12 October 12th or December 10th?"

Sempre confirme soletrando o mês.
Phrase: "What I'm trying to say is..."

Uma ótima frase de transição para resumir seu ponto principal quando você sente que falou demais e ninguém entendeu.

Exemplo:

    "Look, what I'm trying to say is that we love the hotel, but the room is too noisy."

Cultural Tip: Directness

Alemães e Holandeses podem dizer "You are wrong" (Você está errado) diretamente. Britânicos e Americanos preferem "I'm not sure that's correct" (Não tenho certeza se isso está certo).

Ao corrigir um mal-entendido em inglês, ser indireto ("I think there is a misunderstanding") é sempre mais seguro e polido.
Exercise 1: Choose the Best Reaction

Someone gets angry because they think you insulted them, but you didn't. What do you say?

A) "You got the wrong end of the stick. I didn't mean to offend you." B) "You don't understand English." C) "That is not my problem."

Answer: A (Explicação: Usa a expressão idiomática para "entendeu errado" e pede desculpas pela ofensa não intencional).
Exercise 2: Fill in the Blank

Complete the sentence. "I think we got our wires _______. I thought the meeting was at 2 PM, not 4 PM."

A) broken B) crossed C) cut

Answer: B (Explicação: O idioma é "To get wires crossed" - cruzar os fios/informações).
Context for Dialogue

Situation: A guest (Ricardo) asks the receptionist for a "late check-out". The receptionist thinks he wants to book the room for another full night and charges him a high price.

Focus: Use of not what I meant, misunderstanding, and clarify.
Dialogue: The Extra Charge

Receptionist: Okay, sir. I have booked you for another night. That will be $200. Ricardo: $200? Whoa! Sorry, that's not what I meant. Receptionist: You asked to stay longer, correct? Ricardo: Yes, but I think there has been a misunderstanding. I don't want to sleep here tonight. Receptionist: Oh? Ricardo: Let me clarify. I just need to stay in the room until 2 PM because my flight is late. I wanted a late check-out, not an extra night. Receptionist: Ah! I see. You got me confused there. A late check-out is only $20. Ricardo: Perfect. Sorry if I wasn't clear. Does that make sense now? Receptionist: Absolutely. I'll fix it right away.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned how to resolve misunderstandings. If someone interprets me wrongly, I can say 'That's not what I meant' or 'Let me rephrase that'. I learned idioms like 'we got our wires crossed' for logistical mistakes, and 'getting the wrong end of the stick' for total misinterpretation. I also learned to check understanding by asking 'Does that make sense?' instead of 'Do you understand?'."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 37 Tema Central: Describing Feelings: Disappointment
Disappointment: Managing Expectations

Objetivo: Aprender a expressar decepção de forma precisa e variada. Você vai além do "I didn't like it" para usar termos como "Underwhelming", "Overrated" e a expressão essencial "It didn't live up to the hype".

Nem toda viagem é perfeita. Saber descrever o que deu errado ajuda você a ser um crítico melhor e a avisar outros viajantes.
The Core Phrase: "Live up to the hype"

Hype: É a promoção exagerada, o falatório, a fama excessiva de algo antes de você ver.

Quando algo é bom como dizem: "It lived up to the hype." Quando decepciona: "It didn't live up to the hype."

Exemplo:

    "Everyone talks about this burger, but honestly, it didn't live up to the hype." (Todos falam desse hambúrguer, mas honestamente, não fez jus à fama).

Key Adjective: Underwhelming

Uma palavra fantástica para nível intermediário.

    Overwhelming: Esmagador / Impressionante demais.

    Underwhelming: Decepcionante, "sem graça", menos do que se esperava.

Exemplo:

    "We visited the famous statue, but it was a bit underwhelming. It's so small!"

Key Adjective: Overrated

O adjetivo favorito dos críticos. Significa que algo é valorizado demais pelas pessoas, mas não merece.

Overrated: Superestimado.

Exemplo:

    "Don't go to that club. It's expensive, crowded, and totally overrated."

(O oposto é Underrated - Subestimado/Joia escondida).
Phrasal Verb: To Let Down

Decepcionar alguém.

To let someone down: Decepcionar. A letdown (Substantivo): Uma decepção.

Exemplos:

    "The hotel service really let us down." (O serviço nos decepcionou).

    " The view was a bit of a letdown due to the fog." (A vista foi uma decepção por causa da neblina).

Adjective: Lackluster

Usado para descrever algo sem brilho, sem energia ou medíocre. Ótimo para shows, serviços ou comida.

Lackluster: Medíocre, "meia-boca", sem vida.

Exemplo:

    "The performance was lackluster and the dancers looked tired."

Adjective: Run-down

Para descrever hotéis, prédios ou áreas que estão velhas, mal cuidadas e precisando de reforma.

Run-down: Caindo aos pedaços, decadente.

Exemplo:

    "The photos looked great, but in reality, the resort is quite run-down."

Adjective: Tacky / Cheesy

Para descrever atrações turísticas que são de mau gosto, artificiais ou "bregas".

    Tacky: Brega, barato, de mau gosto.

    Cheesy: Cafona, forçado (tentando ser engraçado ou romântico, mas falhando).

Exemplo:

    "The souvenir shop was full of tacky plastic Eiffel Towers."

Comparison: Expectation vs. Reality

Uma estrutura útil para comparar.

    "It wasn't what I expected." (Pode ser neutro ou negativo).

    "It was nothing like the photos." (Geralmente negativo - propaganda enganosa).

Exemplo:

    "Honestly, the room was nothing like the photos on the website."

Adjective: Bland (Food)

A maior decepção culinária.

Bland: Sem gosto, insosso. (Não confunda com "Blend" - misturar).

Exemplo:

    "The curry looked spicy, but it was actually quite bland."

Softening the Blow: "It was okay, but..."

Se você não quer ser cruel, use a técnica do "mas".

Estrutura: Positive + BUT + Negative.

Exemplo:

    "The location was great, but the room was tiny."

    "The staff was friendly, but the food was cold."

Isso soa mais equilibrado e justo.
Vocabulary: Touristy

Embora sejamos turistas, odiamos lugares que parecem feitos só para turistas (sem autenticidade).

Touristy: Turístico demais (sentido pejorativo).

Exemplo:

    "We left the center because it was too touristy and expensive."

Key Phrase: "Not worth the money/wait"

O veredito final financeiro ou de tempo.

    Not worth the money: Não vale o preço.

    Not worth the wait: Não vale a espera (fila).

Exemplo:

    "We waited 2 hours for the ride. It was fun, but not worth the wait."

Cultural Tip: complaining

Americanos tendem a usar hipérboles para decepção: "It was a disaster!", "Horrible!". Britânicos tendem a usar understatement (eufemismo): "It was a bit disappointing", "I wasn't too keen on it".

Entender essa nuance ajuda a interpretar reviews online.
Exercise 1: Choose the Best Word

You went to a famous restaurant. The food was okay, but not amazing like everyone said. It was...

A) Run-down B) Overrated C) Tacky

Answer: B (Explicação: Se todos dizem que é ótimo, mas não é, é "Superestimado/Overrated").
Exercise 2: Fill in the Blank

Complete the sentence. "I was so excited about the museum, but it was a bit of a _______."

A) letdown B) hype C) worth

Answer: A (Explicação: O substantivo para decepção é "a letdown").
Context for Dialogue

Situation: Two friends, Mike and Jess, have just visited the "Walk of Fame" in Hollywood. They are walking back to their car.

Focus: Use of underwhelming, run-down, and live up to the hype.
Dialogue: The Hollywood Reality

Mike: So... that was the famous Walk of Fame. Jess: Yeah. To be honest, I'm a bit disappointed. Mike: Me too. It was incredibly underwhelming, wasn't it? Jess: Completely. I expected glamour, but the street is actually quite run-down and dirty. Mike: And so many tacky souvenir shops! Jess: Exactly. Everyone says you have to see it, but it definitely didn't live up to the hype. Mike: Agreed. It's totally overrated. Next time, let's just go to the beach. Jess: Good plan. Hopefully, the sunset won't be a letdown.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned how to describe disappointment. I learned that if something is not as good as people say, it is 'overrated' and it 'didn't live up to the hype'. If I am unimpressed, I can say the experience was 'underwhelming' or 'a letdown'. I can describe bad buildings as 'run-down' and bad souvenirs as 'tacky'. I also learned to compare reality to expectations by saying 'It was nothing like the photos'."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 40 Tema Central: Review: The Crisis (Revisão da Unidade)
Review: The Flight Cancellation Crisis

Objetivo: Consolidar o vocabulário e as estruturas das Pílulas 31-39 em um cenário prático e de alta pressão: lidar com um voo cancelado no balcão de atendimento, pedindo desculpas, resolvendo mal-entendidos e descrevendo a decepção.

Este é o desafio final da unidade!
Scenario: The Nightmare Delay

Você está no aeroporto e seu voo para Londres foi cancelado devido a problemas técnicos. A fila para o balcão de atendimento é enorme.

Você precisa:

    Chamar a atenção da atendente.

    Perguntar sobre o que aconteceu.

    Expressar a grande decepção com o voo.

    Pedir desculpas por estar estressado.

    Corrigir um mal-entendido sobre a remarcação.

Dialogue: At the Counter

Cast:

    Você: O passageiro (You).

    Agente: A funcionária da companhia aérea (Agent).

1. Starting the Conversation (Polite Request)

Você: "Excuse me. I was wondering if you could possibly help me? My flight to London, BA247, has just been cancelled." (Pílula 33 - Polidez Extrema).

Agente: "I am terribly sorry about the cancellation, sir. It was due to technical issues." (Pílula 35 - Pedido de Desculpas Enfatizado).
2. Expressing Disappointment & Frustration

Você: "I understand, but this is a huge letdown. I had tickets for a show tonight in London. Honestly, this whole situation is completely underwhelming." (Pílula 37 - Vocabulário de Decepção).

Agente: "I know. We take full responsibility. We have rebooked you automatically for tomorrow morning at 6 AM." (Pílula 35 - Assumindo a Culpa).
3. Correcting a Misunderstanding

Você: "Wait, 6 AM? That's not what I meant. I need to be there today. Let me clarify: Unless I arrive today, I miss my connecting flight to Rome tomorrow morning." (Pílula 36 e Pílula 31 - Corrigindo a Informação e Usando "Unless").

Agente: "I see. I think we got our wires crossed. You have a connecting flight to Rome. That changes things." (Pílula 36 - Usando um Idioma para Confusão).
4. Proposing a Solution (Contrasting Ideas)

Agente: "I can get you on a flight this evening at 8 PM, although it has a layover in Dublin. Is that acceptable?" (Pílula 39 - Usando "Although" para Contraste).

Você: "A layover in Dublin is better than losing a whole day. However, does this new flight have extra legroom? I have a bad back." (Pílula 39 e Pílula 34 - Usando "However" e Justificando uma Preferência).

Agente: "Let me check. Yes, it's an aisle seat in the Exit Row."
5. Final Relief & Mixed Conditional

Você: "Fantastic. Thank you so much for fixing this. If I hadn't talked to you, I would be stuck here all night!" (Pílula 32 - Condicional Misto de Alívio).

Agente: "You're welcome, sir. I'm glad I could make it up to you." (Pílula 35 - Idioma para Compensar).
Structure Review: Quick Summary
Pílula	Estrutura Chave	Exemplo no Diálogo
31 (Unless)	Condicional Negativo	"Unless I arrive today, I miss..."
32 (Mixed)	Passado -> Presente	"If I hadn't talked, I would be stuck..."
33 (Polite)	Pedir Ajuda	"I was wondering if you could possibly help me?"
34 (Decline)	Justificar Assento	"I need the extra legroom."
35 (Apology)	Desculpas Sinceras	"I am terribly sorry" / "take full responsibility"
36 (Clarity)	Corrigir Erros	"That's not what I meant" / "got our wires crossed"
37 (Disappoint)	Expressar Frustração	"This is a huge letdown" / "underwhelming"
38 (Amazement)	EXTRA (Para o próximo voo)	"I hope the view is breathtaking."
39 (Contrast)	Contraste de Ideias	"Although it has a layover..." / "...However, does it have..."

Final Challenge for Audio

Releia o diálogo em voz alta, focando na pronúncia clara do vocabulário intermediário (terribly sorry, underwhelming, got our wires crossed, although, however) e na fluidez das frases condicionais.

Envie o áudio para seu professor!

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 41 Tema Central: Storytelling: Setting the Scene
Storytelling: Setting the Scene

Objetivo: Aprender a usar vocabulário descritivo e estruturas gramaticais para "montar o palco" de uma história de viagem. Você saberá como usar adjetivos, advérbios e frases preposicionais para transportar seu ouvinte/leitor para o local da sua narrativa.

Uma boa história de viagem não apenas lista eventos; ela faz o ouvinte sentir que está lá.
The Core Question: The Five Senses

Para descrever uma cena (To set the scene), pense nos cinco sentidos.
Sentido	Vocabulário (Verbos e Adjetivos)
Sight (Visão)	Breathtaking, Picturesque, Glimmering, Hazy
Sound (Audição)	Hustle and bustle, Whispering, Buzzing, Deafening
Smell (Olfato)	Aroma, Fragrant, Stench, Musty
Taste (Paladar)	Spicy, Tangy, Bland, Mouth-watering
Touch (Tato)	Rough, Smooth, Velvet, Humidity, Crisp
Key Structure 1: Adjective Placement

Use adjetivos antes do substantivo para criar um impacto rápido.

Exemplo:

    Boring: "I walked down the street. The street was old."

    Better: "I walked down the ancient cobblestone street." (Andei pela antiga rua de paralelepípedos).

    Better: "We drove past the lush green fields." (Passamos de carro pelos campos verdejantes e exuberantes).

Key Structure 2: Describing Atmosphere

A "vibe" do lugar é essencial.

Vocabulary:

    Atmosphere / Vibe: Atmosfera / Vibração.

    Lively: Animado (muita gente, barulho bom).

    Solemn: Solene (silencioso, sério).

    Eerie: Sinistro, estranho, que dá calafrios.

Exemplo:

    "The town square had a lively atmosphere with street musicians playing."

    "The old castle ruins felt eerie in the moonlight."

Describing Scenery: Landscape

Use essas palavras ao falar sobre natureza e paisagens.

    Lush: Exuberante, farto (vegetação).

    Rugged: Acidentado, áspero (terreno).

    Vast: Vasto, imenso (deserto, oceano).

    Glimmering: Cintilante (água, orvalho).

Exemplo:

    "We looked out over the vast desert under the glimmering stars."

Describing City Settings

Use essas palavras para descrever a cidade.

    Hectic: Frenético, agitado.

    Cramped: Apertado, espremido.

    Bustling: Movimentado, cheio de atividade.

    Gaudy / Glaring: Chamativo, berrante (luzes de neon).

Exemplo:

    "The downtown area was hectic and full of people. The billboards were glaring."

Key Structure 3: Prepositions of Place

Use preposições detalhadas para localizar eventos.
Preposição	Descrição	Exemplo
Beneath	Abaixo / Por baixo	"We swam beneath the rocky arch."
Beyond	Além de	"The path continued beyond the old temple."
Amidst	No meio de / Entre	"I found a quiet cafe amidst the hustle and bustle."

Hustle and bustle: A azáfama/correria da cidade.
Key Structure 4: Sensory Verbs

Use verbos que ativam os sentidos (em vez de "There was...").

    The air smelled of... (O ar cheirava a...).

    The water tasted of... (A água tinha gosto de...).

    I could hear... (Eu podia ouvir...).

Exemplo:

    "As we entered the market, the air smelled of spices and fresh coffee."

    "I could hear the distant whispering of the waves."

Sound Vocabulary

Expanda o vocabulário de sons.

    Buzzing: Zumbido (insetos, conversas).

    Chirping: Pássaros.

    Rattling: Chacoalhar (janelas, trens velhos).

    Distant rumble: Estrondo distante (trovão, trem).

Exemplo:

    "The only sound was the quiet chirping of the crickets."

Combining Descriptions: The Scene

Junte as estruturas para criar um parágrafo de abertura.

Exemplo: "It was late afternoon. Amidst the hectic bustle of the city, we entered a small, picturesque tea house. The air smelled of jasmine, and the only sound was the distant rattling of the subway beneath our feet."
Cultural Tip: Showing vs Telling

Na escrita em inglês, o lema é Show, don't tell (Mostre, não diga).

    Telling: "I was scared."

    Showing: "The castle felt eerie. I could hear the wind whistling through the broken windows, and my heart was pounding."

Exercise 1: Which Sense?

"The streets were slick from the heavy rain." Which sense is this describing?

A) Taste B) Sight C) Touch

Answer: C (Explicação: Slick significa escorregadio/liso, uma qualidade que se sente ao tocar ou caminhar. B também poderia ser uma resposta aceitável, mas o slick é mais ligado à textura).
Exercise 2: Fill in the Blank

Complete the sentence with the best word for environment.

"The small fishing village was incredibly _______. Perfect for a painting."

A) run-down B) bustling C) picturesque

Answer: C (Explicação: Picturesque significa ideal para uma pintura).
Context for Dialogue

Situation: A traveler (Maria) is telling a friend (Chris) about the first few moments in a busy foreign market.

Focus: Using sensory descriptions and atmosphere.
Dialogue: The First Impression

Chris: So, what was the market like? Maria: Oh, Chris, it was mind-blowing. The minute we stepped in, the atmosphere was so lively and hectic. Chris: What did you see? Maria: The stalls were packed close together, almost cramped. And everywhere you looked, the colors were so vibrant, it was a true feast for the eyes. Chris: What about the smells? Maria: The air smelled of roasted peanuts and strong spices. And I could hear the constant hustle and bustle of the vendors shouting prices amidst the crowd. It was intense! Chris: Wow. You really set the scene.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned how to set the scene for a story. I learned to use strong adjectives like 'lush', 'vast', and 'eerie' to describe the landscape and atmosphere. I know that I should engage all five senses by describing what the air 'smelled of' and what sounds I 'could hear'. I also learned to use prepositions like 'amidst' and 'beneath' to make my storytelling more precise and engaging."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 49 Tema Central: Fluency: Fillers
Fluency: The Art of Using Fillers

Objetivo: Aprender a usar Fillers (muletas linguísticas) como "You know," "Like," "Um," e "I mean" de forma natural e estratégica. Essas palavras preenchem pausas, dão tempo para pensar e sinalizam a mudança de um pensamento para outro, tornando sua fala mais fluida e autêntica.

Nativos usam Fillers o tempo todo; usá-los corretamente é um grande passo para soar fluente.
The Core Concept: Buying Time

Fillers não adicionam significado, mas têm três funções essenciais na fluência:

    Thinking Time: Dá ao falante um momento para formular a próxima frase.

    Signal Clarification: Avisa ao ouvinte que você está prestes a corrigir ou refinar o que acabou de dizer.

    Softener: Suaviza a frase, especialmente antes de dar uma opinião forte.

Filler 1: You Know (Você Sabe)

Usado para buscar validação do ouvinte ou assumir que o ouvinte entende o que você está sentindo/descrevendo.

Função: Busca de Entendimento Mútuo.

Exemplo 1 (Validação):

    "The beach was totally breathtaking, you know?" (A praia era de tirar o fôlego, sabe como é?)

Exemplo 2 (Descrição):

    "It's that feeling you get when you're completely alone, you know?"

Filler 2: Like (Tipo / É como se)

O Filler mais comum (e polêmico), especialmente entre jovens falantes de inglês americano. Usado para citar, dar um exemplo ou suavizar uma descrição.

Função: Aproximação/Exemplo.

Exemplo 1 (Exemplo/Aproximação):

    "The hostel room was like, super small, but the view was amazing." (O quarto do hostel era tipo, super pequeno...)

Exemplo 2 (Citação/Pensamento):

    "Like, I opened the door, and I was like, 'No way, I can't stay here!'"

Atenção: Usar "like" mais de três vezes em uma frase pode soar excessivo ou imaturo. Use com moderação.
Filler 3: I Mean (Eu Quero Dizer)

Usado para se corrigir, refinar uma ideia ou adicionar um detalhe.

Função: Clarificação/Correção (Pílula 36).

Exemplo 1 (Correção):

    "The restaurant was expensive, I mean, the main courses were over $40." (O restaurante era caro, eu quero dizer, os pratos principais custavam mais de $40).

Exemplo 2 (Ênfase):

    "The guide was rude, I mean, he actually yelled at us!"

Filler 4: Um / Uh / Ah

Os fillers mais universais. Usados puramente para ganhar tempo de raciocínio.

Função: Tempo de Pensamento.

Exemplo:

    "So, we had to go... um... which direction was it? Ah, yes, north."

Dica: Em vez de silêncio absoluto ou um "Éééé", use "Um". É natural.
Filler 5: Well (Bem)

Usado para começar uma resposta, especialmente se a resposta for um pouco relutante, complexa ou não totalmente direta.

Função: Introdução de Resposta.

Exemplo:

    Pergunta: "Did you like the museum?"

    Resposta: "Well, it was okay, but it didn't really live up to the hype."

Strategy: Position of Fillers

Colocar o Filler no início de uma frase ou cláusula é a forma mais eficaz de sinalizar ao seu ouvinte o que está por vir.
Posição	Exemplo	Função
Início	"Like, the market was super crowded..."	Preparando a descrição.
Meio	"...the line was, you know, extremely long."	Buscando acordo no meio da descrição.
Correção	"...it was 3 PM, I mean, maybe 3:30."	Refinando um detalhe.
Storytelling and Fillers (Pílulas 41-44)

Fillers são essenciais para contar histórias (Pílula 41-44), pois eles criam ritmo e naturalidade no seu Setup e Resolution.

Exemplo:

    "We were walking on this secluded path, you know, it was very eerie. And all of a sudden, like, we ran into this massive moose!"

Warning: When to Avoid Fillers

Evite Fillers em situações formais ou profissionais, onde a clareza e a concisão são cruciais.

    Avoid in: Apresentações formais, entrevistas de emprego, reclamações (Pílula 23) ou chamadas de emergência (Pílula 29).

Exemplo:

    Emergency: "My car broke down on the highway." (Claro e direto).

    Avoid: "Like, my car, um, just kinda broke down, you know?" (Muito vago).

Exercise 1: Choose the Best Filler

You said the service was slow, but you want to emphasize that the food was cold as well. Which filler is best?

A) Like B) You know C) I mean

Answer: C (Explicação: I mean é usado para refinar ou adicionar um detalhe mais forte/de suporte à sua afirmação anterior).
Exercise 2: Fill in the Blank

Complete the sentence with the most suitable filler for seeking validation.

"It was totally exhausting to climb that hill, _______?"

A) I mean B) Well C) You know

Answer: C (Explicação: You know busca validação ("sabe como é?") da experiência compartilhada).
Context for Dialogue

Situation: Two friends, Tom and Lisa, are talking about their recent backpacking trip, discussing the food and the unexpected challenges.

Focus: Using You know, Like, I mean, e Well.
Dialogue: The Backpacking Review

Lisa: So, how was the food in Vietnam? Did it live up to the hype? Tom: Well, it was mostly great, you know? Super fresh. But there was this one place, like, a really small run-down place... Lisa: Yeah? Tom: I ordered what I thought was chicken, I mean, I pointed at the picture. But all of a sudden, I got this tiny bird! Lisa: No way! Tom: Yeah! It was, like, four bites of meat. I mean, I felt so mortified, but I ate it. The takeaway is: don't trust the pictures, you know?

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned to use fillers for natural fluency. I learned that 'You know' is for seeking validation, 'Like' is for approximation or example, and 'I mean' is for clarifying or correcting myself. These words buy me time to think and make my speech less robotic. I must remember to use them strategically, but avoid them in formal situations like an emergency call."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 50 Tema Central: Fluency: Linking Sounds
Fluency: The Art of Linking Sounds

Objetivo: Dominar a técnica de Linking Sounds (Conexão de Sons), que é o segredo por trás do ritmo e da velocidade da fala em inglês. Você aprenderá como falantes nativos conectam o final de uma palavra com o começo da próxima, o que torna a fala mais fluida e faz as palavras parecerem "grudadas".

A fluência não é apenas sobre vocabulário; é sobre ritmo.
The Core Concept: Why Words Blend

Em inglês, a fala é contínua (speech is continuous). Falantes nativos não fazem uma pausa entre cada palavra; eles fundem os sons.

Quando você tenta falar cada palavra separadamente, você soa robótico e lento. Aprender a conectar os sons torna você mais fácil de entender para nativos e acelera sua fluência.

Exemplo:

    Separate: I - want - to - go - out.

    Connected: Iwan-na-go-out.

Type 1: Consonant to Vowel

A regra mais importante. O som de uma consoante no final de uma palavra se conecta perfeitamente ao som de uma vogal no começo da próxima.
Separado (Robótico)	Conectado (Fluente)
Pick → up	Pick-up (Parece uma palavra só: Picup)
Turn → on	Turn-on
Go → out	Go-out (A consoante /w/ é inserida: Gowout)

Exemplo Prático:

    "I want to take an aisle seat." → Teka-na-is-sít (As vogais se fundem).

Type 2: Consonant to Consonant

Quando uma palavra termina com o mesmo som (ou um som similar) com que a próxima palavra começa, o primeiro som é omitido ou alongado.

Exemplo:

    Bad → day → Ba-day (O primeiro 'd' é engolido).

    Hot → tea → Ho-tea (O primeiro 't' é alongado, não repetido).

    Big → game → Bi-game (O 'g' final é engolido).

Type 3: Vowel to Vowel (Inserting Glide Sounds)

Quando uma palavra termina em som de vogal e a próxima também começa com som de vogal, o cérebro insere um som de "glide" (deslizamento) para conectar.

    Sons de /u/ ou /o/ no final → Inserir som de /w/ (W).

        Go → away → Gow-away

        Too → often → Toow-often

    Sons de /i/ ou /e/ no final → Inserir som de /y/ (Y).

        I → am → I-yam

        She → is → Shey-is

Type 4: Reduction (The "Schwa" and "T" sound)

Muitas palavras pequenas são "reduzidas" na fala rápida.

    To → Reduzido para /da/ (Schwa sound).

        Go → to → the → Gow-da-da

    You → Reduzido para /ya/.

        How are → you → How-ar-ya

    Want to → Wanna / Going to → Gonna (Os phrasal verbs de redução mais comuns).

Practical Exercise: Connecting Travel Vocabulary

Vamos conectar o vocabulário das últimas pílulas para treinar.
Frase	Conexão de Sons	Pronúncia Aproximada	Pílula Relacionada
All in all	All-ih-nall	Allinall	Pílula 44
Check in	Che-kihn	Chekin	Pílula 26
Find a ride	Fin-daride	Findaraide	Pílula 47
Out of nowhere	Ou-da-nowhere	Outtanowhere (T vira D)	Pílula 42
What do you	Whad-d'ya	Whad-ya	Pílula 48
Make it up	May-kih-tup	Makeitup	Pílula 35
Strategy: Practice by Shadowing

A melhor forma de aprender Linking Sounds é através do Shadowing:

    Ouça: Um nativo lendo um diálogo ou trecho de um podcast.

    Repita: Imediatamente após (ou ao mesmo tempo), tentando imitar exatamente a melodia e o ritmo.

Isso treina seu ouvido e sua boca para a fluidez.
The Problem: The Glottal Stop (O "Freio")

O erro que impede a fluência é o Glottal Stop (o som de "corte" na garganta que fazemos no meio de palavras como "ã-ã").

Em português, é comum cortar os sons entre as palavras. Em inglês, você deve forçar a ausência desse corte. O som do ar deve sair contínuo.
Final Tip: Don't Repeat Small Words

Nunca pronuncie palavras pequenas como "a", "an", "of", "to" com muita ênfase. Elas são quase sempre reduzidas ou absorvidas pelas palavras vizinhas.

Exemplo:

    A glass of water → A glas-sa-water (O "of" vira um som de schwa suave).

Exercise 1: Identify the Connection

Qual das palavras a seguir deve ser conectada com um som de /w/ (W) com a próxima palavra?

A) She is B) I am C) Go out

Answer: C (Explicação: Go termina com som de /o/, que desliza para o som de /w/ antes da vogal seguinte: Gowout).
Exercise 2: Identify the Reduction

Qual palavra é quase totalmente engolida/reduzida na fala rápida?

A) Suddenly B) Terrible C) Of

Answer: C (Explicação: Palavras funcionais como "of" são reduzidas para um som de schwa (uh) na fala rápida: A glas-sa-water).
Context for Dialogue

Situation: Two friends, Tom and Lisa, are talking about a travel story, using many linking sounds for fluid conversation.

Focus: Using Linking Sounds (marcado com hífen) e Reduções.
Dialogue: The Flowing Story

Lisa: All-ih-nall, how was → it? Did you → enjoy the trip? Tom: Yeah, I loved-it! I had-a great time-out there. But we ran-in-to some trouble, y'know? Lisa: Oh no-ah-gain! Tell me-about-it. Tom: We were trying to pick-up the rental car, but the manager was-a real bad-day guy. We jus-sat there, waiting. Lisa: Did you → get the car in the end? Tom: Yes, eventually. But we had-to pay extra for an upgrade. It was-a whole mess, I-mean!

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned the secret to fluency: Linking Sounds. I know that when a word ends with a consonant and the next starts with a vowel, the sounds connect, like 'pick-up'. I also learned about glide sounds (like inserting a /w/ in 'go-out') and reductions (like turning 'of' into a short sound or 'want to' into 'wanna'). Practicing shadowing is the best way to train my ear for this continuous speech."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 51 Tema Central: Describing Flavors (Advanced)
Describing Flavors: Texture and Aftertaste

Objetivo: Elevar seu vocabulário gastronômico, indo além dos cinco gostos básicos (doce, salgado, etc.). Você aprenderá a descrever a textura (texture) e o sabor residual (aftertaste) dos alimentos, permitindo que você escreva críticas de restaurantes mais ricas e detalhadas.

Uma boa descrição de comida envolve a boca inteira, não apenas a língua.
Focus 1: Texture (The Mouthfeel)

Texture é como a comida se sente na sua boca (mouthfeel). É crucial para descrever pães, carnes, sobremesas e caldos.
Textura	Descrição	Exemplo de Uso
Crispy / Crunchy	Crocante (som ao morder)	"The crust was wonderfully crispy."
Creamy / Velvety	Cremoso, suave	"The soup was rich and velvety."
Chewy	Borrachudo, que exige mastigação	"The noodles were perfectly chewy."
Tender	Macio, que se desfaz facilmente	"The steak was so tender; it melted in my mouth."
Gooey	Pegajoso, melequento (geralmente para chocolate/queijo)	"The inside of the brownie was warm and gooey."
Fluffy	Fofo, aerado (panquecas, bolos)	"The pancakes were incredibly fluffy."
Gritty	Granuloso (areia, açúcar mal dissolvido)	"The sauce had a slightly gritty texture."
Focus 2: Aftertaste (The Lingering Flavor)

Aftertaste é o sabor que permanece na sua boca depois que você engoliu a comida.
Aftertaste	Descrição	Exemplo de Uso
Lingering	Persistente, que fica muito tempo	"The chili had a lingering heat on the tongue."
Clean	Limpo, fresco (o sabor desaparece rápido)	"The wine had a light, clean aftertaste."
Pungent	Forte, penetrante (alho, cebola forte)	"The raw garlic left a very pungent aftertaste."
Bitter	Amargo (café forte, chocolate escuro)	"There was a mild bitter aftertaste from the dark roast."
Acrid	Ácido, cáustico, desagradável (gosto de queimado)	"The burnt rice left an acrid taste."
Adjective: Subtle

Usado para sabores ou aromas que são delicados e não dominantes. É um elogio.

Subtle: Sutil, delicado.

Exemplo:

    "The dish had a subtle hint of lemon and garlic."

Adjective: Robust / Full-bodied

Usado para descrever sabores fortes, ricos e complexos.

    Robust: Robusto, forte (ideal para café, molhos).

    Full-bodied: Encorpado (ideal para vinhos, cervejas escuras).

Exemplo:

    "I love this coffee; it has a robust flavor and a smooth finish."

Verb: To Complement

Como os sabores e as texturas se combinam bem.

To Complement: Complementar, combinar.

Exemplo:

    "The creamy sauce complemented the crispy vegetables perfectly."

Phrasal Verb: To Cut Through

Quando um sabor forte (geralmente ácido) é usado para quebrar a riqueza ou a gordura de um prato.

To Cut Through: Cortar, quebrar (a gordura/riqueza).

Exemplo:

    "The splash of lime juice helped cut through the richness of the pork belly."

Vocabulary: Palate

O seu paladar; a sua capacidade de apreciar o sabor.

    Palate: Paladar.

    To cleanse the palate: Limpar o paladar (com água, sorvete, etc.).

Exemplo:

    "The chef offered us a small sorbet to cleanse our palates before the main course."

Describing Complexity: Layers of Flavor

Para descrever pratos muito sofisticados.

Frase:

    "The dish had incredible layers of flavor."

    "The taste was incredibly complex."

Exemplo:

    "The curry had different layers of flavor, starting with sweet, followed by sour, and ending with a lingering spice."

Negative Textures

Se a comida estiver ruim, você precisa de um vocabulário negativo.

    Rubbery: Borrachudo (camarão cozido demais).

    Soggy: Encharcado, molhado (pão, batata frita).

    Tough: Duro (carne mal cozida).

Exemplo:

    "The fried calamari was unfortunately a bit rubbery."

Context: Wine Tasting

Em degustações, essas palavras são essenciais.

Exemplo:

    "The wine has a full-bodied flavor with a subtle hint of vanilla, and a surprisingly clean aftertaste."

Exercise 1: Texture Match

Which texture best describes a marshmallow?

A) Gritty B) Fluffy C) Chewy

Answer: B (Explicação: Marshmallows são aerados e macios, ou seja, fluffy).
Exercise 2: Fill in the Blank

Complete the sentence. "I loved the sauce, but the fish was overcooked and very _______."

A) gooey B) rubbery C) tender

Answer: B (Explicação: Rubbery (borrachudo) é a textura negativa clássica para frutos do mar cozidos demais).
Context for Dialogue

Situation: Two friends, Leo and Chloe, are reviewing a new, sophisticated dessert at a restaurant.

Focus: Using texture, aftertaste, fluffy, gooey, and complement.
Dialogue: The Dessert Review

Chloe: Wow, that looks absolutely mind-blowing (Pílula 38). What is this? Leo: It's a passionfruit soufflé. You have to try it! Chloe: Okay. (Takes a bite). The texture is amazing! It’s so light and fluffy on the outside. Leo: And the sauce? Chloe: The chocolate inside is warm and incredibly gooey. The bitterness of the dark chocolate really cuts through the sweetness of the passionfruit. Leo: They complement each other perfectly, you know (Pílula 49). Chloe: Yes! The whole dessert is incredibly complex. And it leaves a very clean aftertaste. I can definitely send my compliments to the chef (Pílula 48) for this one.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned advanced food vocabulary. I know how to talk about texture using words like 'fluffy', 'chewy', and 'tender'. I also learned how to describe the aftertaste, using 'lingering' for a long taste and 'clean' for a quick one. If I want to say that two flavors match, I can say they 'complement' each other, and if a flavor reduces richness, it 'cuts through' it. This helps me write much better reviews!"

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 52 Tema Central: Describing Architecture
Describing Architecture: Styles and Eras

Objetivo: Adquirir vocabulário específico para descrever diferentes estilos arquitetônicos, desde os mais antigos até os mais modernos. Você aprenderá a usar adjetivos para analisar a estrutura, a história e o estado de conservação de edifícios, ruínas e monumentos.

A arquitetura conta a história de um lugar.
Focus 1: Historical Styles
Estilo	Vocabulário Chave	Descrição
Ancient	Ruins, Columns, Temple, Excavation	Relacionado a Grécia, Roma, Egito (antes de 500 d.C.).
Gothic	Arches, Vaulted ceilings, Stained glass, Cathedral	Construções medievais (Séc. XII - XVI), focadas na altura e luz.
Baroque	Ornate, Elaborate, Sculptures, Grand, Extravagant	Estilo Séc. XVII - XVIII, focado em drama e riqueza de detalhes.
Renaissance	Symmetry, Harmony, Proportions, Dome	Retorno aos ideais clássicos (Séc. XIV - XVI).

Exemplo:

    "The Gothic cathedral had impressive vaulted ceilings and beautiful stained glass windows."

Focus 2: The Modern Era
Estilo	Vocabulário Chave	Descrição
Modernist	Sleek, Minimalist, Geometric, Functional	Foco na forma e função (pós-Séc. XIX). Linhas limpas.
Contemporary	Innovative, Unique, Sustainable, Experimental	O que está sendo construído agora, uso de novas tecnologias.
Skyscraper	Towering, Steel and glass, Skyline	Prédios muito altos.

Exemplo:

    "The new museum is a perfect example of Modernist design: minimalist and sleek."

Describing Structure and Form

Como a construção é fisicamente.

    Facade: Fachada (a frente do prédio).

    Foundation: Fundação.

    Symmetry: Simetria.

    Proportions: Proporções.

    To dominate the skyline: Dominar o horizonte.

Exemplo:

    "The new skyscraper dominates the skyline with its towering structure."

Describing Condition: Ruins and Age

O estado de conservação é crucial para a arquitetura histórica.

    Ruins: Ruínas.

    Well-preserved: Bem preservado.

    Dilapidated / Run-down: Caindo aos pedaços, mal conservado (Pílula 37).

    Ancient: Antigo, ancestral.

    Crumbling: Desmoronando, esfarelando.

Exemplo:

    "The temple is mostly crumbling ruins, but the main facade is remarkably well-preserved."

Key Adjective: Ornate

Usado para descrever detalhes muito elaborados, especialmente no estilo Barroco.

Ornate: Ornamentado, ricamente decorado.

Exemplo:

    "The palace was incredibly ornate, covered in gold leaf and intricate carvings."

Key Adjective: Imposing

Usado para estruturas grandes, altas ou que inspiram poder e respeito.

Imposing: Imponente.

Exemplo:

    "The castle looked imposing from the valley below."

Key Adjective: Quaint

Usado para descrever prédios antigos, charmosos, que têm um toque de nostalgia (geralmente pequenos).

Quaint: Pitoresco, peculiar (Pílula 38 - similar a Picturesque).

Exemplo:

    "We stayed in a quaint little house with a thatched roof."

Vocabulary: Materials

Os materiais utilizados dizem muito sobre a época.

    Stone: Pedra.

    Brick: Tijolo.

    Timber / Wood: Madeira.

    Steel and glass: Aço e vidro (Moderno).

Exemplo:

    "The cottage was built entirely of local stone."

Storytelling: Setting the Scene (Pílula 41)

Use este vocabulário para descrever onde sua história aconteceu.

Exemplo:

    Calmo: "We were walking through the quaint city center, surrounded by well-preserved Renaissance buildings."

    Suspense: "We entered the dilapidated building; the walls were crumbling, and the atmosphere felt eerie." (Pílula 46).

Exercise 1: Style Match

Which style emphasizes height, pointed arches, and stained glass?

A) Baroque B) Gothic C) Contemporary

Answer: B (Explicação: Gothic (Gótico) é caracterizado por arcos pontiagudos e vitrais).
Exercise 2: Fill in the Blank

Complete the sentence. "The ancient city is now just a vast field of _______."

A) ornaments B) facades C) ruins

Answer: C (Explicação: Ruins (Ruínas) é o termo para os restos de uma cidade antiga).
Context for Dialogue

Situation: Two friends, Sam and Alex, are walking through a city that mixes old and new architecture.

Focus: Using imposing, minimalist, ornate, skyscrapers, and well-preserved.
Dialogue: Architectural Contrast

Sam: Look at that skyscraper. It's so imposing and sleek. Alex: I know. It's too minimalist for me, though (Pílula 39). I prefer the buildings from the 18th century. Sam: Like that church? It's really old. Alex: Yes! That's a perfect example of Baroque architecture. See how ornate the facade is? It has so much detail. Sam: It's beautiful, and incredibly well-preserved, you know (Pílula 49). Alex: Exactly. I think this city is interesting because you have the towering modern glass and steel right next to the quaint stone buildings. It's a great contrast.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned how to describe architecture. I know that Gothic style uses arches and stained glass, while Baroque is ornate and extravagant. Modernist buildings are sleek and minimalist. When describing structures, I can use the words facade and foundation. If something is old, it might be crumbling ruins or, hopefully, well-preserved. I can also use imposing for tall buildings and quaint for charming old ones."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 53 Tema Central: Describing Landscapes
Describing Landscapes: Geography and Terrain

Objetivo: Adquirir vocabulário avançado para descrever a geografia e o relevo de um lugar. Você aprenderá a usar adjetivos que expressam a fertilidade, a forma e a desolação da terra.

Descrever a paisagem é essencial para qualquer história ou relato de viagem.
Focus 1: Fertility and Vegetation

O contraste entre a vida e a desolação.
Vocabulário	Descrição	Exemplo de Uso
Lush	Exuberante, farto, verde e saudável (Pílula 41).	"After the rain, the valley became incredibly lush."
Fertile	Fértil, bom para o cultivo.	"The river delta is known for its fertile soil."
Arid / Barren	Árido, estéril, seco (sem vida ou vegetação).	"The landscape quickly turned barren as we entered the desert."
Dense	Denso, fechado (floresta, folhagem).	"The trail disappeared into the dense jungle."
Focus 2: The Shape of the Land (Terrain)

Como o relevo é formado.
Vocabulário	Descrição	Exemplo de Uso
Hilly	Montanhoso, cheio de colinas suaves (hills).	"San Francisco is famous for its hilly streets."
Mountainous	Montanhoso, com grandes picos (mountains).	"We drove through the rugged mountainous region."
Flat / Level	Plano, liso.	"The plains of the Midwest are entirely flat."
Undulating	Ondulado, suavemente irregular (como ondas).	"The road wound through undulating fields of grain."
Rugged	Acidentado, áspero, difícil de atravessar (Pílula 41).	"The coastline was rugged and wild."
Focus 3: Water Features

Como descrever lagos, rios e costas.

    Coastal: Costeira, na beira do mar.

    Riverbank: Margem do rio.

    Glacier: Geleira.

    Stream / Creek: Riacho, córrego.

    Estuary: Estuário (onde o rio encontra o mar).

Exemplo:

    "We set up camp on the riverbank near a small stream."

    "The coastal road offered breathtaking (Pílula 38) views."

Focus 4: Geological Features

Elementos naturais da paisagem.

    Cave: Caverna.

    Canyon: Desfiladeiro.

    Cliff: Penhasco.

    Valley: Vale.

    Plateau: Planalto.

Exemplo:

    "We climbed to the edge of the canyon to see the vast plateau below."

Key Adjective: Sparse

Usado para descrever algo que está espalhado, ralo.

Sparse: Escasso, esparso.

Exemplo:

    "The houses in the region were sparse, and the trees were thin."

    (Comida): "The meal was disappointingly sparse." (Pílula 37 - decepção).

Key Adjective: Dramatic

Usado para descrever paisagens que causam um forte impacto visual ou emocional.

Dramatic: Dramático, impactante.

Exemplo:

    "The meeting point of the ocean and the rugged cliffs created a dramatic scene."

Storytelling: Setting the Scene (Pílula 41)

Use este vocabulário para enriquecer a descrição.

Exemplo:

    Calmo: "We drove for hours across the vast, flat plains, with only sparse patches of grass visible."

    Suspense: "The car broke down in a secluded (Pílula 46) part of the mountainous terrain."

Exercise 1: Choose the Best Word

You are describing a region that is very dry, without many plants, and unsuitable for farming.

A) Lush B) Hilly C) Arid

Answer: C (Explicação: Arid (Árido) significa muito seco e sem vegetação).
Exercise 2: Fill in the Blank

Complete the sentence. "The terrain was so _______ that we could only see a few scattered houses."

A) dense B) sparse C) fertile

Answer: B (Explicação: Se as casas estão espalhadas e em pequena quantidade, elas são sparse (esparsas). Dense é o oposto).
Context for Dialogue

Situation: Two friends, Sam and Chloe, are reviewing two different legs of a long road trip: one through a lush area and one through a desert.

Focus: Using lush, barren, hilly, rugged, and dramatic.
Dialogue: Contrasting Terrains

Sam: Which part of the road trip did you prefer? The north or the south? Chloe: The north was beautiful. The entire area was so lush and fertile. Everything was green! Sam: Yeah, but the south was more exciting. It was mostly arid and barren, you know (Pílula 49). Chloe: True. The south was much more dramatic. Sam: Exactly! We started with some hilly areas, but then the terrain became so rugged around the canyon. It felt like we were on another planet. Chloe: I remember. The vegetation became really sparse towards the end. But the view from the cliff edge was absolutely breathtaking (Pílula 38).

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned vocabulary to describe landscapes. I know how to contrast the land using lush and fertile versus arid and barren. I also learned terms for the shape of the land, such as hilly, mountainous, and rugged terrain. For density, I use dense or sparse. The key is to use strong adjectives like dramatic when describing features like canyons or cliffs."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 54 Tema Central: Digital Nomad Vocabulary
Digital Nomad Vocabulary: Working Remotely

Objetivo: Adquirir o vocabulário essencial para quem trabalha e viaja ao mesmo tempo (o Nômade Digital). Você aprenderá termos sobre espaços de trabalho, tecnologia, comunidade e a logística de ser um funcionário remoto.

Esta é a língua franca da nova geração de viajantes.
Focus 1: Workspace Essentials

Onde e como o trabalho é feito.
Termo	Significado	Exemplo de Uso
Co-working Space	Espaço de trabalho compartilhado.	"I booked a day pass at the new co-working space downtown."
Hot Desk	Mesa rotativa em um co-working (sem lugar fixo).	"The monthly membership includes access to hot desks."
Dedicated Desk	Mesa reservada e fixa (mais cara).	"I pay extra for a dedicated desk; I need the monitors."
Ergonomics	Ergonomia (postura, conforto).	"I struggled with my back until I improved the ergonomics of my setup."
Zoom Fatigue	Fadiga causada por excesso de reuniões online.	"I had five video calls today; I’m suffering from serious Zoom fatigue."
Focus 2: Connectivity (The Lifeline)

A conectividade é a prioridade número um para o nômade digital.
Termo	Significado	Exemplo de Uso
Bandwidth	Largura de banda (capacidade de dados).	"The bandwidth here is too low for video uploads."
Upload/Download Speed	Velocidade de upload/download (medida em Mbps).	"I checked the download speed, and it’s fast enough for streaming."
Reliable Wi-Fi	Wi-Fi confiável (que não cai).	"I won't book a place unless (Pílula 31) they guarantee reliable Wi-Fi."
VPN (Virtual Private Network)	Rede Privada Virtual (segurança).	"I always use my VPN when connecting to public Wi-Fi."
Hotspot / Tethering	Compartilhar internet do celular.	"My Wi-Fi is down; I'll use my phone's hotspot for a quick call."

A pergunta essencial: "What is the average upload and download speed?"
Focus 3: Lifestyle and Logistics

Termos relacionados à comunidade e ao estilo de vida.

    Digital Nomad Visa: Visto especial para trabalhadores remotos (Pílula 27).

    Time Zone Difference: Diferença de fuso horário.

    Asynchronous Work: Trabalho assíncrono (sem reuniões em tempo real).

    To Clock In / Out: Bater o ponto (virtualmente).

Exemplo:

    "Dealing with the time zone difference is the hardest part of asynchronous work."

    "I need a visa that allows me to stay long-term; I'm looking for a Digital Nomad Visa."

Key Phrase: Fully Remote

O termo oficial para quem não precisa ir ao escritório.

Fully Remote: Totalmente remoto.

Exemplo:

    "My company is now fully remote, so I can work from anywhere in the world."

Key Phrase: Cost of Living

O custo de vida é o fator principal na escolha de onde morar.

Cost of Living: Custo de vida.

Exemplo:

    "Although (Pílula 39) the city is beautiful, the cost of living is too high for my budget."

Key Phrase: Work-Life Balance

Encontrar um equilíbrio entre trabalho e diversão.

Work-Life Balance: Equilíbrio entre vida pessoal e profissional.

Exemplo:

    "I struggle to maintain a good work-life balance when I'm traveling."

Strategy: Finding the Wi-Fi

Como improvisar quando a conectividade falha (Pílula 47).

    "Do you happen to know the Wi-Fi password?"

    "Could I get a coffee and use your reliable Wi-Fi for an hour?"

Exercise 1: Match the Terms

Which term describes a non-fixed desk in a shared office?

A) Dedicated Desk B) Hot Desk C) Co-working Space

Answer: B (Explicação: Hot Desk é o assento rotativo).
Exercise 2: Fill in the Blank

Complete the sentence. "I can't upload the video with this slow _______."

A) hot desk B) bandwidth C) ergonomics

Answer: B (Explicação: Bandwidth (largura de banda) é a capacidade de dados, o que limita a velocidade de upload).
Context for Dialogue

Situation: Two digital nomads, Alex and Sarah, are meeting for coffee to discuss their work situations in a new city.

Focus: Using co-working space, reliable Wi-Fi, time zone difference, and fully remote.
Dialogue: The Digital Nomad Grind

Alex: So, how are you finding the work setup here? Sarah: It’s okay, but I can't find a good co-working space. And the Wi-Fi at my Airbnb is terrible. Alex: You need to find a place with reliable Wi-Fi, I mean (Pílula 49), it’s the most important thing! Have you checked the cafes? Sarah: Yeah, but the upload speed isn't good enough for my video calls. I might rent a dedicated desk. Alex: Well (Pílula 49), that's expensive. I'm struggling with the time zone difference the most. I have to be available until midnight. Sarah: I get it. At least we are fully remote. You know (Pílula 49), despite the challenges, I wouldn't trade this life for anything.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned the vocabulary for digital nomads. I know that I can work in a co-working space at a hot desk or a dedicated desk. The most important factor is reliable Wi-Fi and high bandwidth. I also learned about time zone difference, asynchronous work, and the need to maintain a good work-life balance. I must always use a VPN on public Wi-Fi."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 55 Tema Central: Travel Photography Terms
Travel Photography Terms: Mastering the Shot

Objetivo: Adquirir o vocabulário essencial para falar sobre fotografia de viagem. Você aprenderá termos técnicos básicos relacionados à composição, luz e tipos de fotos, permitindo que você peça ajuda ou dê instruções claras a um fotógrafo (ou amigo!) durante a viagem.

Uma boa foto é a melhor lembrança de viagem.
Focus 1: Composition and Framing

Como você organiza os elementos na foto.
Termo	Significado	Exemplo de Uso
Rule of Thirds	Regra dos Terços (colocar o objeto principal em uma das linhas de intersecção).	"Use the rule of thirds to make the landscape more engaging."
Framing	Enquadramento (uso de elementos naturais para emoldurar o objeto, ex: arco).	"I used the open window for natural framing."
Angle	Ângulo (o ponto de onde a foto é tirada).	"Try a lower angle to make the building look more imposing (Pílula 52)."
Depth of Field	Profundidade de campo (o quanto da imagem está nítida; ideal para retratos).	"Use a shallow depth of field to blur the background."
Leading Lines	Linhas de orientação (linhas que guiam o olho para o objeto principal).	"The river acts as a leading line toward the mountain."
Focus 2: Lighting (The Key Element)

A luz é o fator mais importante para a qualidade da foto.
Termo	Significado	Exemplo de Uso
Golden Hour	Hora Dourada (a primeira hora após o nascer do sol ou a última hora antes do pôr do sol).	"The colors are best during golden hour; the lighting is soft."
Backlight	Luz de fundo (a luz está atrás do objeto, cria silhueta).	"I want to take a portrait against the sunset, using backlight."
Exposure	Exposição (a quantidade de luz capturada pelo sensor).	"The photo is too dark; increase the exposure."
Harsh Light	Luz Dura (luz do sol forte do meio-dia, cria sombras fortes).	"Avoid midday photos; the light is too harsh."
Focus 3: Types of Shots and Selfies

Termos práticos para o dia a dia.

    Selfie: Foto tirada de si mesmo (Pílula 26).

    Wide Shot: Foto ampla, que captura todo o ambiente (bom para paisagens).

    Close-up: Foto de perto, focada em detalhes (bom para comida ou rostos).

    Candid Shot: Foto espontânea (a pessoa não está posando).

    To Strike a Pose: Fazer uma pose.

Exemplo:

    "Don't pose! I want a candid shot of you laughing."

Key Phrase: To Be in Focus / Out of Focus

Onde está a nitidez da foto?

To be in focus: Estar nítido, focado. To be out of focus / Blurry: Estar desfocado.

Exemplo:

    "Can you make sure the landmark (Pílula 47) is in focus, not just the foreground?"

Key Phrase: Photo Dump

Um termo de mídia social: postar muitas fotos de uma vez sem legendas elaboradas.

Photo Dump: Despejo de fotos (Postagem simples).

Exemplo:

    "I didn't have time to edit; I just did a quick photo dump from the trip."

Key Phrase: Do-Over

Uma segunda chance para tirar a foto (informal).

Do-over: Repetição, refazer.

Exemplo:

    "That one was blurry. Can we do a do-over?"

Giving Instructions: How to Ask Someone

Como pedir a um estranho para tirar sua foto (Pílula 33 - Polidez).

Frase:

    "Excuse me, would you mind taking a quick picture of us?"

    "Could you please hold the phone higher and try a wide shot?"

Dica: Ofereça-se para tirar uma foto da pessoa em troca!
Scenario: The Problem

Se a foto não ficou boa, como reclamar educadamente.

Frase:

    "I'm sorry, I think the exposure is a bit off. Could you try increasing the light slightly?" (Pílula 36 - Evitando culpa).

    "My face is completely in backlight. Could we turn around?"

Exercise 1: Choose the Best Time

When is the best time to take a portrait using soft, warm light?

A) Midday (1 PM) B) Golden Hour C) Pitch black (Pílula 46)

Answer: B (Explicação: Golden Hour (Hora Dourada) fornece a luz mais suave e lisonjeira).
Exercise 2: Fill in the Blank

Complete the sentence. "You should put the main subject on one of the grid lines to follow the _______."

A) Wide Shot B) Depth of Field C) Rule of Thirds

Answer: C (Explicação: Rule of Thirds é o princípio de composição).
Context for Dialogue

Situation: A tourist (Chloe) asks a stranger (Liam) to take her photo in front of a monument at sunset.

Focus: Using angle, exposure, backlight, golden hour, and wide shot.
Dialogue: The Perfect Shot

Chloe: Excuse me, would you mind taking a picture of me? It’s the perfect golden hour light! Liam: Sure, no problem. Chloe: Thank you! Could you try a wide shot? I want the whole monument in the frame. Liam: Okay. I think you might be getting too much backlight here. Your face is too dark. Chloe: Oh, good point. Could you try changing the angle and maybe increasing the exposure a little? Liam: Like this? Chloe: Yes! Perfect! That one is definitely a keeper. Thank you so much for the do-over! Liam: You're welcome! Do you want me to try a candid shot while you walk?

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned travel photography terms. I know that the best time for photos is golden hour and that harsh light is bad. For composition, I should use the rule of thirds and good framing. When asking someone for a picture, I can specify a wide shot or a close-up. I also learned to check the exposure and avoid backlight for good portraits. If the picture is blurry, I can ask for a do-over."

###

Trilha: 1. Travel & Culture Nível: Intermediate Pílula #: 56 Tema Central: Socializing: Deep Questions
Socializing: Going Deeper (Deep Questions)

Objetivo: Aprender a fazer perguntas que vão além do superficial ("Where are you from?"). Você adquirirá frases para iniciar conversas mais significativas sobre filosofia de vida, carreira, motivações de viagem e lições aprendidas, essenciais para interagir em hostels, co-working spaces e longas viagens.

O objetivo não é apenas falar, mas conectar-se.
Phase 1: Moving Beyond the Superficial

Depois de quebrar o gelo com perguntas básicas, use essas frases para aprofundar a conversa.

Frases de Transição:

    "That's interesting. What got you into that type of work?"

    "I’m curious: What led you to travel alone?"

    "It sounds amazing. But what's the hardest part about being on the road?"

Focus 1: Motivation (The "Why")

Perguntas que exploram a razão por trás das escolhas de vida e de viagem.
Pergunta	Foco
"What's the story behind your career change?"	História pessoal, carreira.
"What motivates you to keep moving?"	Força motriz, filosofia.
"What are you hoping to figure out on this trip?"	Objetivos, autoconhecimento.
"What's the best decision you've ever made?"	Decisões de vida, arrependimentos (oposto).

Dica: Use Figure out (entender/descobrir) para falar sobre a busca por respostas.
Focus 2: Philosophy and Values

Perguntas sobre como a pessoa vê o mundo.
Pergunta	Foco
"What's your ultimate goal for the next five years?"	Ambição, planejamento a longo prazo.
"What does 'success' mean to you?"	Definição pessoal de sucesso.
"If money wasn't an issue, what would you be doing?"	Paixões, ideal de vida.
"What's the best piece of advice you’ve ever been given?"	Sabedoria, influências.

Exemplo:

    "For me, success is having a good work-life balance (Pílula 54). What about you?"

Focus 3: Travel Philosophy

Perguntas sobre a experiência de viajar.
Pergunta	Foco
"What's the biggest lesson travel has taught you?"	Aprendizado, Takeaway (Pílula 44).
"What's your travel style: slow travel or quick trips?"	Preferências, ritmo.
"How do you deal with homesickness or loneliness?"	Desafios emocionais.
"What makes a place feel like 'home' to you?"	Conceito de lar, apego.

Dica: Use Deal with (Lidar com) para perguntar como a pessoa gerencia desafios.
Vocabulary: Sharing Vulnerability

Você precisa de vocabulário para responder a perguntas profundas e mostrar que está sendo honesto.

    Vulnerable: Vulnerável (aberto, sincero).

    To open up: Abrir-se, desabafar.

    To be honest: Para ser honesto (introdução de uma opinião sincera).

    It's a huge shift: É uma grande mudança.

Exemplo:

    "To be honest, quitting my job was a huge shift, but I haven't regretted it."

Key Phrase: Asking for Clarification

Se a resposta da pessoa for complexa ou ambígua.

Frases:

    "Could you elaborate on that?" (Você poderia elaborar/dar mais detalhes?).

    "What exactly do you mean by 'finding freedom'?" (Pílula 36 - Clarificação).

    "I think I got the wrong end of the stick (Pílula 36). Can you explain?"

Giving an Opinion: The Softener

Ao dar uma resposta profunda ou forte, use Fillers e Softeners (Pílula 49).

Exemplo:

    "Well, I mean (Pílula 49), for me, I realized that chasing money didn't live up to the hype (Pílula 37)." (Dando uma opinião forte, mas suavizada).

The Closing: Ending the Depth

Como encerrar a conversa profunda e expressar gratidão.

Frases:

    "That was a really great answer. Thanks for opening up."

    "That's a lot to think about. Thanks for sharing that with me."

    "I appreciate your vulnerability."

Cultural Tip: Reciprocity

Em inglês, conversas profundas tendem a ser recíprocas. Se você fizer uma pergunta profunda, esteja preparado para respondê-la também.

    After they answer: "That makes sense. What about you?" / "How about yourself?"

Exercise 1: Choose the Best Deepener

You are talking to someone who just finished a six-month trip. What is the best next question?

A) Where are you going next? B) What's the biggest lesson travel has taught you? C) Did you use a lot of Wi-Fi?

Answer: B (Explicação: A opção B busca a sabedoria e o aprendizado, que é um tópico profundo de viagem).
Exercise 2: Fill in the Blank

Complete the sentence. "I want to change jobs, but I'm trying to _______ what I really want to do."

A) deal with B) elaborate on C) figure out

Answer: C (Explicação: Figure out (descobrir/entender) é o verbo comum para resolver um problema pessoal ou uma questão de vida).
Context for Dialogue

Situation: Two travelers, Sam and Maria, are sitting in a hostel common area, discussing their journeys.

Focus: Using What motivates you, ultimate goal, figure out, and vulnerability.
Dialogue: The Inner Journey

Sam: So, you’ve been traveling for a year. I’m curious: What motivates you to keep moving? Maria: Well, I guess it’s the need to keep learning, you know (Pílula 49). I feel like I'm still trying to figure out who I am outside of my old job. Sam: That makes sense. That's a huge shift. Maria: Yeah, I mean, it was terrifying at first. What about you? What's your ultimate goal for this trip? Sam: To be honest, I want to learn a new language and start my fully remote (Pílula 54) business. The big takeaway (Pílula 44) for me is that life is too short to be stuck in one place. Maria: That's a really great answer. Thanks for your vulnerability.

Review for Audio

Read the summary below aloud to practice your pronunciation and fluency. Send the audio to your professor!

"Today I learned how to ask deep questions. I know how to ask about motivation using 'What motivates you to keep moving?' and about life goals using 'What's your ultimate goal?'. I also learned verbs like 'figure out' (descobrir) and 'deal with' (lidar com). When someone gives a good answer, I should thank them for their 'vulnerability' and offer my answer to keep the conversation reciprocal."
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
