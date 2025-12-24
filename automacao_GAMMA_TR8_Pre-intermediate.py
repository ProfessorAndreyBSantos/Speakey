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
Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 01, Tema Central: Expanding Likes: "I enjoy..."
Imagem de person smiling broadly while listening to music with headphones, vibrant and happy atmosphere, white backgroundAbre em uma nova janela

person smiling broadly while listening to music with headphones, vibrant and happy atmosphere, white background
Expanding Likes: "I enjoy..."
Social English - Pill 01

Você já sabe usar "I like". Agora, vamos expandir seu vocabulário para expressar seus gostos de forma mais variada e natural.
Imagem de notebook with the words I like crossed out and new words being written, minimalist styleAbre em uma nova janela

notebook with the words I like crossed out and new words being written, minimalist style
Por que variar?

Dizer apenas "I like" o tempo todo pode parecer repetitivo.

Nesta pílula, você vai aprender três novas formas de dizer que gosta de algo:

    I enjoy...

    I love...

    I am really into...

Isso deixará seu inglês mais rico e interessante.
Imagem de person reading a book comfortably in a park, serene settingAbre em uma nova janela

person reading a book comfortably in a park, serene setting
A Estrutura: I enjoy

Usamos I enjoy para falar de atividades que nos dão prazer.

Regra de Ouro: Se você usar um verbo depois de "enjoy", ele precisa terminar em -ING.

Estrutura: Subject + enjoy + Verb-ing

Exemplo: I enjoy reading books. (Eu gosto de ler livros.)
Imagem de chef cooking with passion in a kitchen, dynamic actionAbre em uma nova janela
stablediffusionweb.com
chef cooking with passion in a kitchen, dynamic action
Exemplos com "I enjoy"

Observe o uso do -ing nos verbos de ação.

    I enjoy cooking for my friends on weekends. (Eu gosto de cozinhar para meus amigos nos fins de semana.)

    She enjoys watching horror movies at night. (Ela gosta de assistir filmes de terror à noite.)

    We enjoy walking in the park. (Nós gostamos de caminhar no parque.)

Imagem de red heart symbol, clean and simple designAbre em uma nova janela

red heart symbol, clean and simple design
A Estrutura: I love

I love é muito mais forte que "I like". Demonstra paixão ou um gosto muito intenso.

Pode ser usado com substantivos (coisas) ou verbos.

Exemplos:

    I love pizza. (Substantivo)

    I love traveling. (Verbo com -ing)

Imagem de person playing a guitar enthusiastically on a stageAbre em uma nova janela

person playing a guitar enthusiastically on a stage
Exemplos com "I love"

Use para coisas que você realmente adora.

    I love coffee in the morning. (Eu amo café de manhã.)

    They love playing soccer. (Eles amam jogar futebol.)

    My brother loves video games. (Meu irmão ama videogames.)

Imagem de person deeply focused and happy while painting on a canvasAbre em uma nova janela

person deeply focused and happy while painting on a canvas
A Expressão: I am really into...

Esta é uma forma mais informal e muito comum de dizer que você está interessado ou dedicado a algo no momento.

Significa "Eu curto muito" ou "Estou muito ligado em".

Estrutura: I am + really into + Noun / Verb-ing
Imagem de collection of vinyl records or photography cameras, representing a hobbyAbre em uma nova janela

collection of vinyl records or photography cameras, representing a hobby
Exemplos com "I am really into..."

Use em conversas casuais com amigos.

    I am really into photography right now. (Estou muito ligado em fotografia agora.)

    He is really into jazz music. (Ele curte muito música jazz.)

    Are you into sports? (Você curte esportes?)

Imagem de comparison chart showing three levels of intensity represented by battery barsAbre em uma nova janela

comparison chart showing three levels of intensity represented by battery bars
Resumo da Intensidade

Veja a diferença de intensidade e formalidade:

    I like... (Neutro/Básico)

    I enjoy... (Prazeroso/Formal ou Informal)

    I am really into... (Entusiasta/Informal)

    I love... (Muito forte/Intenso)

Imagem de checklist on a clipboard with a pencil, educational conceptAbre em uma nova janela

checklist on a clipboard with a pencil, educational concept
Vamos Praticar?

Qual a forma correta de completar a frase abaixo? Lembre-se da regra do "enjoy".

"I enjoy ______ to pop music."

A) listen B) listening C) to listen
Imagem de bright green checkmark indicating a correct answerAbre em uma nova janela
pngtree.com
bright green checkmark indicating a correct answer
Correção

A resposta correta é B.

Explicação: Após o verbo enjoy, o próximo verbo deve sempre estar no gerúndio (-ing).

Frase correta: "I enjoy listening to pop music."
Imagem de puzzle pieces being put together to form a sentenceAbre em uma nova janela
thefirstgraderoundup.com
puzzle pieces being put together to form a sentence
Desafio de Transformação

Transforme a frase abaixo usando "really into" para torná-la mais descolada/informal:

Frase original: "I like yoga very much."

A) I am really into yoga. B) I really into yoga. C) I am really enjoy yoga.
Imagem de person giving a thumbs up, signaling successAbre em uma nova janela

person giving a thumbs up, signaling success
Correção do Desafio

A resposta correta é A.

Explicação: A estrutura exige o verbo to be (am/is/are).

Correto: I am really into yoga.

(A opção B falta o "am", e a C mistura duas estruturas incorretamente).
Imagem de two friends talking in a coffee shop, casual settingAbre em uma nova janela

two friends talking in a coffee shop, casual setting
Dialogue: Hobbies

Veja como usar essas expressões em uma conversa real.

Sarah: So, what do you do on weekends? Mark: Well, I enjoy hiking in the mountains. It is very relaxing. Sarah: That is cool. I am really into cycling lately. Mark: Nice! And do you like camping? Sarah: Oh yes, I love sleeping under the stars!
Imagem de microphone icon, symbolizing audio recordingAbre em uma nova janela

microphone icon, symbolizing audio recording
Review for Audio

Leia o texto abaixo em voz alta para praticar sua pronúncia e fluidez. Tente demonstrar entusiasmo nas partes em negrito!

"Hello! My name is [Your Name]. I want to tell you about my likes. I enjoy learning English every day because it is useful. I am really into movies and series right now. Also, I love meeting new people. What about you? What do you enjoy doing?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 02, Tema Central: Expanding Dislikes: "I can't stand..."
Imagem de person with a frustrated facial expression covering their ears due to noiseAbre em uma nova janela

person with a frustrated facial expression covering their ears due to noise
Expanding Dislikes: "I can't stand..."
Social English - Pill 02

Você já sabe dizer "I don't like". Mas e quando você detesta algo? Quando algo te irrita profundamente?

Hoje vamos aprender a expressar desagrado forte.
Imagem de traffic jam seen through a car windshield, symbolizing annoyanceAbre em uma nova janela

traffic jam seen through a car windshield, symbolizing annoyance
Além do "I don't like"

Às vezes, "I don't like" é muito fraco.

Para expressar intolerância ou irritação forte, usamos a expressão:

"I can't stand..."

Isso significa "Eu não suporto" ou "Eu não aguento".
Imagem de person pushing away a plate of food with a look of disgustAbre em uma nova janela

person pushing away a plate of food with a look of disgust
A Estrutura: I can't stand

Assim como "I enjoy", esta expressão segue regras específicas dependendo do que vem depois.

    Com Substantivos (Coisas): I can't stand traffic. (Eu não suporto trânsito.)

    Com Verbos (Ações): O verbo deve ter -ING. I can't stand waiting. (Eu não suporto esperar.)

Imagem de person looking at a clock impatiently in a waiting roomAbre em uma nova janela

person looking at a clock impatiently in a waiting room
Exemplos com Verbos (-ING)

Lembre-se: Se é uma ação, use o gerúndio.

    I can't stand waking up early. (Eu não suporto acordar cedo.)

    She can't stand doing the dishes. (Ela não suporta lavar a louça.)

    They can't stand losing. (Eles não suportam perder.)

Imagem de mosquito buzzing near someone's ear, representing annoyanceAbre em uma nova janela

mosquito buzzing near someone's ear, representing annoyance
Outra Opção: It drives me crazy!

Quando algo te deixa muito irritado ou "louco" de raiva, usamos:

"It drives me crazy."

    Loud music drives me crazy. (Música alta me deixa louco.)

    Slow internet drives me crazy. (Internet lenta me deixa louco.)

Imagem de polite person declining a drink with a gentle hand gestureAbre em uma nova janela

polite person declining a drink with a gentle hand gesture
Suavizando: "I am not a fan of..."

Se você quer dizer que não gosta, mas sem ser rude ou agressivo, use:

"I am not a fan of..."

É uma forma educada de dizer "Não sou muito fã de...".

    I am not a fan of horror movies.

    I am not a fan of sushi.

Imagem de scale showing emotional intensity from mild dislike to extreme hateAbre em uma nova janela
en.wikipedia.org
scale showing emotional intensity from mild dislike to extreme hate
Escala de Desagrado

Do mais educado ao mais intenso:

    I am not a fan of... (Educado/Suave)

    I don't like... (Neutro)

    I hate... (Forte)

    I can't stand... (Muito forte/Intolerável)

    It drives me crazy! (Irritação extrema)

Imagem de person looking annoyed at a messy roomAbre em uma nova janela

person looking annoyed at a messy room
I hate vs I can't stand

Eles são parecidos, mas têm nuances.

    I hate: Foca no sentimento de ódio/aversão. "I hate winter."

    I can't stand: Foca na incapacidade de tolerar a situação. "I can't stand this cold." (Preciso sair daqui agora!)

Imagem de messy desk with papers everywhereAbre em uma nova janela
www.roadrunnerwm.com
messy desk with papers everywhere
Contexto: Mess (Bagunça)

Vamos ver como aplicar isso a uma situação de bagunça.

    Polite: I am not a fan of mess.

    Direct: I don't like mess.

    Strong: I can't stand mess.

    Extreme: This mess drives me crazy!

Imagem de people arguing or speaking loudly on phones in a cinemaAbre em uma nova janela

people arguing or speaking loudly on phones in a cinema
Exemplos de Situações Irritantes

Use essas frases para reclamar (com amigos!):

    I can't stand rude people.

    People talking in the cinema drives me crazy.

    I can't stand working on weekends.

Imagem de worksheet with a multiple choice question highlightedAbre em uma nova janela
www.chegg.com
worksheet with a multiple choice question highlighted
Vamos Praticar?

Qual a forma gramaticalmente correta de completar a frase?

"My boss is terrible. I can't stand ______ with him."

A) work B) to work C) working
Imagem de green checkmark symbol indicating successAbre em uma nova janela
pngtree.com
green checkmark symbol indicating success
Correção

A resposta correta é C.

Explicação: A expressão can't stand exige que o verbo seguinte esteja no formato -ING.

Frase correta: "My boss is terrible. I can't stand working with him."
Imagem de two distinct scenarios: one polite dinner and one angry moment in trafficAbre em uma nova janela
www.childrensmovementflorida.org
two distinct scenarios: one polite dinner and one angry moment in traffic
Desafio de Contexto

Você está em um jantar formal com o chefe do seu marido/esposa. Oferecem um prato que você odeia. Qual frase é a mais adequada socialmente?

A) I can't stand this food. B) I am not a fan of this dish, thank you. C) This food drives me crazy.
Imagem de polite smile and a hand on chest gestureAbre em uma nova janela
www.freepik.com
polite smile and a hand on chest gesture
Correção do Desafio

A resposta correta é B.

Explicação:

    I am not a fan of... é a forma polida e socialmente aceita para recusar algo ou expressar desagrado em situações formais. As outras opções (A e C) soariam muito rudes.

Imagem de two friends venting to each other, sitting on a sofaAbre em uma nova janela
www.universityofcalifornia.edu
two friends venting to each other, sitting on a sofa
Dialogue: Venting (Desabafando)

Tom: How is your new apartment? Lisa: It is nice, but the neighbors are noisy. It drives me crazy! Tom: Oh no. I can't stand noisy neighbors. Lisa: Me neither. And I am not a fan of the location either. It is too far from work. Tom: That is annoying. I hate commuting for a long time.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo com emoção. Tente parecer irritado nas frases em negrito e educado na última frase.

"Let me tell you about things I dislike. First, I can't stand cold weather. It makes me sad. Second, heavy traffic drives me crazy in the morning! I also hate waiting in long lines at the bank. But, to be polite, let's just say I am not a fan of wasting time."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 03, Tema Central: Music Genres & Preferences
Imagem de colorful collage of musical instruments including a guitar, saxophone, violin, and a synthesizerAbre em uma nova janela

colorful collage of musical instruments including a guitar, saxophone, violin, and a synthesizer
Music Genres & Preferences
Social English - Pill 03

Música é um dos melhores tópicos para iniciar conversas ("small talk").

Hoje vamos aprender a falar sobre os estilos que você gosta e a descrever músicas usando os adjetivos corretos.
Imagem de smartphone screen showing a music playlist with diverse icons representing different stylesAbre em uma nova janela

smartphone screen showing a music playlist with diverse icons representing different styles
Common Music Genres

Primeiro, vamos garantir a pronúncia e o vocabulário dos estilos mais comuns:

    Pop: Música popular, comercial.

    Rock: Guitarras, bateria.

    Hip-hop / Rap: Rimas, batida forte.

    R&B: Rhythm and Blues.

    EDM: Electronic Dance Music (Eletrônica).

Imagem de classical orchestra performing on a stageAbre em uma nova janela
www.kennedy-center.org
classical orchestra performing on a stage
More Genres

Outros estilos importantes:

    Classical: Mozart, Beethoven (Não diga "Classic music", diga "Classical music").

    Jazz: Saxofone, improviso.

    Country: Violão, estilo rural (comum nos EUA).

    Reggae: Ritmo jamaicano.

    Folk: Música tradicional/acústica.

Imagem de person dancing happily with headphones onAbre em uma nova janela

person dancing happily with headphones on
Adjectives: Upbeat & Catchy

Como descrever a música?

    Upbeat: Música feliz, com ritmo rápido, que levanta o ânimo.

        "I need some upbeat music for the gym."

    Catchy: Música que "pega", que fica na cabeça.

        "This song is so catchy, I can't stop singing it."

Imagem de person lying on a sofa looking peaceful listening to musicAbre em uma nova janela

person lying on a sofa looking peaceful listening to music
Adjectives: Relaxing & Soothing

Para músicas mais calmas:

    Relaxing: Que relaxa.

        "Jazz is very relaxing after work."

    Soothing: Que acalma, alivia o estresse (muito usado para música clássica ou sons da natureza).

        "Her voice is very soothing."

Imagem de heavy metal band playing with energy and loud speakersAbre em uma nova janela
www.loopearplugs.com
heavy metal band playing with energy and loud speakers
Adjectives: Heavy & Loud

Para estilos mais agressivos:

    Heavy: Pesado (ritmo denso, guitarras distorcidas).

        "I don't like heavy metal."

    Loud: Alto (volume ou intensidade).

        "The music at the club was too loud."

Imagem de slice of cheese next to a CD, representing the slang termAbre em uma nova janela
en.wikipedia.org
slice of cheese next to a CD, representing the slang term
Slang: Cheesy

Uma gíria muito comum para música (e filmes):

Cheesy: Brega, clichê, exageradamente sentimental, mas às vezes divertido.

    "I love 80s pop ballads, even though they are a bit cheesy." (Eu amo baladas dos anos 80, mesmo sendo um pouco bregas.)

Imagem de two people talking with question marks floating above themAbre em uma nova janela

two people talking with question marks floating above them
Asking about Taste

Como perguntar sobre gosto musical?

    "What kind of music are you into?" (Mais natural)

    "What sort of music do you like?"

    "Who is your favorite artist/band?"

    "Do you play any instruments?"

Imagem de person shaking their head 'no' politelyAbre em uma nova janela

person shaking their head 'no' politely
Expressing Preferences

Use o vocabulário das lições anteriores:

    "I'm really into Indie Rock."

    "I mostly listen to Podcasts, actually."

    "I'm not a big fan of Techno. It's too repetitive."

    "I have eclectic taste. I listen to everything."

Imagem de ticket for a live showAbre em uma nova janela
www.pond5.com
ticket for a live show
Live Music Vocabulary

    Gig: Um show pequeno ou informal (muito usado no Reino Unido e entre músicos).

        "My friend has a gig at the bar tonight."

    Concert: Um show grande, em arena ou estádio.

        "I went to a Beyoncé concert."

    Live: Ao vivo.

        "I prefer listening to live music."

Imagem de quiz sheet with a multiple choice questionAbre em uma nova janela
www.zipgrade.com
quiz sheet with a multiple choice question
Vamos Praticar?

Escolha o adjetivo correto para a situação:

"I can't get this song out of my head! The melody is so _______."

A) heavy B) catchy C) cheesy
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: Catchy é o adjetivo usado para descrever músicas "chiclete", fáceis de lembrar e que grudam na cabeça.
Imagem de sentence with a missing word related to music genresAbre em uma nova janela
www.teacherspayteachers.com
sentence with a missing word related to music genres
Desafio de Vocabulário

Qual a palavra correta para completar a frase?

"Mozart is a famous composer of _______ music."

A) Classic B) Classical C) Classy
Imagem de bust of a classical composer like Beethoven or MozartAbre em uma nova janela
www.etsy.com
bust of a classical composer like Beethoven or Mozart
Correção do Desafio

A resposta correta é B.

Explicação: Em inglês, o gênero musical é sempre Classical Music. Classic refere-se a algo que é um clássico (ex: "A classic car"), mas não ao gênero erudito.
Imagem de two friends sharing earphones, smilingAbre em uma nova janela
www.alamy.com
two friends sharing earphones, smiling
Dialogue: Sharing Music

Alex: Hey, what kind of music are you into? Bia: I listen to a lot of R&B and Soul. It is very relaxing. And you? Alex: I prefer Rock. I like upbeat music to give me energy. Bia: Do you like Heavy Metal? Alex: No, that is too loud for me. I prefer 90s Rock. Bia: Cool. Sometimes I listen to 90s Pop, but it is a bit cheesy!
Imagem de microphone icon symbolizing speech practiceAbre em uma nova janela

microphone icon symbolizing speech practice
Review for Audio

Leia o texto abaixo para treinar os nomes dos estilos e adjetivos.

"I have eclectic taste in music. Sometimes I want something upbeat, so I listen to Pop or Hip-hop. It makes me want to dance. But when I am tired, I prefer Classical music because it is soothing. Honestly, the only thing I can't stand is Heavy Metal. It is just too loud for my ears!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 04, Tema Central: Movies & TV Shows Types
Imagem de bucket of popcorn and a remote control on a sofa, cozy movie night atmosphereAbre em uma nova janela

bucket of popcorn and a remote control on a sofa, cozy movie night atmosphere
Movies & TV Shows Types
Social English - Pill 04

"Have you seen anything good lately?"

Discutir filmes e séries é essencial para a vida social. Hoje, vamos aprender os nomes corretos dos gêneros para você poder descrever o que gosta de assistir.
Imagem de dramatic masks representing comedy and tragedy, theatre conceptAbre em uma nova janela

dramatic masks representing comedy and tragedy, theatre concept
The Big Three: Action, Comedy, Drama

Os gêneros mais comuns:

    Action: Carros rápidos, lutas, explosões.

        "I love action movies like Mission Impossible."

    Comedy: Filmes feitos para rir.

        "We need a comedy to cheer us up."

    Drama: Histórias sérias, emocionais e realistas.

        "This drama made me cry."

Imagem de dark forest with fog, creating a spooky and mysterious atmosphereAbre em uma nova janela

dark forest with fog, creating a spooky and mysterious atmosphere
Horror vs. Thriller

Muitos alunos confundem estes dois:

    Horror: O objetivo é assustar, causar medo (monstros, fantasmas, sangue).

        "I can't watch horror movies alone."

    Thriller: O objetivo é criar tensão e suspense (mistérios policiais, crimes). Você fica ansioso para saber o final.

        "That psychological thriller was intense!"

Imagem de spaceship flying near a planet or a futuristic cityAbre em uma nova janela

spaceship flying near a planet or a futuristic city
Sci-Fi & Fantasy

Para mundos imaginários:

    Sci-Fi (Science Fiction): Tecnologia futurista, espaço, alienígenas. (Pronúncia: "Sai-Fai").

        "Star Wars is a famous Sci-Fi movie."

    Fantasy: Magia, dragões, mundos medievais.

        "Lord of the Rings is a classic fantasy film."

Imagem de couple holding hands in a park, romantic silhouetteAbre em uma nova janela

couple holding hands in a park, romantic silhouette
Romance & Rom-Com

    Romance: Foco no amor e relacionamento sério.

        "The Notebook is a sad romance."

    Rom-Com (Romantic Comedy): Uma mistura de história de amor com situações engraçadas. É leve e divertido.

        "I love watching rom-coms on rainy days."

Imagem de film camera recording a real life nature sceneAbre em uma nova janela

film camera recording a real life nature scene
Documentary & Biopic

Para histórias reais:

    Documentary: Fatos reais, entrevistas, natureza ou história. Não tem atores atuando (geralmente).

        "I watched a documentary about lions."

    Biopic: Um filme dramatizado sobre a vida de uma pessoa famosa (Biography Picture).

        "Elvis is a biopic about the singer."

Imagem de classic living room set setup typical of a TV show with a laughter audience conceptAbre em uma nova janela
kendallrivers.medium.com
classic living room set setup typical of a TV show with a laughter audience concept
TV Series Specifics: Sitcoms

Na TV, temos um gênero muito específico:

Sitcom (Situation Comedy): Séries de comédia com episódios curtos (20 min), geralmente gravadas em estúdio e com risadas de fundo.

Exemplos clássicos: Friends, The Office, Seinfeld.

    "My favorite sitcom is Friends."

Imagem de animated character sketch or storyboardAbre em uma nova janela
superpixel.sg
animated character sketch or storyboard
Animation / Cartoon

Animation é o termo geral para filmes feitos por computador ou desenho.

    Cartoon: Geralmente usado para desenhos mais infantis ou de TV.

    Anime: Animação japonesa específica.

    "Pixar makes great animations for both kids and adults."

Imagem de clapperboard with scene information written on itAbre em uma nova janela
www.studiobinder.com
clapperboard with scene information written on it
Vocabulário de Estrutura

Ao falar de séries, usamos:

    Series / TV Show: O programa em si.

    Season: A temporada (Season 1, Season 2).

    Episode: O capítulo individual.

    Plot: O enredo, a história do filme.

    "I am watching the second season of Stranger Things."

Imagem de multiple choice quiz question on a screenAbre em uma nova janela

multiple choice quiz question on a screen
Vamos Praticar?

Qual gênero melhor descreve um filme com naves espaciais, robôs e futuro?

A) Fantasy B) Sci-Fi C) Thriller
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: Sci-Fi (Science Fiction) lida com ciência e futuro. Fantasy lida com magia e passado. Thriller lida com suspense e crime.
Imagem de word puzzle game with missing lettersAbre em uma nova janela
www.puzzles-world.com
word puzzle game with missing letters
Desafio de Definição

Qual é o nome do gênero que mistura romance e comédia?

A) Com-Rom B) Rom-Com C) Love-Laugh
Imagem de heart and a smiling face symbol combinedAbre em uma nova janela

heart and a smiling face symbol combined
Correção do Desafio

A resposta correta é B.

Explicação: A abreviação correta e muito usada em inglês é Rom-Com (Romantic Comedy).
Imagem de couple sitting on a couch with a remote control, looking at a TV screen, choosing something to watchAbre em uma nova janela
www.alamy.com
couple sitting on a couch with a remote control, looking at a TV screen, choosing something to watch
Dialogue: Choosing a Movie

Carol: Shall we watch a movie tonight? Dan: Sure. What are you in the mood for? Carol: I want something funny. Maybe a Rom-Com? Dan: Hmm, I prefer Action or Sci-Fi. Carol: We watched Action yesterday. How about a Sitcom? We can watch a few episodes of "The Office". Dan: Perfect! I love that show. It is hilarious.
Imagem de microphone icon aimed at the user for audio recordingAbre em uma nova janela
pikbest.com
microphone icon aimed at the user for audio recording
Review for Audio

Leia o texto abaixo para praticar a pronúncia dos gêneros.

"I love talking about movies. My favorite genre is Sci-Fi because I like stories about the future. However, my girlfriend prefers Rom-Coms. We usually compromise and watch a Thriller. On weekends, I like to watch Sitcoms because they are short and funny. I rarely watch Horror movies because I get scared easily!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 05, Tema Central: Discussing a Movie Plot
Imagem de film reel unwinding to tell a story, cinematic atmosphereAbre em uma nova janela

film reel unwinding to tell a story, cinematic atmosphere
Discussing a Movie Plot
Social English - Pill 05

Quando alguém pergunta "What is the movie about?", você precisa saber resumir a história sem contar o final.

Hoje vamos aprender a descrever o enredo (plot) de um filme de forma interessante.
Imagem de person putting a finger to their lips in a shushing gesture, secret conceptAbre em uma nova janela
www.alamy.com
person putting a finger to their lips in a shushing gesture, secret concept
The Plot vs The Spoiler

    The Plot: É a história, o enredo, o que acontece no filme.

    A Spoiler: É quando você conta uma parte crucial do final ou uma surpresa que estraga a experiência para quem não viu.

Regra de Ouro: Antes de falar demais, pergunte: "Do you mind spoilers?" (Você se importa com spoilers?)
Imagem de vintage map or a futuristic city skyline, representing settingAbre em uma nova janela

vintage map or a futuristic city skyline, representing setting
Setting the Scene: "It is set in..."

Para começar, diga onde e quando a história acontece.

Use a estrutura: "It is set in [Place] in [Time]."

Exemplos:

    "The movie is set in New York in the 1990s."

    "It is set in a fantasy world."

    "It is set in the future."

Imagem de silhouette of a hero looking at a mountain, representing the protagonistAbre em uma nova janela

silhouette of a hero looking at a mountain, representing the protagonist
The Protagonist: "It is about..."

Depois do cenário, introduza o personagem principal.

Use: "It is about [Character] who..."

Exemplos:

    "It is about a detective who tries to solve a crime."

    "It is about two friends who go on a road trip."

    "It is about an alien who wants to go home."

Imagem de person facing a giant obstacle or monster, representing conflictAbre em uma nova janela

person facing a giant obstacle or monster, representing conflict
The Conflict: "He/She has to..."

Toda história tem um problema. Descreva o desafio principal usando verbos de ação.

Exemplos:

    "He has to save the world from a virus."

    "She tries to find her lost parents."

    "They must escape from a haunted house."

Imagem de open book transforming into a film stripAbre em uma nova janela
samplechaps.com
open book transforming into a film strip
Origin: "It is based on..."

Muitos filmes vêm de livros ou fatos reais.

    "It is based on a true story." (Baseado em fatos reais).

    "It is based on a novel by Stephen King." (Baseado num romance/livro).

    "It is a remake of an old movie." (É uma refilmagem).

Imagem de twisted road sign or a maze, symbolizing a plot twistAbre em uma nova janela

twisted road sign or a maze, symbolizing a plot twist
Useful Vocabulary

Palavras úteis para enriquecer sua descrição:

    The Villain: O vilão, o "bad guy".

    A Twist: Uma reviravolta surpresa na história.

    The Soundtrack: A música do filme.

    The Cast: Os atores (o elenco).

Imagem de person crying watching a screen and another person sitting on the edge of their seatAbre em uma nova janela
www.peacefulparent.com
person crying watching a screen and another person sitting on the edge of their seat
Adjectives for Plots

Como descrever a experiência da história?

    Moving: Emocionante, que faz chorar.

        "It is a very moving story."

    Gripping: Tão interessante que prende sua atenção totalmente.

        "The plot is gripping from start to finish."

    Slow: Lento, um pouco chato.

        "The beginning is a bit slow."

Imagem de three blocks connecting to each other forming a flowAbre em uma nova janela
www.youtube.com
three blocks connecting to each other forming a flow
The 3-Step Formula

Para não se perder, use esta fórmula simples ao falar:

    Setting: "It is set in Paris..."

    Character: "It is about a chef..."

    Conflict: "Who falls in love with a critic."

Simples e direto!
Imagem de quiz question displayed on a tablet screenAbre em uma nova janela

quiz question displayed on a tablet screen
Vamos Praticar?

Qual a preposição correta para falar do local/tempo do filme?

"The film is set ______ World War II."

A) on B) at C) in
Imagem de bright green checkmark indicating correct answerAbre em uma nova janela

bright green checkmark indicating correct answer
Correção

A resposta correta é C.

Explicação: Usamos IN para períodos de tempo (anos, eras, séculos) e para cidades/países.

Frase correta: "The film is set in World War II."
Imagem de person looking surprised with hands on cheeksAbre em uma nova janela

person looking surprised with hands on cheeks
Desafio de Vocabulário

Qual a palavra usada para descrever uma "mudança surpresa" na história?

A) A turn B) A twist C) A spin
Imagem de spiral symbol representing a twistAbre em uma nova janela
www.freepik.com
spiral symbol representing a twist
Correção do Desafio

A resposta correta é B.

Explicação: Chamamos uma reviravolta no enredo de Plot Twist ou apenas Twist.

Exemplo: "The ending has a huge twist!"
Imagem de two friends chatting with popcorn in handAbre em uma nova janela

two friends chatting with popcorn in hand
Dialogue: Summarizing

Tom: What is your favorite movie? Ana: I love "Titanic". Tom: What is it about? Ana: Well, it is set in 1912 on a huge ship. It is about a rich girl and a poor artist who fall in love. Tom: And what happens? Ana: They have to survive when the ship hits an iceberg. It is very moving. It is based on a true story.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Descreva o filme "O Rei Leão" (ou outro que preferir) seguindo o modelo.

"My favorite movie is The Lion King. It is set in Africa. It is about a young lion cub named Simba who loses his father. He has to fight his evil uncle to become King. The story is very moving and the soundtrack is amazing. It is based on Hamlet by Shakespeare!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 06, Tema Central: Sports: "Play" vs "Go" vs "Do"
Imagem de varied sports equipment: a ball, a yoga mat, and running shoes arranged neatlyAbre em uma nova janela

varied sports equipment: a ball, a yoga mat, and running shoes arranged neatly
Sports: Play, Go, or Do?
Social English - Pill 06

Em inglês, não dizemos apenas "practice sports" para tudo.

Existem três verbos principais para falar de esportes: Play, Go e Do.

Usar o verbo errado (como "I make yoga" ou "I play swimming") soa muito estranho para um nativo. Vamos aprender a regra!
Imagem de soccer ball and a basketball on a courtAbre em uma nova janela

soccer ball and a basketball on a court
1. The Verb "Play"

Usamos Play para:

    Esportes com bola (Ball games).

    Esportes de time (Team sports).

    Jogos competitivos contra um oponente.

Se tem bola ou é um jogo com regras de vitória/derrota, geralmente é Play.
Imagem de people playing tennis or volleyball, action shotAbre em uma nova janela

people playing tennis or volleyball, action shot
Exemplos com "Play"

    I play soccer every Wednesday. (Eu jogo futebol toda quarta.)

    Do you play tennis? (Você joga tênis?)

    We play basketball at school. (Nós jogamos basquete na escola.)

    They play golf on Sundays. (Eles jogam golfe aos domingos.)

Imagem de person swimming in a pool or running on a trackAbre em uma nova janela
www.swimmingworldmagazine.com
person swimming in a pool or running on a track
2. The Verb "Go"

Usamos Go para:

    Atividades que terminam em -ING.

    Esportes que envolvem deslocamento (ir de um lugar a outro).

A estrutura é: Go + Verb-ing.
Imagem de skier going down a snowy mountain or a surfer on a waveAbre em uma nova janela
www.outdoorjapan.com
skier going down a snowy mountain or a surfer on a wave
Exemplos com "Go"

    I go swimming in the morning. (Eu vou nadar/faço natação de manhã.)

    She loves to go running. (Ela ama correr.)

    Let's go hiking this weekend. (Vamos fazer trilha neste fim de semana.)

    They go skiing in winter. (Eles vão esquiar no inverno.)

Imagem de person in a karate pose or doing a stretching exerciseAbre em uma nova janela
www.alamy.com
person in a karate pose or doing a stretching exercise
3. The Verb "Do"

Usamos Do para:

    Esportes individuais.

    Artes marciais.

    Atividades recreativas sem bola.

    Exercícios focados no corpo.

Imagem de yoga mat and weights in a gym settingAbre em uma nova janela

yoga mat and weights in a gym setting
Exemplos com "Do"

    My mother does yoga. (Minha mãe faz ioga.)

    He does karate/judo. (Ele faz karatê/judô.)

    I need to do some exercise. (Preciso fazer algum exercício.)

    They do gymnastics. (Eles fazem ginástica.)

Imagem de modern gym building exterior or interior with machinesAbre em uma nova janela

modern gym building exterior or interior with machines
Cuidado: The Gym

A palavra "Gym" (academia) é um lugar, não um esporte.

Por isso dizemos:

    "I go to the gym." (Eu vou para a academia).

Mas lá dentro, você faz a ação:

    "I work out." (Eu malho/treino).

Não diga "I play gym".
Imagem de chart dividing sports into three columns visuallyAbre em uma nova janela
www.datylon.com
chart dividing sports into three columns visually
Summary Table

Para memorizar rápido:
PLAY (Ball/Team)	GO (-ING)	DO (Individual)
Soccer	Swimming	Yoga
Tennis	Running	Karate
Basketball	Hiking	Judo
Volleyball	Dancing	Aerobics
Golf	Bowling	Pilates
Imagem de multiple choice question displayed on a digital screenAbre em uma nova janela
www.craiyon.com
multiple choice question displayed on a digital screen
Vamos Praticar? - Exercício 1

Escolha o verbo correto para completar a frase:

"My friends and I love to ______ volleyball on the beach."

A) go B) do C) play
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Volleyball é um esporte com bola e de time. Portanto, usamos Play.

"My friends and I love to play volleyball."
Imagem de person holding a yoga mat looking confusedAbre em uma nova janela
www.freepik.com
person holding a yoga mat looking confused
Vamos Praticar? - Exercício 2

Qual a frase gramaticalmente correta?

A) She plays yoga every day. B) She goes yoga every day. C) She does yoga every day.
Imagem de person meditating in a yoga pose, peaceful atmosphereAbre em uma nova janela

person meditating in a yoga pose, peaceful atmosphere
Correção - Exercício 2

A resposta correta é C.

Explicação: Yoga é uma atividade individual, sem bola e focada no corpo. Usamos Do.

"She does yoga every day."
Imagem de two friends talking, holding sports gearAbre em uma nova janela

two friends talking, holding sports gear
Dialogue: Active Lifestyle

Paul: You look fit! Do you go to the gym? Mike: No, I prefer outdoor sports. I go running in the park every morning. Paul: That's great. I am lazy. I only play video games. Mike: You should join me! Or maybe we can play tennis sometime? Paul: Tennis? I am terrible at it. Maybe I can do yoga to relax instead.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo para fixar as colocações (collocations) corretas.

"I have a very active routine. On Mondays, I go swimming before work. On Wednesdays, I do karate to relieve stress. And on weekends, I usually play soccer with my friends. Sometimes, if it rains, we just play cards at home. I love to do exercise!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 07, Tema Central: Talking about Gym/Fitness
Imagem de modern gym interior with various machines and weights, clean and brightAbre em uma nova janela

modern gym interior with various machines and weights, clean and bright
Talking about Gym & Fitness
Social English - Pill 07

Ir à academia ("Gym") é um assunto muito comum.

Mas como dizer "fazer esteira", " puxar ferro" ou "estou dolorido" em inglês?

Nesta pílula, vamos aprender o vocabulário essencial para o seu treino.
Imagem de person lifting a dumbbell focusing on the actionAbre em uma nova janela

person lifting a dumbbell focusing on the action
Work out vs Exercise

Esses dois termos são parecidos, mas usados de formas diferentes:

    To work out: Usado especificamente para exercícios físicos estruturados (academia, treino).

        "I work out three times a week." (Eu treino três vezes por semana).

    To exercise: Mais geral, qualquer atividade física.

        "Doctors say we must exercise regularly."

Nota: O substantivo é "Workout" (O treino).

    "That was a great workout!"

Imagem de person stretching their arms and legs before a runAbre em uma nova janela

person stretching their arms and legs before a run
The Warm Up & Stretching

Antes de começar pesado, você precisa preparar o corpo.

    Warm up: Aquecer.

        "Always warm up before running."

    Stretch: Alongar.

        "Don't forget to stretch your legs."

Imagem de heart icon representing cardio and a dumbbell icon representing strengthAbre em uma nova janela

heart icon representing cardio and a dumbbell icon representing strength
Cardio vs Weightlifting

Dois tipos principais de treino:

    Cardio: Exercícios para o coração (correr, pular).

        "I hate cardio, I prefer weights."

    Lifting weights / Weight training: "Puxar ferro", musculação.

        "He is lifting weights to get strong."

Imagem de treadmill machine in a gym settingAbre em uma nova janela
www.puregym.com
treadmill machine in a gym setting
The Treadmill

A máquina mais comum da academia não se chama "running machine".

O nome correto é Treadmill (Esteira).

    "I run on the treadmill for 20 minutes."

Imagem de person doing squats or pushups, bodyweight exerciseAbre em uma nova janela
www.eatthis.com
person doing squats or pushups, bodyweight exercise
Sets & Reps

Como descrever a contagem do exercício?

    Reps (Repetitions): Quantas vezes você faz o movimento.

    Sets: As séries (conjunto de repetições).

Exemplo:

    "I do 3 sets of 10 reps." (Eu faço 3 séries de 10 repetições.)

Imagem de muscular person and a person holding a belly, contrast illustrationAbre em uma nova janela

