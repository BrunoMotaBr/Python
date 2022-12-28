from collections import defaultdict
from collections import Counter

usuarios_data_science = [15,23,43,56]
usuarios_machine_learning = [13,23,56,42]

assistiram = []
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(set(assistiram))#Conjutos não repete os dados#
for usuario in set(assistiram):
    print(usuario)

usuarios2 = {
    "Bruno": 2,
    "Joao": 3,
    "José": 4,
    "Bruna": 5,
}
usuarios3 = defaultdict(int)
palavras = "No duelo entre duas seleções que estão entre as favoritas ao título da Eurocopa Feminina, a Alemanha venceu a Espanha por 2 a 0, em Londres, e garantiu na segunda rodada uma das vagas do Grupo B para as quartas de final da competição, em primeiro lugar na chave. Outra seleção já garantida na próxima fase é a Inglaterra, líder do Grupo A."
print(Counter(palavras.split()))

texto1 = """
Nosso blog agora está de cara "nova".
 Na verdade, é apenas uma repaginada no layout para unificar com o layout de nosso site principal. Há muito tempo que precisávamos abandonar o tema padrão do wordpress!
Esta nova cara vem para celebrar o 
sucesso que o blog vem alcançando ultimamente. Começamos a experiência um ano atrás e a blogar pra valer mesmo a partir de agosto de 2006. A receptividade tem sido muito grande! Até hoje publicamos 42 artigos e recebemos mais de 240 comentários, uma excelente média.
O sucesso do blog é tamanho que 
recebemos milhares de visitantes todos os meses. Muitos vêm direto ao blog através do Google (que pelo jeito adora nossos artigos) e talvez não percebessem que o blog é da Caelum. Este novo tema tenta situar melhor o visitante no nosso site e aproveita para melhorar a usabilidade do blog (agora os artigos 
são mostrados na página toda, sem barra lateral, para facilitar a leitura!).
Esperamos que gostem do blog, do novo tema, dos artigos aqui publicados e que voltem sempre (e comentem!).
"""
texto2 = """Quais são os desafios de grupos minorizados na hora de ingressar no mercado 
de trabalho de tecnologia? Que transformação é necessária dentro das empresas para 
receber estes grupos e fortalecer de fato a diversidade na cultura organizacional? 
No dia 30 de junho, a Alura promoveu um debate para responder essas e outras perguntas 
ligadas ao tema Recrutamento e Carreira em Tecnologia para pessoas LGBTQIA+, na sede da 
Google For Startups.
A mediadora e tech recruiter Ana Ribeiro, instrutora da escola de Inovação e Gestão da 
Alura, conversou com Alejandra Yacovodonato, diretora da Fly Educação, com Noah Scheffel, 
CEO da Educa TRANSforma e com Mayara Gonçalves, Diretora de Pessoas e Cultura da Letrus.
Confira a seguir alguns highlights dessa conversa em prol da inclusão, ou assista à 
gravação da Live no canal da Alura.."""