muscular person and a person holding a belly, contrast illustration
In Shape vs Out of Shape

Como descrever o condicionamento físico?

    Fit / In shape: Em forma, condicionado.

        "She is very fit."

    Out of shape: Fora de forma, sedentário.

        "I get tired easily because I am out of shape."

Imagem de person holding their shoulder or leg with a pained expression after exerciseAbre em uma nova janela

person holding their shoulder or leg with a pained expression after exercise
I am Sore!

Depois de um treino pesado, seus músculos doem.

Não dizemos "I have muscle pain" (embora entendam). O mais natural é:

"I am sore."

    "My legs are so sore from yesterday's workout."

Imagem de person sweating profoundly, wiping forehead with a towelAbre em uma nova janela

person sweating profoundly, wiping forehead with a towel
Sweat vs Sweet

Cuidado com a pronúncia!

    Sweat (Suor/Suar): Pronuncia-se "Suét".

        "I am sweating a lot!"

    Sweet (Doce): Pronuncia-se "Suít".

        "This cake is sweet."

Imagem de protein shake bottle and a healthy mealAbre em uma nova janela
www.blenderbottle.com
protein shake bottle and a healthy meal
Gym Goals

Por que você treina?

    To lose weight: Perder peso / emagrecer.

    To build muscle: Ganhar músculo.

    To get ripped/shredded: Ficar "trincado" (Gíria de academia).

    To stay healthy: Manter a saúde.

Imagem de multiple choice quiz graphicAbre em uma nova janela
www.vectorstock.com
multiple choice quiz graphic
Vamos Praticar?

Qual a frase correta para dizer que você está fazendo esteira?

A) I am making treadmill. B) I am running on the treadmill. C) I am playing treadmill.
Imagem de green checkmark indicating successAbre em uma nova janela
freerangestock.com
green checkmark indicating success
Correção

A resposta correta é B.

Explicação: Você "corre" ou "anda" na esteira (on the treadmill). Não usamos "make" ou "play" para máquinas de academia.
Imagem de person looking stiff and walking with difficultyAbre em uma nova janela
my.clevelandclinic.org
person looking stiff and walking with difficulty
Desafio de Vocabulário

Complete a frase: "I worked out too hard yesterday. Today my muscles hurt. I am _______."

A) sorry B) sour C) sore
Imagem de muscle anatomy diagram highlighting sorenessAbre em uma nova janela
gym-mikolo.com
muscle anatomy diagram highlighting soreness
Correção do Desafio

A resposta correta é C.

Explicação:

    Sore: Dolorido (músculo).

    Sorry: Desculpe.

    Sour: Azedo.

Frase: "I am sore."
Imagem de two gym buddies talking near the water fountainAbre em uma nova janela
en.wikipedia.org
two gym buddies talking near the water fountain
Dialogue: Gym Bros

Leo: Hey man, good to see you. What are you training today? Max: Today is leg day. I am going to do some squats and run on the treadmill. Leo: Nice. I am focusing on building muscle, so I am just lifting weights. Max: Cool. Are you sore from last time? Leo: Yes, totally! My arms are killing me. I need to stretch more.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo para treinar a fluidez.

"I decided to get fit this year. I joined a gym and I go there to work out four times a week. I usually start with a warm up on the treadmill. Then, I lift weights. I do 3 sets of 12 reps. It is hard work and I sweat a lot. The next day, I am usually sore, but it feels good to be healthy!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 08, Tema Central: Reading & Books
Imagem de cozy reading corner with an open book and a cup of teaAbre em uma nova janela

cozy reading corner with an open book and a cup of tea
Reading & Books
Social English - Pill 08

Você gosta de ler? Hoje vamos expandir seu vocabulário para falar sobre livros, formatos e hábitos de leitura.

Seja você um leitor voraz ou casual, estas expressões vão ajudar na conversa.
Imagem de stack of physical books next to a tablet and a pair of headphonesAbre em uma nova janela

stack of physical books next to a tablet and a pair of headphones
Formats: Paper vs Digital

Hoje em dia, lemos de várias formas. Qual a sua favorita?

    Paperback: Livro de capa mole (o mais comum e barato).

    Hardcover: Livro de capa dura (mais caro e resistente).

    E-book: Livro digital (Kindle, iPad).

    Audiobook: Livro narrado em áudio.

    "I prefer reading paperbacks, but audiobooks are great for driving."

Imagem de library shelf showing two distinct sections labeled with symbols onlyAbre em uma nova janela
barkerbooks.com
library shelf showing two distinct sections labeled with symbols only
Fiction vs Non-Fiction

A grande divisão dos livros:

    Fiction: Histórias inventadas (Romances, Contos).

        Novel: É a palavra em inglês para "Romance" (livro de história longa). Não diga "Romance book" a menos que seja sobre amor.

    Non-Fiction: Fatos reais (História, Ciência, Biografias).

Imagem de four book covers representing Mystery, Biography, Selfhelp, and SciFiAbre em uma nova janela
booktrib.com
four book covers representing Mystery, Biography, Selfhelp, and SciFi
Common Genres

Alguns gêneros populares:

    Thriller / Mystery: Histórias de crime e suspense.

    Biography / Memoir: A vida de uma pessoa real.

    Self-help: Livros de autoajuda e desenvolvimento pessoal.

    Sci-Fi / Fantasy: Mundos imaginários (como vimos na pílula de filmes).

Imagem de person holding a book close to their face, looking intense and excitedAbre em uma nova janela

person holding a book close to their face, looking intense and excited
Describing a Good Book: "A Page-Turner"

Quando o livro é tão bom que você não consegue parar de ler (virar as páginas), dizemos:

"It is a real page-turner!"

Outra expressão útil: "I couldn't put it down." (Eu não conseguia largar).
Imagem de person falling asleep with an open book on their chestAbre em uma nova janela

person falling asleep with an open book on their chest
Describing a Difficult Book

E quando o livro é chato ou difícil?

    Heavy going: Difícil de ler, denso.

        "This history book is a bit heavy going."

    Slow: Quando a história demora para acontecer.

        "The beginning was slow, but it got better."

Imagem de cute worm wearing glasses coming out of an apple or book illustrationAbre em uma nova janela

cute worm wearing glasses coming out of an apple or book illustration
Idiom: Bookworm

Como chamamos alguém que ama ler e lê o tempo todo?

Em português: "Traça de livro" ou "Rato de biblioteca". Em inglês: Bookworm.

    "My sister reads 50 books a year. She is a total bookworm."

Imagem de one person giving a book to another personAbre em uma nova janela
www.alamy.com
one person giving a book to another person
Verbs: Borrow vs Lend

Cuidado para não confundir:

    Borrow: Pegar emprestado (Você recebe).

        "Can I borrow your book?"

    Lend: Emprestar (Você dá).

        "I can lend you my copy."

Imagem de two friends talking in a library or bookstoreAbre em uma nova janela

two friends talking in a library or bookstore
Asking about Habits

Perguntas para iniciar o assunto:

    "Do you read much?" (Você lê muito?)

    "What are you reading at the moment?" (O que está lendo no momento?)

    "Do you prefer paper books or e-books?"

    "Who is your favorite author?"

Imagem de multiple choice quiz layout on a screenAbre em uma nova janela

multiple choice quiz layout on a screen
Vamos Praticar?

Qual a palavra correta para um livro de história longa (ficção)?

"I am reading a fantastic ______ by Stephen King."

A) romance B) novel C) history
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: Em inglês, Novel significa romance (literatura/ficção longa). Romance refere-se especificamente ao gênero de histórias de amor. History é para fatos históricos.
Imagem de sentence with a missing verb related to booksAbre em uma nova janela
www.k12reader.com
sentence with a missing verb related to books
Desafio de Vocabulário

Você quer ler o livro do seu amigo. O que você diz?

"Hey, can I ______ that book when you finish it?"

A) lend B) borrow C) take out
Imagem de hand taking a book from another handAbre em uma nova janela
www.freepik.com
hand taking a book from another hand
Correção do Desafio

A resposta correta é B.

Explicação: Você quer pegar emprestado, então usa Borrow. Se você fosse o dono do livro oferecendo, usaria Lend.

Frase: "Can I borrow that book?"
Imagem de two people sitting in armchairs with books and coffeeAbre em uma nova janela

two people sitting in armchairs with books and coffee
Dialogue: Book Recommendations

Alice: What are you reading? Bob: It is a biography of Steve Jobs. It is fascinating. Alice: Is it easy to read? Bob: Yes, it is a real page-turner. I can't put it down. Are you reading anything? Alice: I am reading a novel, but it is a bit slow. Bob: Maybe I can lend you this one when I finish!
Imagem de microphone icon symbolizing audio practiceAbre em uma nova janela

microphone icon symbolizing audio practice
Review for Audio

Leia o texto abaixo para praticar o vocabulário de leitura.

"I admit, I am a huge bookworm. I read every night before bed. I usually prefer paperbacks because I like the smell of paper. Right now, I am reading a thriller that is a real page-turner. However, I sometimes read non-fiction too. If you need a recommendation, I can lend you my favorite novel."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 09, Tema Central: Video Games & Gaming
Imagem de modern video game controller next to a keyboard and mouse, sleek designAbre em uma nova janela

modern video game controller next to a keyboard and mouse, sleek design
Video Games & Gaming
Social English - Pill 09

Videogames não são mais coisa de criança; são uma das maiores indústrias do entretenimento.

Seja você um jogador casual ou "hardcore", é importante saber o vocabulário básico para conversar sobre seus jogos favoritos em inglês.
Imagem de icons representing a computer, a game console, and a smartphoneAbre em uma nova janela

icons representing a computer, a game console, and a smartphone
Platforms: Where do you play?

A primeira pergunta geralmente é sobre a plataforma.

    PC: Computador (Personal Computer).

    Console: PlayStation, Xbox, Nintendo Switch.

    Mobile: Celular ou Tablet.

    "I usually play on console, but sometimes on mobile."

Imagem de symbols representing different game genres: a sword, a gun, and a soccer ballAbre em uma nova janela

symbols representing different game genres: a sword, a gun, and a soccer ball
Common Genres (Types)

Existem muitos gêneros, mas estes são essenciais:

    FPS (First-Person Shooter): Jogos de tiro em primeira pessoa (ex: Call of Duty).

    RPG (Role-Playing Game): Jogos de evolução de personagem e história (ex: Final Fantasy).

    Sports: Futebol, Basquete (ex: FIFA, NBA).

    Battle Royale: Jogos de sobrevivência (ex: Fortnite).

Imagem de two people sitting side by side holding controllers, cooperative conceptAbre em uma nova janela
builtin.com
two people sitting side by side holding controllers, cooperative concept
Modes: Single vs Multiplayer

Como você joga? Sozinho ou com outros?

    Single-player: Um jogador (Modo história/campanha).

        "I prefer single-player games with a good story."

    Multiplayer: Vários jogadores online.

        "We played multiplayer all night."

    Co-op (Cooperative): Jogar junto com um amigo para vencer o jogo.

Imagem de character climbing a staircase or gaining a golden starAbre em uma nova janela

character climbing a staircase or gaining a golden star
Verbs: Level Up & Beat

Ações importantes dentro do jogo:

    To level up: Subir de nível, ficar mais forte.

        "I need to level up before the boss fight."

    To beat the game: Zerar o jogo (terminar a história).

        "It took me 50 hours to beat the game."

Nota: Não usamos "zero the game".
Imagem de computer screen showing a frozen image or a disconnect iconAbre em uma nova janela

computer screen showing a frozen image or a disconnect icon
Tech Problems: Lag & Glitch

Problemas técnicos comuns:

    Lag: Quando a internet está lenta e o jogo trava ou responde atrasado.

        "I can't play, I have too much lag!"

    Glitch / Bug: Um erro de programação no jogo (atravessar paredes, voar sem querer).

        "Look at this funny glitch!"

Imagem de novice player looking confused and a pro player looking confidentAbre em uma nova janela

novice player looking confused and a pro player looking confident
Gamer Slang: Noob vs Pro

Gírias universais dos jogos:

    Noob (Newbie): Um novato, alguém que joga mal ou está aprendendo.

        "Don't be a noob, learn the controls!"

    Pro: Profissional ou alguém que joga muito bem.

        "Wow, that move was pro."

    GG: "Good Game" (Dito ao final da partida em respeito).

Imagem de person wearing a headset with a microphone, ready to talkAbre em uma nova janela
site-craft.net
person wearing a headset with a microphone, ready to talk
Hardware Vocabulary

Para jogar no PC ou conversar online:

    Headset: Fone de ouvido com microfone.

    Keyboard & Mouse: Teclado e mouse.

    Controller: O controle (joystick).

    Monitor / Screen: A tela.

    "I need a new headset to talk to my team."

Imagem de person completely absorbed in a game, ignoring the surroundingsAbre em uma nova janela
www.simplypsychology.org
person completely absorbed in a game, ignoring the surroundings
Describing Games

    Addictive: Viciante (você não consegue parar).

        "This puzzle game is so addictive."

    Immersive: Imersivo (você se sente dentro do mundo).

        "The graphics are amazing, it feels very immersive."

    Challenging: Desafiador (difícil de um jeito bom).

Imagem de Game Over screen concept without text, just a skull or sad faceAbre em uma nova janela

Game Over screen concept without text, just a skull or sad face
Game Over & Respawn

    To die: Morrer no jogo.

        "I keep dying at this level."

    To respawn: Renascer/Reaparecer após morrer.

        "You will respawn in 5 seconds."

    Save point / Checkpoint: Local onde o jogo salva seu progresso.

Imagem de quiz layout with a question about gaming vocabularyAbre em uma nova janela
www.teacherspayteachers.com
quiz layout with a question about gaming vocabulary
Vamos Praticar?

Qual a expressão correta para dizer que você "terminou/zerou" a história do jogo?

"I finally ______ Zelda yesterday!"

A) zeroed B) finished up C) beat
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção

A resposta correta é C.

Explicação: O verbo mais comum para "zerar" um jogo é To beat. Você também pode usar "finish" ou "complete", mas "beat" é o termo nativo mais usado. "Zeroed" não existe neste contexto.
Imagem de screen showing a character stuck in a wallAbre em uma nova janela

screen showing a character stuck in a wall
Desafio de Vocabulário

Seu personagem está andando sozinho e atravessando paredes por causa de um erro do jogo. Isso é um:

A) Lag B) Glitch C) Noob
Imagem de pixelated bug iconAbre em uma nova janela

pixelated bug icon
Correção do Desafio

A resposta correta é B.

Explicação:

    Glitch é um erro de software/visual.

    Lag é lentidão de conexão.

    Noob é um jogador inexperiente.

Imagem de two friends sitting on a couch holding controllers, looking at a TVAbre em uma nova janela
www.gettyimages.co.uk
two friends sitting on a couch holding controllers, looking at a TV
Dialogue: Gaming Session

Sam: Do you want to play some FIFA? Ben: I am terrible at sports games. I am such a noob. Sam: Don't worry, we can play Co-op against the computer. Ben: Okay. Do you play on PC or Console? Sam: Console. Here, take this controller. Ben: Thanks. Just don't get angry if I don't score!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo para praticar o vocabulário gamer.

"I love playing video games in my free time. I usually play FPS games on my PC because I prefer using a mouse and keyboard. Sometimes, I play with my friends online, but the lag can be annoying. Right now, I am trying to beat a very difficult RPG. It is challenging, but the story is amazing. I hope I can level up soon!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 10, Tema Central: Cooking as a Hobby
Imagem de person happily tossing vegetables in a pan in a modern kitchen, capturing the joy of cookingAbre em uma nova janela

person happily tossing vegetables in a pan in a modern kitchen, capturing the joy of cooking
Cooking as a Hobby
Social English - Pill 10

Para muita gente, cozinhar é uma obrigação ("chore"). Mas para outros, é uma paixão!

Hoje vamos aprender a falar sobre culinária como um passatempo e descrever suas habilidades na cozinha.
Imagem de chef's hat and a wooden spoon on a tableAbre em uma nova janela

chef's hat and a wooden spoon on a table
Cook vs. Chef

Primeiro, uma distinção importante:

    Cook: Alguém que cozinha (pode ser amador ou profissional, mas geralmente é o termo para a ação ou profissão menos formal).

    Chef: Um cozinheiro profissional, geralmente o chefe da cozinha de um restaurante.

    "I am not a chef, but I am a pretty good cook."

Imagem de cake inside an oven and a pot of soup on a stove, side by side comparisonAbre em uma nova janela
rainbowplantlife.com
cake inside an oven and a pot of soup on a stove, side by side comparison
Verbs: Cook vs. Bake

Não usamos "Cook" para tudo.

    To Cook: Geral (usar calor, fogão).

        "I am cooking pasta for dinner."

    To Bake: Assar (usar o forno para massas, pães, bolos).

        "I love to bake cakes and cookies."

Imagem de nicely plated meal versus a paper bag with food containersAbre em uma nova janela
www.supplysmiths.com
nicely plated meal versus a paper bag with food containers
Homemade vs. Takeout

    Homemade: Comida feita em casa ("caseira").

        "Nothing beats homemade pizza."

    Takeout / Takeaway: Comida comprada pronta para levar/comer em casa (Delivery).

        "I was lazy, so I ordered takeout."

Imagem de empty white ceramic plate next to a complex prepared lasagna dishAbre em uma nova janela
bakedbree.com
empty white ceramic plate next to a complex prepared lasagna dish
Confusing Words: Dish vs. Plate

Em português, usamos "prato" para as duas coisas. Em inglês, não!

    Plate: O objeto físico (louça) onde você coloca a comida.

        "Please put the plates on the table."

    Dish: A refeição preparada, a receita específica.

        "My favorite dish is Lasagna." (Não diga "My favorite plate").

Imagem de person proudly holding a platter with a special mealAbre em uma nova janela

person proudly holding a platter with a special meal
My Signature Dish

Como você chama aquele prato que você faz melhor que ninguém?

Em inglês, chamamos de Signature Dish.

    "My signature dish is spicy chicken curry."

    "Everyone loves my chocolate brownies. It's my signature dish."

Imagem de hands chopping vegetables on a board and a frying pan with oilAbre em uma nova janela

hands chopping vegetables on a board and a frying pan with oil
Action Verbs: The Basics

Para descrever o processo:

    Chop: Picar/Cortar (vegetais).

    Boil: Ferver (água, massa).

    Fry: Fritar (óleo).

    Grill: Grelhar (churrasqueira ou grill).

    Roast: Assar (carne ou vegetais no forno).

Imagem de open recipe book with ingredients laid outAbre em uma nova janela
www.alamy.com
open recipe book with ingredients laid out
Following a Recipe

Para cozinhar algo novo, você segue uma Recipe (Receita).

Uma receita tem:

    Ingredients: O que você precisa.

    Steps / Instructions: O passo a passo.

    "I need to buy the ingredients for this recipe."

Imagem de person smelling a pot of food with a look of delightAbre em uma nova janela
experiencelife.lifetime.life
person smelling a pot of food with a look of delight
Describing the Result

Como dizer que ficou bom?

    Delicious: Delicioso (Formal/Neutro).

    Tasty: Saboroso.

    Yummy: "Gostoso" (Mais informal/infantil, mas usado entre amigos).

    Bland: Sem gosto / Insosso (Negativo).

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar?

Qual o verbo correto para fazer pão no forno?

"My grandmother loves to ______ bread on weekends."

A) cook B) make C) bake
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é C.

Explicação: Para pães, bolos e tortas feitos no forno, o verbo específico é Bake. "She loves to bake bread."
Imagem de sentence with a blank space regarding food vocabularyAbre em uma nova janela
7esl.com
sentence with a blank space regarding food vocabulary
Desafio de Vocabulário

Qual a palavra correta para descrever a refeição preparada?

"Feijoada is a traditional Brazilian ______."

A) plate B) dish C) bowl
Imagem de traditional clay pot with FeijoadaAbre em uma nova janela

traditional clay pot with Feijoada
Correção do Desafio

A resposta correta é B.

Explicação: Estamos falando da receita/refeição, não do objeto de louça. Portanto, usamos Dish.

"Feijoada is a traditional Brazilian dish."
Imagem de two friends eating dinner at a dining tableAbre em uma nova janela

two friends eating dinner at a dining table
Dialogue: The Dinner Party

Julie: This pasta is delicious! Did you make it? Mike: Yes, it is homemade. Julie: Wow. You are a great cook. Is this your signature dish? Mike: Actually, no. I prefer to bake. My specialty is carrot cake. Julie: I love cake! Can I have the recipe? Mike: Sure. It is very easy. You just need a few ingredients.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo com orgulho das suas habilidades culinárias!

"I find cooking very relaxing. I enjoy chopping vegetables and creating new flavors. My signature dish is grilled salmon with vegetables. I usually prefer homemade food over takeout because it is healthier. On Sundays, I like to bake cookies for my family. They say my cookies are very tasty!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 11, Tema Central: Outdoor Activities
Imagem de breathtaking landscape with mountains, a lake, and a forest, sunny dayAbre em uma nova janela

breathtaking landscape with mountains, a lake, and a forest, sunny day
Outdoor Activities
Social English - Pill 11

Passar tempo na natureza é uma ótima forma de relaxar.

Em inglês, chamamos as atividades ao ar livre de Outdoor Activities ou simplesmente The Great Outdoors.

Vamos aprender o vocabulário para sua próxima aventura.
Imagem de group of friends walking on a dirt path in the mountains wearing backpacksAbre em uma nova janela

group of friends walking on a dirt path in the mountains wearing backpacks
Hiking vs Trekking

Caminhar na natureza tem nomes específicos:

    Hiking: Caminhada longa em trilhas (trails), geralmente de um dia.

        "We go hiking every Sunday."

    Trekking: Caminhada mais difícil, longa (vários dias), muitas vezes em montanhas altas e lugares remotos.

        "They went trekking in the Himalayas."

Imagem de pair of sturdy hiking boots and a backpack on a rockAbre em uma nova janela

pair of sturdy hiking boots and a backpack on a rock
Hiking Vocabulary

Para fazer uma trilha (Trail), você precisa do equipamento certo (Gear).

    Hiking boots: Botas de trilha.

    Backpack: Mochila.

    Water bottle: Garrafa de água.

    Path: O caminho.

    "Stay on the path so you don't get lost."

Imagem de tent set up in a forest with a small fire nearbyAbre em uma nova janela

tent set up in a forest with a small fire nearby
Camping

Dormir ao ar livre se chama Camping.

Usamos a estrutura com "Go": Go Camping.

    Tent: A barraca.

    Pitch a tent: A expressão (colocation) para "montar a barraca".

        "It took us an hour to pitch the tent."

Imagem de warm sleeping bag inside a tentAbre em uma nova janela
www.intentsoutdoors.co.nz
warm sleeping bag inside a tent
Camping Gear

O que levar para não passar frio?

    Sleeping bag: Saco de dormir.

    Flashlight / Torch: Lanterna.

    Campfire: Fogueira.

    "We sat around the campfire telling stories."

Imagem de person sitting by a calm lake holding a fishing rodAbre em uma nova janela

person sitting by a calm lake holding a fishing rod
Fishing

Pescar é uma atividade relaxante para muitos.

    Fishing rod: Vara de pescar.

    Bait: Isca.

    Hook: Anzol.

    Catch a fish: Pegar um peixe.

    "My father loves to go fishing at the lake."

Imagem de canoe and a kayak side by side on water to show the differenceAbre em uma nova janela
www.onakcanoes.com
canoe and a kayak side by side on water to show the difference
Water Activities: Kayaking & Canoeing

Se você gosta de água:

    Kayaking: Caiaque (remo de duas pontas, fechado).

    Canoeing: Canoagem (remo de uma ponta, aberto).

    Life jacket: Colete salva-vidas (Item obrigatório!).

    "Put on your life jacket before getting in the boat."

Imagem de checkered blanket on the grass with a basket of food and fruitsAbre em uma nova janela

checkered blanket on the grass with a basket of food and fruits
Having a Picnic

Para algo mais leve, você pode fazer um piquenique.

Verbo: Have a picnic.

    Picnic basket: Cesta de piquenique.

    Blanket: A toalha/cobertor que se põe no chão.

    Spot: O lugar escolhido.

    "Let's find a nice shady spot for our picnic."

Imagem de bottle of sunscreen and a spray bottle of insect repellentAbre em uma nova janela
www.bullfrogsunscreen.com
bottle of sunscreen and a spray bottle of insect repellent
Safety & Protection

A natureza tem seus desafios. Proteja-se:

    Sunscreen: Protetor solar.

    Bug spray / Insect repellent: Repelente de insetos.

    Mosquitoes: Pernilongos/Mosquitos.

    Sunburn: Queimadura de sol.

    "Don't forget the bug spray, there are many mosquitoes."

Imagem de luxurious tent with a real bed inside, mixing nature and comfortAbre em uma nova janela
www.travelingsocotra.com
luxurious tent with a real bed inside, mixing nature and comfort
Slang: Glamping

Uma tendência moderna:

Glamping = Glamorous + Camping.

É acampar, mas com luxo (cama, ar condicionado, banheiro privativo) dentro da tenda.

    "I don't like bugs, so I prefer glamping."

Imagem de serene forest view with a river, focusing on the beautyAbre em uma nova janela

serene forest view with a river, focusing on the beauty
Describing the Scenery

A paisagem ou vista se chama Scenery.

Adjetivos úteis:

    Breathtaking: De tirar o fôlego (lindo demais).

    Peaceful: Pacífico/Calmo.

    Stunning: Deslumbrante.

    "The scenery from the top of the mountain was breathtaking."

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar?

Qual a expressão correta para "montar a barraca"?

"We arrived late and had to ______ the tent in the dark."

A) build B) pitch C) make
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: A combinação fixa (collocation) para montar barraca é Pitch a tent. Embora "set up" também seja usado, "pitch" é o termo específico. "Build" e "Make" estão incorretos.
Imagem de two friends looking at a paper map in the woodsAbre em uma nova janela

two friends looking at a paper map in the woods
Dialogue: Weekend Plans

John: The weather is going to be stunning this weekend. Let's go camping. Dave: Sounds fun. Do you have a tent? John: Yes, I do. We can go to the lake and go fishing too. Dave: Great. I will bring the sleeping bags and the bug spray. John: Perfect. We can pitch the tent near the water and make a campfire at night.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo imaginando que você está planejando uma viagem.

"I love the great outdoors. Next weekend, my friends and I are going to go hiking. We found a beautiful trail in the mountains. The scenery there is supposed to be breathtaking. After the hike, we plan to have a picnic by the river. I just hope I don't get a sunburn!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 12, Tema Central: Describing Talent: "I am good at..."
Imagem de person juggling balls with ease and a smile, white backgroundAbre em uma nova janela

person juggling balls with ease and a smile, white background
Describing Talent: "I am good at..."
Social English - Pill 12

Todos nós temos algo que fazemos bem. Pode ser cozinhar, matemática ou esportes.

Mas em inglês, a preposição correta faz toda a diferença. Não dizemos "good in".

Hoje vamos aprender a falar dos seus talentos com confiança.
Imagem de person standing on a podium holding a trophyAbre em uma nova janela

person standing on a podium holding a trophy
The Golden Rule: Good AT

O erro número 1 dos brasileiros é dizer "I am good in math".

Em inglês, para habilidades e talentos, usamos sempre a preposição AT.

Estrutura: To be + Good + AT

    Correct: I am good at tennis.

    Incorrect: I am good in tennis.

Imagem de math equation symbol next to a paintbrush and a soccer ballAbre em uma nova janela

math equation symbol next to a paintbrush and a soccer ball
Using Nouns (Substantivos)

A forma mais simples é usar um substantivo depois da preposição.

    I am good at math. (Sou bom em matemática.)

    She is good at languages. (Ela é boa em línguas.)

    He is good at sports. (Ele é bom em esportes.)

Imagem de person cooking and another person playing guitar, emphasizing the actionAbre em uma nova janela
rombopicks.com
person cooking and another person playing guitar, emphasizing the action
Using Verbs (-ING Rule)

Se você quiser dizer que é bom em fazer algo (ação), o verbo PRECISA terminar em -ING.

Esta é uma regra universal: Preposição (at) + Verbo com -ing.

    I am good at cooking. (Não diga "cook")

    We are good at solving problems.

    Are you good at drawing?

Imagem de scale ranging from red (bad) to green (amazing)Abre em uma nova janela
www.alamy.com
scale ranging from red (bad) to green (amazing)
Levels of Talent

Você pode variar a intensidade:

    I am amazing at... (Incrível / Muito bom)

    I am great at... (Ótimo)

    I am good at... (Bom)

    I am okay at... (Razoável / "Mais ou menos")

    "My sister is amazing at singing."

Imagem de person looking confused looking at a map or burning toastAbre em uma nova janela

person looking confused looking at a map or burning toast
The Negative: "I am bad at..."

E para o que não sabemos fazer?

    I am bad at... (Sou ruim em...)

    I am terrible at... (Sou péssimo em...)

    I am hopeless at... (Sou um caso perdido...)

    "I am terrible at drawing."

    "Sorry, I am bad at remembering names."

Imagem de lightbulb moment appearing above someone's headAbre em uma nova janela

lightbulb moment appearing above someone's head
Idiom: "I have a knack for..."

Quer soar mais sofisticado? Use esta expressão.

To have a knack for something significa ter um talento natural, um "jeito" para a coisa.

    "He has a knack for fixing things." (Ele tem o dom/jeito para consertar coisas.)

Imagem de graduation cap vs a DNA helix strandAbre em uma nova janela

graduation cap vs a DNA helix strand
Talented vs Skilled

Qual a diferença?

    Talented: Você nasceu com isso (Natural).

        "She is a naturally talented musician."

    Skilled: Você treinou para aprender (Aprendido).

        "He is a highly skilled surgeon."

Imagem de two people talking with question marks above their headsAbre em uma nova janela

two people talking with question marks above their heads
Asking Others

Como descobrir os talentos dos seus amigos?

    "What are you good at?"

    "Do you have any hidden talents?" (Talentos ocultos)

    "Are you good at [Activity]?"

Imagem de job interview setting, professional atmosphereAbre em uma nova janela

job interview setting, professional atmosphere
Professional Context

Em entrevistas de emprego, usamos essa estrutura para falar de Soft Skills.

    "I am good at working under pressure."

    "I am great at organizing events."

    "I am good at dealing with customers."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar?

Qual a frase gramaticalmente correta?

A) I am good in playing chess. B) I am good at play chess. C) I am good at playing chess.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção

A resposta correta é C.

Explicação: Precisamos da preposição AT (não in) e o verbo precisa ter -ING (playing) porque vem depois de uma preposição.

"I am good at playing chess."
Imagem de person trying to fix a computer but looking confused and frustratedAbre em uma nova janela

person trying to fix a computer but looking confused and frustrated
Desafio de Vocabulário

Complete a frase com a palavra que significa "Péssimo/Muito ruim":

"Don't ask me to fix your computer. I am ______ at technology!"

A) great B) terrible C) knack
Imagem de red cross or warning signAbre em uma nova janela
www.alamy.com
red cross or warning sign
Correção do Desafio

A resposta correta é B.

Explicação: Terrible é o oposto extremo de Great ou Good.

"I am terrible at technology!"
Imagem de two friends sitting on a park bench chattingAbre em uma nova janela

two friends sitting on a park bench chatting
Dialogue: Hidden Talents

Anna: Wow, that drawing is beautiful! I didn't know you were an artist. Ben: Thanks! I am pretty good at drawing, but I am terrible at painting. Anna: Do you have any other hidden talents? Ben: Well, I have a knack for learning languages. I speak three. Anna: That is amazing. I am hopeless at languages. I can only speak English.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Fale sobre seus talentos (e falta deles) usando o modelo abaixo.

"I think everyone is good at something. Personally, I am great at cooking Italian food. It is my passion. However, I am terrible at sports. I am especially bad at playing soccer because I run very slowly. Also, my friends say I have a knack for making people laugh."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 13, Tema Central: Frequency Adverbs (Position)
Imagem de calendar with all days marked with a checkmark vs a calendar with only one day markedAbre em uma nova janela

calendar with all days marked with a checkmark vs a calendar with only one day marked
Frequency Adverbs: Position
Social English - Pill 13

Você sabe as palavras ("Always", "Never"), mas sabe onde colocá-las na frase?

Em inglês, a posição do advérbio de frequência muda o sentido ou pode estar gramaticalmente errada se colocada no lugar do português.

Hoje vamos dominar a posição correta.
Imagem de percentage scale from 0% to 100% listing Never to AlwaysAbre em uma nova janela

percentage scale from 0% to 100% listing Never to Always
The Scale of Frequency

Primeiro, vamos relembrar a escala de frequência:

    100% - Always: Sempre.

    90% - Usually: Geralmente.

    70% - Often: Frequentemente.

    50% - Sometimes: Às vezes.

    10% - Hardly ever / Rarely: Quase nunca.

    0% - Never: Nunca.

Imagem de person drinking coffee, with an arrow pointing before the actionAbre em uma nova janela
www.singlecare.com
person drinking coffee, with an arrow pointing before the action
Rule 1: Before Main Verbs

Esta é a regra para a maioria dos verbos (drink, eat, work, go, sleep).

O advérbio vem ANTES do verbo principal.

Estrutura: Subject + Adverb + Verb

    Correto: I always drink coffee.

    Incorreto: I drink always coffee. (Erro comum de brasileiros!)

Imagem de clock showing 8 AM and a person arriving at 8 AM, routine conceptAbre em uma nova janela
www.trualta.com
clock showing 8 AM and a person arriving at 8 AM, routine concept
Examples: Rule 1

Veja a posição antes da ação:

    She often goes to the gym. (Ela frequentemente vai à academia.)

    We hardly ever watch TV. (Nós quase nunca assistimos TV.)

    They never eat meat. (Eles nunca comem carne.)

Imagem de person looking at a watch being late, with an arrow pointing after the personAbre em uma nova janela
swisswatches-magazine.com
person looking at a watch being late, with an arrow pointing after the person
Rule 2: After Verb "To Be"

O verbo To Be (am, is, are) é especial. Ele é "o rei".

O advérbio vem DEPOIS do verbo To Be.

Estrutura: Subject + To Be + Adverb

    Correto: She is always happy.

    Incorreto: She always is happy.

Imagem de traffic light on red and a person waitingAbre em uma nova janela
www.freepik.com
traffic light on red and a person waiting
Examples: Rule 2

Veja a posição depois de am/is/are:

    I am never late. (Eu nunca estou atrasado.)

    He is usually tired after work. (Ele geralmente está cansado depois do trabalho.)

    They are often busy. (Eles estão frequentemente ocupados.)

Imagem de signpost with arrows pointing in different directions labeled SometimesAbre em uma nova janela

signpost with arrows pointing in different directions labeled Sometimes
The "Sometimes" Exception

Sometimes (Às vezes) é flexível.

Ele pode aparecer em três lugares:

    No início: Sometimes I go to the park.

    No meio (Regra 1): I sometimes go to the park.

    No final: I go to the park sometimes.

Todas estão corretas!
Imagem de warning sign with an exclamation markAbre em uma nova janela

warning sign with an exclamation mark
Common Mistake: "Never" with Negatives

Em inglês, Never já é negativo. Não use "Don't" ou "Doesn't" junto com ele.

    Incorreto: I ~~don't~~ never smoke.

    Correto: I never smoke.

(A dupla negação é proibida na gramática padrão).
Imagem de puzzle putting words in order to form a sentenceAbre em uma nova janela
15worksheets.com
puzzle putting words in order to form a sentence
Visual Summary

Memorize visualmente:

    Action Verbs: User -> ALWAYS -> Action (I always run)

    Verb To Be: User -> IS -> ALWAYS -> State (I am always happy)

Imagem de multiple choice quiz question layoutAbre em uma nova janela
gdoc.io
multiple choice quiz question layout
Vamos Praticar? - Regra 1

Qual a ordem correta das palavras?

"My brother / plays / video games / often"

A) My brother plays often video games. B) My brother often plays video games. C) Often my brother plays video games.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Regra 1

A resposta correta é B.

Explicação: "Play" é um verbo de ação (Main Verb). O advérbio Often deve vir ANTES dele.

Frase: "My brother often plays video games."
Imagem de sentence with scrambled words needing arrangementAbre em uma nova janela
15worksheets.com
sentence with scrambled words needing arrangement
Desafio - Regra 2

Organize a frase corretamente: [ late / is / for meetings / Susan / hardly ever ]

A) Susan hardly ever is late for meetings. B) Susan is late hardly ever for meetings. C) Susan is hardly ever late for meetings.
Imagem de clock showing punctualityAbre em uma nova janela

clock showing punctuality
Correção do Desafio

A resposta correta é C.

Explicação: Temos o verbo IS (To Be). O advérbio Hardly ever deve vir DEPOIS dele.

Frase: "Susan is hardly ever late for meetings."
Imagem de two friends talking about their weekly routineAbre em uma nova janela
www.youtube.com
two friends talking about their weekly routine
Dialogue: Routine & Habits

Liam: Do you want to go to the cinema tonight? Emma: I can't. I usually go to the gym on Fridays. Liam: Really? You are so disciplined. I am often too tired on Fridays. Emma: Well, I sometimes skip the gym if I have a date. Liam: So... is this a date? Emma: Maybe! I hardly ever say no to a good movie.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Leia o texto abaixo prestando atenção na posição dos advérbios.

"I have a very predictable routine. I always wake up at 7 AM. I am never late for work because I dislike rushing. I usually have lunch with my colleagues, but sometimes I eat alone to read a book. I hardly ever go out on weeknights because I am usually exhausted by 10 PM."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 14, Tema Central: "How often do you...?"
Imagem de large calendar with several days marked with circles, representing frequencyAbre em uma nova janela
www.researchgate.net
large calendar with several days marked with circles, representing frequency
"How often do you...?"
Social English - Pill 14

Você quer saber se seu amigo vai à academia todo dia ou só uma vez por ano?

A pergunta mágica para descobrir a frequência das coisas é "How often...?".

Hoje vamos aprender a perguntar e a responder corretamente.
Imagem de person looking at a clock and a calendar, thinking about timeAbre em uma nova janela

person looking at a clock and a calendar, thinking about time
A Estrutura da Pergunta

Para fazer a pergunta, usamos o auxiliar Do ou Does.

Estrutura: How often + do/does + Subject + Verb?

Exemplos:

    How often do you go to the cinema?

    How often does she visit her parents?

    How often do they eat out?

Imagem de single finger held up, representing oneAbre em uma nova janela

single finger held up, representing one
Respondendo: Once & Twice

Cuidado! Não dizemos "one time" ou "two times" geralmente. Temos palavras especiais:

    Once: Uma vez.

        "I go there once."

    Twice: Duas vezes.

        "I check my email twice."

Imagem de three fingers held up and then four fingers, representing countingAbre em uma nova janela
multilingual-families.com
three fingers held up and then four fingers, representing counting
Respondendo: Three times +

A partir do número 3, voltamos ao padrão normal usando a palavra "times".

    Three times (Três vezes).

    Four times (Quatro vezes).

    Ten times (Dez vezes).

    "I brush my teeth three times a day."

Imagem de weekly planner showing Monday to SundayAbre em uma nova janela
www.etsy.com
weekly planner showing Monday to Sunday
O Período de Tempo: "a week"

Para dizer "por dia" ou "por semana", usamos o artigo "a" (que aqui significa "per").

    Once a day (Uma vez por dia).

    Twice a week (Duas vezes por semana).

    Three times a month (Três vezes por mês).

    Four times a year (Quatro vezes por ano).

Imagem de continuous loop symbol or a daily calendar flipping pagesAbre em uma nova janela

continuous loop symbol or a daily calendar flipping pages
Usando "Every"

Se a ação acontece repetidamente em todos os períodos, usamos Every.

    Every day: Todo dia. (Espaço entre as palavras!)

    Every week: Toda semana.

    Every weekend: Todo fim de semana.

    Every Sunday: Todo domingo.

    "I drink coffee every morning."

Imagem de person shrugging shoulders, indicating uncertainty or vaguenessAbre em uma nova janela

person shrugging shoulders, indicating uncertainty or vagueness
Respostas Vagas

Às vezes não sabemos o número exato.

    "Not very often." (Não muito frequentemente).

    "Quite often." (Com bastante frequência).

    "All the time." (O tempo todo).

    "Every now and then." (De vez em quando).

Imagem de gym setting with weights and a treadmillAbre em uma nova janela
sosfitnessservices.com
gym setting with weights and a treadmill
Exemplos de Contexto: Hobbies

Vamos aplicar aos hobbies:

Q: How often do you exercise? A: I go to the gym every day.

Q: How often do you see your friends? A: We meet twice a month.
Imagem de doctor talking to a patient in an officeAbre em uma nova janela

doctor talking to a patient in an office
Exemplos de Contexto: Saúde

Muito comum em consultas médicas:

Q: How often do you take this medicine? A: You must take it once a day after lunch.

Q: How often do you get headaches? A: Unfortunately, quite often.
Imagem de road sign splitting into two paths: How often and WhenAbre em uma nova janela

road sign splitting into two paths: How often and When
How Often vs. When

Não confunda!

    When: Pergunta sobre um momento específico (Ontem, Amanhã, 1999).

        "When did you go?" -> "Yesterday."

    How often: Pergunta sobre frequência/repetição.

        "How often do you go?" -> "Every Friday."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a forma correta de dizer "duas vezes por ano"?

"I visit my dentist ______ a year."

A) two times B) second time C) twice
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Em inglês, a forma padrão para "duas vezes" é Twice. Dizer "two times" não é proibido, mas soa menos natural e básico demais.

Frase: "I visit my dentist twice a year."
Imagem de sentence with a blank space asking for the correct question wordAbre em uma nova janela
askfilo.com
sentence with a blank space asking for the correct question word
Vamos Praticar? - Exercício 2

Você quer saber a frequência com que seu amigo viaja.

"______ do you travel to Europe?"

A) When B) How often C) How much
Imagem de globe with travel routes markedAbre em uma nova janela

globe with travel routes marked
Correção - Exercício 2

A resposta correta é B.

Explicação: Se você quer saber a regularidade (frequência), usa How often. Se usasse "When", a resposta seria uma data específica ("Last year").
Imagem de two colleagues drinking coffee in an office kitchenAbre em uma nova janela

two colleagues drinking coffee in an office kitchen
Dialogue: Coffee Habits

Sarah: You love coffee, right? How often do you drink it? Mike: Oh, all the time. I drink about five cups a day. Sarah: Wow, that is a lot! Mike: And you? Do you ever drink coffee? Sarah: Not very often. Maybe once or twice a week. Mike: I don't know how you survive!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Responda às perguntas abaixo em voz alta seguindo o modelo.

"Let me tell you about my routine. How often do I study English? I study every day for 20 minutes. How often do I cook? I cook once a day, usually dinner. How often do I travel? Sadly, only once a year. But I go to the cinema quite often, maybe three times a month."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 15, Tema Central: Expression: "Once/Twice a week"
Imagem de calendar with one circle on a date and another calendar with two circles, highlighting the differenceAbre em uma nova janela

calendar with one circle on a date and another calendar with two circles, highlighting the difference
Expression: "Once/Twice a week"
Social English - Pill 15

Na última aula, vimos a pergunta "How often?". Hoje, vamos focar exclusivamente na resposta numérica.

Como dizer "uma vez por semana", "duas vezes por ano" ou "dez vezes por dia" sem errar a estrutura.
Imagem de number 1 next to the word ONCE and the number 2 next to the word TWICE in a clean designAbre em uma nova janela
www.aengusart.co.uk
number 1 next to the word ONCE and the number 2 next to the word TWICE in a clean design
The Golden Rule: 1 and 2

Em inglês, os números 1 e 2 têm formas especiais para frequência.

É muito comum brasileiros dizerem "one time" ou "two times". Embora não seja impossível de entender, soa muito básico.

O correto é:

    1 vez = Once (Pronúncia: "Uâns")

    2 vezes = Twice (Pronúncia: "Tuáis")

Imagem de numbers 3, 4, and 5 followed by the word TIMESAbre em uma nova janela
www.youtube.com
numbers 3, 4, and 5 followed by the word TIMES
The Rule for 3+

Do número 3 em diante, a regra fica fácil. Basta usar o número normal + a palavra times.

    3 vezes = Three times

    4 vezes = Four times

    10 vezes = Ten times

    100 vezes = A hundred times

Imagem de clock showing per day and a calendar showing per weekAbre em uma nova janela
jadcotime.com.au
clock showing per day and a calendar showing per week
The Preposition "A"

Em português, dizemos "por" dia ou "por" semana. Em inglês, usamos o artigo "a" (ou "an" antes de vogal) para indicar essa distribuição.

    a day (por dia)

    a week (por semana)

    a month (por mês)

    a year (por ano)

Nota: Não use "per" em conversas informais (soa muito técnico/matemático).

+ [a] + [Period] ]
Imagem de mathematical formula style graphic: [FrequencyAbre em uma nova janela
www.youtube.com
mathematical formula style graphic: [Frequency
The Full Structure

A fórmula para montar sua frase é:

[Frequency Word] + a + [Time Period]

Exemplos:

    Once a week

    Twice a month

    Three times a year

Imagem de person brushing teeth in the morning and eveningAbre em uma nova janela
www.healthline.com
person brushing teeth in the morning and evening
Examples: Daily Habits

Coisas que fazemos todos os dias.

    I brush my teeth three times a day. (Eu escovo os dentes três vezes por dia.)

    She drinks water five times a day. (Ela bebe água cinco vezes por dia.)

    We walk the dog twice a day. (Nós passeamos com o cachorro duas vezes por dia.)

Imagem de gym bag and a yoga matAbre em uma nova janela
labelrama.com
gym bag and a yoga mat
Examples: Weekly Habits

Coisas que fazemos durante a semana.

    I go to the gym four times a week. (Eu vou à academia quatro vezes por semana.)

    They eat pizza once a week, usually on Fridays. (Eles comem pizza uma vez por semana.)

    We have English classes twice a week. (Temos aulas de inglês duas vezes por semana.)

Imagem de suitcase and a plane ticket representing annual travelAbre em uma nova janela
www.cnet.com
suitcase and a plane ticket representing annual travel
Examples: Monthly & Yearly

Coisas que acontecem menos frequentemente.

    I visit my parents once a month. (Visito meus pais uma vez por mês.)

    She goes on vacation twice a year. (Ela sai de férias duas vezes por ano.)

    It rains here only five times a year. (Chove aqui apenas cinco vezes por ano.)

Imagem de warning sign comparing in the week crossed out vs a week checkedAbre em uma nova janela
freedomclinics.com
warning sign comparing in the week crossed out vs a week checked
Common Mistake: "In the..."

Cuidado para não traduzir direto do português ("na semana").

    Incorreto: I go twice in the week.

    Correto: I go twice a week.

A estrutura é sempre direta com o artigo "a".
Imagem de schedule planner showing alternate days markedAbre em uma nova janela
www.naturalcycles.com
schedule planner showing alternate days marked
Every Other Day

Uma expressão bônus muito útil:

Se você faz algo "dia sim, dia não", dizemos:

"Every other day."

    I wash my hair every other day. (Lavo o cabelo dia sim, dia não.)

Imagem de quiz layout with a missing word in a sentenceAbre em uma nova janela
worksheet-creator.com
quiz layout with a missing word in a sentence
Vamos Praticar? - Exercício 1

Qual a frase correta para "Eu viajo uma vez por ano"?

A) I travel one time a year. B) I travel once in the year. C) I travel once a year.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Usamos a palavra especial Once para "uma vez" e o artigo a para "por". Não usamos "in the".

Frase: "I travel once a year."
Imagem de person holding two fingers up smilingAbre em uma nova janela
www.alamy.com
person holding two fingers up smiling
Desafio de Tradução

Como você diria "Nós nos encontramos duas vezes por mês" em inglês natural?

A) We meet two times for month. B) We meet twice a month. C) We meet double a month.
Imagem de calendar with two dates circled in the same monthAbre em uma nova janela

calendar with two dates circled in the same month
Correção do Desafio

A resposta correta é B.

Explicação:

    Twice é a palavra para 2 vezes.

    A month é a estrutura para "por mês".

Frase: "We meet twice a month."
Imagem de two friends looking at their smartphones trying to schedule a meetingAbre em uma nova janela
www.alamy.com
two friends looking at their smartphones trying to schedule a meeting
Dialogue: Scheduling

Tom: Hey, we should play tennis soon. Jerry: Sure! I usually play once a week on Saturdays. Tom: Only once? I play three times a week. Jerry: Wow, you are fit. I don't have time. I work late every day. Tom: I understand. What about dinner? Jerry: I go out for dinner twice a month. Let's go next Friday!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Fale sobre sua rotina real usando as estruturas aprendidas.

"I have a busy schedule. I go to work five times a week. I try to exercise three times a week, but sometimes I am lazy. I visit my family once a month because they live far away. And I go to the dentist twice a year for a check-up. Other than that, I drink coffee every single day!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 16, Tema Central: Shopping for Fun
Imagem de colorful shopping bags being held by a happy person walking down a streetAbre em uma nova janela
www.freepik.com
colorful shopping bags being held by a happy person walking down a street
Shopping for Fun
Social English - Pill 16

Fazer compras é uma das melhores atividades sociais.

Hoje vamos aprender o vocabulário para quando você vai ao shopping por lazer, não por obrigação. Vamos falar de vitrines, provadores e descontos!
Imagem de grocery cart with food vs a person holding fashion bags, visual contrastAbre em uma nova janela
modernpicnic.com
grocery cart with food vs a person holding fashion bags, visual contrast
Go Shopping vs Do the Shopping

Cuidado com a diferença sutil:

    To go shopping: Ir às compras por diversão (roupas, sapatos, eletrônicos). É um hobby.

        "Let's go shopping at the mall this weekend."

    To do the shopping: Fazer as compras de casa (supermercado, comida, limpeza). É uma tarefa doméstica.

        "I need to do the shopping; the fridge is empty."

Imagem de person looking through a shop window at a display without enteringAbre em uma nova janela

person looking through a shop window at a display without entering
Window Shopping

E se você não tem dinheiro para gastar, mas gosta de olhar?

Chamamos isso de Window Shopping (olhar as vitrines).

    "I am broke, so I am just window shopping today."

    "We spent the afternoon window shopping."

Imagem de person looking through racks of clothes in a store casuallyAbre em uma nova janela

person looking through racks of clothes in a store casually
Browsing

Quando você entra na loja e o vendedor pergunta "Can I help you?", mas você só está olhando:

Use o verbo To Browse (dar uma olhada).

    "No thanks, I am just browsing."

    "I love browsing in bookstores."

Imagem de red tag showing a percentage sign for discountAbre em uma nova janela
pngtree.com
red tag showing a percentage sign for discount
Sales & Bargains

O melhor vocabulário para economizar:

    On sale: Em promoção.

        "These shoes are on sale."

    A bargain: Uma pechincha (algo muito barato e bom).

        "This jacket was a real bargain!"

    Discount: Desconto.

        "Can I get a discount?"

Imagem de person standing inside a small curtained room trying on clothesAbre em uma nova janela

person standing inside a small curtained room trying on clothes
The Fitting Room

O lugar onde você prova as roupas se chama Fitting Room (ou Changing Room).

Verbo: Try on.

    "Where is the fitting room? I want to try this on."

Imagem de shirt that is clearly too small for the person wearing itAbre em uma nova janela

shirt that is clearly too small for the person wearing it
Fit vs Suit (Crucial!)

Dois verbos que confundem brasileiros:

    Fit: Refere-se ao tamanho. (Serve ou não serve no corpo).

        "This shirt doesn't fit. It is too small."

    Suit: Refere-se ao estilo/cor. (Fica bem em você, combina).

        "That color really suits you!" (Ficou bonito em você).

Imagem de credit card machine and cash money on a counterAbre em uma nova janela
www.alamy.com
credit card machine and cash money on a counter
Paying for It

Na hora de pagar (Checkout):

    Cash: Dinheiro vivo.

    Credit Card: Cartão de crédito.

    Receipt: A nota fiscal/recibo (Pronúncia: "Ri-cít", o P é mudo!).

    "Would you like a receipt?"

    "I will pay in cash."

Imagem de person handing a product back to a cashierAbre em uma nova janela

person handing a product back to a cashier
Returns & Refunds

Se você se arrependeu:

    Return: Devolver o produto.

        "I want to return this dress."

    Refund: Reembolso (dinheiro de volta).

        "Can I get a refund?"

    Exchange: Trocar por outro (tamanho/cor).

        "I'd like to exchange this for a larger size."

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar?

Você provou um sapato e ele apertou seu pé. O que você diz?

"These shoes don't ______ me."

A) suit B) fit C) combine
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: Se é uma questão física de tamanho/conforto, usamos Fit. "These shoes don't fit me."
Imagem de sentence asking for the correct verbAbre em uma nova janela
www.madebyteachers.com
sentence asking for the correct verb
Desafio de Vocabulário

Qual a expressão correta para "só estou olhando" (dentro da loja)?

"Thanks, I am just ______."

A) watching B) seeing C) browsing
Imagem de person looking at books on a shelf casuallyAbre em uma nova janela

person looking at books on a shelf casually
Correção do Desafio

A resposta correta é C.

Explicação: O verbo específico para olhar produtos em uma loja (ou arquivos na internet) é Browse. "I am just browsing."
Imagem de two friends carrying shopping bags walking in a mallAbre em uma nova janela

two friends carrying shopping bags walking in a mall
Dialogue: At the Mall

Ana: Look at that red dress! It is on sale. Bia: It is beautiful. You should try it on. Ana: Okay, I will go to the fitting room. (Minutes later) Ana: What do you think? Bia: It fits perfectly, but I don't think red suits you. Ana: You are right. I prefer blue. Let's keep browsing.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique o vocabulário de compras em voz alta.

"I love to go shopping with my friends. Sometimes we don't buy anything, we just go window shopping. But yesterday, I found a great bargain. I bought a jacket that was on sale. I tried it on in the fitting room and it fit perfectly. Also, the black color really suits my style. I paid by credit card and kept the receipt just in case."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 17, Tema Central: Eating Out: Types of Restaurants
Imagem de variety of restaurant fronts ranging from a burger joint to an elegant restaurantAbre em uma nova janela
insideguide.co.za
variety of restaurant fronts ranging from a burger joint to an elegant restaurant
Eating Out: Types of Restaurants
Social English - Pill 17

Comer fora ("Eating out") é uma das atividades sociais mais comuns.

Mas nem todo restaurante é igual. Em inglês, temos nomes específicos para cada tipo de estabelecimento, do mais barato ao mais luxuoso.
Imagem de burger, fries, and a soda cup on a plastic trayAbre em uma nova janela
pngtree.com
burger, fries, and a soda cup on a plastic tray
Fast Food

O tipo mais básico e conhecido.

    Fast Food: Comida rápida, geralmente não saudável ("Junk food"). Você pede no balcão ("Counter") e leva sua própria bandeja.

    Chains: Cadeias de restaurantes (McDonald's, Burger King).

    "I was in a hurry, so I just grabbed some fast food."

Imagem de family sitting at a wooden table eating pizza and salad comfortablyAbre em uma nova janela

family sitting at a wooden table eating pizza and salad comfortably
Casual Dining

É o restaurante comum, onde você senta e um garçom te atende, mas o ambiente é relaxado.

    Casual Dining: Restaurante informal.

    Family Style: Restaurantes com porções grandes para dividir.

    Diner: (Específico dos EUA) Lanchonete estilo retrô que serve café da manhã e hambúrgueres o dia todo.

    "Let's go to a casual Italian place for dinner."

Imagem de elegant table setting with wine glasses, candles, and white tableclothAbre em uma nova janela

elegant table setting with wine glasses, candles, and white tablecloth
Fine Dining

Quando a ocasião é especial e você quer luxo.

    Fine Dining: Restaurante de alta gastronomia, chique e caro.

    Upscale / Fancy: Adjetivos para descrever lugares luxuosos.

    Dress Code: Regra de vestimenta (ex: não pode entrar de shorts).

    "We are going to a fine dining restaurant for our anniversary."

Imagem de colorful truck serving food to people in a parkAbre em uma nova janela
www.frontenacpark.ca
colorful truck serving food to people in a park
Street Food & Food Trucks

Uma tendência muito popular hoje em dia.

    Food Truck: Caminhão/Van adaptado que vende comida na rua.

    Street Food: Comida de rua (barracas, feiras).

    Stall: A barraca de comida.

    "This food truck makes the best tacos in the city."

Imagem de long table filled with many different trays of food for selfserviceAbre em uma nova janela

long table filled with many different trays of food for selfservice
Buffets & All-you-can-eat

Quando você pode comer o quanto quiser.

    Buffet: Self-service (você se serve).

    All-you-can-eat: "Tudo o que você puder comer" (Rodízio ou Buffet livre). Preço fixo.

    "I love going to all-you-can-eat sushi places."

Imagem de small, cozy coffee shop with pastries in a glass displayAbre em uma nova janela

small, cozy coffee shop with pastries in a glass display
Cafes & Bistros

Para refeições leves.

    Cafe / Coffee Shop: Foco em café, bolos e sanduíches.

    Bistro: Um restaurante pequeno e simples, geralmente estilo francês.

    "Let's meet at the cafe for a quick lunch."

Imagem de paper bag and a coffee cup in a carrierAbre em uma nova janela
nashonuma.com
paper bag and a coffee cup in a carrier
Takeout vs Eat-in

Ao pedir comida (especialmente em Fast Food ou Cafés), vão te perguntar:

    "For here or to go?" (Para comer aqui ou para levar?)

        Eat-in / For here: Comer no local.

        Takeout / To go / Takeaway: Levar para casa.

    "I'd like a cheeseburger to go, please."

Imagem de generic menu with sections for Starters, Main Course, and DessertAbre em uma nova janela

generic menu with sections for Starters, Main Course, and Dessert
The 3 Courses

Em restaurantes (Casual ou Fine Dining), a refeição é dividida em:

    Starter / Appetizer: Entrada (sopa, salada).

    Main Course / Entrée: Prato principal (carne, massa).

    Dessert: Sobremesa.

    "I will skip the starter and go straight to the main course."

Imagem de busy restaurant interior with many people talkingAbre em uma nova janela

busy restaurant interior with many people talking
Describing the Atmosphere

Como descrever o lugar?

    Cozy: Aconchegante (pequeno e confortável).

    Crowded: Lotado (muita gente).

    Noisy: Barulhento.

    Romantic: Romântico (luz baixa, velas).

    "I love this bistro. It is very cozy and quiet."

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar?

Qual o nome do tipo de restaurante onde você paga um preço fixo e pode comer sem limites?

"Let's go to an ______ restaurant. I am starving!"

A) fine dining B) all-you-can-eat C) fast food
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: All-you-can-eat é a expressão correta para buffets livres ou rodízios onde a quantidade não é limitada.
Imagem de sentence asking to identify the type of restaurantAbre em uma nova janela

sentence asking to identify the type of restaurant
Desafio de Vocabulário

Você quer levar sua namorada/namorado para um jantar romântico, chique e elegante. Que tipo de restaurante você escolhe?

A) A Food Truck B) A Diner C) A Fine Dining restaurant
Imagem de waiter pouring wine at a fancy tableAbre em uma nova janela

waiter pouring wine at a fancy table
Correção do Desafio

A resposta correta é C.

Explicação: Fine Dining refere-se a restaurantes de alta classe, serviço formal e ambiente elegante (fancy).
Imagem de two friends looking at a restaurant app on a phoneAbre em uma nova janela

two friends looking at a restaurant app on a phone
Dialogue: Choosing a Place

John: I am hungry. Where should we eat? Emma: I don't want fast food. I want a proper meal. John: Okay. How about that new Italian place? It is casual dining, not too expensive. Emma: Is it good? John: Yes, but it gets very crowded on Fridays. We might need a reservation. Emma: If it is full, we can just grab some tacos from a food truck.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Fale sobre seus lugares favoritos para comer.

"I love eating out. When I am busy, I usually get takeout from a fast food chain. But on weekends, I prefer casual dining with my friends. We often go to an all-you-can-eat sushi restaurant because we eat a lot! I rarely go to fine dining places because they are too expensive for me. My favorite atmosphere is cozy and quiet."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 18, Tema Central: Describing Food Taste
Imagem de variety of colorful foods: lemons, chili peppers, cake, and pretzels, arranged artisticallyAbre em uma nova janela
www.lemon8-app.com
variety of colorful foods: lemons, chili peppers, cake, and pretzels, arranged artistically
Describing Food Taste
Social English - Pill 18

Quando você come algo, dizer apenas "It is good" ou "It is bad" é muito básico.

A comida tem sabor (Flavor/Taste). Hoje vamos aprender os adjetivos essenciais para descrever exatamente o que você está sentindo na língua.
Imagem de chocolate cake slice and a bowl of potato chips side by sideAbre em uma nova janela
www.theroastedroot.net
chocolate cake slice and a bowl of potato chips side by side
The Basics: Sweet vs. Salty

Os dois sabores mais comuns:

    Sweet: Doce. (Açúcar, mel, frutas).

        "This chocolate cake is too sweet."

    Salty: Salgado. (Sal, batata frita, snacks).

        "These chips are very salty. I need water."

Imagem de cut lemon showing juice and a cup of black coffeeAbre em uma nova janela
www.medicalnewstoday.com
cut lemon showing juice and a cup of black coffee
Strong Tastes: Sour vs. Bitter

Cuidado para não confundir estes dois:

    Sour: Azedo. A sensação que repuxa a boca (Limão, vinagre, iogurte natural).

        "Lemons are extremely sour."

    Bitter: Amargo. Aquele gosto de fundo, menos agressivo (Café sem açúcar, chocolate amargo, cerveja IPA).

        "I love bitter chocolate (dark chocolate)."

Imagem de red chili peppers and a bottle of hot sauceAbre em uma nova janela
www.chilipeppermadness.com
red chili peppers and a bottle of hot sauce
Spicy (Hot)

Quando a comida "queima" a boca:

    Spicy: Picante / Apimentado.

    Hot: Também usado para pimenta, além de temperatura.

    "Do you like spicy food?"

    "This curry is very hot!"

Nota: Se a comida tem muitos temperos (ervas), mas não pimenta, dizemos "well-seasoned".
Imagem de steak, a block of cheese, and mushroomsAbre em uma nova janela
thecozyapron.com
steak, a block of cheese, and mushrooms
Savory

Esta é uma palavra essencial em inglês que não tem tradução direta exata, mas é o oposto de doce.

    Savory: Refere-se a comidas salgadas/temperadas em geral (carnes, queijos, tortas salgadas), mas com um sentido positivo de "saboroso" e "rico".

    "I prefer savory snacks like nuts over candy."

Imagem de bowl of plain white rice without anything on itAbre em uma nova janela
www.eatingchina.com
bowl of plain white rice without anything on it
Bland vs. Rich

Descrevendo a intensidade do sabor:

    Bland: Insosso, sem gosto, "sem graça". (Arroz sem sal, pão puro).

        "Hospital food is usually bland."

    Rich: Rico, pesado, com muita gordura/creme/açúcar. (Cheesecake, massas com molho branco).

        "I can't eat much of this dessert, it is remarkably rich."

Imagem de carrot being snapped and a piece of chewing gum being stretchedAbre em uma nova janela
www.cookandnelson.com
carrot being snapped and a piece of chewing gum being stretched
Texture: Crunchy vs. Chewy

O sabor também envolve a textura:

    Crunchy / Crispy: Crocante. (Cenoura crua, batata frita, torrada).

        "I love crunchy apples."

    Chewy: "Borrachudo", difícil de mastigar ou que exige mastigação (Carne passada, balas de goma).

        "This steak is overcooked and chewy."

Imagem de jar of pickles and a glass of milk, contrasting acidic and creamyAbre em uma nova janela
stpetersburgfoodies.com
jar of pickles and a glass of milk, contrasting acidic and creamy
More Textures: Creamy & Greasy

    Creamy: Cremoso. (Sopas, sorvetes, queijos macios).

        "This mushroom soup is so creamy."

    Greasy / Oily: Gorduroso/Oleoso. (Pizza barata, frituras ruins).

        "I feel sick when I eat greasy food."

Imagem de person tasting something with a thoughtful expressionAbre em uma nova janela

person tasting something with a thoughtful expression
Structure: "It tastes..."

Usamos o verbo Taste para descrever a sensação.

    "It tastes [Adjective]."

        "It tastes sour."

    "It tastes like [Noun]." (Tem gosto de...)

        "It tastes like chicken."

Imagem de quiz question displayed on a restaurant menu boardAbre em uma nova janela
wayground.com
quiz question displayed on a restaurant menu board
Vamos Praticar? - Exercício 1

Qual adjetivo descreve melhor o sabor de um limão?

A) Bitter B) Sour C) Spicy
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação:

    Sour é azedo (limão, vinagre).

    Bitter é amargo (café).

    Spicy é picante (pimenta).

Imagem de bowl of soup without saltAbre em uma nova janela
oohlalaitsvegan.com
bowl of soup without salt
Desafio de Vocabulário

Você prova uma sopa e ela não tem gosto de nada (falta sal e tempero). Como você descreve?

"This soup is completely ______."

A) bland B) savory C) rich
Imagem de salt shakerAbre em uma nova janela
www.thekitchn.com
salt shaker
Correção do Desafio

A resposta correta é A.

Explicação: Bland é a palavra para comida sem sabor, insossa.
Imagem de two friends sharing different dishes at a restaurant tableAbre em uma nova janela

two friends sharing different dishes at a restaurant table
Dialogue: Tasting Menu

John: Try this shrimp. It is amazing. Emma: Wow, it is very spicy! I need water. John: Sorry, I forgot you don't like hot food. Try the risotto instead. Emma: Mmm, this is delicious. It is very creamy and rich. John: And how is your lemonade? Emma: It is a bit too sour. I think I will add some sugar to make it sweet.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Descreva sua comida favorita (ou a que menos gosta) usando os adjetivos.

"I have a sweet tooth, so I love desserts. My favorite is chocolate cake, especially if it is rich and moist. However, I also enjoy savory snacks like salty popcorn. I can't stand bland food like plain tofu. And I am careful with spicy food because it hurts my stomach!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 19, Tema Central: Recommending Things
Imagem de person excitedly pointing at a menu item to a friend in a restaurantAbre em uma nova janela

person excitedly pointing at a menu item to a friend in a restaurant
Recommending Things
Social English - Pill 19

Quando você gosta muito de um filme, de um restaurante ou de um lugar, você quer compartilhar.

Hoje vamos aprender a dar recomendações e dicas ("tips") usando as estruturas corretas, do básico ao avançado.
Imagem de lightbulb symbol representing an idea or suggestionAbre em uma nova janela

lightbulb symbol representing an idea or suggestion
The Modal Verb: "Should"

A maneira mais comum e direta de dar um conselho ou recomendação é usando Should.

Estrutura: Subject + should + Verb (Base form)

    You should go to that new museum. (Você deveria ir àquele novo museu.)

Imagem de person holding a movie ticket offering it to someoneAbre em uma nova janela

person holding a movie ticket offering it to someone
Examples with "Should"

Use para sugestões amigáveis.

    You should watch the new Marvel movie.

    You should try the cheesecake here. It is delicious.

    He should visit the castle if he likes history.

Imagem de waiter presenting a bottle of wine with an elegant gestureAbre em uma nova janela

waiter presenting a bottle of wine with an elegant gesture
The Verb "Recommend" + Noun

Para soar um pouco mais formal ou enfático, usamos o verbo Recommend.

A forma mais fácil é usar com um Substantivo (coisa).

Estrutura: I recommend + [The Thing]

    I recommend the lasagna.

    I recommend this book.

Imagem de warning sign highlighting a grammar trapAbre em uma nova janela
hoxhunt.com
warning sign highlighting a grammar trap
The Grammar Trap: Recommend + ING

Atenção! Este é um erro muito comum de brasileiros.

Se você usar um verbo depois de Recommend, ele PRECISA estar no gerúndio (-ING).

    Incorreto: I recommend ~~to go~~ there.

    Correto: I recommend going there.

Imagem de person visiting a tourist attraction taking a photoAbre em uma nova janela

person visiting a tourist attraction taking a photo
Examples: Recommend + ING

Memorize este padrão:

    I recommend booking a table in advance. (Recomendo reservar uma mesa com antecedência.)

    She recommends visiting the park in the morning. (Ela recomenda visitar o parque de manhã.)

    Do you recommend taking a taxi? (Você recomenda pegar um táxi?)

Imagem de finger pointing specifically at a dish on a tableAbre em uma nova janela
www.daijob.com
finger pointing specifically at a dish on a table
Imperatives: "Try the..."

Se você está com amigos, pode ser bem direto usando o Imperativo. Soa como um convite entusiasmado.

    "Try the wine!" (Experimente o vinho!)

    "Don't miss the show!" (Não perca o show!)

    "Go to the beach!" (Vá à praia!)

Imagem de person with wide eyes and a big smile showing excitementAbre em uma nova janela

person with wide eyes and a big smile showing excitement
Strong Recommendations: "You have to..."

Quando algo é incrível e indispensável, usamos "You have to..." ou "You must...".

Aqui, não é uma obrigação chata, é entusiasmo!

    You have to see the view from the top!

    You must try the chocolate cake!

Imagem de set of scales balancing price and value perfectlyAbre em uma nova janela

set of scales balancing price and value perfectly
Is it worth it?

Uma expressão excelente para dizer que algo vale o tempo ou o dinheiro investido:

"It is worth it." (Vale a pena).

    The ticket is expensive, but it is worth it.

    It is a long drive, but it is worth visiting.

Imagem de 5star review symbol or a gold medalAbre em uma nova janela
www.freepik.com
5star review symbol or a gold medal
A "Must-See" / "Must-Do"

Podemos transformar "Must" em um adjetivo substantivado.

    A must-see: Algo que é obrigatório ver.

        The Eiffel Tower is a must-see.

    A must-do: Algo obrigatório fazer.

    A must-have: Algo obrigatório ter.

Imagem de tourist holding a map asking a local person for directionsAbre em uma nova janela

tourist holding a map asking a local person for directions
Asking for Recommendations

Como pedir dicas?

    Do you have any recommendations?

    What do you recommend?

    Is there anything worth seeing around here?

    What is the best place to eat pizza?

Imagem de multiple choice quiz layout on a tablet screenAbre em uma nova janela
www.rosemet.com
multiple choice quiz layout on a tablet screen
Vamos Praticar? - Exercício 1

Qual a frase gramaticalmente correta?

A) I recommend to visit the museum. B) I recommend visit the museum. C) I recommend visiting the museum.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Após o verbo recommend, se usarmos outro verbo, ele deve estar no formato -ING.

Frase: "I recommend visiting the museum."
Imagem de sentence completion exercise with a missing wordAbre em uma nova janela
www.turtlediary.com
sentence completion exercise with a missing word
Desafio de Vocabulário

Qual a expressão para dizer que algo "vale a pena"?

"The line was long, but the ride was totally ______."

A) worth it B) worthy C) value
Imagem de thumbs up sign indicating approvalAbre em uma nova janela

thumbs up sign indicating approval
Correção do Desafio

A resposta correta é A.

Explicação: A expressão fixa é It is worth it.

Frase: "The ride was totally worth it."
Imagem de two friends looking at a travel brochure or phone screen togetherAbre em uma nova janela

two friends looking at a travel brochure or phone screen together
Dialogue: Travel Tips

Tourist: I have one free day in the city. Do you have any recommendations? Local: Definitely. You should go to the Central Market. Tourist: Is it good for lunch? Local: Yes! I recommend trying the fish sandwich. It is a local classic. Tourist: Thanks. Is the Art Museum good? Local: It is nice, but the ticket is expensive. I don't think it is worth it. Tourist: Okay, I will skip it. Local: But you have to see the Sunset Park. It is a must-see!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique dar recomendações em voz alta.

"If you visit my city, I have some tips for you. First, you should visit the old town. It is beautiful. For dinner, I recommend going to 'Mario's Pizza'. You have to try their pepperoni pizza, it is the best! Also, don't miss the botanical garden. It is a bit far, but it is totally worth it."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 20, Tema Central: Review: My Perfect Weekend
Imagem de sunny weekend morning with coffee, a book, and a relaxed atmosphereAbre em uma nova janela

sunny weekend morning with coffee, a book, and a relaxed atmosphere
Review: My Perfect Weekend
Social English - Pill 20

Chegamos à pílula de revisão!

Hoje vamos consolidar tudo o que aprendemos até agora: gostos, desgostos, frequência, esportes e hobbies, montando a narrativa do seu fim de semana ideal.
Imagem de weekly planner highlighting Saturday and SundayAbre em uma nova janela
inkpx.com
weekly planner highlighting Saturday and Sunday
Step 1: The Morning Routine

Comece descrevendo como você acorda. Use advérbios de frequência.

    On my perfect Saturday, I usually wake up late.

    I can't stand waking up early on weekends!

    I love having a big breakfast with pancakes.

Imagem de person putting on running shoes or hiking bootsAbre em uma nova janela
www.mammut.com
person putting on running shoes or hiking boots
Step 2: Morning Activity (Sports)

Lembre-se da diferença entre Play, Go e Do.

    After breakfast, I go running in the park.

    Or sometimes I do yoga to relax.

    If the weather is nice, I go hiking.

(Não diga "play running" ou "make yoga"!)
Imagem de delicious burger and a salad on a restaurant tableAbre em uma nova janela
www.freepik.com
delicious burger and a salad on a restaurant table
Step 3: Lunch Time (Eating Out)

Fale sobre onde você come e o sabor.

    For lunch, I go to my favorite burger place.

    It is a casual dining restaurant.

    The burgers there are very tasty and savory.

    I recommend trying their fries too.

Imagem de person holding a book and another holding a game controllerAbre em uma nova janela
www.alamy.com
person holding a book and another holding a game controller
Step 4: Afternoon Hobbies

Fale sobre o que você gosta de fazer ("I enjoy...", "I am really into...").

    In the afternoon, I enjoy reading a good book.

    Right now, I am reading a thriller. It is a real page-turner.

    Or sometimes I play video games. I am really into RPGs.

Imagem de group of friends laughing at a dinner tableAbre em uma nova janela
www.freepik.com
group of friends laughing at a dinner table
Step 5: Evening Socializing

Encontrando amigos.

    In the evening, I meet my friends.

    We usually go out for dinner or drinks.

    We talk about everything. It is always fun.

Imagem de movie theater screen showing a comedy sceneAbre em uma nova janela
www.freepik.com
movie theater screen showing a comedy scene
Step 6: Late Night (Movies/Series)

Terminando o dia.

    Before bed, I watch a movie.

    I am not a fan of horror movies, so I watch a comedy.

    I love sitcoms like "Friends".

    It helps me relax.

Imagem de roadmap showing connectors: First > Then > After that > FinallyAbre em uma nova janela
www.slideteam.net
roadmap showing connectors: First > Then > After that > Finally
Connecting Ideas

Para sua história não ficar "robótica", use conectores:

    First, I wake up...

    Then, I go to the gym...

    After that, I have lunch...

    Later, I meet friends...

    Finally, I go to sleep.

Imagem de signpost pointing to Good and BadAbre em uma nova janela

signpost pointing to Good and Bad
Recap: Likes & Dislikes

Use variações para não repetir "I like":

    Positivo: I enjoy, I love, I am really into, I am crazy about.

    Negativo: I don't like, I am not a fan of, I can't stand, It drives me crazy.

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar? - Gramática

Complete a frase corretamente:

"I enjoy ______ tennis, but I am terrible ______ it."

A) play / in B) playing / at C) to play / at
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação:

    Depois de enjoy, usamos -ING (playing).

    Depois de good/terrible, a preposição é AT.

Frase: "I enjoy playing tennis, but I am terrible at it."
Imagem de scrambled sentence puzzleAbre em uma nova janela
educationtothecore.com
scrambled sentence puzzle
Desafio de Estrutura

Coloque a frase na ordem certa:

[ go / usually / on Saturdays / I / cycling ]

A) I usually go cycling on Saturdays. B) I go usually cycling on Saturdays. C) Usually I cycling go on Saturdays.
Imagem de cyclist on a roadAbre em uma nova janela
en.wikipedia.org
cyclist on a road
Correção do Desafio

A resposta correta é A.

Explicação: Advérbio de frequência (usually) vem antes do verbo principal (go).

Frase: "I usually go cycling on Saturdays."
Imagem de person holding a microphone preparing to speakAbre em uma nova janela

person holding a microphone preparing to speak
Preparation for the Final Task

Agora você vai juntar tudo.

Imagine seu fim de semana perfeito. Não precisa ser verdade, pode ser inventado!

Use:

    1 Atividade física (Go/Play/Do).

    1 Comida (Taste/Restaurant).

    1 Hobby (Book/Movie/Game).

    Conectores de tempo.

Imagem de two friends listening intently to a storyAbre em uma nova janela

two friends listening intently to a story
Example Narrative

"First, I wake up late. Then, I go swimming because I love being in the water. After that, I eat at an Italian restaurant. The pasta is delicious. Later, I read a sci-fi book. Finally, I watch a movie."
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Tarefa Final: Grave um áudio descrevendo seu fim de semana ideal (use o texto abaixo como base ou crie o seu).

"My perfect weekend starts on Saturday morning. First, I sleep until 10 AM because I can't stand waking up early. Then, I go hiking with my friends. The scenery is breathtaking. For lunch, we go to a casual restaurant. I usually order a burger because I love savory food. In the afternoon, I relax. I enjoy playing video games on my console. Finally, at night, I watch a Sitcom. It is the perfect way to end the day."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 21, Tema Central: Making Suggestions: "Let's..."
Imagem de group of friends looking at a map or phone together, deciding where to goAbre em uma nova janela

group of friends looking at a map or phone together, deciding where to go
Making Suggestions: "Let's..."
Social English - Pill 21

Você está com seus amigos e quer propor uma atividade. Como dizer "Vamos..." em inglês?

Hoje vamos dominar o uso de "Let's", a forma mais comum e natural de fazer sugestões inclusivas.
Imagem de two puzzle pieces joining: one labeled Let and the other Us forming Let'sAbre em uma nova janela
chemistrytalk.org
two puzzle pieces joining: one labeled Let and the other Us forming Let's
O que significa "Let's"?

"Let's" é a contração de "Let us" (Deixe-nos).

Nós usamos para sugerir algo que nós (eu + você + outros) faremos juntos.

É o equivalente direto ao nosso imperativo "Vamos" (Vamos comer, vamos sair).
Imagem de simple formula: Let's + Verb (Base Form)Abre em uma nova janela
www.curiousjr.com
simple formula: Let's + Verb (Base Form)
A Estrutura de Ouro

A regra é muito simples, mas muita gente erra colocando "to" ou "-ing".

Estrutura: Let's + Verbo (Forma Base)

    Correto: Let's go home.

    Incorreto: ~~Let's to go~~ home.

    Incorreto: ~~Let's going~~ home.

Imagem de icons representing actions: a pizza slice, a movie camera, and a carAbre em uma nova janela

icons representing actions: a pizza slice, a movie camera, and a car
Exemplos Práticos

Use para qualquer atividade em grupo:

    Let's eat pizza tonight. (Vamos comer pizza hoje à noite.)

    Let's watch a movie. (Vamos assistir a um filme.)

    Let's take a taxi. (Vamos pegar um táxi.)

Imagem de thumbs up icon and a smiling faceAbre em uma nova janela
pngtree.com
thumbs up icon and a smiling face
Accepting a Suggestion

Se alguém diz "Let's go out!", como você concorda?

    "Good idea!" (Boa ideia!)

    "Sure!" (Claro!)

    "Why not?" (Por que não?)

    "Let's do it!" (Vamos fazer isso!)

Imagem de polite hand gesture declining, or a calendar marked BusyAbre em uma nova janela
piktochart.com
polite hand gesture declining, or a calendar marked Busy
Declining Politely

E se você não quiser ir? Não diga apenas "No".

    "Maybe later." (Talvez mais tarde.)

    "I'd love to, but I can't." (Eu adoraria, mas não posso.)

    "I'm a bit tired, sorry." (Estou um pouco cansado, desculpe.)

    "Actually, I prefer to stay home." (Na verdade, prefiro ficar em casa.)

Imagem de sunny beach scene with friends walkingAbre em uma nova janela

sunny beach scene with friends walking
Context: Weekend Plans

Sugerindo lazer:

    "The weather is beautiful. Let's go to the beach."

    "It is Saturday night. Let's have a party."

    "I am bored. Let's go shopping."

Imagem de two coworkers holding coffee cups in an officeAbre em uma nova janela

two coworkers holding coffee cups in an office
Context: Work & Study

Sugerindo pausas ou foco:

    "We are tired. Let's take a break."

    "This meeting is long. Let's finish early."

    "The exam is tomorrow. Let's study together."

Imagem de road sign splitting into Let's and Let meAbre em uma nova janela
www.gymshark.com
road sign splitting into Let's and Let me
Let's vs. Let me

Cuidado para não confundir:

    Let's (Let us): Sugestão para o grupo (Nós).

        "Let's go!" (Eu e você).

    Let me: Pedido de permissão ou oferta de ajuda (Eu).

        "Let me help you." (Eu ajudo você).

Imagem de warning sign highlighting the negative form Let's notAbre em uma nova janela
www.bringthedonuts.com
warning sign highlighting the negative form Let's not
The Negative: "Let's not..."

Como sugerir não fazer algo?

Estrutura: Let's not + Verbo

    It is raining. Let's not go out. (Está chovendo. Não vamos sair.)

    It is late. Let's not argue. (Está tarde. Não vamos discutir.)

Imagem de multiple choice quiz layout on a screenAbre em uma nova janela

multiple choice quiz layout on a screen
Vamos Praticar?

Qual a frase gramaticalmente correta?

A) Let's to play soccer. B) Let's playing soccer. C) Let's play soccer.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção

A resposta correta é C.

Explicação: Depois de Let's, usamos o verbo na sua forma base pura, sem "to" e sem "-ing".

Frase: "Let's play soccer."
Imagem de person looking at a menu and shaking their headAbre em uma nova janela
www.hopkinsmedicine.org
person looking at a menu and shaking their head
Desafio de Tradução

Seu amigo diz: "Let's eat Japanese food." Mas você não gosta. Como você diz "Não vamos comer isso" educadamente?

A) Let's not eat that. B) Let's don't eat that. C) No, I hate it.
Imagem de polite conversation sceneAbre em uma nova janela

polite conversation scene
Correção do Desafio

A resposta correta é A.

Explicação: A negativa gramatical de "Let's" é Let's not. (A opção C está gramaticalmente correta, mas socialmente pode soar um pouco rude dependendo do tom).

Frase: "Let's not eat that. I prefer Italian."
Imagem de group of friends standing in a circle making plansAbre em uma nova janela

group of friends standing in a circle making plans
Dialogue: Making Plans

Alice: I am so bored. Ben: Me too. Let's do something fun. Alice: Let's go to the cinema. There is a new comedy. Ben: Hmm, I don't feel like sitting in the dark. Alice: Okay. Let's go to the park then. We can have a picnic. Ben: Good idea! Let's buy some snacks first.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique fazer sugestões com entusiasmo!

"It is finally Friday! Let's make plans for the weekend. Let's call our friends and organize a dinner. We can try that new burger place. Or, if you prefer, let's just stay home and order pizza. Let's not worry about work until Monday!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 22, Tema Central: Making Suggestions: "Why don't we...?"
Imagem de group of friends brainstorming ideas, looking thoughtful and happyAbre em uma nova janela

group of friends brainstorming ideas, looking thoughtful and happy
Making Suggestions: "Why don't we...?"
Social English - Pill 22

Já aprendemos "Let's". Agora vamos aprender uma forma um pouco mais educada e democrática de fazer sugestões.

A estrutura "Why don't we...?" é essencial para propor planos de forma natural.
Imagem de question mark transforming into a lightbulb, symbolizing a suggestion phrased as a questionAbre em uma nova janela

question mark transforming into a lightbulb, symbolizing a suggestion phrased as a question
Uma Sugestão, Não Uma Pergunta

Apesar de começar com "Why" (Por que), essa frase não está perguntando o motivo real de não fazermos algo.

Ela é uma forma retórica de dizer: "Que tal se a gente fizesse X?" ou "Por que a gente não faz X?".

É um convite, não uma investigação.
Imagem de grammatical structure: Why + don't + we + Verb (Base)Abre em uma nova janela
vocaberry.com
grammatical structure: Why + don't + we + Verb (Base)
A Estrutura

A gramática é simples e fixa.

Why + don't + we + Verb (Base Form) + ...?

    Correto: Why don't we go to the cinema?

    Incorreto: ~~Why don't we going~~ to the cinema?

Imagem de couple looking at a restaurant menu in a windowAbre em uma nova janela
www.alamy.com
couple looking at a restaurant menu in a window
Exemplos com "We" (Nós)

Use para planos conjuntos:

    Why don't we eat Italian food tonight? (Por que não comemos comida italiana hoje?)

    Why don't we take a taxi? It is raining. (Por que não pegamos um táxi?)

    Why don't we meet at 8 PM? (Que tal nos encontrarmos às 20h?)

Imagem de one person giving advice to another person who looks confusedAbre em uma nova janela
www.marriage.com
one person giving advice to another person who looks confused
Variação: "Why don't you...?" (Conselho)

Você pode trocar "We" por "You" para dar um conselho ou sugestão para a outra pessoa.

Why + don't + you + Verb...?

Significa: "Por que você não..." (Eu sugiro que você faça isso).
Imagem de person tired at a desk and a friend pointing to a bed or rest areaAbre em uma nova janela
openup.com
person tired at a desk and a friend pointing to a bed or rest area
Exemplos com "You" (Conselho)

    Why don't you call him? (Por que você não liga para ele?)

    Why don't you rest a little? (Por que você não descansa um pouco?)

    Why don't you try the new app? (Por que você não experimenta o novo app?)

Imagem de two people shaking hands or giving a thumbs upAbre em uma nova janela

two people shaking hands or giving a thumbs up
Aceitando a Sugestão

Como responder a um "Why don't we..."?

    "That sounds good." (Soa bem / Boa ideia.)

    "That's a great idea." (Ótima ideia.)

    "Sure, why not?" (Claro, por que não?)

    "Let's do that." (Vamos fazer isso.)

Imagem de person looking unsure or checking an empty walletAbre em uma nova janela

person looking unsure or checking an empty wallet
Recusando Educadamente

Se você não quer ir:

    "I am not sure about that." (Não tenho certeza sobre isso.)

    "Maybe we could go somewhere else." (Talvez pudéssemos ir em outro lugar.)

    "I'd rather not." (Prefiro que não.)

Imagem de mouth showing pronunciation movement for linking soundsAbre em uma nova janela

mouth showing pronunciation movement for linking sounds
Pronunciation Tip: Linking

Nativos falam rápido e conectam os sons.

    Why don't we: Soa como "Wai-don-wi".

    Why don't you: Soa como "Wai-don-tchu". (O som T + Y vira CH).

Treine falar junto: "Why don't you" -> "Wai-don-tchu".
Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Seu amigo está entediado. Qual a forma correta de sugerir um filme?

A) Why don't we watching a movie? B) Why don't we watch a movie? C) Why no watch a movie?
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Após Why don't we, usamos o verbo na forma base (sem -ing, sem to).

Frase: "Why don't we watch a movie?"
Imagem de sentence transformation puzzleAbre em uma nova janela
topnotchteaching.com
sentence transformation puzzle
Desafio de Transformação

Transforme o imperativo em uma sugestão polida usando "Why don't you".

Original: "Buy the blue shirt." Sugestão: ______________________.

A) Why don't you buy the blue shirt? B) Why you don't buy the blue shirt? C) Why don't buy the blue shirt?
Imagem de person holding a blue shirt smilingAbre em uma nova janela

person holding a blue shirt smiling
Correção do Desafio

A resposta correta é A.

Explicação: A estrutura de pergunta exige o auxiliar antes do sujeito: Why don't you...

Frase: "Why don't you buy the blue shirt?"
Imagem de two colleagues organizing a meeting or lunchAbre em uma nova janela

two colleagues organizing a meeting or lunch
Dialogue: Lunch Break

Tom: I am starving. Where should we go for lunch? Jerry: Why don't we try that new burger place? Tom: I am not sure. It is usually very crowded. Jerry: Okay. Why don't we order pizza then? Tom: That sounds good. Why don't you call them? Jerry: Sure, I will do it now.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique sugerir planos em voz alta.

"I am bored. Why don't we go out? The weather is nice, so why don't we go to the park? We can play soccer. Or, if you are tired, why don't you take a nap first? After that, why don't we eat ice cream? That sounds like a perfect plan."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 23, Tema Central: Inviting Someone: "Do you want to...?"
Imagem de two friends looking at a smartphone screen, one showing something to the other with a questioning lookAbre em uma nova janela
www.t-mobile.com
two friends looking at a smartphone screen, one showing something to the other with a questioning look
Inviting Someone: "Do you want to...?"
Social English - Pill 23

Você quer chamar um amigo para sair, comer ou jogar?

A forma mais comum, direta e natural de fazer um convite informal em inglês é usando a estrutura "Do you want to...?".

]
Imagem de simple diagram: Do you want to + [Action VerbAbre em uma nova janela
safehugs.in
simple diagram: Do you want to + [Action Verb
The Structure

A gramática é simples. Usamos o auxiliar de presente Do.

Estrutura: Do + you + want + to + Verb (Base Form)?

Significa literalmente: "Você quer...?"

    Correto: Do you want to go to the park?

    Incorreto: Do you want going to the park?

Imagem de coffee cup and a movie ticket side by sideAbre em uma nova janela
www.makeuseof.com
coffee cup and a movie ticket side by side
Common Invitations

Exemplos clássicos do dia a dia:

    Do you want to grab a coffee? (Quer pegar um café?)

    Do you want to see a movie? (Quer ver um filme?)

    Do you want to come with us? (Quer vir com a gente?)

Imagem de speech bubble showing Wanna text being formed from Want toAbre em uma nova janela
www.animaker.com
speech bubble showing Wanna text being formed from Want to
Pronunciation: "Wanna"

Em situações sociais e informais, os nativos quase nunca pronunciam "want to" separadamente. Eles juntam os sons.

Want to = Wanna

    Escrita: "Do you want to go?"

    Fala: "Do you wanna go?"

Dica: Use "Wanna" na fala ou mensagens de texto para amigos, mas evite em e-mails formais.
Imagem de casual setting like a burger joint vs a formal boardroom setting, contrasting contextsAbre em uma nova janela
www.restaurantindia.in
casual setting like a burger joint vs a formal boardroom setting, contrasting contexts
Context: Informal vs Formal

Esta estrutura é Informal.

    Use com: Amigos, família, colegas próximos.

        "Do you want to eat pizza?"

    Evite com: Chefes, clientes importantes ou desconhecidos (Para eles, usamos "Would you like to..." - veremos na próxima pílula).

Imagem de clock showing 8 PM and a map pin iconAbre em uma nova janela
www.freepik.com
clock showing 8 PM and a map pin icon
Adding Details: When & Where

Um convite precisa de detalhes.

Adicione o tempo e o lugar no final da frase.

    Do you want to have dinner tonight?

    Do you want to go to the mall on Saturday?

    Do you want to play tennis after work?

Imagem de hand holding a phone sending a text messageAbre em uma nova janela

hand holding a phone sending a text message
Ultra-Short Version (Texting)

Em mensagens de texto (WhatsApp) ou fala muito rápida entre melhores amigos, às vezes o "Do" ou o "Do you" desaparece.

    "Want to go out?" (Tirou o "Do you")

    "Wanna hang out?" (Tirou tudo e usou gíria)

Isso é muito informal!
Imagem de two people sitting on a sofa chatting and laughingAbre em uma nova janela

two people sitting on a sofa chatting and laughing
Useful Phrasal Verb: Hang out

O verbo mais usado para "passar tempo junto sem fazer nada específico" é Hang out.

    "Do you want to hang out?" (Quer "ficar de bobeira"/sair/passar um tempo junto?)

    "Let's hang out at my place."

Imagem de person holding a door open for another, inviting them insideAbre em uma nova janela

person holding a door open for another, inviting them inside
Useful Phrasal Verb: Come over

Convite para ir à casa de alguém.

    "Do you want to come over?" (Quer vir aqui em casa?)

    "Do you want to come over for dinner?" (Quer vir aqui jantar?)

Imagem de green thumbs up iconAbre em uma nova janela
designbundles.net
green thumbs up icon
Accepting the Invitation

Como dizer sim?

    "Sure, I'd love to." (Claro, adoraria.)

    "Yeah, sounds good." (Sim, soa bem.)

    "Definitely!" (Com certeza!)

    "Why not?" (Por que não?)

Imagem de multiple choice quiz layout on a screenAbre em uma nova janela

multiple choice quiz layout on a screen
Vamos Praticar? - Exercício 1

Qual a forma correta e completa de convidar alguém para dançar?

A) You want dance? B) Do you want to dance? C) Do you want dancing?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A estrutura completa exige o auxiliar Do no início e o infinitivo com to depois de want.

Frase: "Do you want to dance?"
Imagem de puzzle with words to be arranged in orderAbre em uma nova janela
www.64ouncegames.com
puzzle with words to be arranged in order
Desafio de Estrutura

Coloque as palavras na ordem para convidar um amigo para almoçar hoje.

[ lunch / to / have / want / today / do / you ]

A) Do you want to have lunch today? B) Do you have to want lunch today? C) You want do to have lunch today?
Imagem de plate of lunch with a calendar showing today's dateAbre em uma nova janela

plate of lunch with a calendar showing today's date
Correção do Desafio

A resposta correta é A.

Explicação: Ordem: Auxiliar (Do) + Sujeito (you) + Verbo 1 (want) + to + Verbo 2 (have) + Objeto (lunch) + Tempo (today).

Frase: "Do you want to have lunch today?"
Imagem de two friends texting on their phones, split screen effectAbre em uma nova janela

two friends texting on their phones, split screen effect
Dialogue: Making Plans via Text

Max: Hey, are you busy? Leo: No, just watching TV. Max: Do you want to hang out? Leo: Sure. What do you have in mind? Max: Do you want to play video games at my house? Leo: Yeah, sounds fun. Max: Do you want to come over around 7 PM? Leo: Perfect. See you then.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique fazer convites usando a pronúncia natural (pode usar "wanna" se quiser soar bem fluente!).

"Hey! Are you free this weekend? Do you want to go to the beach on Saturday? Or maybe do you want to see a movie? If you are tired, do you want to just hang out at my place? We can order pizza. Do you want to come over at 8?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 24, Tema Central: Inviting Someone: "Would you like to...?"
Imagem de person in a suit offering a hand or a seat to someone in a polite mannerAbre em uma nova janela
www.daijob.com
person in a suit offering a hand or a seat to someone in a polite manner
Inviting Someone: "Would you like to...?"
Social English - Pill 24

Na aula passada, vimos o convite informal ("Do you want to...?").

Mas e se você estiver convidando um chefe, um cliente ou alguém em um primeiro encontro?

Você precisa de mais polidez. Para isso, usamos "Would you like to...?".
Imagem de butler holding a silver tray, representing service and politenessAbre em uma nova janela

butler holding a silver tray, representing service and politeness
The Politeness Level

A diferença principal é o tom.

    "Do you want to go?" = Informal, direto. (Amigos).

    "Would you like to go?" = Formal, educado, sofisticado. (Trabalho, Romance, Desconhecidos).

Em português, seria a diferença entre "Quer ir?" e "Você gostaria de ir?".
Imagem de grammatical structure: Would + you + like + to + VerbAbre em uma nova janela
test-english.com
grammatical structure: Would + you + like + to + Verb
The Structure

A gramática é fixa. O auxiliar Would vem sempre no início da pergunta.

Estrutura: Would + you + like + to + Verb (Base)?

    Correto: Would you like to dance?

    Incorreto: ~~Do you would like to~~ dance?

Imagem de romantic dinner setting with candles and flowersAbre em uma nova janela

romantic dinner setting with candles and flowers
Examples: Romantic Context

Em encontros ("dates"), usar essa estrutura mostra respeito e cavalheirismo.

    Would you like to have dinner with me? (Você gostaria de jantar comigo?)

    Would you like to go for a walk? (Gostaria de dar uma caminhada?)

Imagem de business meeting room with professionals talkingAbre em uma nova janela
www.alamy.com
business meeting room with professionals talking
Examples: Business Context

No trabalho, sempre prefira esta forma.

    Would you like to join us for lunch? (Gostaria de se juntar a nós para o almoço?)

    Would you like to see the project? (Gostaria de ver o projeto?)

Imagem de glass of water and a cup of coffeeAbre em uma nova janela
pontevecchiosrl.it
glass of water and a cup of coffee
Offering Things (Nouns)

Você também pode usar para oferecer coisas (comida/bebida), sem o "to".

    Would you like some coffee? (Gostaria de um pouco de café?)

    Would you like a glass of water? (Gostaria de um copo d'água?)

Imagem de person smiling and nodding enthusiasticallyAbre em uma nova janela
www.freepik.com
person smiling and nodding enthusiastically
Accepting: "I'd love to"

A resposta padrão e entusiasmada para esse convite é:

"I would love to."

Geralmente contraímos o "I would" para "I'd".

    "I'd love to, thank you!" (Eu adoraria, obrigado!)

Imagem de person looking apologetic with hand on chestAbre em uma nova janela
www.alamy.com
person looking apologetic with hand on chest
Declining: "I'd love to, but..."

Para recusar sem ser rude, use a técnica do "sanduíche" (Positivo + Negativo).

    Comece aceitando a ideia: "I'd love to..."

    Dê a negativa: "...but I can't."

    Dê o motivo (opcional): "I have to work."

    "I'd love to, but I have a meeting."

Imagem de mouth showing the pronunciation of the sound JAbre em uma nova janela
www.youtube.com
mouth showing the pronunciation of the sound J
Pronunciation: "Would you"

Quando falamos rápido, o som do D em "Would" se junta com o Y de "you".

O som resultante é um "Dj" ou "J" suave.

"Would you" soa como "Wuh-ju".

    "Wuh-ju like to go?"

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar? - Exercício 1

Qual a forma correta de convidar seu chefe para uma reunião?

A) Do you want come to the meeting? B) Would you like to come to the meeting? C) Would you like coming to the meeting?
Imagem de green checkmark indicating successAbre em uma nova janela
freerangestock.com
green checkmark indicating success
Correção - Exercício 1

A resposta correta é B.

Explicação: Usamos Would you like + to + Verbo base. A opção A é muito informal para um chefe e tem erro gramatical. A opção C usa o gerúndio incorretamente.
Imagem de sentence transformation puzzleAbre em uma nova janela
topnotchteaching.com
sentence transformation puzzle
Desafio de Polidez

Transforme este convite informal em formal:

Informal: "Do you want to drink tea?" Formal: __________________________?

A) Would you like to drink tea? B) Would you want to drink tea? C) Do you like to drink tea?
Imagem de porcelain tea cup and saucerAbre em uma nova janela
ichkan.com
porcelain tea cup and saucer
Correção do Desafio

A resposta correta é A.

Explicação: Trocamos "Do you want" por Would you like. O resto da frase mantém a estrutura com "to".

Frase: "Would you like to drink tea?"
Imagem de man and a woman standing in an office corridor talkingAbre em uma nova janela
www.freepik.com
man and a woman standing in an office corridor talking
Dialogue: The Invitation

Mr. Smith: Good morning, Jessica. Are you busy right now? Jessica: No, Mr. Smith. Just finishing a report. Mr. Smith: Would you like to join me for a coffee break? We need to discuss the new client. Jessica: I'd love to. I need a break anyway. Mr. Smith: Great. Would you like to go to the cafe downstairs? Jessica: Perfect. Let's go.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique fazer convites formais e aceitá-los.

"Hello. I have an extra ticket for the opera tonight. Would you like to come with me? I know you like music. Also, would you like to grab dinner before the show? There is a nice French restaurant nearby. If you are free, I'd love to see you there."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 25, Tema Central: Accepting an Invitation
Imagem de person receiving an invitation card and smiling happilyAbre em uma nova janela

person receiving an invitation card and smiling happily
Accepting an Invitation
Social English - Pill 25

Recebeu um convite ("Do you want to...?" ou "Would you like to...?")?

Agora você precisa saber responder Sim com entusiasmo e naturalidade. Dizer apenas "Yes" pode soar frio. Vamos aprender as melhores respostas.
Imagem de large green thumbs up symbolAbre em uma nova janela

large green thumbs up symbol
The Basic Yes: "Sure" & "Of course"

Para aceitar de forma rápida e direta, evite o simples "Yes". Use:

    Sure: Claro/Com certeza. (Muito comum e amigável).

        "Sure, let's go!"

    Of course: Claro que sim.

        "Of course I want to come."

Imagem de heart symbol representing love or enthusiasmAbre em uma nova janela
en.wikipedia.org
heart symbol representing love or enthusiasm
The Enthusiastic Yes: "I'd love to!"

Esta é a resposta perfeita para convites com "Would you like...?", mas serve para todos. Demonstra que você ficou feliz com o convite.

"I'd love to." (Eu adoraria).

    A: Would you like to have dinner?

    B: I'd love to, thank you!

Imagem de musical note or ear icon representing listeningAbre em uma nova janela

musical note or ear icon representing listening
The Casual Yes: "Sounds good"

Quando alguém propõe um plano ("Let's go to the park"), você reage à ideia.

    "That sounds good." (Soa bem).

    "Sounds great!" (Soa ótimo).

    "Sounds like a plan." (Parece um plano/Combinado).

    "Sounds fun." (Parece divertido).

Imagem de group of friends putting their hands together in a circleAbre em uma nova janela
unsplash.com
group of friends putting their hands together in a circle
The Slang Yes: "Count me in"

Uma expressão idiomática muito usada entre amigos para dizer "Pode contar comigo" ou "Estou dentro".

"Count me in."

    A: We are going to the beach.

    B: Awesome. Count me in!

Imagem de person shrugging shoulders with a relaxed smileAbre em uma nova janela

person shrugging shoulders with a relaxed smile
The Relaxed Yes: "Why not?"

Se você não tem nada melhor para fazer e aceita o convite de forma tranquila:

"Sure, why not?"

    A: Do you want to try that new bar?

    B: Why not? Let's go.

Imagem de smartphone screen with chat bubbles showing short abbreviationsAbre em uma nova janela
www.omnisend.com
smartphone screen with chat bubbles showing short abbreviations
Texting & Short Answers

Em mensagens de texto (WhatsApp), somos breves:

    "Def!" (Short for Definitely).

    "I'm down." (Gíria para "Estou dentro" / "Topo").

    "You bet!" (Pode apostar / Com certeza).

Imagem de clock face and a map pin iconAbre em uma nova janela

clock face and a map pin icon
Confirming Details

Ao aceitar, é educado confirmar os detalhes imediatamente.

    "I'd love to. What time?"

    "Sure. Where should we meet?"

    "Sounds good. Do I need to bring anything?"

Imagem de checklist showing different levels of formality from formal to slangAbre em uma nova janela
www.oneteam.io
checklist showing different levels of formality from formal to slang
Summary of Acceptance

Escolha de acordo com a situação:

    Formal: I would be delighted. (Muito formal)

    Polite: I'd love to. (Padrão ouro)

    Standard: Sure / Sounds good. (Dia a dia)

    Slang: I'm down / Count me in. (Amigos)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a melhor resposta para um convite formal ("Would you like to join us?")?

A) I'm down. B) Why not? C) I'd love to.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Se a pergunta usa Would you like, a resposta mais adequada e educada é I'd love to. As outras são informais demais.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a expressão que significa "Pode contar comigo":

"That trip sounds amazing. Count me ______!"

A) on B) in C) up
Imagem de person raising their hand to join a groupAbre em uma nova janela

person raising their hand to join a group
Correção do Desafio

A resposta correta é B.

Explicação: A expressão fixa é Count me in (Me inclua). O oposto (se você não vai) seria Count me out.
Imagem de two friends chatting excitedly in a coffee shopAbre em uma nova janela

two friends chatting excitedly in a coffee shop
Dialogue: The Plan

Alice: Hey, do you want to go to the cinema on Friday? Bob: Sure, sounds fun. What movie is playing? Alice: The new Spider-Man. Bob: Oh, I'd love to see that! Count me in. Alice: Great. Why don't we eat tacos before the movie? Bob: Sounds like a plan. I am always hungry for tacos.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique aceitar convites com entonação positiva.

"Thanks for the invitation! I'd love to come to your party. It sounds like a lot of fun. Count me in for sure. What time does it start? Also, do you want me to bring any food or drinks? See you there!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 26, Tema Central: Refusing Politely
Imagem de person with a gentle, apologetic expression holding their hands up in a stop but sorry gestureAbre em uma nova janela

person with a gentle, apologetic expression holding their hands up in a stop but sorry gesture
Refusing Politely
Social English - Pill 26

Dizer "não" é difícil, mas necessário.

Em inglês, responder apenas "No" para um convite é considerado muito rude.

Hoje vamos aprender a recusar convites com classe e educação, sem ofender ninguém.
Imagem de red X symbol next to a green checkmark, contrasting rude and politeAbre em uma nova janela

red X symbol next to a green checkmark, contrasting rude and polite
Don't just say "No"

Se alguém diz: "Do you want to go out?" E você responde: "No."

A pessoa vai achar que você está bravo ou é mal-educado.

Precisamos suavizar (soften) a resposta.
Imagem de simple diagram: Sorry + I can'tAbre em uma nova janela
www.youtube.com
simple diagram: Sorry + I can't
The Classic: "I'm sorry, I can't"

A forma mais simples e segura de recusar qualquer coisa.

Estrutura: Apology + Refusal

    "I'm sorry, I can't."

    "Sorry, I can't make it." ("Make it" = conseguir ir).

Imagem de sandwich illustration: Bread (Positive), Meat (Negative), Bread (Reason)Abre em uma nova janela
medium.com
sandwich illustration: Bread (Positive), Meat (Negative), Bread (Reason)
The Sandwich Technique

A melhor técnica para recusar:

    Positive: "I'd love to..." (Eu adoraria).

    Negative: "...but I can't." (mas não posso).

    Reason: "I have to work." (Tenho que trabalhar).

    "I'd love to, but I can't tonight."

Imagem de calendar with the word Busy represented by a filled block of timeAbre em uma nova janela
www.parents.com
calendar with the word Busy represented by a filled block of time
Giving a Reason (Vague)

Você não precisa contar sua vida toda. Pode ser vago.

    "I have plans." (Tenho planos/compromisso).

    "I'm busy that day." (Estou ocupado nesse dia).

    "I have something else on." (Tenho outra coisa marcada - Britânico).

Imagem de battery icon showing low energy or a person sleepingAbre em uma nova janela

battery icon showing low energy or a person sleeping
Giving a Reason (Honest)

Às vezes, a verdade é que você está cansado.

    "I'm a bit tired today."

    "I'm exhausted, I need to rest."

    "I have an early start tomorrow." (Tenho que acordar cedo amanhã).

Imagem de rain cloud and a ticket stubAbre em uma nova janela

rain cloud and a ticket stub
Idiom: "Take a rain check"

Essa é uma expressão essencial do inglês social.

Significa: "Não posso agora, mas aceito fazer isso outra hora/futuramente."

    "Can I take a rain check?"

    "I'll take a rain check."

(É uma recusa educada que deixa a porta aberta).
Imagem de person covering their glass with a hand to signal no moreAbre em uma nova janela

person covering their glass with a hand to signal no more
Refusing Food or Drink

Se alguém oferece algo ("Would you like a beer?"):

    "No, thank you."

    "I'm good, thanks." (Estou bem/satisfeito).

    "I'm driving." (Estou dirigindo).

    "I just ate, thanks." (Acabei de comer).

Imagem de smartphone screen showing a text message bubbleAbre em uma nova janela

smartphone screen showing a text message bubble
Texting Refusals

Em mensagens, somos breves, mas ainda educados.

    "Can't make it, sorry!"

    "Maybe next time!"

    "Busy tonight, have fun!"

Imagem de sad face emoji next to a party hatAbre em uma nova janela

sad face emoji next to a party hat
"Unfortunately"

Uma palavra formal para mostrar que você lamenta não ir.

    "Unfortunately, I won't be able to come." (Infelizmente, não poderei ir).

    Nota: Use mais em e-mails ou situações sérias.

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Seu amigo convida para o cinema, mas você tem um jantar de família. Como recusar?

A) No, I have a dinner. B) I'd love to, but I have a family dinner. C) Unfortunately no.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Usar a estrutura "I'd love to, but..." é a forma mais amigável. A opção A é muito seca.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a expressão para adiar o convite para outro dia:

"I can't go today. Can I take a ______ check?"

A) sun B) rain C) time
Imagem de ticket with a rain cloud symbolAbre em uma nova janela

ticket with a rain cloud symbol
Correção do Desafio

A resposta correta é B.

Explicação: A expressão é Rain check.

Frase: "Can I take a rain check?"
Imagem de two friends talking outside an office buildingAbre em uma nova janela

two friends talking outside an office building
Dialogue: The Invitation

John: Hey, we are going for a beer after work. Do you want to come? Mike: I'd love to, but I can't. I have to finish this report. John: Oh, come on! Just one drink. Mike: Sorry, I really can't make it. My boss is waiting for this. John: Okay, maybe next time. Mike: Yeah, I'll take a rain check. Have fun!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique recusar com educação.

"Thank you for the invitation. I'd love to go to your party, but I can't this weekend. I have plans with my family already. I'm sorry I can't make it. But please invite me next time. I'll take a rain check!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 27, Tema Central: Giving an Excuse
Imagem de person holding a phone looking apologetic, scratching their headAbre em uma nova janela

person holding a phone looking apologetic, scratching their head
Giving an Excuse
Social English - Pill 27

Você recusou o convite ("I can't"). Agora, a pessoa pergunta: "Why?" (Por quê?).

Você precisa dar uma desculpa (Excuse).

Hoje vamos aprender as frases padrão para justificar sua ausência sem precisar contar sua vida inteira.
Imagem de heavy chain connected to a person's ankle, representing obligationAbre em uma nova janela

heavy chain connected to a person's ankle, representing obligation
The Obligation: "I have to..."

A estrutura mais comum para dar uma desculpa é usar "I have to..." (Eu tenho que...).

Isso mostra que não é sua escolha, mas uma obrigação externa.

    "Sorry, I can't go. I have to work late."

Imagem de stack of paperwork and a laptop on a deskAbre em uma nova janela

stack of paperwork and a laptop on a desk
Common Work/Study Excuses

As desculpas mais aceitáveis socialmente envolvem trabalho ou estudo.

    "I have to work." (Tenho que trabalhar.)

    "I have to finish a report." (Tenho que terminar um relatório.)

    "I have to study for an exam." (Tenho que estudar para uma prova.)

Imagem de alarm clock ringing at 5 AMAbre em uma nova janela

alarm clock ringing at 5 AM
The "Early Start" Excuse

Se o evento é à noite e você quer dormir cedo, use esta expressão clássica:

"I have an early start tomorrow."

Significa: "Tenho que acordar/começar o dia muito cedo amanhã."

    "I can't stay late. I have an early start tomorrow."

Imagem de generic calendar with a block marked simply as BusyAbre em uma nova janela
youcanbook.me
generic calendar with a block marked simply as Busy
The Vague Excuse: "Something came up"

E se você não quiser dizer o motivo real? Ou se aconteceu um imprevisto pessoal?

Use a frase mágica: "Something came up." (Surgiu um imprevisto).

    "I'm sorry, I have to cancel. Something came up."

Imagem de family silhouette icon representing private timeAbre em uma nova janela

family silhouette icon representing private time
Family Obligations

Compromissos familiares são desculpas muito fortes e respeitadas.

    "It is my mother's birthday."

    "I have a family dinner."

    "I have to look after my little brother." (Cuidar de...)

Imagem de low battery iconAbre em uma nova janela

low battery icon
Health & Energy

Se o motivo é físico:

    "I'm not feeling very well." (Não estou me sentindo muito bem).

    "I'm exhausted." (Estou exausto).

    "I have a headache." (Estou com dor de cabeça).

Evite dizer apenas "I am tired" para convites importantes, pois pode soar como preguiça.
Imagem de wishbone symbol or a person looking wistfully at a party through a windowAbre em uma nova janela

wishbone symbol or a person looking wistfully at a party through a window
Softener: "I wish I could"

Para mostrar que você realmente queria ir (mesmo que seja mentira), use:

"I wish I could, but..." (Quem dera eu pudesse / Eu gostaria de poder, mas...)

    "I wish I could, but I have to work."

Imagem de person running to catch a bus but missing itAbre em uma nova janela

person running to catch a bus but missing it
Expression: "Make it"

No contexto de compromissos, "Make it" significa "conseguir ir/comparecer".

    "I can't make it." (Não vou conseguir ir).

    "I won't be able to make it." (Não poderei ir - Mais formal).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a melhor frase para dizer que surgiu um imprevisto misterioso?

A) Something appeared. B) Something came up. C) I have a problem.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A expressão fixa para "surgiu um imprevisto" é Something came up. É educada e não exige mais explicações.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que precisa acordar cedo amanhã:

"I can't go to the party. I have an ______ start tomorrow."

A) early B) soon C) fast
Imagem de sunrise iconAbre em uma nova janela

sunrise icon
Correção do Desafio

A resposta correta é A.

Explicação: A expressão (collocation) correta é Early start.

Frase: "I have an early start tomorrow."
Imagem de two friends talking on the phoneAbre em uma nova janela

two friends talking on the phone
Dialogue: Canceling Plans

Anna: Hey, are we still meeting for lunch? Ben: I am so sorry, Anna. I won't be able to make it. Anna: Oh no! Why? Ben: Something came up at work. I have to finish this project urgently. Anna: That is too bad. Ben: I wish I could go. Can we reschedule for tomorrow?
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique dar desculpas convincentes em voz alta.

"I really wanted to go to the cinema, but I can't make it. I have to study for my English test tonight. Also, I have an early start tomorrow morning. I wish I could go with you. But something came up last minute. Have fun without me!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 28, Tema Central: Arranging a Time
Imagem de two watches side by side showing slightly different times, symbolizing coordinationAbre em uma nova janela

two watches side by side showing slightly different times, symbolizing coordination
Arranging a Time
Social English - Pill 28

Você combinou o evento ("Let's go!"), mas agora falta o detalhe principal: Que horas?

Hoje vamos aprender a definir o horário de um encontro de forma polida e prática.
Imagem de large question mark over a clock faceAbre em uma nova janela

large question mark over a clock face
The Golden Question: "Shall"

Uma forma muito educada e comum (especialmente no inglês britânico, mas entendida mundialmente) de sugerir um horário é usando Shall.

"What time shall we meet?" (Que horas devemos nos encontrar?)

Shall aqui funciona como uma sugestão suave, um convite para decidir juntos.
Imagem de calendar and a clock icon mergingAbre em uma nova janela

calendar and a clock icon merging
"What time works for you?"

Esta é a frase mais útil e moderna para agendar compromissos (social ou trabalho).

"What time works for you?" (Que horário funciona/fica bom para você?)

É perfeito porque coloca a preferência da outra pessoa em primeiro lugar.
Imagem de person holding a planner suggesting a timeAbre em uma nova janela

person holding a planner suggesting a time
Suggesting a Time: "How about...?"

Para propor um horário específico, use "How about".

    "How about 7 PM?" (Que tal às 19h?)

    "How about we meet at 8?" (Que tal nos encontrarmos às 8?)

Imagem de hand giving a thumbs up and another giving a thumbs downAbre em uma nova janela

hand giving a thumbs up and another giving a thumbs down
Asking: "Is... okay?"

Outra forma simples de verificar a disponibilidade:

    "Is 8 o'clock okay for you?"

    "Does 7:30 suit you?" (O verbo suit aqui significa "convém/serve").

Imagem de clock showing exactly 8:00 and another showing approximately 8:00 (blurred zone)Abre em uma nova janela

clock showing exactly 8:00 and another showing approximately 8:00 (blurred zone)
Exact vs. Approximate

Nem sempre precisamos ser exatos.

    Exact: "Let's meet at 8:00 sharp." (Em ponto).

    Approximate: "Let's meet around 8:00." (Por volta das 8).

    Approximate: "Let's meet at about 8:00."

Imagem de preposition triangle: AT (top), ON (middle), IN (bottom)Abre em uma nova janela
reallifeglobal.com
preposition triangle: AT (top), ON (middle), IN (bottom)
Prepositions Review (Time)

Não erre a preposição na hora de marcar!

    AT + Horário: At 5 PM.

    ON + Dia: On Monday.

    IN + Parte do dia: In the morning / In the afternoon / In the evening.

Nota: Dizemos AT night.
Imagem de person shaking hands with another, indicating agreementAbre em uma nova janela

person shaking hands with another, indicating agreement
Confirming the Time

Se o horário proposto for bom:

    "That works for me." (Funciona para mim.)

    "Perfect. See you then." (Perfeito. Te vejo lá/então.)

    "That sounds good." (Soa bem.)

Imagem de clock with hands moving forward, indicating a later timeAbre em uma nova janela

clock with hands moving forward, indicating a later time
Adjusting the Time

Se você precisa mudar um pouco:

    "Can we make it a bit later?" (Podemos marcar um pouco mais tarde?)

    "Can we make it earlier?" (Podemos marcar mais cedo?)

    "Actually, 7 is a bit tight. Say 7:30?" ("Say" aqui significa "Digamos/Que tal").

Imagem de person running late looking at a watchAbre em uma nova janela

person running late looking at a watch
"Running late"

Se você marcou às 8:00, mas vai atrasar:

"I'm running a bit late." (Estou um pouco atrasado).

    "I'm running late. Let's meet at 8:15 instead."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a melhor forma de perguntar "Que horário fica bom para você?"?

A) What time works for you? B) What time works to you? C) What time is good of you?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é A.

Explicação: A regência correta do verbo work neste contexto é com FOR. "What time works for you?"
Imagem de sentence completion puzzle with a clockAbre em uma nova janela

sentence completion puzzle with a clock
Desafio de Vocabulário

Complete a frase para sugerir um horário aproximado:

"I finish work late. Let's meet ______ 8 PM."

A) sharp B) around C) on
Imagem de clock showing a fuzzy area around the number 8Abre em uma nova janela

clock showing a fuzzy area around the number 8
Correção do Desafio

A resposta correta é B.

Explicação:

    Around significa "por volta de" / "aproximadamente".

    Sharp significa "em ponto".

    On é para dias.

Imagem de two friends looking at their phones to sync calendarsAbre em uma nova janela

two friends looking at their phones to sync calendars
Dialogue: Setting the Time

Ana: So, dinner on Friday is confirmed. What time shall we meet? Bob: I finish work at 6. How about 7 PM? Ana: That is a bit early for me. Can we make it 7:30? Bob: That works for me. Ana: Great. Meet you there at 7:30 sharp. Don't be late! Bob: Don't worry, I won't.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique agendar um compromisso com clareza.

"Great, let's go to the cinema on Saturday. What time works for you? I am free all afternoon. How about we meet around 4 PM? We can grab a coffee before the movie. Or, if you prefer, can we make it 5 PM? Let me know what suits you best. See you then!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 29, Tema Central: Arranging a Place
Imagem de map pin icon located on a specific building on a city mapAbre em uma nova janela

map pin icon located on a specific building on a city map
Arranging a Place
Social English - Pill 29

Você já definiu o horário ("What time?"). Agora é hora de definir o local.

Saber usar as preposições corretas (at, in) e combinar o ponto de encontro (meeting point) é essencial para ninguém ficar perdido.
Imagem de two people standing in a large city looking confused holding a mapAbre em uma nova janela

two people standing in a large city looking confused holding a map
The Main Question

Para perguntar onde vocês vão se encontrar, use:

    "Where should we meet?" (Onde devemos nos encontrar?)

    "Where do you want to meet?" (Onde você quer se encontrar?)

    "Where shall we meet?" (Onde nos encontramos? - Sugestão)

Imagem de person pointing specifically at the door of a cinemaAbre em uma nova janela

person pointing specifically at the door of a cinema
Preposition: AT (Specific Point)

Para pontos de encontro específicos, usamos AT.

    "Let's meet at the cinema."

    "I'll see you at the bus stop."

    "Let's meet at the entrance."

O foco aqui é o ponto de referência, não estar "dentro" dele.
Imagem de person sitting inside a coffee shop, visible through the windowAbre em uma nova janela

person sitting inside a coffee shop, visible through the window
Preposition: IN (Inside)

Se o ponto de encontro é dentro de um lugar fechado ou uma área, usamos IN.

    "I'll be in the coffee shop." (Já estou lá dentro).

    "Let's meet in the lobby."

    "Wait for me in the car."

Imagem de large shopping mall entrance with many peopleAbre em uma nova janela

large shopping mall entrance with many people
Common Meeting Points

Lugares clássicos para marcar:

    The entrance: A entrada.

    The ticket office / Box office: A bilheteria (cinema/teatro).

    The station: A estação de trem/metrô.

    The food court: A praça de alimentação (shopping).

Imagem de smartphone screen displaying a map application with a shared location pinAbre em uma nova janela

smartphone screen displaying a map application with a shared location pin
Sharing Location (Tech)

Hoje em dia, usamos o GPS.

    "Send me your location." (Me manda sua localização.)

    "I'll send you a pin." (Vou te mandar um "pin" no mapa.)

    "Share your live location." (Compartilhe sua localização em tempo real.)

Imagem de car stopping and a driver opening the door for a passengerAbre em uma nova janela

car stopping and a driver opening the door for a passenger
Offering a Ride: "Pick you up"

Se você está de carro e quer buscar o amigo:

"I can pick you up." (Posso te buscar/pegar).

    "I'll pick you up at 7."

    "Don't worry, I'll pick you up at home."

Imagem de car dropping someone off and driving awayAbre em uma nova janela

car dropping someone off and driving away
The Opposite: "Drop you off"

E para deixar a pessoa em casa depois?

"I can drop you off." (Posso te deixar/largar lá).

    "I'll drop you off at the station."

Imagem de person gesturing straight ahead or pointing distanceAbre em uma nova janela

person gesturing straight ahead or pointing distance
Asking about Distance

    "Is it far from here?" (É longe daqui?)

    "How do I get there?" (Como chego lá?)

    "It's walking distance." (Dá para ir a pé).

Imagem de chart showing AT = Point, IN = Enclosed SpaceAbre em uma nova janela
undergroundmathematics.org
chart showing AT = Point, IN = Enclosed Space
Summary: At vs In

Para não errar mais:

    Meet AT the mall: Ponto de referência geral (pode ser na porta).

    Meet IN the mall: Você vai entrar e esperar lá dentro.

Na dúvida para ponto de encontro? Use AT.
Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a preposição correta para marcar um encontro "na" entrada do cinema?

"Let's meet ______ the entrance."

A) in B) on C) at
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: A entrada é um ponto específico. Usamos AT. "Let's meet at the entrance."
Imagem de sentence completion puzzle with a car iconAbre em uma nova janela

sentence completion puzzle with a car icon
Desafio de Vocabulário

Você quer oferecer uma carona para buscar seu amigo. O que você diz?

"I have a car. I can ______ you up at 8 PM."

A) take B) pick C) get
Imagem de hand picking up a small figureAbre em uma nova janela

hand picking up a small figure
Correção do Desafio

A resposta correta é B.

Explicação: O phrasal verb para "buscar alguém" (de carro) é Pick up.

Frase: "I can pick you up at 8 PM."
Imagem de two friends looking at a map on a phone screenAbre em uma nova janela

two friends looking at a map on a phone screen
Dialogue: Deciding the Place

Sarah: Okay, Friday is confirmed. Where should we meet? Tom: How about that new sushi bar downtown? Sarah: Sounds good. Should we meet at the restaurant? Tom: It might be crowded. Let's meet at the subway station nearby. Sarah: Okay. Send me the location just in case. Tom: Sure. Or I can pick you up if you want. Sarah: No need, I'll meet you there!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique combinar o local e oferecer carona.

"Great, let's go to the concert. Where do you want to meet? We can meet at the main entrance. Or, if it is raining, let's meet in the coffee shop across the street. Is that okay for you? Also, I am driving, so I can pick you up at your house if you prefer. Just send me your location."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 30, Tema Central: Changing Plans (Canceling)
Imagem de calendar with a red cross mark over a scheduled event, indicating cancellationAbre em uma nova janela

calendar with a red cross mark over a scheduled event, indicating cancellation
Changing Plans (Canceling)
Social English - Pill 30

Imprevistos acontecem. Às vezes, você precisa desmarcar um compromisso.

O segredo não é o cancelamento em si, mas como você faz isso. É preciso ser educado para não magoar a outra pessoa.
Imagem de sad face icon next to a polite smiling face icon, contrasting rude vs politeAbre em uma nova janela
ux.stackexchange.com
sad face icon next to a polite smiling face icon, contrasting rude vs polite
The Golden Rule

Nunca diga apenas "I can't go" ou cancele em cima da hora sem explicação.

A estrutura ideal para cancelar é:

    Pedir desculpas.

    Dizer que não pode ir.

    Dar um motivo (breve).

    Propor uma nova data.

Imagem de person looking worried holding a phoneAbre em uma nova janela

person looking worried holding a phone
Step 1 & 2: Breaking the News

Use frases que suavizam o impacto.

    "I'm afraid I can't make it." (Receio que não vou conseguir ir.)

    "I'm really sorry, but I won't be able to come." (Sinto muito mesmo, mas não poderei ir.)

Note: "I'm afraid" aqui não é medo, é uma forma polida de dar más notícias.
Imagem de question mark and an exclamation mark representing a sudden eventAbre em uma nova janela

question mark and an exclamation mark representing a sudden event
Step 3: The Reason (Something came up)

Como vimos na pílula 27, você não precisa contar detalhes.

    "Something has come up." (Surgiu um imprevisto.)

    "Something unexpected happened." (Algo inesperado aconteceu.)

    "I'm not feeling well." (Não estou me sentindo bem.)

Imagem de calendar page being flipped to the next monthAbre em uma nova janela

calendar page being flipped to the next month
Step 4: Rescheduling (The Verb)

O verbo para "reagendar" ou "remarcar" é Reschedule.

    "Can we reschedule?" (Podemos remarcar?)

    "Can we do it another time?" (Podemos fazer isso outra hora?)

    "Can we move it to next week?" (Podemos mudar para a semana que vem?)

Imagem de arrow moving an event forward on a timelineAbre em uma nova janela

arrow moving an event forward on a timeline
Postpone vs Push Back

Para adiar (jogar para frente):

    Postpone: Adiar (Formal).

        "We need to postpone the meeting."

    Push back: Atrasar/Jogar para mais tarde (Informal/Phrasal Verb).

        "Can we push back our dinner to 9 PM?"

Imagem de rain cloud symbol on a ticketAbre em uma nova janela

rain cloud symbol on a ticket
Review: Rain Check

Lembre-se da expressão da pílula 26. É perfeita aqui.

"Can I take a rain check?"

Isso diz implicitamente: "Não posso hoje, mas quero muito ir na próxima vez. Por favor, me convide de novo."
Imagem de person offering a gift or buying coffee for a friendAbre em uma nova janela

person offering a gift or buying coffee for a friend
"I'll make it up to you"

Se você cancelou em cima da hora e se sente mal, use esta frase para prometer compensar o erro.

"I'll make it up to you." (Vou te compensar / Vou me redimir).

    "Dinner is on me next time. I'll make it up to you."

Imagem de cancel button and a delay button side by sideAbre em uma nova janela

cancel button and a delay button side by side
Cancel vs Call off

    To cancel: O verbo padrão.

    To call off: Um Phrasal Verb muito comum para cancelar eventos.

    "They called off the game because of the rain."

    "I had to call off the meeting."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a forma mais educada de dizer que você quer mudar a data do encontro?

A) I want new date. B) Can we reschedule? C) Change the day, please.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Reschedule é o verbo correto e polido para pedir uma nova data. As outras opções são imperativas e soam rudes.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase com o Phrasal Verb que significa "adiar/atrasar" o horário:

"I am running late. Can we ______ back our meeting by 30 minutes?"

A) pull B) push C) take
Imagem de hands pushing a clock forwardAbre em uma nova janela

hands pushing a clock forward
Correção do Desafio

A resposta correta é B.

Explicação: Push back significa empurrar para frente (mais tarde). Pull forward significaria antecipar (mais cedo).

Frase: "Can we push back our meeting?"
Imagem de two friends looking disappointed but understanding on a video callAbre em uma nova janela
timeforkindness.co.uk
two friends looking disappointed but understanding on a video call
Dialogue: The Cancellation

Sara: Hi Tom. I am so sorry, but I won't be able to make it tonight. Tom: Oh no! Is everything okay? Sara: Yes, but something came up at work and I have to stay late. Tom: I understand. Don't worry about it. Sara: Can we reschedule for Friday? Tom: Sure, Friday works for me. Sara: Thanks for understanding. I'll make it up to you!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique cancelar um compromisso com educação e empatia.

"I am really sorry, but I have to cancel our lunch today. Something unexpected came up with my family. I feel terrible because I really wanted to see you. Can we take a rain check? How about we meet next Tuesday instead? Lunch is on me, I'll make it up to you."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 31, Tema Central: Running Late
Imagem de person looking at their watch with a stressed expression in a carAbre em uma nova janela

person looking at their watch with a stressed expression in a car
Running Late
Social English - Pill 31

Atrasos acontecem. O trânsito para, o despertador falha ou uma reunião demora mais que o esperado.

O problema não é o atraso, mas a falta de aviso. Hoje vamos aprender a avisar que você vai atrasar ("run late") e estimar sua chegada.
Imagem de person running with a briefcase or bag, checking the timeAbre em uma nova janela

person running with a briefcase or bag, checking the time
The Key Phrase: "Running Late"

Não diga apenas "I am late" (que soa como se você já tivesse chegado atrasado ou é uma característica sua).

Se você ainda está a caminho, a expressão correta é:

"I'm running late." (Estou atrasado / Estou correndo contra o tempo).

    "Hi! Just texting to say I'm running late."

    "I'm running a bit late this morning."

Imagem de long line of cars with brake lights on, showing heavy trafficAbre em uma nova janela

long line of cars with brake lights on, showing heavy traffic
The Classic Excuse: Traffic

A razão número 1 para atrasos.

A expressão para "preso no trânsito" é Stuck in traffic.

    "Sorry, I'm stuck in traffic."

    "The traffic is terrible. I'm stuck."

Imagem de person looking at a GPS app on a phone showing 10 minAbre em uma nova janela

person looking at a GPS app on a phone showing 10 min
Estimating Arrival: "In" vs "Away"

Para dizer quanto tempo falta:

    I'll be there in [Time]: (Chegarei em...)

        "I'll be there in 10 minutes."

    I'm [Time] away: (Estou a X tempo de distância).

        "I'm 5 minutes away."

        "GPS says I'm 15 minutes away."

Imagem de person holding a hand up apologetically to a waiting friendAbre em uma nova janela
seejesus.net
person holding a hand up apologetically to a waiting friend
Sorry to Keep You Waiting

Se alguém está te esperando num restaurante ou esquina, peça desculpas pelo tempo dela.

"Sorry to keep you waiting." (Desculpe fazer você esperar).

    "Hi! I'm here. Sorry to keep you waiting."

Imagem de padlock or a person stopped by a boss at a deskAbre em uma nova janela
twistedsifter.com
padlock or a person stopped by a boss at a desk
Other Reasons: "Held up"

Se você ficou preso no trabalho ou em outro compromisso (não fisicamente preso, mas retido):

"I got held up." (Fiquei retido / Me seguraram).

    "Sorry, I got held up at work."

    "I got held up in a meeting."

Imagem de dinner table with one person eating and an empty chairAbre em uma nova janela

dinner table with one person eating and an empty chair
Managing the Situation

Se você vai demorar muito, libere a pessoa:

    "Start without me." (Comecem sem mim).

    "Don't wait for me." (Não me esperem).

    "Go ahead and order." (Pode ir pedindo).

Imagem de warning sign comparing Late vs DelayAbre em uma nova janela

warning sign comparing Late vs Delay
Late vs. Delay

    Delay: Geralmente usado para transportes ou coisas técnicas.

        "My flight was delayed."

        "Sorry for the delay." (Desculpe a demora - Substantivo).

    Late: Adjetivo para pessoas.

        "I am late." (Não diga "I am delayed").

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você está no carro, indo para o trabalho, mas percebe que não chegará no horário. O que você manda por mensagem?

A) I'm walking late. B) I'm running late. C) I'm going late.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A expressão fixa (collocation) é Running late. Mesmo que você esteja sentado no carro ou no ônibus, o verbo é "run".
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que o trânsito te prendeu:

"I will be 20 minutes late. I am ______ in traffic."

A) stopped B) stuck C) glued
Imagem de car trapped in gridlockAbre em uma nova janela

car trapped in gridlock
Correção do Desafio

A resposta correta é B.

Explicação: Usamos o adjetivo Stuck para dizer que estamos presos, sem conseguir sair do lugar (trânsito, elevador, lama).

Frase: "I am stuck in traffic."
Imagem de two friends texting; chat bubbles on screenAbre em uma nova janela

two friends texting; chat bubbles on screen
Dialogue: Texting on the Go

Alex (Text): Hey, are you close? We are waiting at the bar. Ben (Text): So sorry! I'm running late. Alex (Text): Is everything okay? Ben (Text): Yeah, I got held up at the office. And now I'm stuck in traffic. Alex (Text): No worries. How long? Ben (Text): GPS says I'm 15 minutes away. Please start without me. Alex (Text): Okay, we will order drinks. See you soon.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique avisar sobre seu atraso com clareza.

"Hi! I am calling to let you know that I'm running late. There was an accident on the bridge and I'm stuck in traffic. I think I'll be there in about 20 minutes. I am really sorry to keep you waiting. Please go ahead and order some appetizers. I will drive as fast as I can!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 32, Tema Central: At a Party: Introductions
Imagem de three people standing at a party holding drinks; one person is gesturing between the other two, making an introductionAbre em uma nova janela

three people standing at a party holding drinks; one person is gesturing between the other two, making an introduction
At a Party: Introductions
Social English - Pill 32

As festas são ótimas para socializar. Às vezes, tu és o elo de ligação entre dois amigos que não se conhecem.

O teu papel é apresentá-los e ajudar a iniciar a conversa. Hoje vamos aprender a fazer isso com naturalidade.
Imagem de person pointing casually to a friend beside themAbre em uma nova janela

person pointing casually to a friend beside them
The Golden Rule: "This is..."

A regra mais importante: Em inglês, quando apresentamos pessoas fisicamente, usamos "This is".

Nunca digas "He is" ou "She is" para apresentar alguém que está ao teu lado.

    Correto: "Tom, this is Sarah."

    Incorreto: ~~Tom, she is Sarah.~~

Imagem de diagram connecting two people with a line labeled ConnectionAbre em uma nova janela

diagram connecting two people with a line labeled Connection
Adding Context (The Link)

Dizer apenas os nomes é um pouco "seco". Diz de onde os conheces para criar contexto.

    "John, this is Mike. He is my colleague from work."

    "Alice, this is Julie. We went to university together."

    "This is Pedro. He is my neighbor."

Imagem de two puzzle pieces fitting together, representing a shared interestAbre em uma nova janela
therapy-central.com
two puzzle pieces fitting together, representing a shared interest
The Icebreaker (Common Ground)

Para evitar aquele silêncio constrangedor, menciona algo que eles tenham em comum. Isso é o "quebra-gelo".

    "You both love football."

    "Sarah is also into photography."

    "Mike works in IT too."

Imagem de speech bubble saying Nice to meet youAbre em uma nova janela

speech bubble saying Nice to meet you
The Response

Se fores tu a ser apresentado, as respostas clássicas são:

    "Nice to meet you." (Prazer em conhecer-te).

    "Good to meet you." (Bom conhecer-te).

    "Pleasure to meet you." (Um prazer - Um pouco mais formal).

Imagem de person with a surprised/happy face pointing at the other personAbre em uma nova janela

person with a surprised/happy face pointing at the other person
"I've heard a lot about you"

Uma frase muito simpática para usar se o teu amigo já falou dessa pessoa antes.

"I've heard a lot about you." (Ouvi falar muito de ti / sobre si).

    "Hi Jessica. I've heard so much about you!"

    "Nice to meet you finally. John talks about you all the time."

Imagem de person smiling and asking a simple questionAbre em uma nova janela

person smiling and asking a simple question
Asking a Follow-up Question

Não deixes a conversa morrer. Faz uma pergunta simples logo a seguir ao "Nice to meet you".

    "How do you know Mark?" (De onde conheces o Mark?)

    "Are you enjoying the party?" (Estás a gostar da festa?)

    "Do you live near here?" (Moras aqui perto?)

Imagem de person holding a drink stepping away from the groupAbre em uma nova janela

person holding a drink stepping away from the group
Leaving Them to Chat

Depois de apresentá-los, se quiseres sair para buscar uma bebida ou falar com outra pessoa:

    "I'll let you two chat." (Vou deixar-vos a conversar.)

    "I'm going to grab a drink. Excuse me." (Vou buscar uma bebida. Com licença.)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Estás a apresentar o teu irmão, David, à tua amiga Anna. Qual a frase correta?

A) Anna, he is my brother, David. B) Anna, this is my brother, David. C) Anna, here is my brother, David.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Para apresentações presenciais, usamos sempre o demonstrativo This is. "Anna, this is my brother, David."
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Queres dizer à pessoa que o teu amigo fala muito bem dela. "Prazer em conhecer-te. Ouvi falar muito de ti."

"Nice to meet you. I have ______ a lot about you."

A) listened B) heard C) knew
Imagem de ear icon representing hearingAbre em uma nova janela

ear icon representing hearing
Correção do Desafio

A resposta correta é B.

Explicação: A expressão correta é "ouvir dizer/ouvir falar", que em inglês usa o verbo Hear no participio (Heard).

Frase: "I have heard a lot about you."
Imagem de three friends standing in a living room with music in the backgroundAbre em uma nova janela

three friends standing in a living room with music in the background
Dialogue: The Introduction

You: Hey Alex, come here for a second. Alex: Hi! What's up? You: Alex, this is Bruno. Alex: Hi Bruno, nice to meet you. You: Bruno is visiting from Brazil. You both play the guitar, so I thought you should meet. Bruno: Really? Good to meet you, Alex. What kind of music do you play? Alex: Mostly rock. I've heard a lot about your Bossa Nova skills! You: Great. I'll let you two chat. I need a refill.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Imagina que estás numa festa. Apresenta dois amigos (fictícios) em voz alta.

"Hi Lisa. Have you met Tom? Tom, this is Lisa. Lisa is my cousin from Porto. Tom works as a graphic designer too. Lisa, Tom is the one who designed my website. I think you two have a lot in common. I'll let you chat while I go say hello to the host."

Envia ao teu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 33, Tema Central: At a Party: Small Talk
Imagem de two people holding plastic cups at a house party, smiling and talking casuallyAbre em uma nova janela

two people holding plastic cups at a house party, smiling and talking casually
At a Party: Small Talk
Social English - Pill 33

Você já foi apresentado a alguém ("This is..."), mas agora precisa manter a conversa viva. Isso é o Small Talk (conversa casual).

A pergunta número 1 em qualquer festa é descobrir a conexão entre as pessoas e o anfitrião (The Host).
Imagem de diagram with YOU and STRANGER connected by HOST in the middleAbre em uma nova janela

diagram with YOU and STRANGER connected by HOST in the middle
The Magic Question

Quando o assunto acaba, use esta pergunta infalível:

"So, how do you know [Host's Name]?" (Então, de onde você conhece o [Nome do Anfitrião]?)

Exemplo:

    "So, how do you know Mark?"

    "How do you know the host?"

Imagem de icons representing different connections: A briefcase (work), a graduation cap (school), and a family treeAbre em uma nova janela

icons representing different connections: A briefcase (work), a graduation cap (school), and a family tree
Common Answers

Prepare-se para ouvir (ou dizer) respostas como:

    Work: "We work together." / "We are colleagues."

    School/College: "We went to college together."

    Family: "I am his cousin." / "She is my sister-in-law."

    History: "We go way back." (Nos conhecemos há muito tempo / das antigas).

Imagem de person nodding and listening attentivelyAbre em uma nova janela

person nodding and listening attentively
"And you?"

Small talk é como um jogo de tênis: a bola tem que ir e voltar.

Se alguém te pergunta "How do you know Mark?", você responde e devolve imediatamente:

    "We play football together. How about you?"

    "We are neighbors. And you?"

Imagem de tray of appetizers and a DJ or speakerAbre em uma nova janela

tray of appetizers and a DJ or speaker
Talking about the Environment

Se você não quer falar de pessoas, fale sobre a festa.

    The Food: "Have you tried the appetizers? They are delicious."

    The Drink: "Where can I get a drink?" / "This punch is strong!"

    The Music: "I love this song." / "The music is a bit loud, isn't it?"

Imagem de person holding a drink making a gesture to excuse themselvesAbre em uma nova janela

person holding a drink making a gesture to excuse themselves
Escaping the Conversation

Conversa de festa deve ser leve e curta. Se você quiser sair, seja educado:

    "I'm going to grab another drink/some food." (Vou pegar outra bebida/comida.)

    "Excuse me, I see a friend over there." (Com licença, vi um amigo ali.)

    "It was nice talking to you." (Foi bom falar com você.)

Imagem de question mark versus a handshake iconAbre em uma nova janela

question mark versus a handshake icon
Meet vs. Know

Cuidado com a tradução de "Conhecer".

    To Know: Ter um relacionamento/conexão (Presente/Geral).

        "How do you know him?" (De onde você o conhece?)

    To Meet: O ato de ser apresentado pela primeira vez (Passado).

        "Where did you meet?" (Onde vocês se conheceram pela primeira vez?)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a pergunta correta para descobrir a conexão da pessoa com o dono da festa?

A) Where do you know Mark? B) How do you know Mark? C) Who do you know Mark?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Em inglês, perguntamos HOW (Como) você conhece a pessoa, não "De onde" (Where). "How do you know Mark?"
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que você e o anfitrião estudaram na mesma universidade.

"We ______ to college together."

A) go B) went C) study
Imagem de graduation capAbre em uma nova janela
pearlyarts.com
graduation cap
Correção do Desafio

A resposta correta é B.

Explicação: Como a faculdade já acabou (passado), usamos o passado do verbo Go.

Frase: "We went to college together."
Imagem de two strangers standing near a food table at a partyAbre em uma nova janela
driehausfoundation.org
two strangers standing near a food table at a party
Dialogue: Breaking the Ice

Guest A: Hi, I'm Sarah. Guest B: Nice to meet you, Sarah. I'm David. Guest A: Great party, isn't it? Guest B: Yes, it is very crowded! So, how do you know the host? Guest A: We work together at the bank. How about you? Guest B: Oh, really? We went to high school together. We are old friends. Guest A: That's nice. Have you tried the pizza? It's amazing. Guest B: Not yet. I'm going to grab some right now. See you around!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Imagine que você está em uma festa. Responda a uma pessoa desconhecida.

"Hi! I am [Seu Nome]. Nice to meet you. How do you know the host? I know him because we play soccer together on weekends. Also, have you tried the chocolate cake? It is delicious. I am going to grab a drink. It was nice talking to you!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 34, Tema Central: Offering Food/Drink (Host)
Imagem de welcoming host opening the door and gesturing into the living roomAbre em uma nova janela

welcoming host opening the door and gesturing into the living room
Offering Food/Drink (Host)
Social English - Pill 34

Na última aula, aprendemos a fazer "Small Talk". Hoje, o foco muda: Você é o anfitrião (Host).

Sua função é fazer o convidado se sentir bem-vindo. A primeira regra de ouro é oferecer algo para beber ou comer assim que a pessoa chega.
Imagem de person holding a tray with a glass of water, a beer, and a juiceAbre em uma nova janela

person holding a tray with a glass of water, a beer, and a juice
The Golden Phrase: "Can I get you...?"

A frase mais natural e comum para oferecer algo não é "Do you want...?", mas sim usando o verbo Get (buscar/trazer).

"Can I get you something to drink?" (Posso te trazer algo para beber?)

    "Can I get you a glass of water?"

    "Can I get you a beer?"

Imagem de diagram showing the movement: Kitchen > Host > Guest (Meaning of GET)Abre em uma nova janela

diagram showing the movement: Kitchen > Host > Guest (Meaning of GET)
The Verb "Get"

Neste contexto, Get significa "buscar e trazer".

Estrutura: Can I + get + [Person] + [Object]?

    "Can I get you a coffee?"

    "Can I get Maria a juice?"

Imagem de table full of food with plates and cutlery, buffet styleAbre em uma nova janela
adornthetable.com
table full of food with plates and cutlery, buffet style
"Help yourself"

Se a comida ou bebida está em uma mesa e você quer que os convidados se sirvam sozinhos, use esta expressão essencial:

"Please, help yourself." (Por favor, sirva-se / Fique à vontade).

    "There is plenty of food. Help yourself."

    "Help yourself to the fridge." (Pode pegar o que quiser na geladeira).

Imagem de person holding a wine bottle poised to pour more into a guest's glassAbre em uma nova janela

person holding a wine bottle poised to pour more into a guest's glass
Offering More (Refills)

O copo do seu convidado está vazio? Ofereça mais.

    "Would you like a refill?" (Quer que encha de novo?)

    "Can I get you another one?" (Posso te trazer mais uma?)

    "Anyone for more wine?" (Alguém quer mais vinho?)

Imagem de waiter or host handing a plate to someone saying Here you goAbre em uma nova janela

waiter or host handing a plate to someone saying Here you go
Serving the Guest

Quando você entrega a bebida ou comida na mão da pessoa, diga:

"Here you go." (Aqui está).

    Guest: "Water, please."

    Host: (Hands water) "Here you go."

Imagem de list of drink options: Tea, Coffee, Water, Juice, Wine, BeerAbre em uma nova janela
nawon.com.vn
list of drink options: Tea, Coffee, Water, Juice, Wine, Beer
Listing Options

Geralmente, listamos o que temos disponível:

    "We have water, juice, beer, and wine. What would you like?"

    "Who wants coffee? And who wants tea?"

Imagem de thumbs up and a 'stop' hand gestureAbre em uma nova janela

thumbs up and a 'stop' hand gesture
How Guests Respond (Review)

Lembre-se do que você pode ouvir como resposta:

    Accepting: "Yes, please. I'd love a water."

    Refusing: "I'm fine, thanks." / "I'm good for now."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você preparou um jantar estilo buffet e quer que seus amigos comam à vontade. O que você diz?

A) Serve yourself. B) Help yourself. C) Get yourself.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A expressão idiomática para "sirva-se" é Help yourself. "Serve yourself" soa como uma ordem rude ou técnica demais.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Organize a frase para oferecer uma bebida ao seu chefe (Formal/Polite).

[ get / something / I / can / drink / you / to / ? ]

A) Can get I you to drink something? B) Can I get you something to drink? C) Can something get you to drink?
Imagem de polite host offering a cup of teaAbre em uma nova janela
emilypost.com
polite host offering a cup of tea
Correção do Desafio

A resposta correta é B.

Explicação: Estrutura: Can I + Get + You + Objeto.

Frase: "Can I get you something to drink?"
Imagem de host opening the door for a guestAbre em uma nova janela

host opening the door for a guest
Dialogue: The Arrival

Host: Hi Mike! Come on in. Mike: Hi! Thanks for having me. Host: Can I get you something to drink? Mike: I'd love a beer, if you have one. Host: Sure. Here you go. Mike: Thanks. Host: The food is on the table. Please, help yourself. Mike: It looks delicious!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique ser um anfitrião acolhedor.

"Welcome! I am so happy you came. Make yourself at home. Can I get you something to drink? I have soda, water, or wine. Here you go, a glass of wine. Please, help yourself to the appetizers. And let me know if you need anything else. Would you like a refill?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 35, Tema Central: Asking for the Bathroom
Imagem de standard blue male/female restroom signAbre em uma nova janela

standard blue male/female restroom sign
Asking for the Bathroom
Social English - Pill 35

Esta é talvez a pergunta mais importante em qualquer viagem!

Mas cuidado: dependendo do país, usar a palavra errada pode soar indelicado. Hoje vamos aprender a pedir para usar o banheiro com educação, seja em público ou na casa de alguém.
Imagem de two signs side by side: one saying Restroom and the other ToiletAbre em uma nova janela

two signs side by side: one saying Restroom and the other Toilet
Vocabulary: Restroom vs. Toilet

A palavra muda dependendo de onde você está e com quem fala:

    Restroom: (EUA) Termo padrão para banheiros públicos (restaurantes, shoppings). É educado e seguro.

    Bathroom: (EUA/UK) Geralmente refere-se ao banheiro de uma casa (onde tem banheira/chuveiro).

    Toilet: (UK/Europa) Comum na Europa, mas evite nos EUA. Nos EUA, "toilet" refere-se apenas ao objeto (vaso sanitário) e soa um pouco grosseiro perguntar "Where is the toilet?".

    Dica de Ouro: Na dúvida, use Restroom ou Bathroom.

Imagem de person politely raising a hand to ask a waiter a questionAbre em uma nova janela

person politely raising a hand to ask a waiter a question
The Standard Question

A forma mais direta e educada em lugares públicos:

"Excuse me, where is the restroom?" (Com licença, onde fica o banheiro?)

Se você estiver na Europa: "Excuse me, where is the toilet?" (Aceitável).
Imagem de person washing hands with soap and waterAbre em uma nova janela
medicine.tufts.edu
person washing hands with soap and water
The Polite Excuse: "Wash my hands"

Se você está na casa de alguém ou num jantar chique e quer ser discreto, não precisa dizer que quer usar o vaso sanitário.

Use o eufemismo:

"Could I use your bathroom to wash my hands?" (Poderia usar seu banheiro para lavar as mãos?)

Ou simplesmente: "Where can I wash my hands?"
Imagem de door slightly open showing a sinkAbre em uma nova janela

door slightly open showing a sink
Visiting a Home

Ao visitar amigos, use o verbo modal May ou Could para pedir permissão.

    "May I use your bathroom?" (Posso usar seu banheiro?)

    "Could I use your bathroom?" (Poderia usar seu banheiro?)

Imagem de airplane bathroom lock indicating Vacant (Green) and Occupied (Red)Abre em uma nova janela

airplane bathroom lock indicating Vacant (Green) and Occupied (Red)
Occupied vs. Vacant

Antes de entrar, verifique a porta ou a placa (em aviões/trens).

    Occupied: Ocupado (Tem gente).

    Vacant: Vago (Livre).

Se a porta está fechada e você quer bater, pergunte: "Is anyone in there?" (Tem alguém aí?)
Imagem de finger pointing down a hallwayAbre em uma nova janela

finger pointing down a hallway
Understanding Directions

Prepare-se para ouvir a resposta:

    "It is down the hall." (No fim do corredor).

    "Second door on the left." (Segunda porta à esquerda).

    "Around the corner." (Virando a esquina/canto).

    "Upstairs / Downstairs." (No andar de cima / baixo).

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar? - Exercício 1

Você está em um restaurante chique em Nova York. Qual a forma mais educada de perguntar?

A) Where is the toilet? B) Where is the pee room? C) Excuse me, where is the restroom?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Nos EUA, evite "toilet" em situações sociais. "Restroom" é a palavra correta. "Pee room" é infantil/vulgar.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Você está jantando na casa do seu chefe. Você quer ser discreto. Complete a frase:

"Excuse me, where can I ______ my hands?"

A) clean B) wash C) water
Imagem de sink with running waterAbre em uma nova janela

sink with running water
Correção do Desafio

A resposta correta é B.

Explicação: A expressão fixa é Wash my hands. É a maneira mais elegante de pedir para ir ao banheiro sem ser específico sobre necessidades fisiológicas.
Imagem de two friends talking in a living roomAbre em uma nova janela

two friends talking in a living room
Dialogue: At a Friend's House

Guest: This dinner is delicious, Sarah. Host: I am glad you like it! Guest: By the way, may I use your bathroom? Host: Of course! It is down the hall, the first door on the right. Guest: First on the right? Host: Yes. The light switch is on the outside. Guest: Thanks. I'll be right back.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique as frases essenciais para não passar aperto.

"Excuse me, where is the restroom? I need to wash my hands. Is it down the hall? Thank you. (Knock on door) Is anyone in there? Oh, it is occupied. I will wait until it is vacant."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 36, Tema Central: Complimenting
Imagem de two people smiling, one pointing admiringly at the other's outfitAbre em uma nova janela

two people smiling, one pointing admiringly at the other's outfit
Complimenting
Social English - Pill 36

Fazer um elogio (Compliment) é a maneira mais rápida de criar uma conexão positiva com alguém.

Mas não basta dizer "It is beautiful". Hoje vamos aprender as estruturas naturais para elogiar roupas, aparência e habilidades.
Imagem de person holding a heart symbol next to a dressAbre em uma nova janela

person holding a heart symbol next to a dress
Structure 1: "I like / I love..."

A maneira mais direta e pessoal de elogiar algo que alguém possui (roupas, acessórios, carro).

    "I like your [Object]." (Gostei do seu...)

    "I love your [Object]." (Adorei o seu...)

Exemplos:

    "I like your dress. It is very colorful."

    "I love your shoes! Where did you buy them?"

Imagem de mirror reflecting a person with a new haircutAbre em uma nova janela

mirror reflecting a person with a new haircut
Structure 2: "You look..."

Para elogiar a aparência geral da pessoa, usamos o verbo Look (Parecer/Estar).

    "You look great today." (Você está ótimo hoje.)

    "You look nice." (Você está bonito/bem.)

    "You look beautiful / handsome."

Atenção: "Handsome" é geralmente usado para homens, e "Beautiful" para mulheres.
Imagem de stylish jacket on a mannequinAbre em uma nova janela

stylish jacket on a mannequin
Structure 3: "That is a..."

Para focar no objeto específico.

"That is a [Adjective] [Noun]."

    "That is a lovely necklace."

    "That is a cool T-shirt."

    "That is a nice car."

Imagem de person holding a trophy or cooking a meal skillfullyAbre em uma nova janela

person holding a trophy or cooking a meal skillfully
Complimenting Skills

Se alguém fez algo bem feito:

    "Good job!" (Bom trabalho!)

    "Well done!" (Muito bem feito!)

    "You are a great [Noun]."

        "You are a great cook."

        "You are a talented singer."

Imagem de person receiving a gift and blushing slightlyAbre em uma nova janela

person receiving a gift and blushing slightly
Accepting a Compliment

No Brasil, temos o hábito de recusar o elogio por modéstia ("Imagina, foi baratinho", "É velho").

Em inglês, a regra de ouro é: Aceite e Agradeça.

    "Thank you."

    "Thanks, I like it too."

    "Thank you. It was a gift."

    "That is very kind of you to say." (Muito gentil da sua parte).

Imagem de price tag showing a very low priceAbre em uma nova janela

price tag showing a very low price
The "Bargain" Follow-up

Se você quiser ser modesto sobre uma roupa, pode dizer que foi barato (um costume ocidental comum).

    "Thanks! I got it on sale."

    "Thanks! It was a real bargain."

Imagem de warning sign about personal spaceAbre em uma nova janela

warning sign about personal space
Caution: Personal Comments

Evite comentar sobre o corpo das pessoas (peso, tamanho) a menos que você tenha muita intimidade. Foque em escolhas (roupas, cabelo, estilo).

    Bom: "I love your haircut."

    Arriscado: "You look thinner." (Você parece mais magro - pode ser mal interpretado).

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar? - Exercício 1

Sua colega chegou com uma bolsa nova e bonita. O que você diz?

A) I want your bag. B) I love your bag. C) You look bag.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Usamos "I love/like your [Objeto]" para elogiar pertences. A opção A ("I want") soa invejosa ou agressiva.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Alguém diz "You look wonderful tonight". Como você responde educadamente?

"Thank you. That is very ______ of you."

A) good B) kind C) gentle
Imagem de smiling face emojiAbre em uma nova janela
emojiisland.com
smiling face emoji
Correção do Desafio

A resposta correta é B.

Explicação: A frase fixa para agradecer a gentileza de alguém é: That is very kind of you.
Imagem de two friends meeting on the streetAbre em uma nova janela

two friends meeting on the street
Dialogue: The New Coat

Mary: Hi Jane! Wow, I love your coat. Jane: Really? Thank you! Mary: Is it new? The color really suits you. Jane: Yes, I bought it last week. It was on sale. Mary: Well, that is a great find. You look very elegant. Jane: That is very kind of you to say. I love your boots too!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique elogiar e agradecer.

"Hi! You look great today. I like your new glasses, they are very stylish. And that is a beautiful watch. (Recebendo elogio): Oh, thank you. I got it on sale at the mall. It is very kind of you to notice. Thanks!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 37, Tema Central: Responding to Compliments
Imagem de person smiling shyly and happy while receiving a compliment from a friendAbre em uma nova janela

person smiling shyly and happy while receiving a compliment from a friend
Responding to Compliments
Social English - Pill 37

Na pílula anterior, você aprendeu a elogiar. Agora, vamos aprender a receber o elogio.

No Brasil, temos o hábito de dizer: "Imagina, é velho" ou "Custou dez reais". Em inglês, a regra é aceitar com gratidão e, muitas vezes, compartilhar a origem do item.

]
Imagem de simple equation: Smile + Thank you + [DetailAbre em uma nova janela
medium.com
simple equation: Smile + Thank you + [Detail
The Golden Rule: Accept It

Primeiro, não rejeite o elogio. Aceite-o!

A resposta mais simples e perfeita é:

    "Thank you."

    "Thanks, I'm glad you like it." (Obrigado, fico feliz que tenha gostado).

    "Thank you, that's very kind of you."

Imagem de shopping bag with a generic store logoAbre em uma nova janela

shopping bag with a generic store logo
Sharing the Source: "I bought it at..."

É muito comum, após agradecer, dizer onde você comprou. Isso cria conversa.

Estrutura: "I bought it at [Store Name / Place]."

    "Thank you! I bought it at Zara."

    "Thanks! I bought it at the mall."

    "I bought it online." (Sem "at" para online).

Imagem de person holding a new shirt and giving a thumbs upAbre em uma nova janela

person holding a new shirt and giving a thumbs up
Using "Get" instead of "Buy"

Em conversas informais, o verbo Get (passado: Got) é extremamente comum para substituir "Buy".

    "I got it at [Place]."

    "Thanks! I got it at a vintage store."

    "I got it in London last year."

Imagem de price tag with a discount percentageAbre em uma nova janela

price tag with a discount percentage
The Bargain Hunter

Se você pagou barato e tem orgulho disso (muito comum nos EUA e UK), você pode dizer:

    "It was on sale." (Estava em promoção).

    "It was a bargain." (Foi uma pechincha).

    "It was really cheap!"

Exemplo: "I love your shoes!" "Thanks! I got them on sale."
Imagem de wrapped gift boxAbre em uma nova janela
waterleafpaperco.com
wrapped gift box
When it was a Gift

E se você não comprou?

    "It was a gift." (Foi um presente).

    "It was a present from my mom."

    "My boyfriend gave it to me."

Imagem de old, favorite sweater or itemAbre em uma nova janela
chascrazycreations.com
old, favorite sweater or item
When it is Old

Se o item é antigo, usamos o Present Perfect para dizer há quanto tempo o temos.

    "I've had it for years." (Tenho isso há anos).

    "I've had it for ages." (Tenho há "séculos").

    "It's actually quite old." (Na verdade, é bem velho).

Imagem de two mirrors facing each other, representing reciprocityAbre em uma nova janela

two mirrors facing each other, representing reciprocity
Returning the Compliment

Se você quiser ser simpático de volta:

    "You look nice too."

    "I like your [Item] as well."

    "Thanks, yours is lovely too."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Alguém elogia sua camisa. Você a comprou na loja "Target". Qual a resposta mais natural?

A) Thanks, I buyed it at Target. B) Thanks, I bought it at Target. C) Thanks, I bought it on Target.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação:

    O passado de buy é bought (irregular). "Buyed" não existe.

    Para lojas físicas, usamos a preposição at.

Frase: "Thanks, I bought it at Target."
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que você tem aquele relógio há muito tempo.

"Thank you! It is not new. I have ______ it for years."

A) had B) has C) have
Imagem de calendar showing pages turningAbre em uma nova janela

calendar showing pages turning
Correção do Desafio

A resposta correta é A.

Explicação: Estrutura de Present Perfect (ter algo por um tempo): Have + Had (Particípio).

Frase: "I have had it for years."
Imagem de two friends looking at a handbagAbre em uma nova janela

two friends looking at a handbag
Dialogue: The Handbag

Susan: Wow, Julie! I love your handbag. Is it new? Julie: Thank you! Yes, I just got it. Susan: It is beautiful. Where did you buy it? Julie: I bought it at that new boutique downtown. Susan: Was it expensive? Julie: Actually, no. It was on sale. Fifty percent off! Susan: That is amazing. It really suits you.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique responder a elogios com naturalidade.

"Thank you, I am glad you like my dress. I bought it at a small shop in Paris. It was on sale, so it was a great deal. And my shoes? I've had them for years. Actually, they were a gift from my sister. You look great today too!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 38, Tema Central: Asking for Contact Info
Imagem de social media icons: Instagram, WhatsApp, LinkedIn floating around a smartphoneAbre em uma nova janela

social media icons: Instagram, WhatsApp, LinkedIn floating around a smartphone
Asking for Contact Info
Social English - Pill 38

A festa acabou, a conversa foi ótima e você quer manter contato. Antigamente, pedíamos o telefone. Hoje, pedimos o Instagram ou WhatsApp.

Vamos aprender a trocar contatos e, principalmente, a soletrar seu usuário (@) com os símbolos corretos.
Imagem de person holding a phone ready to typeAbre em uma nova janela

person holding a phone ready to type
The Modern Question: "Are you on...?"

A maneira mais natural de saber se a pessoa tem uma rede social não é apenas "Do you have...?". Usamos a preposição ON.

    "Are you on Instagram?" (Você tem/está no Instagram?)

    "Are you on Facebook?"

    "Are you on WhatsApp?"

Se a resposta for "Yes", então perguntamos:

    "What is your username / handle?"

Imagem de symbols: @ (at), _ (underscore), . (dot), (dash) with labelsAbre em uma nova janela

symbols: @ (at), _ (underscore), . (dot), (dash) with labels
Speling your Username: Symbols

Esta é a parte crucial! Não adianta saber os números e letras se você travar nos símbolos.

    @ (Arroba): Dizemos At.

        My email is john at gmail dot com.

    . (Ponto): Dizemos Dot. (Em endereços de web/email).

        www dot google dot com.

    _ (Underline): Em inglês, o nome correto é Underscore.

        john underscore silva.

    - (Hífen/Traço): Dizemos Dash ou Hyphen.

Imagem de smartphone screen adding a new phone number contactAbre em uma nova janela
seniortechclub.com
smartphone screen adding a new phone number contact
Asking for the Phone Number

Para o WhatsApp ou ligação:

    "Can I have your number?" (Posso pegar seu número?)

    "What is your number?" (Qual seu número?)

    "Let me add you on WhatsApp." (Deixa eu te adicionar no WhatsApp.)

Imagem de two people holding phones, one scanning a QR code on the other's screenAbre em uma nova janela
folksrh.com
two people holding phones, one scanning a QR code on the other's screen
The QR Code Era

Hoje em dia, é comum nem falar, apenas escanear.

    "Let me scan your QR code." (Deixa eu escanear seu QR code.)

    "Do you have a code I can scan?" (Você tem um código que eu possa escanear?)

    "I'll follow you right now." (Vou te seguir agora mesmo.)

Imagem de distinct buttons: Add Friend vs Follow vs ConnectAbre em uma nova janela

distinct buttons: Add Friend vs Follow vs Connect
Verbs: Add, Follow, Connect

Cada rede tem seu verbo:

    To Follow: Instagram, Twitter/X, TikTok.

        "I'll follow you."

    To Add: Facebook, WhatsApp, Snapchat.

        "I'll add you as a friend."

    To Connect: LinkedIn (Profissional).

        "Let's connect on LinkedIn."

Imagem de person typing a message on a phoneAbre em uma nova janela

person typing a message on a phone
"I'll send you a message"

Depois de pegar o contato, é educado mandar um "oi" para a pessoa salvar seu número.

    "I'll send you a text so you have my number." (Vou mandar uma mensagem para você ter meu número.)

    "I'll DM you." (Direct Message - Instagram/Twitter). (Vou te mandar uma DM/Direct.)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Como se diz o símbolo _ em um endereço de e-mail ou usuário?

A) Underline B) Down dash C) Underscore
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Embora no Brasil falemos "underline", em inglês o termo correto para o traço baixo _ em computação é Underscore.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Qual a preposição correta para perguntar se alguém usa o Instagram?

"Are you ______ Instagram?"

A) in B) on C) at
Imagem de Instagram logoAbre em uma nova janela

Instagram logo
Correção do Desafio

A resposta correta é B.

Explicação: Para plataformas de mídia e internet, usamos a preposição ON. "Are you on Facebook?"
Imagem de two new friends exchanging phones at a cafeAbre em uma nova janela

two new friends exchanging phones at a cafe
Dialogue: Staying in Touch

Leo: It was great talking to you, Bia. We should hang out again. Bia: Definitely! Are you on Instagram? Leo: Yes. What's your handle? Bia: It is bia_silva99. Leo: Wait, is that underscore or dash? Bia: Underscore. bia underscore silva. Leo: Found you! I'll follow you. Bia: Cool. I'll DM you my phone number later so we can combine the next coffee.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique soletrar um usuário fictício com os símbolos corretos.

"Let's keep in touch! Are you on Instagram? My username is English_Student.2024. That is: English underscore Student dot 2024. Or can I have your number? I'll add you on WhatsApp. I'll send you a text right now."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 39, Tema Central: Saying Goodbye (Social)
Imagem de two friends hugging or waving goodbye at a door, smilingAbre em uma nova janela

two friends hugging or waving goodbye at a door, smiling
Saying Goodbye (Social)
Social English - Pill 39

Saber se despedir é tão importante quanto saber cumprimentar. Ninguém gosta de quem sai "à francesa" sem dizer nada, nem de quem não sabe encerrar a conversa.

Hoje vamos aprender a sair de uma situação social com elegância e carinho.
Imagem de diagram contrasting Nice to MEET you (handshake/strangers) vs Nice to SEE you (wave/friends)Abre em uma nova janela
homosabiens.substack.com
diagram contrasting Nice to MEET you (handshake/strangers) vs Nice to SEE you (wave/friends)
Crucial: Meet vs. See

Este é o erro mais clássico!

    Nice to MEET you: Use apenas na primeira vez que conhece a pessoa.

    It was nice SEEING you: Use para amigos, conhecidos ou pessoas que você já encontrou antes.

    Cenário: Você encontra um amigo no shopping. Na hora de ir embora:

        Correto: It was nice seeing you.

        Errado: ~~Nice to meet you.~~

Imagem de person looking at a watch subtly, signaling they need to leaveAbre em uma nova janela

person looking at a watch subtly, signaling they need to leave
The Pre-Goodbye (The Signal)

Em inglês, raramente dizemos "Bye" do nada. Precisamos "sinalizar" que vamos sair.

Use estas frases de transição:

    "Well, I should get going." (Bom, eu "deveria" ir indo / preciso ir).

    "I've got to run." (Tenho que correr/ir).

    "It is getting late." (Está ficando tarde).

Imagem de hand waving goodbye casuallyAbre em uma nova janela

hand waving goodbye casually
Casual Goodbyes

Para amigos e situações informais, evite o "Goodbye" (que pode soar muito definitivo ou dramático). Prefira:

    "Bye!" / "Bye-bye!"

    "See you!" / "See ya!" (Até mais).

    "See you later." (Te vejo mais tarde).

    "Take care." (Se cuida - Muito comum e carinhoso).

Imagem de calendar showing a specific day highlightedAbre em uma nova janela

calendar showing a specific day highlighted
Being Specific: "See you..."

Se você sabe quando vai ver a pessoa de novo:

    "See you tomorrow."

    "See you on Monday."

    "See you at the party."

    "See you soon." (Te vejo em breve).

Imagem de guest thanking the host at the front doorAbre em uma nova janela
restaurant.eatapp.co
guest thanking the host at the front door
Leaving a Party/Dinner

Se você foi convidado para a casa de alguém, a despedida exige um agradecimento.

    "Thanks for having me." (Obrigado por me receber/convidar).

    "Thank you for the lovely dinner." (Obrigado pelo jantar adorável).

Imagem de two phones connecting or a Call Me hand gestureAbre em uma nova janela

two phones connecting or a Call Me hand gesture
"Let's do this again"

Para mostrar que você gostou da companhia e quer repetir:

    "Let's do this again soon." (Vamos fazer isso de novo em breve).

    "Let's keep in touch." (Vamos manter contato).

    "Text me!" (Me manda mensagem!)

Imagem de car driving away with someone waving from the windowAbre em uma nova janela

car driving away with someone waving from the window
"Drive safe" / "Safe travels"

Se a pessoa vai dirigir ou viajar:

    "Drive safe!" (Dirija com cuidado).

    "Get home safe!" (Chegue bem em casa).

    "Safe travels!" (Boa viagem - se ela for pegar estrada/avião).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você encontrou seu melhor amigo na rua, conversaram por 10 minutos e agora você precisa ir. O que você diz?

A) Nice to meet you. Bye. B) It was nice seeing you. See ya. C) Good to know you. Goodbye.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Como é seu amigo, você já o conhece, então usamos Seeing you (não meet). "See ya" é a despedida casual perfeita.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase de transição para dizer que "precisa ir indo".

"Look at the time! I really should ______ going."

A) have B) make C) get
Imagem de person walking towards a doorAbre em uma nova janela

person walking towards a door
Correção do Desafio

A resposta correta é C.

Explicação: A expressão fixa é Get going (ir indo / começar a ir).

Frase: "I really should get going."
Imagem de two friends finishing coffee at a cafe tableAbre em uma nova janela

two friends finishing coffee at a cafe table
Dialogue: Ending the Coffee Date

Carol: Wow, look at the time. It is almost 6 PM. Dan: Really? Time flies! Carol: I really should get going. I have a dinner tonight. Dan: No problem. It was so nice seeing you, Carol. Carol: You too, Dan. Thanks for the coffee. Dan: My pleasure. Let's do this again soon. Carol: Definitely. Text me next week. Take care! Dan: See you!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique a despedida completa e natural.

"Well, look at the time. I've got to run. But it was really nice seeing you today. Thanks for having me, the food was delicious. Let's do this again soon, okay? I'll text you later. Get home safe! See you!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 40, Tema Central: Review: Making Plans
Imagem de two friends looking at a smartphone calendar together, smiling and pointing at a dateAbre em uma nova janela

two friends looking at a smartphone calendar together, smiling and pointing at a date
Review: Making Plans
Social English - Pill 40

Chegamos à revisão final deste bloco!

Nas últimas 20 pílulas, aprendemos a fazer sugestões, convidar, aceitar, recusar, definir horários, locais e lidar com atrasos.

Hoje, o objetivo é juntar todas essas peças para montar um quebra-cabeça social completo: Combinar um Jantar (Arranging a Dinner).
Imagem de roadmap with 4 stops: 1. Idea > 2. Time > 3. Place > 4. ConfirmationAbre em uma nova janela
forexbee.co
roadmap with 4 stops: 1. Idea > 2. Time > 3. Place > 4. Confirmation
Step 1: The Idea (Suggestion)

Comece verificando a disponibilidade ou sugerindo a atividade.

    "Are you free on Saturday night?"

    "Do you want to grab a bite to eat?" (Grab a bite = Comer algo rápido/informal).

    "Why don't we try that new Italian restaurant?"

    "Let's go out for dinner."

Imagem de clock showing 7:00 PM and 8:00 PM with arrows adjusting the timeAbre em uma nova janela

clock showing 7:00 PM and 8:00 PM with arrows adjusting the time
Step 2: The Time (Negotiation)

Lembre-se de perguntar a preferência do outro.

    "What time works for you?"

    "How about 7:30?"

    "Is 8:00 PM okay for you?"

    "Can we make it a bit later? Say 8:30?"

Imagem de map pin on a restaurant entrance and another on a subway stationAbre em uma nova janela

map pin on a restaurant entrance and another on a subway station
Step 3: The Place (Meeting Point)

Defina onde se encontrarão. Use as preposições AT e IN.

    "Where should we meet?"

    "Let's meet at the restaurant."

    "I can pick you up at your house."

    "Let's meet at the station."

Imagem de checkmark symbol and a 'thumbs up' emojiAbre em uma nova janela

checkmark symbol and a 'thumbs up' emoji
Step 4: Confirmation & Excitement

Feche o acordo com energia positiva.

    "Sounds like a plan."

    "Perfect. See you then."

    "I'm really looking forward to it." (Estou ansioso por isso).

Imagem de warning triangle with text Plan BAbre em uma nova janela
thetravelballdad.com
warning triangle with text Plan B
Recap: Handling Issues (Problems)

O que fazer se der errado?

    Recusar: "I'd love to, but I can't. I have to work."

    Adiar: "Can we take a rain check?"

    Reagendar: "Can we reschedule for next week?"

    Atrasar: "I'm running late. Start without me."

Imagem de multiple choice quiz layoutAbre em uma nova janela
gdoc.io
multiple choice quiz layout
Vamos Praticar? - Gramática

Complete a frase para sugerir um horário:

"What time ______ for you?"

A) work B) works C) working
Imagem de green checkmark indicating the correct answerAbre em uma nova janela

green checkmark indicating the correct answer
Correção

A resposta correta é B.

Explicação: A expressão é "What time works for you?". O sujeito é "What time" (singular/it), então o verbo leva 's'.
Imagem de scrambled sentence puzzleAbre em uma nova janela
educationtothecore.com
scrambled sentence puzzle
Desafio de Estrutura

Coloque a frase na ordem para marcar um ponto de encontro.

[ entrance / at / meet / let's / the ]

A) Let's meet at the entrance. B) Meet let's at the entrance. C) Let's the entrance meet at.
Imagem de cinema entranceAbre em uma nova janela

cinema entrance
Correção do Desafio

A resposta correta é A.

Explicação: Estrutura de imperativo com Let's: Let's + Verbo + Preposição + Local.

Frase: "Let's meet at the entrance."
Imagem de two friends texting; split screen showing both phonesAbre em uma nova janela

two friends texting; split screen showing both phones
Full Dialogue Simulation

Vamos ver como tudo se encaixa em uma conversa natural.

Tom: Hey Sarah, are you free this Friday? Sarah: Hi Tom! Yes, I am. Why? Tom: Why don't we go to that new burger place downtown? Sarah: That sounds good. I heard their fries are amazing. Tom: Great. What time works for you? Sarah: I work until 6. How about 7:30? Tom: 7:30 is perfect. Shall I pick you up? Sarah: No need, thanks. Let's meet at the restaurant. Tom: Okay. See you then!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Tarefa Final: Você vai gravar um áudio simulando que está convidando seu professor para jantar.

Use o roteiro abaixo como guia, mas sinta-se livre para adaptar:

    Convite: "Hi! Do you want to have dinner on Saturday?"

    Sugestão: "Why don't we try the new Pizza place?"

    Horário: "What time works for you? How about 8 PM?"

    Local: "I can pick you up, or we can meet at the entrance."

    Confirmação: "Great. Sounds like a plan. See you there!"

Envie ao seu professor e parabéns por concluir o módulo de Social English!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 41, Tema Central: Talking about Last Weekend
Imagem de two colleagues talking by a coffee machine on a Monday morningAbre em uma nova janela

two colleagues talking by a coffee machine on a Monday morning
Talking about Last Weekend
Social English - Pill 41

É segunda-feira de manhã. A pergunta número 1 no escritório ou na escola é: "Como foi o seu fim de semana?".

Para responder, precisamos sair do "presente" e usar o Past Simple. Hoje vamos praticar como contar suas histórias de sábado e domingo.
Imagem de large question mark bubble over a calendar showing Saturday and SundayAbre em uma nova janela

large question mark bubble over a calendar showing Saturday and Sunday
The Opener: "How was your weekend?"

Para iniciar a conversa, usamos o verbo To Be no passado (Was).

    "How was your weekend?" (Como foi seu fim de semana?)

    "Did you have a good weekend?" (Você teve um bom fim de semana?)

Imagem de three emojis: 1. Stareyed (Great), 2. Relaxed/Sleeping (Quiet), 3. Bored (Boring)Abre em uma nova janela

three emojis: 1. Stareyed (Great), 2. Relaxed/Sleeping (Quiet), 3. Bored (Boring)
The Verdict: Adjectives

A resposta curta geralmente vem primeiro, usando um adjetivo.

    "It was great!" (Foi ótimo!)

    "It was relaxing." (Foi relaxante.)

    "It was pretty quiet." (Foi bem tranquilo/quieto.)

    "It was busy." (Foi corrido/cheio de coisas.)

    "It was okay, nothing special." (Foi ok, nada de especial.)

Imagem de person asking What did you do? with icons of activities appearingAbre em uma nova janela

person asking What did you do? with icons of activities appearing
The Details: "What did you do?"

Depois do "It was great", a pessoa vai perguntar o que você fez.

"What did you do?"

Aqui você precisa usar verbos de ação no Passado.
Imagem de chart comparing Present vs Past verbs: Go>Went, Have>Had, See>SawAbre em uma nova janela

chart comparing Present vs Past verbs: Go>Went, Have>Had, See>Saw
Key Irregular Verbs (Review)

Os verbos mais usados no fim de semana são irregulares. Memorize estes três:

    Go -> Went (Ir -> Fui)

        "I went to the beach."

        "I went to a party."

    Have -> Had (Ter/Comer -> Tive/Comi)

        "I had dinner with friends."

        "We had a barbecue."

    See -> Saw (Ver -> Vi)

        "I saw a movie."

        "I saw my family."

Imagem de person sitting on a sofa watching TVAbre em uma nova janela

person sitting on a sofa watching TV
The "Nothing" Answer (Regular Verbs)

Se você não fez nada demais, use verbos regulares (-ED).

    "I stayed home." (Fiquei em casa.)

    "I relaxed." (Relaxei.)

    "I watched Netflix." (Assisti Netflix.)

    "I cleaned the house." (Limpei a casa.)

Imagem de polite conversationalist saying What about you?Abre em uma nova janela
davetgc.com
polite conversationalist saying What about you?
Returning the Question

Não fale apenas sobre você. Devolva a pergunta para ser educado.

    "How about you?" (E você?)

    "What about yours?" (E o seu?)

    "Did you do anything interesting?" (Você fez algo interessante?)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Seu amigo pergunta: "What did you do?". Você quer dizer que foi ao cinema.

A) I go to the cinema. B) I went to the cinema. C) I was to the cinema.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: O passado de Go é Went. "I went to the cinema."
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Estrutura

Complete a pergunta para saber se o amigo teve um bom fim de semana.

"______ you have a good weekend?"

A) Do B) Were C) Did
Imagem de question mark symbolAbre em uma nova janela
commons.wikimedia.org
question mark symbol
Correção do Desafio

A resposta correta é C.

Explicação: Para perguntas no passado com verbos de ação (como have), usamos o auxiliar Did.

Frase: "Did you have a good weekend?"
Imagem de two coworkers chatting at their desksAbre em uma nova janela

two coworkers chatting at their desks
Dialogue: Monday Morning

Alice: Morning, Bob. How was your weekend? Bob: It was great, thanks. Alice: What did you do? Bob: I went hiking on Saturday. And on Sunday, I just relaxed at home. How about you? Alice: Mine was pretty quiet. I watched a series and cooked dinner. Bob: Nice. sometimes a quiet weekend is the best.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Prepare-se para responder "Como foi seu fim de semana?" em voz alta.

"My weekend was relaxing. On Saturday, I went shopping with my sister. We had lunch at a Japanese restaurant. On Sunday, I stayed home. I cleaned my apartment and read a book. It was simple, but good. How about you? Did you do anything special?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 42, Tema Central: "How was it?" (Opinions)
Imagem de person holding a movie ticket with a happy face and another holding a bill with a sad faceAbre em uma nova janela

person holding a movie ticket with a happy face and another holding a bill with a sad face
"How was it?" (Opinions)
Social English - Pill 42

Na aula passada, aprendemos a dizer o que fizemos. Hoje, vamos focar na qualidade da experiência.

Quando alguém diz "I went to a party", a pergunta mais natural a se fazer em seguida é: "How was it?" (Como foi?). Vamos aprender a pedir e dar opiniões sobre eventos passados.

? ]
Imagem de grammatical structure: How + was + [SubjectAbre em uma nova janela

grammatical structure: How + was + [Subject
The Core Question

Para perguntar a opinião sobre algo no passado, usamos o verbo To Be (Was/Were).

    "How was it?" (Como foi? - Geral)

    "How was the movie?" (Como foi o filme?)

    "How was the food?" (Como estava a comida?)

    "How was your trip?" (Como foi sua viagem?)

Atenção: Não use "How did the movie?". O correto é "How was".
Imagem de scale from sad red face (Negative) to happy green face (Positive)Abre em uma nova janela

scale from sad red face (Negative) to happy green face (Positive)
Positive Adjectives

Evite usar apenas "good". Enriqueça seu vocabulário:

    Amazing: Incrível.

    Wonderful: Maravilhoso.

    Fantastic: Fantástico.

    Great: Ótimo.

    Delicious: Delicioso (para comida).

    "The concert was amazing!"

Imagem de neutral face emoji, implying averageAbre em uma nova janela
emojiterra.com
neutral face emoji, implying average
Neutral Adjectives

Se não foi nem ótimo, nem ruim:

    Okay: Ok / Razoável.

    Not bad: Nada mal.

    Average: Na média / mediano.

    All right: Tudo bem / Passável.

    "The movie was okay, but a bit long."

Imagem de thumbs down emoji and a storm cloudAbre em uma nova janela

thumbs down emoji and a storm cloud
Negative Adjectives

Se a experiência foi ruim:

    Terrible: Terrível.

    Awful: Horrível.

    Boring: Chato/Entediante.

    Expensive: Caro (sentido negativo).

    Crowded: Lotado (cheio de gente).

    "The traffic was terrible."

Imagem de volume knob showing levels: A bit > Very > ReallyAbre em uma nova janela

volume knob showing levels: A bit > Very > Really
Intensifiers

Para dar força ao adjetivo, usamos palavras antes dele:

    A bit / A little: Um pouco.

        "It was a bit boring."

    Very: Muito.

        "It was very good."

    Really: Realmente/Muito (Mais enfático).

        "It was really fantastic."

Imagem de warning sign contrasting Boring vs BoredAbre em uma nova janela

warning sign contrasting Boring vs Bored
Common Mistake: -ING vs -ED

Cuidado ao descrever o evento versus seu sentimento.

    O Evento (Coisa): Use -ING.

        "The movie was boring." (O filme foi chato).

    Você (Sentimento): Use -ED.

        "I was bored." (Eu fiquei entediado).

Regra rápida: Se você fala de "IT" (o filme, a festa), use Boring/Interesting/Tiring.
Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Seu amigo foi a um restaurante novo. Como você pergunta sobre a comida?

A) How did the food? B) How was the food? C) How the food was?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A estrutura de pergunta com to be inverte o verbo e o sujeito: How + Was + The food?
Imagem de sentence scrambling puzzleAbre em uma nova janela
educationtothecore.com
sentence scrambling puzzle
Desafio de Vocabulário

Complete a frase para dizer que a festa estava "um pouco chata".

"The party was ______ boring."

A) very B) a bit C) really
Imagem de person yawning at a partyAbre em uma nova janela

person yawning at a party
Correção do Desafio

A resposta correta é B.

Explicação: Para suavizar uma crítica negativa (chato), usamos a bit (um pouco). Very e Really intensificariam o problema.

Frase: "The party was a bit boring."
Imagem de two friends talking, one looking excited and the other listeningAbre em uma nova janela

two friends talking, one looking excited and the other listening
Dialogue: The Review

John: I went to see that new Marvel movie yesterday. Lisa: Oh! How was it? John: It was fantastic! The special effects were amazing. Lisa: And how was the story? John: It was okay. A bit predictable, but fun. Lisa: Was the cinema crowded? John: Yes, it was really crowded. But I loved it.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique dar sua opinião sobre eventos passados.

"How was your weekend? It was wonderful, thanks. I went to a new Italian restaurant. How was the food? It was delicious, specifically the pasta. But the service was a bit slow. And how was the price? It was very expensive, unfortunately. But I recommend it!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 43, Tema Central: Talking about Holidays: Christmas, New Year
Imagem de split scene: left side showing a decorated Christmas tree, right side showing fireworks in the night skyAbre em uma nova janela

split scene: left side showing a decorated Christmas tree, right side showing fireworks in the night sky
Talking about Holidays
Social English - Pill 43

Chegamos ao final do ano! É a hora das festas (The Holiday Season).

Em situações sociais, todos vão perguntar sobre seus planos para o Natal (Christmas) e o Ano Novo (New Year). Hoje vamos aprender o vocabulário essencial para não ficar calado na ceia.
Imagem de calendar highlighting December 24th and December 31stAbre em uma nova janela

calendar highlighting December 24th and December 31st
The Concept of "Eve"

Em inglês, a véspera de um feriado importante é chamada de Eve.

    Christmas Eve: 24 de dezembro (Véspera de Natal).

    Christmas Day: 25 de dezembro.

    New Year's Eve: 31 de dezembro (Véspera de Ano Novo - a grande festa).

    New Year's Day: 1º de janeiro.

Exemplo: "We usually have a big dinner on Christmas Eve."
Imagem de family exchanging wrapped boxes around a treeAbre em uma nova janela

family exchanging wrapped boxes around a tree
Christmas Vocabulary

Palavras-chave para descrever as tradições:

    To exchange gifts/presents: Trocar presentes.

    To decorate the tree: Decorar a árvore.

    Turkey: Peru (o prato principal tradicional).

    Relatives: Parentes (a família estendida que vem visitar).

    "I love exchanging gifts with my relatives."

Imagem de champagne glasses clinking with fireworks in the backgroundAbre em uma nova janela

champagne glasses clinking with fireworks in the background
New Year Vocabulary

Para a virada do ano:

    Fireworks: Fogos de artifício.

        "We are going to watch the fireworks."

    Midnight: Meia-noite.

        "We cheer at midnight."

    To make a toast: Fazer um brinde.

        "Let's make a toast to the new year!"

Imagem de person writing a list titled GoalsAbre em uma nova janela

person writing a list titled Goals
New Year's Resolutions

Uma tradição muito forte nos países de língua inglesa (e no Brasil também) são as Resolutions. São as promessas ou metas para o próximo ano.

    "What is your New Year's resolution?" (Qual sua promessa de ano novo?)

    "My resolution is to join a gym."

    "My resolution is to improve my English."

Imagem de person holding a planner talking to a friendAbre em uma nova janela
unsplash.com
person holding a planner talking to a friend
Asking about Plans

Como perguntar o que a pessoa vai fazer? Use o Present Continuous (para planos fixos) ou Going to.

    "What are you doing for Christmas?" (O que você vai fazer no Natal?)

    "Do you have any plans for New Year's Eve?" (Tem planos para a véspera de ano novo?)

    "Are you going away?" (Você vai viajar/sair da cidade?)

Imagem de greeting card with text: Merry Christmas and Happy HolidaysAbre em uma nova janela

greeting card with text: Merry Christmas and Happy Holidays
Greetings: Merry vs. Happy

    Para o Natal, a saudação clássica é "Merry Christmas!".

    Para o Ano Novo, dizemos "Happy New Year!".

    Para englobar tudo (ou se você não sabe a religião da pessoa), use "Happy Holidays!" (Boas Festas).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Como se chama o dia 31 de dezembro em inglês?

A) New Year's Day B) New Year's Eve C) The Turn of the Year
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A véspera (dia 31) é New Year's Eve. O dia 1º é New Year's Day. A opção C é uma tradução literal do português ("Virada") que não é usada dessa forma.
Imagem de sentence scrambling puzzleAbre em uma nova janela
educationtothecore.com
sentence scrambling puzzle
Desafio de Vocabulário

Complete a frase sobre a promessa de ano novo.

"My New Year's ______ is to stop smoking."

A) promise B) resolution C) solution
Imagem de Stop Smoking signAbre em uma nova janela

Stop Smoking sign
Correção do Desafio

A resposta correta é B.

Explicação: O termo cultural específico para metas de ano novo é Resolution.

Frase: "My New Year's resolution is to stop smoking."
Imagem de two friends talking, wearing winter clothes or summer clothes depending on the hemisphereAbre em uma nova janela

two friends talking, wearing winter clothes or summer clothes depending on the hemisphere
Dialogue: Holiday Plans

Tom: Can you believe it is almost Christmas? Anna: I know! Time flies. Do you have any plans? Tom: Yes, I am going to my parents' house for Christmas Eve. We usually eat turkey and exchange gifts. How about you? Anna: I am staying here. But for New Year's Eve, I am going to the beach to see the fireworks. Tom: That sounds fun. Do you have a New Year's resolution? Anna: Yes, to travel more! Merry Christmas, Tom! Tom: Happy Holidays, Anna!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Conte seus planos (reais ou imaginários) para o fim de ano.

"I am excited for the holidays. On Christmas Eve, I am going to have dinner with my family. We love to exchange gifts after midnight. For New Year's Eve, I don't have plans yet. Maybe I will go to a party and make a toast with friends. My New Year's resolution is to study English every day. Happy New Year!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 44, Tema Central: Birthday Vocabulary
Imagem de birthday party scene with a cake, balloons, and gifts on a tableAbre em uma nova janela

birthday party scene with a cake, balloons, and gifts on a table
Birthday Vocabulary
Social English - Pill 44

Aniversários são momentos universais de celebração. Mas você sabe como dizer "soprar as velinhas" ou "dar uma festa" em inglês?

Hoje vamos expandir seu vocabulário para além do simples "Happy Birthday".
Imagem de group of friends shouting Surprise! to a person entering a roomAbre em uma nova janela

group of friends shouting Surprise! to a person entering a room
The Party: "Throwing" a party

Podemos dizer "have a party", mas o verbo mais dinâmico e comum para quem organiza a festa é To Throw.

    To throw a party: Dar/Organizar uma festa.

        "I am throwing a party for my sister."

    Surprise party: Festa surpresa.

    Get-together: Uma reuniãozinha (algo menor e mais íntimo que uma "party").

Imagem de birthday cake with lit candles and a person preparing to blow themAbre em uma nova janela

birthday cake with lit candles and a person preparing to blow them
The Cake Ritual

O momento mais importante da festa tem verbos específicos (collocations).

    Candles: Velas.

    Make a wish: Fazer um pedido (mentalmente).

    Blow out: Soprar/Apagar (as velas).

    "Make a wish and blow out the candles!"

Imagem de colorful wrapped boxes and a birthday cardAbre em uma nova janela

colorful wrapped boxes and a birthday card
Gifts and Cards

Em inglês, usamos duas palavras para presente: Gift e Present. São sinônimos.

    To wrap: Embrulhar.

    To unwrap: Desembrulhar/Abrir.

    Birthday Card: Cartão de aniversário (muito tradicional em países de língua inglesa, entregue junto com o presente).

Imagem de invitation card with the text RSVP by Friday highlightedAbre em uma nova janela

invitation card with the text RSVP by Friday highlighted
Invitations & RSVP

Quando você recebe um convite, geralmente vê a sigla RSVP.

Ela vem do francês "Répondez s'il vous plaît" (Responda, por favor).

Significa que você precisa confirmar se vai ou não.

    "Please RSVP by Friday." (Por favor, confirme presença até sexta).

Imagem de number changing, like a odometer, from 29 to 30Abre em uma nova janela

number changing, like a odometer, from 29 to 30
Age: "Turning"

Para dizer que você vai fazer/completar uma nova idade, usamos o verbo Turn.

    "I am turning 30 next week." (Vou fazer 30 anos semana que vem).

    "He just turned 18." (Ele acabou de fazer 18).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual o verbo correto para "apagar" as velas do bolo?

A) Turn off the candles. B) Blow out the candles. C) Shut down the candles.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A expressão fixa (phrasal verb) para soprar ar para apagar fogo é Blow out.

Frase: "Time to blow out the candles!"
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que vai "dar uma festa" para seu amigo.

"I am going to ______ a surprise party for John."

A) make B) do C) throw
Imagem de confetti poppingAbre em uma nova janela
freepik.com
confetti popping
Correção do Desafio

A resposta correta é C.

Explicação: Embora "have" seja possível, a collocation mais específica para organizar/oferecer uma festa é Throw.

Frase: "I am going to throw a party."
Imagem de two friends whispering and planningAbre em uma nova janela

two friends whispering and planning
Dialogue: Planning a Surprise

Alice: Hey, next Saturday is Tom's birthday. Ben: Really? Is he turning 25? Alice: Yes! I want to throw a surprise party for him. Ben: Great idea. I can buy the cake. Alice: Perfect. Don't forget the candles. Ben: Should we send invitations? Alice: Yes, I will send a message and ask everyone to RSVP. Ben: I will get him a nice gift too. Maybe a video game.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Descreva como você gosta de comemorar seu aniversário.

"I love birthdays! Usually, I don't throw a big party. I prefer a small get-together with my family. My mother always makes a chocolate cake. I love to make a wish and blow out the candles. I also enjoy opening my birthday cards. Next year, I am turning [sua idade]!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 45, Tema Central: Describing a Past Trip
Imagem de person standing at an airport with a suitcase looking at a departures boardAbre em uma nova janela

person standing at an airport with a suitcase looking at a departures board
Describing a Past Trip
Social English - Pill 45

Viajar é um dos melhores tópicos para Social English. As pessoas adoram perguntar: "Where did you go?" (Onde você foi?).

Para responder, você precisa dominar o Simple Past e o vocabulário de logística de viagem (transporte e hospedagem). Vamos montar seu relato de viagem.
Imagem de world map with a red pin on a specific countryAbre em uma nova janela

world map with a red pin on a specific country
Step 1: Destination (Where?)

Para dizer para onde você foi, use os verbos Go (Went), Travel (Traveled) ou Visit (Visited).

    "I went to [Place]." (Fui para...)

        "I went to Paris last year."

    "I traveled to [Place]." (Viajei para...)

        "I traveled to Brazil."

    "I visited [Place]." (Visitei...)

        "I visited my parents." (Note: Visit não usa "to").

Imagem de icons representing transport: A plane, a train, a car, and a busAbre em uma nova janela

icons representing transport: A plane, a train, a car, and a bus
Step 2: Transportation (How?)

Como você chegou lá? Existem duas formas principais de dizer:

    By + Meio de transporte:

        "I went by plane."

        "We traveled by car."

        "I went by train."

    Took + Meio de transporte:

        "I took a flight." (Peguei um voo).

        "We took a bus."

        "I took a taxi."

Imagem de hotel icon, a hostel bunk bed, and a house iconAbre em uma nova janela

hotel icon, a hostel bunk bed, and a house icon
Step 3: Accommodation (Where did you sleep?)

O verbo essencial aqui é To Stay (Ficar/Hospedar-se). Passado: Stayed.

    "I stayed at a hotel." (Fiquei num hotel).

    "I stayed at a resort."

    "I stayed in an Airbnb."

    "I stayed with friends." (Fiquei na casa de amigos).

Imagem de calendar showing a blocked period of 7 daysAbre em uma nova janela
youcanbook.me
calendar showing a blocked period of 7 days
Step 4: Duration (How long?)

Para dizer quanto tempo durou a viagem, usamos a preposição For ou o verbo Spend (Spent).

    "I stayed for [Time]."

        "I stayed for a week."

        "I stayed for 3 days."

    "I spent [Time] there."

        "I spent 10 days in Italy."

Imagem de person holding a camera taking a photo of a monumentAbre em uma nova janela

person holding a camera taking a photo of a monument
Vocabulary: "Sightseeing"

Esta palavra é difícil de traduzir, mas essencial. Sightseeing significa "turistar", ver os pontos turísticos.

    "To go sightseeing."

    "We went sightseeing." (Nós fomos ver os pontos turísticos/passear).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a preposição correta para meio de transporte?

"I traveled to London ______ plane."

A) in B) on C) by
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: Sempre usamos By para indicar o meio de transporte (by car, by bus, by train, by plane). A exceção é "On foot" (a pé).
Imagem de sentence scrambling puzzleAbre em uma nova janela
educationtothecore.com
sentence scrambling puzzle
Desafio de Estrutura

Coloque a frase na ordem certa para dizer onde se hospedou.

[ hotel / at / I / nice / a / stayed / very ]

A) I stayed at a very nice hotel. B) I at a very nice hotel stayed. C) I stayed very nice at a hotel.
Imagem de luxury hotel lobbyAbre em uma nova janela

luxury hotel lobby
Correção do Desafio

A resposta correta é A.

Explicação: Ordem: Sujeito + Verbo (Stayed) + Preposição (at) + Artigo/Adjetivo/Objeto (a very nice hotel).

Frase: "I stayed at a very nice hotel."
Imagem de two friends looking at travel photos on a phoneAbre em uma nova janela

two friends looking at travel photos on a phone
Dialogue: The Trip Report

Jess: Welcome back! How was your trip? Mike: It was amazing! I went to Spain. Jess: Nice! Did you go by plane? Mike: Yes, I took a flight to Madrid. Jess: And where did you stay? Mike: I stayed at a hostel in the city center. It was cheap and fun. Jess: How long did you stay? Mike: I stayed for 10 days. I went sightseeing every day.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Descreva sua última viagem (ou invente uma viagem dos sonhos).

"Last year, I traveled to Rio de Janeiro. I went by car because I love road trips. I stayed at a beautiful hotel near the beach. I stayed there for one week. The weather was perfect and I went sightseeing to see the Christ Redeemer. It was the best trip of my life."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 46, Tema Central: Means of Transport (Travel)
Imagem de collage showing a plane in the sky, a highspeed train, a bus, and a carAbre em uma nova janela

collage showing a plane in the sky, a highspeed train, a bus, and a car
Means of Transport (Travel)
Social English - Pill 46

Quando viajamos, a pergunta logística principal é: "How did you get there?" (Como você chegou lá?) ou "How are you going?" (Como você vai?).

Hoje vamos dominar as preposições essenciais (By, On, In) e os verbos usados para transportes.

(No 'the' or 'a') ]
Imagem de diagram: BY + [Transport IconAbre em uma nova janela

diagram: BY + [Transport Icon
The General Rule: "By"

Para falar do modo de transporte de forma geral, usamos sempre a preposição BY.

Regra: By + Meio de transporte (SEM artigo "the" ou "a").

    By plane (De avião).

    By train (De trem).

    By car (De carro).

    By bus (De ônibus).

    By boat / sea (De barco / mar).

Exemplo: "I love traveling by train."
Imagem de pair of sneakers walkingAbre em uma nova janela

pair of sneakers walking
The Exception: "On foot"

Se você vai caminhando, nunca diga "by foot" ou "by walk".

A expressão correta é: On foot. (A pé).

    "It is very close. Let's go on foot."

Imagem de person stepping inside a specific car vs. stepping onto a busAbre em uma nova janela

person stepping inside a specific car vs. stepping onto a bus
Specific Situations: In vs. On

Quando falamos de estar dentro de um veículo específico (usando "a" ou "the"), a preposição muda.

    ON (Veículos onde você pode ficar em pé/caminhar):

        On the bus.

        On the train.

        On the plane.

        On the ship.

    IN (Veículos onde você precisa se abaixar/sentar):

        In the car.

        In the taxi / In a cab.

Imagem de hand grabbing a ticketAbre em uma nova janela

hand grabbing a ticket
Verbs: Take vs. Ride vs. Drive

Qual verbo usar?

    Take: Para transporte público ou táxi (como passageiro).

        "I took a taxi."

        "Let's take the bus."

    Drive: Se você é o motorista do carro.

        "I drove to work."

    Ride: Para motos, bicicletas ou cavalos.

        "I ride a motorcycle."

Imagem de person running after a bus that is leavingAbre em uma nova janela

person running after a bus that is leaving
Catch vs. Miss

    To Catch: Conseguir pegar.

        "I ran and caught the last train."

    To Miss: Perder (chegar atrasado).

        "I woke up late and missed my flight."

        (Cuidado: Não diga "I lost the bus". "Lost" é perder objeto/desaparecer).

Imagem de arrows indicating movement: Up/In (Get on/in) and Down/Out (Get off/out)Abre em uma nova janela

arrows indicating movement: Up/In (Get on/in) and Down/Out (Get off/out)
Getting In and Out

Phrasal Verbs para entrar e sair:

    Get on / Get off: Ônibus, Trem, Avião (Grandes).

        "We need to get off at the next station."

    Get in / Get out of: Carro, Táxi (Pequenos).

        "Get in the car, let's go!"

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a frase gramaticalmente correta para dizer que você vai ao trabalho de carro?

A) I go to work by the car. B) I go to work by car. C) I go to work on car.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Com a preposição By, não usamos artigos (the/a). É direto: By car.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Você chegou atrasado na estação e o trem partiu sem você. Complete a frase:

"Oh no! I ______ the train."

A) lost B) missed C) failed
Imagem de departing train and a sad personAbre em uma nova janela

departing train and a sad person
Correção do Desafio

A resposta correta é B.

Explicação: Quando perdemos um transporte (ou um evento) por atraso, o verbo é Miss. "Lost" seria se você não soubesse onde o trem está (o que é impossível!).

Frase: "I missed the train."
Imagem de two travelers looking at a map and scheduleAbre em uma nova janela

two travelers looking at a map and schedule
Dialogue: Choosing Transport

Lea: How should we go to Paris? By plane or by train? Max: Well, going by plane is faster, but the airport is far. Lea: True. If we go by train, we arrive in the city center. Max: Exactly. And I hate waiting in lines at the airport. Lea: Okay, let's take the Eurostar train then. Max: Good idea. We just need to make sure we don't miss it! Lea: Don't worry, we will get on the train early.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique falar sobre seus hábitos de transporte.

"I usually go to work by car, but sometimes I take the bus. I don't like going on foot because it is too far. Last year, I traveled to Europe by plane. I almost missed my flight because of traffic! When I arrived, I took a taxi to the hotel. Traveling by train is my favorite way to see the country."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 47, Tema Central: At the Airport: Basic
Imagem de busy airport terminal with travelers standing at checkin countersAbre em uma nova janela

busy airport terminal with travelers standing at checkin counters
At the Airport: Basic
Social English - Pill 47

Viajar de avião pode ser estressante se você não entender o que os agentes estão dizendo.

Hoje vamos focar na primeira etapa da viagem: do Check-in até o Boarding (embarque). Vamos aprender as frases essenciais para passar por esse processo com tranquilidade.
Imagem de person handing a passport to an airline agent at a counterAbre em uma nova janela

person handing a passport to an airline agent at a counter
Step 1: The Check-in Desk

Ao chegar, você vai ao balcão (Check-in desk/counter) para despachar as malas e pegar seu cartão de embarque.

O agente vai pedir:

    "Can I see your passport and ticket, please?"

Você responde:

    "Here you are." (Aqui está.)

    "Here is my passport."

Imagem de two types of bags: a large suitcase (Checked) and a small rolling bag (Carryon)Abre em uma nova janela
aotos.com
two types of bags: a large suitcase (Checked) and a small rolling bag (Carryon)
Vocabulary: Bags vs. Luggage

A confusão número 1: qual mala vai onde?

    Checked bag/luggage: A mala grande que vai no porão do avião (que você despacha).

        "I have one checked bag."

    Carry-on / Hand luggage: A mala pequena que vai com você na cabine.

        "This is just my carry-on."

Verbo: To check a bag (Despachar uma mala).
Imagem de airplane seat layout highlighting a window seat and an aisle seatAbre em uma nova janela

airplane seat layout highlighting a window seat and an aisle seat
Step 2: Choosing a Seat

O agente pode perguntar sua preferência: "Window or aisle?"

    Window seat: Janela (para ver a vista).

    Aisle seat: Corredor (para levantar fácil).

        Pronúncia: A palavra Aisle se pronuncia "I-ll" (como "I will"). O "S" é mudo!

    "I would like an aisle seat, please."

Imagem de boarding pass with the Gate number and Seat number highlightedAbre em uma nova janela
pngtree.com
boarding pass with the Gate number and Seat number highlighted
Step 3: The Boarding Pass

Depois do check-in, você recebe o Boarding Pass (Cartão de embarque).

Nele, procure duas informações cruciais:

    Gate: O portão de embarque (Ex: Gate 12B).

    Boarding Time: A hora que começa o embarque.

    "Your flight leaves from Gate 20."

Imagem de line of people showing their documents to get on the planeAbre em uma nova janela

line of people showing their documents to get on the plane
Step 4: Boarding

Quando chamam o voo, é hora do Boarding (entrar no avião).

    "Boarding is now open." (O embarque está aberto).

    "Please have your boarding pass ready." (Tenha seu cartão em mãos).

    "Final call." (Última chamada - corra!).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você quer levar sua mala pequena dentro do avião com você. Como você a chama?

A) Check-in bag B) Carry-on C) Big luggage
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A mala de mão é chamada de Carry-on (que você "carrega" para dentro) ou Hand luggage.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Pronúncia e Vocabulário

Você prefere sentar no corredor. Complete a frase (lembrando que o 's' é mudo na escrita!):

"I would like an ______ seat, please."

A) isle B) aisle C) corridor
Imagem de airplane aisleAbre em uma nova janela
jayatravel.com
airplane aisle
Correção do Desafio

A resposta correta é B.

Explicação: A palavra correta para corredor de avião, teatro ou igreja é Aisle. Corridor é usado mais para prédios e casas.

Frase: "I would like an aisle seat."
Imagem de interaction at the airport counterAbre em uma nova janela

interaction at the airport counter
Dialogue: At the Counter

Agent: Good morning. Can I see your passport? You: Good morning. Here you are. Agent: Are you checking any bags? You: Yes, one checked bag. And I have this backpack as my carry-on. Agent: Perfect. Put it on the scale, please. Do you prefer window or aisle? You: Window seat, please. Agent: Okay. Here is your boarding pass. Your flight is at Gate 15. Boarding starts at 10:30. You: Thank you!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique o diálogo do check-in.

"Hi. I am flying to London. Here is my passport. I would like to check this suitcase. I will keep this small bag as my carry-on. Can I have an aisle seat, please? I need to stretch my legs. Which gate is it? Okay, Gate 4. Thank you!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 48, Tema Central: At the Hotel: Basic
Imagem de person standing at a hotel reception desk talking to a receptionistAbre em uma nova janela

person standing at a hotel reception desk talking to a receptionist
At the Hotel: Basic
Social English - Pill 48

Depois do aeroporto, o próximo passo é o hotel.

A interação na recepção (Front Desk ou Reception) segue um padrão muito previsível. Hoje vamos aprender o essencial para fazer o Check-in e pegar sua chave.
Imagem de person handing a credit card and passport to the receptionistAbre em uma nova janela

person handing a credit card and passport to the receptionist
Step 1: The Arrival

Ao chegar no balcão, a frase mágica é:

"Hello, I have a reservation." (Olá, eu tenho uma reserva.)

Você também pode adicionar seu nome:

    "I have a reservation under the name of Silva."

    "I booked online." (Eu reservei online.)

Imagem de form being filled outAbre em uma nova janela

form being filled out
Step 2: ID and Form

O recepcionista pedirá seus documentos.

    "Can I see your ID / Passport, please?"

    "Please fill out this form." (Por favor, preencha este formulário.)

    "Sign here, please." (Assine aqui).

Dica: Eles geralmente pedem um cartão de crédito para "incidentals" (gastos extras como frigobar). Não se assuste, é apenas uma garantia.
Imagem de modern plastic hotel key card next to an old metal keyAbre em uma nova janela

modern plastic hotel key card next to an old metal key
Step 3: The Key Card

Hoje em dia, raramente usamos chaves de metal. Usamos cartões magnéticos.

    Key card: Cartão-chave.

    "Here is your key card."

O recepcionista dirá o número do quarto e o andar.

    "You are in room 305, on the third floor."

Imagem de elevator icon and a stairs iconAbre em uma nova janela

elevator icon and a stairs icon
Step 4: Getting to the Room

Como subir?

    Elevator: (EUA) Elevador.

    Lift: (UK) Elevador.

    Stairs: Escadas.

    "The elevator is over there, on your right."

Imagem de WiFi symbol and a clock showing 7:00 AMAbre em uma nova janela

WiFi symbol and a clock showing 7:00 AM
Step 5: Important Questions

Antes de subir, garanta o essencial: a internet e a comida.

    "What is the Wi-Fi password?" (Qual a senha do Wi-Fi?)

    "Is breakfast included?" (O café da manhã está incluso?)

    "What time is breakfast served?" (A que horas é servido o café?)

Imagem de person carrying luggage for a guestAbre em uma nova janela

person carrying luggage for a guest
Step 6: Luggage Help

Em hotéis maiores, alguém pode oferecer ajuda com as malas.

    Bellboy / Porter: O funcionário que carrega malas.

    "Do you need help with your bags?"

        Sim: "Yes, please."

        Não: "No thanks, I can manage." (Eu me viro/consigo levar).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você chegou na recepção. Qual a primeira frase correta a dizer?

A) I want a room now. B) Hello, I have a reservation. C) Give me the key.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: É a forma polida e padrão de iniciar o atendimento. As outras opções soam rudes (imperativas).
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Hoje em dia, a "chave" do hotel é geralmente um cartão de plástico. Como chamamos isso em inglês?

"Here is your key ______."

A) map B) board C) card
Imagem de hand holding a key cardAbre em uma nova janela

hand holding a key card
Correção do Desafio

A resposta correta é C.

Explicação: O termo é Key card.

Frase: "Here is your key card."
Imagem de receptionist handing a key card to a guestAbre em uma nova janela

receptionist handing a key card to a guest
Dialogue: Checking In

Receptionist: Good afternoon. Welcome to the Grand Hotel. You: Hi. I have a reservation under the name of Santos. Receptionist: Let me check... Yes, a double room for three nights. Can I see your passport? You: Here you are. Is breakfast included? Receptionist: Yes, it is served from 7 to 10 AM. You: Great. And what is the Wi-Fi password? Receptionist: It is written on this card. Here is your key card. You are in room 402. The elevator is on the left. You: Thank you!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique fazer o check-in.

"Hello, good evening. I have a reservation for two nights. My last name is [Seu Sobrenome]. Here is my credit card. Could you tell me, what time is breakfast? And what is the Wi-Fi password? Okay, room 501. Thank you. Where is the elevator?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 49, Tema Central: Sightseeing Vocabulary
Imagem de tourist holding a camera and a map, looking at a famous landmarkAbre em uma nova janela

Sightseeing Vocabulary
Social English - Pill 49

Você chegou ao seu destino! Agora é hora de explorar.

Em inglês, o ato de passear e ver os pontos turísticos tem um nome específico: Sightseeing (Sight = Vista/Visão + Seeing = Vendo).

Hoje vamos aprender os verbos e expressões essenciais para descrever seus passeios turísticos.
Imagem de doubledecker tour bus driving through a cityAbre em uma nova janela
unsplash.com
The Main Verb: "Go Sightseeing"

Não dizemos "make tourism". A expressão correta é:

"To go sightseeing." (Passear / Turistar).

    "I want to go sightseeing tomorrow."

    "We went sightseeing all day."

Imagem de person taking a picture of a monument with a smartphoneAbre em uma nova janela
unsplash.com
Taking Photos

O erro número 1 de brasileiros: dizer "take out photos" ou "make photos".

Em inglês, o verbo correto é Take.

    "Take a photo / Take a picture."

    "Take a selfie."

    "Can you take a photo of us, please?"

    "I took many pictures of the castle."

Imagem de famous museum entrance and an art gallery interiorAbre em uma nova janela

Culture: Museums and Monuments

Para locais históricos e culturais, usamos os verbos Visit (Visitar) ou See (Ver).

    "Visit a museum." (Visitar um museu).

    "Visit an art gallery." (Visitar uma galeria de arte).

    "See the monuments." (Ver os monumentos).

    "See the landmarks." (Ver os marcos históricos - ex: Torre Eiffel, Cristo Redentor).

Imagem de group of tourists following a guide holding a flagAbre em uma nova janela

Guided Tours

Se você contrata alguém para te mostrar a cidade:

    Go on a tour: Fazer um tour/excursão.

        "We went on a walking tour."

    Tour guide: O guia turístico.

        "The tour guide was very funny."

Imagem de souvenir shop display with magnets, keychains, and mugsAbre em uma nova janela

Shopping: Souvenirs

Aquelas lembrancinhas que compramos (imãs, chaveiros, camisetas) são chamadas de Souvenirs (pronuncia-se su-ve-nir).

    "To buy souvenirs."

        "I need to buy some souvenirs for my family."

Imagem de person looking confused at a map in the streetAbre em uma nova janela

Getting Lost vs. Exploring

Às vezes, perder-se faz parte da diversão (ou não!).

    "To get lost:" Perder-se.

        "We got lost in the old city."

    "To explore:" Explorar (andar sem rumo definido, mas intencionalmente).

        "I love to explore new neighborhoods."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
Vamos Praticar? - Exercício 1

Qual a forma correta de pedir para alguém tirar uma foto sua?

A) Can you make a photo of me? B) Can you take a photo of me? C) Can you do a photo of me?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

Correção - Exercício 1

A resposta correta é B.

Explicação: A collocation (combinação de palavras) correta é Take a photo.
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
Desafio de Vocabulário

Complete a frase para dizer que você quer "fazer turismo/passear".

"Tomorrow, I want to go ______."

A) tourism B) sighting C) sightseeing
Imagem de pair of binocularsAbre em uma nova janela

Correção do Desafio

A resposta correta é C.

Explicação: O termo correto para a atividade de ver pontos turísticos é Sightseeing.

Frase: "Tomorrow, I want to go sightseeing."
Imagem de two friends planning their day with a brochureAbre em uma nova janela
twistedsifter.com
Dialogue: Planning the Day

Alice: What should we do today? Bob: I really want to go sightseeing. Alice: Great. We can visit the History Museum in the morning. Bob: Okay. And after that, let's go on a boat tour. Alice: Good idea. Don't forget your camera. We will take lots of photos. Bob: Definitely. And I need to buy some souvenirs before we leave.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
Review for Audio

Descreva um dia típico de turista.

"When I travel, I wake up early to go sightseeing. First, I like to visit museums and learn about history. I always take a lot of photos of the landmarks. Sometimes, I go on a walking tour with a guide. And, of course, I always buy souvenirs for my friends. I love to explore new cities!"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 50, Tema Central: Souvenirs & Gifts
Imagem de colorful souvenir shop display with magnets, mugs, and TshirtsAbre em uma nova janela

colorful souvenir shop display with magnets, mugs, and Tshirts
Souvenirs & Gifts
Social English - Pill 50

Chegamos à última pílula desta trilha! Para fechar com chave de ouro, vamos às compras.

Viajar e não trazer uma "lembrancinha" é quase impossível. Hoje vamos aprender o vocabulário para comprar Souvenirs (lembranças de viagem) e presentes para quem ficou em casa.
Imagem de keychain and a wrapped present box side by sideAbre em uma nova janela

keychain and a wrapped present box side by side
Souvenir vs. Gift

Qual a diferença?

    Souvenir: É um objeto que você compra para lembrar de um lugar (como um imã da Torre Eiffel). A palavra vem do francês "memória".

    Gift / Present: É um presente geral que você dá a alguém (pode ser um souvenir ou não).

    "I bought this magnet as a souvenir of my trip."

    "I need to buy a birthday gift for my mom."

Imagem de common items: Fridge magnet, Keychain, Mug, PostcardAbre em uma nova janela

common items: Fridge magnet, Keychain, Mug, Postcard
The Classics (Vocabulary)

Os itens mais comuns que compramos:

    Fridge magnet: Imã de geladeira (o campeão de vendas).

    Keychain / Key ring: Chaveiro.

    Mug: Caneca.

    T-shirt: Camiseta.

    Postcard: Cartão postal.

    Handicrafts: Artesanato local (feito à mão).

Imagem de person looking at items on a shelf while a shop assistant approachesAbre em uma nova janela
staffmatch.com
person looking at items on a shelf while a shop assistant approaches
Browsing: "Just looking"

Quando você entra na loja e o vendedor pergunta "Can I help you?", se você ainda não decidiu, use a frase mágica:

"No thanks, I'm just looking." (Não obrigado, estou apenas olhando/dando uma olhadinha).

Se precisar de ajuda: "I'm looking for a souvenir for my [Relative]."
Imagem de price tagAbre em uma nova janela

price tag
Asking the Price

Para perguntar o preço de itens individuais ou no plural:

    Singular: "How much is this T-shirt?"

    Plural: "How much are these keychains?"

Se não tem preço na etiqueta:

    "Excuse me, how much is this?"

Imagem de person holding three identical itemsAbre em uma nova janela

person holding three identical items
Deals: "3 for 10"

Em lojas turísticas, é comum ver promoções de quantidade.

    "Three for ten dollars." (3 por 10).

    "Buy one, get one free." (Pague um, leve outro grátis).

Se você vai levar o produto, diga ao vendedor: "I'll take it." (Vou levar). "I'll take two of these." (Vou levar dois desses).
Imagem de gift bag and a receiptAbre em uma nova janela
ohhdeer.com
gift bag and a receipt
"Can you wrap it?"

Se for presente, você pode pedir para embrulhar ou pedir uma sacola bonita.

    "Can you wrap it, please?" (Pode embrulhar?)

    "Do you have a gift bag?" (Você tem uma sacola de presente?)

    "Can I have the receipt, please?" (Pode me dar o recibo/nota?)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você está na loja e o vendedor pergunta se pode ajudar. Você só quer ver os produtos sem compromisso. O que você diz?

A) I am seeing. B) I'm just looking. C) I watch only.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: A expressão fixa para "só estou olhando" em lojas é "I'm just looking" ou "Just browsing".
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que comprou um imã para sua geladeira.

"I bought a fridge ______ as a souvenir."

A) magnetic B) sticker C) magnet
Imagem de fridge door covered in magnetsAbre em uma nova janela

fridge door covered in magnets
Correção do Desafio

A resposta correta é C.

Explicação: O objeto é chamado de Magnet. Magnetic é o adjetivo (magnético).

Frase: "I bought a fridge magnet."
Imagem de tourist paying at the counterAbre em uma nova janela

tourist paying at the counter
Dialogue: At the Souvenir Shop

Shopkeeper: Hello! Can I help you find something? You: Hi. How much are these keychains? Shopkeeper: They are 5 dollars each, or 3 for 12 dollars. You: Oh, that is a good deal. I'll take three, please. Shopkeeper: Sure. Anything else? You: Yes, how much is this T-shirt? Shopkeeper: That one is 20 dollars. You: Okay, I'll take it too. It is a gift for my brother. Can you wrap it? Shopkeeper: Certainly. Here is your receipt.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique suas habilidades de compra para sua próxima viagem!

"Excuse me, how much is this mug? I am looking for a souvenir for my mother. Do you have this T-shirt in blue? Okay, I'll take it. And I also want two fridge magnets. Can you wrap the mug, please? It is a gift. Do you accept credit cards? Thank you!"

Parabéns! Você completou a trilha Social English (Pre-Intermediate). Continue praticando!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 51, Tema Central: Future Plans: "Going to"
Imagem de person writing in a planner/agenda with a focused expressionAbre em uma nova janela
engagethebrain.org
person writing in a planner/agenda with a focused expression
Future Plans: "Going to"
Social English - Pill 51

Bem-vindo a um novo bloco! Agora vamos focar em falar do futuro.

Em situações sociais, é muito comum perguntar: "O que você vai fazer no fim de semana?". Para responder sobre planos que você já decidiu, usamos a estrutura Going to.
Imagem de formula: Person + BE + GOING TO + ActionAbre em uma nova janela
formula: Person + BE + GOING TO + Action
The Structure

A fórmula é simples, mas exige o verbo To Be.

Subject + am/is/are + going to + Verb

    I am going to buy a car. (Eu vou comprar um carro).

    She is going to visit her mom. (Ela vai visitar a mãe dela).

    We are going to travel. (Nós vamos viajar).

Dica: Pense no "Going to" como o nosso "Vou/Vai" para planos firmes.
Imagem de thought bubble showing a clear image of a beach tripAbre em uma nova janela

thought bubble showing a clear image of a beach trip
When to use it: Concrete Plans

Use Going to quando a decisão já foi tomada antes da conversa. É uma intenção clara.

    "I am going to play soccer on Saturday." (Já combinei, já tenho o horário).

    "They are going to get married in June." (O casamento já está marcado).

Imagem de casual chat bubble with Gonna written insideAbre em uma nova janela

casual chat bubble with Gonna written inside
Pronunciation Tip: "Gonna"

Na fala rápida e informal (filmes, músicas, conversas com amigos), "Going to" quase sempre vira Gonna.

    "I'm gonna study."

    "She's gonna leave."

Atenção: Use "Gonna" apenas na fala ou em mensagens de texto muito informais. Na escrita formal, mantenha "Going to".
Imagem de calendar highlighting Tomorrow and Next WeekAbre em uma nova janela

calendar highlighting Tomorrow and Next Week
Time Expressions

Para situar seu plano, use expressões de tempo no final da frase:

    Tonight: Hoje à noite.

    Tomorrow: Amanhã.

    Next week / Next month: Semana que vem / Mês que vem.

    This weekend: Neste fim de semana.

    "I am going to cook tonight."

Imagem de question mark and a No symbolAbre em uma nova janela

question mark and a No symbol
Questions and Negatives

Como perguntar sobre os planos de alguém? Inverta o verbo To Be.

    Question: "Are you going to stay home?" (Você vai ficar em casa?)

    Negative: "I am not going to work tomorrow." (Não vou trabalhar amanhã).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a frase gramaticalmente correta para dizer "Nós vamos assistir um filme"?

A) We going to watch a movie. B) We are going to watch a movie. C) We is going to watch a movie.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Você não pode esquecer o verbo To Be (am/is/are). Para "We" (nós), usamos are. Frase: "We are going to watch a movie."
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase com a gíria informal para "going to".

"I am tired. I am ______ sleep."

A) go to B) gonna C) wanna
Imagem de sleepy person going to bedAbre em uma nova janela

sleepy person going to bed
Correção do Desafio

A resposta correta é B.

Explicação: Gonna é a contração informal de going to. (Wanna seria "want to").

Frase: "I am gonna sleep."
Imagem de two friends talking while looking at a smartphone screenAbre em uma nova janela

two friends talking while looking at a smartphone screen
Dialogue: Weekend Plans

Paul: Hey, simple question: Are you going to do anything special this weekend? Mary: Yes! I am going to visit my sister in the countryside. Paul: That sounds nice. Are you driving? Mary: No, I am going to take the bus. My car is broken. And you? Paul: I am going to stay here. I am going to paint my living room. Mary: Good luck! That sounds like hard work.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique falar sobre seus planos reais ou imaginários.

"Next weekend, I am going to relax. I am going to wake up late on Saturday. Then, I am going to have lunch with my friends. We are going to try a new restaurant. On Sunday, I am not going to do anything. I am just going to watch TV. What are you going to do?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 52, Tema Central: Future Plans: "Want to"
Imagem de person looking at a travel brochure with a dreamy expressionAbre em uma nova janela
blog.ricksteves.com
person looking at a travel brochure with a dreamy expression
Future Plans: "Want to"
Social English - Pill 52

Na aula passada, falamos sobre planos concretos (Going to). Hoje, vamos falar sobre desejos e vontades.

Quando você tem a intenção ou o sonho de fazer algo, mas ainda não é um plano fixo com data marcada, usamos o verbo Want.
Imagem de formula: Person + WANT TO + ActionAbre em uma nova janela

formula: Person + WANT TO + Action
The Structure

A estrutura é muito simples, mas lembre-se do TO entre os verbos.

Subject + want + to + Verb

    I want to buy a new house. (Eu quero comprar uma casa nova).

    She wants to learn French. (Ela quer aprender francês).

    We want to go to Italy next year. (Nós queremos ir para a Itália).

Nota Gramatical: Para He/She/It, adicione o S no verbo: He wants to.
Imagem de comic bubble with the word Wanna insideAbre em uma nova janela

comic bubble with the word Wanna inside
Pronunciation: "Wanna"

Assim como o Going to vira Gonna, o Want to vira Wanna em conversas informais.

    "I wanna go home."

    "Do you wanna come?"

Atenção: Wanna é apenas para situações casuais. Em e-mails de trabalho ou situações formais, escreva e fale "want to".
Imagem de waiter taking an order vs a friend talking to another friendAbre em uma nova janela

waiter taking an order vs a friend talking to another friend
Want to vs. Would like to

Cuidado para não soar rude!

    Want to: Use para expressar desejos gerais ou falar com amigos.

        "I want to be rich." (Desejo).

    Would like to: Use para fazer pedidos (restaurantes, lojas) ou ser educado.

        "I would like a coffee, please." (Pedido).

        Evite dizer "I want a coffee" para o garçom.

Imagem de question mark and a cross (X) symbolAbre em uma nova janela

question mark and a cross (X) symbol
Questions and Negatives

Para fazer perguntas ou negar, precisamos do auxiliar Do/Does.

    Question: "Do you want to come with us?"

    Negative: "I don't want to go out tonight."

        She doesn't want to cook.

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a frase correta para dizer que ela quer viajar?

A) She want to travel. B) She wants to travel. C) She wanna travel.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Na terceira pessoa (She), o verbo ganha um 's': Wants. A opção C (She wanna) está gramaticalmente incorreta porque wanna não leva 's', e mesmo informalmente soaria estranho sem o ajuste correto (o certo informal seria "She wants to" ou, em gíria muito solta, às vezes ouve-se sem o S, mas o padrão correto é B).
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase com a forma negativa. Você está cansado e não quer ir à festa.

"I am tired. I ______ want to go to the party."

A) not B) no C) don't
Imagem de person refusing an invitation politelyAbre em uma nova janela
parade.com
person refusing an invitation politely
Correção do Desafio

A resposta correta é C.

Explicação: Para negar verbos no presente (como want), usamos o auxiliar Don't (para I/You/We/They).

Frase: "I don't want to go."
Imagem de two friends looking at a shop windowAbre em uma nova janela

two friends looking at a shop window
Dialogue: Window Shopping

Karen: Look at those shoes! They are beautiful. Leo: Do you want to buy them? Karen: I want to, but they are too expensive. I don't have money right now. Leo: Maybe you can buy them next month. Karen: Yes. I want to save money first. What about you? Do you want to go inside? Leo: No, I don't want to spend money today. Let's just walk.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Fale sobre seus desejos para o futuro próximo.

"In the future, I want to travel more. I want to visit Japan because I love the culture. I also want to get a better job. But right now, I just want to relax. I don't want to worry about work today. Do you wanna come to the park with me?"

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 53, Tema Central: New Year's Resolutions
Imagem de person writing a list titled 2026 Goals with a determined lookAbre em uma nova janela
the7minutelife.com
person writing a list titled 2026 Goals with a determined look
New Year's Resolutions
Social English - Pill 53

No início do ano, é tradição fazer New Year's Resolutions (Resoluções de Ano Novo). São promessas que fazemos a nós mesmos para melhorar a vida.

Hoje vamos aprender a falar sobre estas metas pessoais e usar os verbos certos para descrever mudanças de hábitos.
Imagem de icons representing common goals: a piggy bank (money), a salad (health), a book (learning)Abre em uma nova janela

icons representing common goals: a piggy bank (money), a salad (health), a book (learning)
Common Resolutions

Aqui estão as resoluções mais comuns. Consegues identificar alguma tua?

    Get fit / Join a gym: Ficar em forma / Inscrever-se num ginásio.

    Lose weight: Perder peso.

    Save money: Poupar dinheiro.

    Learn a new skill: Aprender uma nova habilidade.

    Quit smoking: Deixar de fumar.

    Spend more time with family: Passar mais tempo com a família.

Imagem de formula: I plan to + VerbAbre em uma nova janela
englishstudypage.com
formula: I plan to + Verb
Structure 1: "I plan to..."

Para além do "Going to" (que vimos na pílula 51), podemos usar Plan to para soar mais organizado.

    "I plan to save more money this year." (Planeio poupar mais dinheiro este ano.)

    "I plan to travel to Europe." (Planeio viajar para a Europa.)

Imagem de start button and a stop signAbre em uma nova janela

start button and a stop sign
Start vs. Stop / Quit (+ ING)

Atenção à gramática aqui! Quando usamos Stop (Parar) ou Quit (Desistir/Largar), o verbo seguinte precisa de terminar em -ING.

    Stop / Quit:

        "I want to quit smoking." (Quero deixar de fumar.)

        "I need to stop eating fast food." (Preciso de parar de comer fast food.)

    Start: (Pode usar -ING ou TO, mas -ING é muito comum para hobbies).

        "I want to start running." (Quero começar a correr.)

Imagem de calendar with Once a week and Every day markedAbre em uma nova janela
betterhumans.pub
calendar with Once a week and Every day marked
Frequency Goals

Muitas metas envolvem frequência.

    More (Mais) vs. Less (Menos).

        "I want to exercise more."

        "I want to use my phone less."

    Every day: Todos os dias.

    Twice a week: Duas vezes por semana.

Imagem de person looking hopefulAbre em uma nova janela

person looking hopeful
Structure 2: "I hope to..."

Se a meta é um desejo forte, mas talvez não dependa só de ti, usa Hope.

    "I hope to get a promotion." (Espero ser promovido.)

    "I hope to find a new job." (Espero encontrar um novo emprego.)

Imagem de checklist with items crossed outAbre em uma nova janela

checklist with items crossed out
"Stick to it"

Uma expressão idiomática importante. Manter a promessa e não desistir chama-se Stick to it (Manter-se fiel a ela).

    "It is hard to stick to my resolutions." (É difícil manter as minhas resoluções.)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

O João quer parar de comer açúcar. Qual a frase gramaticalmente correta?

A) I want to stop eat sugar. B) I want to stop eating sugar. C) I want to stop to eat sugar.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Depois do verbo Stop (no sentido de abandonar um hábito), o verbo seguinte deve vir no gerúndio (-ING). "Stop eating sugar."
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Completa a frase para dizer que queres inscrever-te num ginásio para ficar em forma.

"My goal is to ______ a gym."

A) enter B) make C) join
Imagem de gym membership cardAbre em uma nova janela

gym membership card
Correção do Desafio

A resposta correta é C.

Explicação: O verbo correto para tornar-se membro de um clube, ginásio ou grupo é Join.

Frase: "My goal is to join a gym."
Imagem de two friends drinking coffee and comparing notebooksAbre em uma nova janela

two friends drinking coffee and comparing notebooks
Dialogue: Sharing Goals

Marta: Happy New Year, Tiago! Do you have any resolutions? Tiago: Yes! This year, I plan to learn French. And you? Marta: Nice! I have a few. First, I want to quit smoking. Tiago: That is a great goal. It is hard, but you can do it. Marta: Thanks. I also want to start doing yoga to relax. Tiago: I need to relax too. Maybe I should join your yoga class. Marta: You should! Let's help each other stick to our plans.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratica dizer as tuas resoluções em voz alta.

"My New Year's resolutions are simple. First, I plan to read one book every month. I also want to save money for a new car. I need to stop going to bed so late. And finally, I hope to visit my friends in London. I promise to stick to these goals!"

Envia ao teu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 54, Tema Central: Describing a Friend
Imagem de person looking in a mirror (reflection showing appearance) and a thought bubble showing a heart/brain (personality)Abre em uma nova janela

person looking in a mirror (reflection showing appearance) and a thought bubble showing a heart/brain (personality)
Describing a Friend
Social English - Pill 54

Quando falamos de amigos, geralmente descrevemos duas coisas: a aparência física e a personalidade.

O maior desafio em inglês é não confundir as perguntas. Hoje vamos aprender a diferenciar "Como ele é?" (físico) de "Como ele é?" (jeito de ser).
Imagem de diagram contrasting two questions: What is he like? vs What does he look like?Abre em uma nova janela

diagram contrasting two questions: What is he like? vs What does he look like?
The Two Key Questions

Preste muita atenção, pois são parecidas mas significam coisas opostas:

    "What does he LOOK LIKE?"

        Refere-se à aparência física. (Alto, loiro, olhos azuis).

        Resposta: "He is tall and handsome."

    "What IS he LIKE?"

        Refere-se à personalidade. (Engraçado, inteligente, tímido).

        Resposta: "He is funny and kind."

Imagem de icons representing physical traits: Height chart, Hair styles, Eye colorsAbre em uma nova janela

icons representing physical traits: Height chart, Hair styles, Eye colors
Appearance: Be vs. Have

Para descrever o corpo, usamos dois verbos diferentes.

    To Be (Ser/Estar): Para adjetivos gerais (Altura, peso, idade).

        He is tall / short / average height. (Ele é alto/baixo/estatura média).

        She is slim / fit. (Ela é magra/em forma).

        He is handsome / She is beautiful.

    To Have (Ter): Para partes específicas (Cabelo, olhos, barba).

        He has blue eyes. (Ele tem olhos azuis).

        She has long, curly hair. (Ela tem cabelo longo e cacheado).

        He has a beard. (Ele tem barba).

Imagem de emojis representing personality traits: Laughing (Funny), Glasses (Smart), Hiding face (Shy), Star eyes (Outgoing)Abre em uma nova janela
parade.com
emojis representing personality traits: Laughing (Funny), Glasses (Smart), Hiding face (Shy), Star eyes (Outgoing)
Personality Adjectives

Para responder a "What is he like?", use o verbo To Be + Adjetivo.

    Funny: Engraçado.

    Smart / Intelligent: Inteligente.

    Kind: Gentil/Bondoso.

    Shy: Tímido.

    Outgoing: Extrovertido (sociável).

    Hardworking: Trabalhador.

    Lazy: Preguiçoso.

    "My best friend is very outgoing."

Imagem de person holding a photo of a famous actor next to their faceAbre em uma nova janela

person holding a photo of a famous actor next to their face
"He looks like..."

Se o seu amigo se parece com outra pessoa (um parente ou uma celebridade), usamos a estrutura Look like + Substantivo.

    "He looks like his father." (Ele se parece com o pai dele).

    "She looks like [Famous Actress]." (Ela se parece com a [Atriz Famosa]).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você quer saber se o novo namorado da sua amiga é gente boa (personalidade). O que você pergunta?

A) How is he? B) What does he look like? C) What is he like?
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação:

    How is he? = Como ele está? (Saúde/Momento).

    What does he look like? = Como ele é fisicamente?

    What is he like? = Como é a personalidade dele?

Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase descrevendo o cabelo dela.

"She is tall and she ______ short blonde hair."

A) is B) has C) have
Imagem de woman with short blonde hairAbre em uma nova janela

woman with short blonde hair
Correção do Desafio

A resposta correta é B.

Explicação: Para partes do corpo (cabelo, olhos), usamos o verbo Have. Como é "She" (ela), conjugamos para Has.

Frase: "She has short blonde hair."
Imagem de two friends looking at a photo on a phoneAbre em uma nova janela

two friends looking at a photo on a phone
Dialogue: The Blind Date

Ana: I want you to meet my friend, Mike. I think you guys would be a great couple. Bia: Really? What does he look like? Ana: He is tall and has dark curly hair. He is very cute. Bia: Nice. And what is he like? Ana: He is really funny and smart. He works as an engineer. Bia: Is he shy? Ana: A little bit at first, but then he is very outgoing. Bia: Okay, show me a photo!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Descreva seu melhor amigo ou amiga.

"My best friend is [Nome]. He is tall and thin. He has brown eyes and short hair. He looks like a soccer player. Personality-wise, he is very funny and always happy. Sometimes he is a bit lazy, but he is a great friend. We love playing video games together."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 55, Tema Central: Social Media Vocabulary
Imagem de smartphone screen displaying social media icons: Instagram, TikTok, Facebook, X (Twitter)Abre em uma nova janela

smartphone screen displaying social media icons: Instagram, TikTok, Facebook, X (Twitter)
Social Media Vocabulary
Social English - Pill 55

Hoje em dia, grande parte da nossa vida social acontece online.

Para navegar no Instagram, TikTok ou Facebook em inglês, você precisa dominar os verbos de ação básicos. Vamos aprender a interagir digitalmente.
Imagem de three icons in a row: A plus sign (Post), a heart (Like), and an arrow (Share)Abre em uma nova janela

three icons in a row: A plus sign (Post), a heart (Like), and an arrow (Share)
The Big Three: Post, Like, Share

Estas são as ações fundamentais:

    To Post: (Verbo) Publicar / Postar.

        Noun: A post (Uma publicação).

        "I posted a new photo today."

    To Like: (Verbo) Curtir.

        "Don't forget to like the video."

    To Share: (Verbo) Compartilhar.

        "Please share this with your friends."

Imagem de comment section on a phone screen with an @ symbol highlighting a usernameAbre em uma nova janela
meta.stackexchange.com
comment section on a phone screen with an @ symbol highlighting a username
Interaction: Tag & Comment

Como você fala com as pessoas nas publicações?

    To Comment: Comentar.

        "Leave a comment below."

    To Tag: Marcar alguém (usando o @).

        "Did you tag me in that photo?"

        "I will tag you in the comments."

Imagem de smartphone showing the difference between the main scrolling area (Feed) and the circles at the top (Stories)Abre em uma nova janela
differentbrains.org
smartphone showing the difference between the main scrolling area (Feed) and the circles at the top (Stories)
The Content: Feed vs. Stories

    Feed / Timeline: A linha do tempo onde você rola a tela para ver as postagens fixas.

        "I saw it on my feed."

        "Scroll down the timeline."

    Story / Stories: As postagens temporárias que somem em 24 horas.

        "I posted a video on my stories."

Imagem de paper plane icon or a chat bubble iconAbre em uma nova janela

paper plane icon or a chat bubble icon
Private Messages: DM

Quando você quer falar em privado, você manda uma DM (Direct Message).

    "I'll send you a DM." (Vou te mandar um direct).

    "Check your DMs." (Olhe suas mensagens privadas).

    "Slide into DMs:" (Gíria para puxar papo com alguém com segundas intenções).

Imagem de graph going up sharply or a flame iconAbre em uma nova janela

graph going up sharply or a flame icon
Popularity: Viral & Trending

    To go viral: Viralizar (espalhar-se muito rápido).

        "The cat video went viral."

    Trending: O que está em alta no momento (Assuntos do momento).

        "This song is trending on TikTok."

Imagem de person clicking the 'Follow' button on a profileAbre em uma nova janela

person clicking the 'Follow' button on a profile
Connections: Follow & Unfollow

    To Follow: Seguir.

        "Do you follow him?"

    To Unfollow: Deixar de seguir.

        "I unfollowed her because she posts too much."

    Followers: Seguidores.

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você viu um meme engraçado e quer que seu amigo veja. Você coloca o nome dele (@user) nos comentários. O que você fez?

A) You liked him. B) You tagged him. C) You shared him.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Usar o @ para notificar alguém em uma foto ou comentário chama-se Tag (Marcar).
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase com o verbo que significa "publicar".

"Wait! Don't ______ that photo. I look terrible in it!"

A) paste B) post C) past
Imagem de delete buttonAbre em uma nova janela

delete button
Correção do Desafio

A resposta correta é B.

Explicação: O verbo para colocar conteúdo na rede social é Post.

Frase: "Don't post that photo."
Imagem de two friends looking at a phone screen laughingAbre em uma nova janela

two friends looking at a phone screen laughing
Dialogue: Check this out!

Sam: Hey, did you see the video I shared with you? Tina: No, where did you send it? Sam: I tagged you in the comments on Instagram. Tina: Oh, let me check my notifications. Haha! That is hilarious. Sam: I know, right? It is going viral. Everyone is sharing it. Tina: I'm going to post it on my stories right now. Sam: Good idea. Don't forget to tag the creator.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique falar sobre seus hábitos digitais.

"I spend a lot of time on social media. I usually post photos of my travel on Instagram. I always tag my friends when we are together. I don't like to comment on public posts, but I like everything I see. Sometimes I send funny memes via DM. Yesterday, a video I watched went viral."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 56, Tema Central: Texting Abbreviations
Imagem de smartphone screen displaying a chat conversation full of acronymsAbre em uma nova janela

smartphone screen displaying a chat conversation full of acronyms
Texting Abbreviations
Social English - Pill 56

Quando escrevemos mensagens (Texting/Chatting), a velocidade é tudo. Por isso, os nativos usam muitas abreviações e siglas.

Você não precisa usá-las em e-mails formais, mas precisa entendê-las para conversar no WhatsApp ou redes sociais. Vamos decifrar esse código!
Imagem de three speech bubbles: one saying LOL, one OMG, one BTWAbre em uma nova janela

three speech bubbles: one saying LOL, one OMG, one BTW
The Big Three: LOL, OMG, BTW

Estas são as mais famosas. Todo mundo usa.

    LOL: Laughing Out Loud. (Rindo muito alto / "Kkkk").

        Uso: Quando algo é engraçado.

        Atenção: Não significa "Lots of Love" (muito amor).

    OMG: Oh My God / Oh My Gosh. (Ai meu Deus).

        Uso: Surpresa ou choque.

    BTW: By The Way. (A propósito / Por falar nisso).

        Uso: Para mudar de assunto ou adicionar uma informação.

        "BTW, did you see the game?"

Imagem de person shrugging their shoulders with a question mark above their headAbre em uma nova janela

person shrugging their shoulders with a question mark above their head
Knowledge & Opinion: IDK, IMO

Para expressar o que você sabe (ou não) e o que pensa.

    IDK: I Don't Know. (Eu não sei).

        A: "Where is Tom?"

        B: "IDK."

    IMO: In My Opinion. (Na minha opinião).

        Uso: Para dar sua opinião de forma suave.

        "IMO, the movie was boring."

Imagem de clock or an hourglassAbre em uma nova janela

clock or an hourglass
Time & Urgency: ASAP, BRB

    ASAP: As Soon As Possible. (O mais rápido possível / Assim que der).

        "Call me ASAP."

    BRB: Be Right Back. (Já volto).

        Uso: Muito comum em chats quando você vai sair da tela por um minuto.

    TTYL: Talk To You Later. (Falo com você mais tarde / Tchau).

Imagem de clown face or a Just Kidding signAbre em uma nova janela
tenor.com
clown face or a Just Kidding sign
Fun & Politeness: JK, THX, NP

    JK: Just Kidding. (Estou brincando / "Zoeira").

        "You are fired! ... JK!"

    THX / TNX: Thanks. (Obrigado).

    NP: No Problem. (Sem problemas / De nada).

Imagem de visual equation: U = You, R = Are, 2 = To/Two, 4 = ForAbre em uma nova janela

visual equation: U = You, R = Are, 2 = To/Two, 4 = For
Phonetic Spelling (Sons)

Muitas vezes, substituímos a palavra pela letra ou número que tem o mesmo som.

    U = You (Você).

    R = Are (É/Estão).

    C = See (Ver).

    2 = To / Too (Para / Também).

    4 = For (Para).

    Gr8 = Great (Ótimo).

Exemplo: "R u coming 2 the party?" (Are you coming to the party?)
Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Seu amigo mandou uma piada no WhatsApp. Qual a resposta correta para mostrar que você achou engraçado?

A) BRB B) LOL C) IDK
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: LOL (Laughing Out Loud) é o equivalente ao nosso "kkkk" ou "rsrs". BRB é "já volto" e IDK é "não sei".
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Traduza a mensagem de texto abaixo para o inglês completo:

"Thx 4 the gift!"

A) Thanks four the gift! B) Thanks for the gift! C) Thanks far the gift!
Imagem de wrapped gift boxAbre em uma nova janela
waterleafpaperco.com
wrapped gift box
Correção do Desafio

A resposta correta é B.

Explicação: O número 4 (four) tem o mesmo som da preposição for (por/para). "Thanks for the gift!"
Imagem de smartphone chat interface with green and gray bubblesAbre em uma nova janela

smartphone chat interface with green and gray bubbles
Dialogue: Text Message Style

Sam: Hey! R u busy? Liz: A little bit. Working on a project. Y? (Why?) Sam: Just wanted to ask if u saw the news. OMG! Liz: No, IDK what happened. Tell me! Sam: Can't type now. Call u ASAP. Liz: Ok, NP. TTYL. Sam: Thx. Bye!
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Atenção: Embora a gente escreva abreviado, geralmente lemos a palavra completa (exceto para LOL e ASAP, que às vezes falamos as letras).

Leia o texto abaixo em voz alta, transformando as siglas em palavras completas:

"Hi! How are you? (How r u?) I missed the bus, oh my God! (OMG) I don't know when I will arrive. (IDK) Please start the meeting as soon as possible. (ASAP) Just kidding! (JK) I am almost there. See you soon!" (C u soon!)

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 57, Tema Central: Expressing Feelings: Happy/Sad
Imagem de two theatre masks, one smiling (comedy) and one crying (tragedy) side by sideAbre em uma nova janela

two theatre masks, one smiling (comedy) and one crying (tragedy) side by side
Expressing Feelings: Happy/Sad
Social English - Pill 57

Expressar emoções é a base da conexão humana. Mas não basta dizer "I am happy".

Para ter uma conversa real, precisamos explicar o motivo do sentimento. Hoje vamos aprender a conectar a emoção à causa usando "When" e "Makes me".

+ "when" + [Action] ]
Imagem de formula: I feel + [EmojiAbre em uma nova janela

formula: I feel + [Emoji
Structure 1: "I feel... when..."

Esta é a estrutura mais simples e poderosa para explicar seus sentimentos.

"I feel [Adjective] when [Situation]."

    "I feel happy when I listen to music." (Sinto-me feliz quando ouço música.)

    "I feel sad when it rains all weekend." (Sinto-me triste quando chove o fim de semana todo.)

    "I feel relaxed when I am at the beach."

Imagem de smiley face, a stareyed face, and an excited faceAbre em uma nova janela

smiley face, a stareyed face, and an excited face
Vocabulary: Shades of Happy

Vamos além do "Happy"?

    Glad: Contente / Satisfeito (Leve).

        "I am glad you came."

    Excited: Empolgado / Animado (Muita energia).

        "I am excited about the trip."

    Delighted: Encantado / Muito feliz.

        "She was delighted with the gift."

Imagem de sad face, a crying face, and a frustrated faceAbre em uma nova janela

sad face, a crying face, and a frustrated face
Vocabulary: Shades of Sad

E se o dia não estiver bom?

    Upset: Chateado (Pode ser tristeza ou leve raiva).

        "Don't be upset."

    Lonely: Solitário (Sentir-se sozinho).

        "I feel lonely when you are away."

    Disappointed: Decepcionado.

        "I was disappointed with the movie."

Imagem de arrow pointing from an object (sun) to a person, causing a smileAbre em uma nova janela
sreenivasaraos.com
arrow pointing from an object (sun) to a person, causing a smile
Structure 2: "It makes me..."

Outra forma de dizer a mesma coisa é focar na causa.

[Coisa/Ação] + makes me + [Adjetivo]

    "Music makes me happy." (A música me faz feliz.)

    "Traffic makes me stressed." (O trânsito me deixa estressado.)

    "You make me smile." (Você me faz sorrir.)

Imagem de person asking a friend What makes you happy?Abre em uma nova janela

person asking a friend What makes you happy?
Asking about Feelings

Para conhecer alguém melhor, pergunte o que move as emoções dela.

    "What makes you happy?" (O que te faz feliz?)

    "What makes you sad/angry?"

    "How does that make you feel?" (Como isso faz você se sentir?)

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Qual a frase correta para dizer que dias ensolarados te deixam feliz?

A) Sunny days make me happy. B) Sunny days makes me happy. C) Sunny days feeling me happy.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é A.

Explicação: "Sunny days" é plural (They), então o verbo não tem 's'.

    It makes me happy.

    They make me happy.

Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase para dizer que ele fica chateado quando perde o jogo.

"He gets ______ when his team loses."

A) glad B) upset C) up
Imagem de person with arms crossed looking angry/sadAbre em uma nova janela

person with arms crossed looking angry/sad
Correção do Desafio

A resposta correta é B.

Explicação: Upset é a palavra perfeita para descrever o sentimento ruim (tristeza/irritação) quando algo dá errado.

Frase: "He gets upset when his team loses."
Imagem de two friends talking on a park benchAbre em uma nova janela

two friends talking on a park bench
Dialogue: Sharing Feelings

Tom: You look smiling today! Jerry: Yes! I feel really happy when the sun is shining. Tom: I agree. Good weather makes me feel energetic. Jerry: And you? How are you? Tom: To be honest, I am a bit upset. Jerry: Why? What happened? Tom: I got a bad grade on my test. It makes me feel disappointed. Jerry: Don't worry. You will do better next time.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Fale sobre o que afeta suas emoções.

"Generally, I am a happy person. I feel happy when I am with my friends. Also, eating good food makes me delighted! But sometimes I feel sad when I watch the news. And traffic makes me really upset. However, listening to music always makes me feel better."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 58, Tema Central: Expressing Feelings: Excited/Bored
Imagem de split screen: On the left, a person yawning (Bored). On the right, a gray, dull book (Boring). An arrow points from the book to the person.Abre em uma nova janela
unfocussed.com
split screen: On the left, a person yawning (Bored). On the right, a gray, dull book (Boring). An arrow points from the book to the person.
Expressing Feelings: Excited/Bored
Social English - Pill 58

Este é um dos erros mais comuns (e às vezes engraçados) que estudantes cometem.

Confundir -ED com -ING pode mudar completamente o sentido da frase. Se você disser "I am boring", você não está dizendo que está entediado, está dizendo que você é uma pessoa chata!

Hoje vamos resolver essa confusão para sempre.
Imagem de diagram showing: CAUSE (Adjective + ING) > EFFECT (Adjective + ED)Abre em uma nova janela

diagram showing: CAUSE (Adjective + ING) > EFFECT (Adjective + ED)
The Golden Rule: -ED vs -ING

A regra é simples:

    -ED (Sentimento): Descreve como você se sente (o efeito em você).

        I am bored. (Estou entediado).

        I am excited. (Estou empolgado).

    -ING (Causa): Descreve a coisa/situação que causa o sentimento.

        The movie is boring. (O filme é chato).

        The game is exciting. (O jogo é empolgante).

Imagem de sleepy person watching a TV with Bla bla bla on the screenAbre em uma nova janela

sleepy person watching a TV with Bla bla bla on the screen
Bored vs. Boring

    Bored: Entediado (Estado temporário).

        "I am bored because I have nothing to do."

    Boring: Chato / Entediante (Característica).

        "This class is so boring."

        Cuidado: Se você disser "I am boring", significa que você não é interessante.

Imagem de fan cheering at a stadium vs a stadium with fireworksAbre em uma nova janela

fan cheering at a stadium vs a stadium with fireworks
Excited vs. Exciting

    Excited: Animado / Empolgado (Seu sentimento).

        "I am so excited about the party!"

    Exciting: Emocionante / Empolgante (A situação).

        "It was an exciting match."

        "New York is an exciting city."

Imagem de battery icon low (Tired) vs a person carrying heavy boxes (Tiring)Abre em uma nova janela

battery icon low (Tired) vs a person carrying heavy boxes (Tiring)
Other Common Pairs

A regra vale para quase todos os adjetivos de emoção:

    Tired vs. Tiring:

        "My job is tiring." (Meu trabalho é cansativo).

        "I am tired." (Estou cansado).

    Interested vs. Interesting:

        "This book is interesting." (Este livro é interessante).

        "I am interested in history." (Estou interessado em história).

Imagem de person with a shocked face vs a scary monsterAbre em uma nova janela

person with a shocked face vs a scary monster
Shocked vs. Shocking

    "The news was shocking." (A notícia foi chocante).

    "I was shocked." (Eu fiquei chocado).

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Você está assistindo a um filme muito ruim e quer reclamar. O que você diz?

A) I am boring. B) The movie is bored. C) The movie is boring.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é C.

Explicação: O filme é a causa do tédio, então usamos -ING. "The movie is boring." (E por causa disso, I am bored).
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Vocabulário

Complete a frase: "O trabalho foi cansativo, então estou cansado."

"The work was ______, so I am ______."

A) tired / tiring B) tiring / tired C) tiring / tiring
Imagem de person sleeping at their deskAbre em uma nova janela

person sleeping at their desk
Correção do Desafio

A resposta correta é B.

Explicação:

    O trabalho (Causa) = Tiring.

    Eu (Sentimento) = Tired.

Frase: "The work was tiring, so I am tired."
Imagem de two friends leaving a cinemaAbre em uma nova janela

two friends leaving a cinema
Dialogue: The Movie Review

Lisa: Well, that was a long movie. Mark: Yes. To be honest, I was a bit bored. Lisa: Me too. The story was very boring. Nothing happened! Mark: I agree. But the special effects were interesting. Lisa: True. Are you hungry? Mark: Yes! I am excited to eat pizza. Lisa: Let's go. It has been a tiring week, we deserve it.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique a diferença entre Causa e Sentimento.

"I had a very tiring day at work. Now, I am completely tired. I tried to read a book, but it was boring. So I got bored and stopped reading. Tomorrow I am going to a concert. It will be exciting! I am really excited to see the band."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 59, Tema Central: Giving Advice (Simple)
Imagem de two friends talking; one looks worried (holding head), the other looks supportive offering a suggestionAbre em uma nova janela

two friends talking; one looks worried (holding head), the other looks supportive offering a suggestion
Giving Advice (Simple)
Social English - Pill 59

Quando um amigo tem um problema, queremos ajudar. Mas não queremos dar ordens ("Faça isso!"), queremos dar um conselho amigo ("Acho que você deveria fazer isso").

Para isso, usamos o Verbo Modal SHOULD.
Imagem de traffic light on Yellow (Caution/Suggestion) vs Red (Prohibition/Must)Abre em uma nova janela

traffic light on Yellow (Caution/Suggestion) vs Red (Prohibition/Must)
The Magic Word: "Should"

Should significa "Deveria". Ele é suave. É uma sugestão, não uma obrigação.

Structure: Subject + SHOULD + Verb (Base)

    Certo: "You should talk to him." (Você deveria falar com ele).

    Errado: ~~You should to talk.~~ (Nunca use "To" depois de should).

    Errado: ~~He shoulds talk.~~ (Nunca mude o modal para "He/She").

Imagem de doctor icon and a bed iconAbre em uma nova janela

doctor icon and a bed icon
Positive Advice (+)

Use para recomendar algo bom.

    "You look sick. You should go to the doctor." (Você parece doente. Deveria ir ao médico.)

    "It is a great movie. You should watch it." (É um ótimo filme. Você deveria assistir.)

    "You should take a break." (Você deveria fazer uma pausa.)

Imagem de cigarette with a prohibited sign over itAbre em uma nova janela

cigarette with a prohibited sign over it
Negative Advice (-)

Use para recomendar que a pessoa não faça algo.

Should + not = Shouldn't

    "You shouldn't smoke." (Você não deveria fumar.)

    "You shouldn't worry so much." (Você não deveria se preocupar tanto.)

    "You shouldn't drink coffee at night."

Imagem de thought bubble cloud saying I think...Abre em uma nova janela

thought bubble cloud saying I think...
Softening the Advice

Para soar ainda mais educado e menos "mandão", comece a frase com "I think..." (Eu acho...).

    "I think you should go home." (Acho que você deveria ir para casa.)

    "I don't think you should do that." (Não acho que você deveria fazer isso - Note que o "don't" vai para o primeiro verbo).

Imagem de large Question MarkAbre em uma nova janela

large Question Mark
Asking for Advice

E se você é quem tem o problema?

"What should I do?" (O que eu deveria fazer?)

    Scenario: "I lost my wallet. What should I do?"

    Scenario: "Do you think I should call her?"

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Exercício 1

Seu amigo está com dor de dente. Qual o conselho correto?

A) You should to go to the dentist. B) You should go to the dentist. C) You must going to the dentist.
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Exercício 1

A resposta correta é B.

Explicação: Verbos modais como Should são seguidos pelo verbo na forma base, sem o TO. "You should go..."
Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Estrutura

Complete a frase para dar um conselho negativo. Está chovendo, não saia.

"It is raining. You ______ go out now."

A) don't should B) should no C) shouldn't
Imagem de person looking out at the rain through a windowAbre em uma nova janela

person looking out at the rain through a window
Correção do Desafio

A resposta correta é C.

Explicação: A negativa de should é Shouldn't (Should not). Nunca usamos "don't" com modais.

Frase: "You shouldn't go out now."
Imagem de two colleagues talking in an office break roomAbre em uma nova janela

two colleagues talking in an office break room
Dialogue: The Problem

Jess: I am so tired today. I can't focus on my work. Ben: Oh no. What happened? Jess: I stayed up late watching TV. Ben: Well, you shouldn't watch TV until 3 AM! Jess: I know. What should I do now? Ben: I think you should drink some coffee. Jess: Good idea. Ben: And tonight, you should go to bed early.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Review for Audio

Pratique dar conselhos para diferentes situações.

"You have a headache? I think you should take an aspirin. And you shouldn't look at your phone screen. You should close your eyes and rest. Are you hungry? You should eat something healthy. You shouldn't eat fast food every day."

Envie ao seu professor!

###

Trilha: 8. Social English, Nível: Pre-Intermediate, Pílula #: 60, Tema Central: Final Review: Social Story
Imagem de person holding a photo album or a smartphone showing travel photos to a group of friendsAbre em uma nova janela

person holding a photo album or a smartphone showing travel photos to a group of friends
Final Review: Social Story
Social English - Pill 60

Parabéns! Você chegou à pílula 60.

Nas últimas 20 aulas, aprendemos a falar sobre o passado, viagens, sentimentos, planos futuros e dar conselhos.

Hoje, não vamos aprender nada novo. Vamos consolidar. O objetivo final do nível Pre-Intermediate é conseguir contar uma história com começo, meio e fim. Vamos montar a sua História de Férias.
Imagem de timeline roadmap: 1. Destination > 2. Transport > 3. Activities > 4. Opinion > 5. AdviceAbre em uma nova janela
medium.com
timeline roadmap: 1. Destination > 2. Transport > 3. Activities > 4. Opinion > 5. Advice
The Story Arc (O Arco da História)

Para não se perder na conversa, siga este roteiro mental de 5 passos:

    Intro: Onde e quando você foi? (Past Simple).

    Journey: Como você chegou lá? (Transport).

    Action: O que você fez? (Sightseeing).

    Feeling: Como foi? (Opinions & Feelings).

    Closing: Recomendação (Advice).

Imagem de passport stamped and a plane ticketAbre em uma nova janela

passport stamped and a plane ticket
Part 1: Logistics (Where & How)

Use o Simple Past e as preposições de transporte.

    "Last month, I traveled to Bahia."

    "I went by plane because it is faster."

    "I stayed at a small hotel near the beach."

Review: Lembra da diferença? I went by car vs I went in my car.
Imagem de collage: Person swimming, eating food, and taking a selfieAbre em uma nova janela

collage: Person swimming, eating food, and taking a selfie
Part 2: Highlights (What did you do?)

Use verbos de ação no passado.

    "I went sightseeing in the old town."

    "I took a lot of photos."

    "I bought souvenirs for my family."

    "I ate the local food. It was delicious."

Imagem de person smiling (Happy) and a thumbs up icon (Good)Abre em uma nova janela

person smiling (Happy) and a thumbs up icon (Good)
Part 3: The Vibe (How was it?)

Misture opiniões sobre o lugar e seus sentimentos.

    "The trip was amazing."

    "I felt very relaxed."

    "The city was a bit crowded, but interesting."

    "I was sad when I had to leave."

Review: Cuidado! The trip was tiring (cansativa) vs I was tired (cansado).
Imagem de speech bubble with a lightbulb idea insideAbre em uma nova janela

speech bubble with a lightbulb idea inside
Part 4: The Recommendation (Advice)

Feche a história dizendo ao seu amigo o que ele deve fazer.

    "You should go there one day."

    "You should try the fish restaurant."

    "You shouldn't go in December because it rains."

Imagem de multiple choice quiz layout on a tabletAbre em uma nova janela
twinreality.in
multiple choice quiz layout on a tablet
Vamos Praticar? - Quiz Final

Complete a história com as palavras corretas:

"I ______ to London last year. The city is beautiful but very ______."

A) go / expensive B) went / expensive C) went / excited
Imagem de bright green checkmark indicating the correct answerAbre em uma nova janela

bright green checkmark indicating the correct answer
Correção - Quiz

A resposta correta é B.

Explicação:

    Passado de Go = Went.

    Adjetivo para cidade (coisa) = Expensive (Cara). Excited seria um sentimento de pessoa.

Imagem de sentence completion puzzleAbre em uma nova janela
wordmint.com
sentence completion puzzle
Desafio de Estrutura

Coloque a frase na ordem para dar um conselho final.

[ visit / should / definitely / you / place / that ]

A) You should definitely visit that place. B) You definitely visit should that place. C) Should you visit definitely place that.
Imagem de tourist pointing at a map recommending a spotAbre em uma nova janela

tourist pointing at a map recommending a spot
Correção do Desafio

A resposta correta é A.

Explicação: Ordem: Sujeito (You) + Modal (should) + Advérbio (definitely) + Verbo (visit) + Objeto.

Frase: "You should definitely visit that place."
Imagem de two friends chatting over coffeeAbre em uma nova janela

two friends chatting over coffee
Full Simulation: The Conversation

Veja como todas as peças se encaixam:

Friend: Hey! How was your vacation? You: It was wonderful! I went to Rio de Janeiro. Friend: Nice! Did you go by car? You: No, I went by bus. It was cheaper. Friend: And what did you do there? You: I went sightseeing. I visited Christ the Redeemer and took many photos. Friend: Was it expensive? You: A little bit. And the beaches were crowded. But I felt very happy. Friend: I want to go next year. You: You should go! You will love it.
Imagem de microphone icon aimed at the userAbre em uma nova janela
pngtree.com
microphone icon aimed at the user
Consolidated Audio Task

Esta é a sua missão final do nível Pre-Intermediate.

Grave um áudio de 30 a 60 segundos contando sobre sua última viagem (ou uma viagem inventada). Você deve incluir:

    Destino e Meio de Transporte.

    Onde ficou hospedado.

    Duas coisas que você fez (atividades).

    Como você se sentiu.

    Uma recomendação usando "Should".

Roteiro Sugerido: "Last summer, I traveled to... I went by... and I stayed at... During the day, I... and I... The trip was... and I felt... If you like travel, you should..."
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