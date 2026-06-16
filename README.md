SPRINT 2 PYTHON

INTEGRANTES:
Kethelyn de Oliveira Rocha
RM:574016

Anna Luiza Carvalhaes 
RM:573330

Gabriela Batista
RM:573583

Samara Carvalho
RM:573666

Video Demonstração: https://youtu.be/v8lsIHF_daE

 Contexto e Conceito

A GoodWe está expandindo seu portfólio de energia limpa (solar e armazenamento) para o mercado comercial de Veículos Elétricos (VEs) com o ChargeGrid. Trata-se de um ecossistema baseado em IA e IoT que transforma carregadores comuns em hubs inteligentes, gerenciando a recarga de forma integrada à geração solar local e à rede elétrica.

Residencial: Baixa complexidade, focado em menor tempo ou tarifa mais barata.
Comercial: Altíssima complexidade. Exige gerenciamento de dezenas de carregadores simultâneos para evitar multas de ultrapassagem de demanda, controlar múltiplos usuários e realizar split de pagamentos.

 Os 4 Pilares do Desafio

1. Controle de Demanda (*Dynamic Load Balancing*): Regular a potência dos carregadores em tempo real para não estourar o limite elétrico do prédio, evitando quedas de energia e multas.
2. Protocolos Abertos (Interoperabilidade):Uso do padrão global **OCPP** para garantir que o software gerencie hardwares de marcas diferentes, evitando o bloqueio a um único fornecedor (*Vendor Lock-in*).
3. Tarifação e Pagamento (Monetização):Automação de cobranças por kWh, horário e tempo de vaga, garantindo conformidade fiscal e repasse correto aos comércios.
4. Uso de Inteligência Artificial: Algoritmos preditivos para otimizar os ciclos de carga (baseado no histórico e previsão do tempo), mitigando o risco de deixar frotas sem bateria.

  Problemas e Soluções em Destaque

 Sobrecarga da Rede Comercial                                                                                                                                      Solução: Peak Shavingnteligente via IA: Ao aproximar-se do limite elétrico contratado, a IA reduz a potência de carros com maior tempo de permanência ou aciona as baterias GoodWe para suprir o pico.
Vagas Bloqueadas por Carros Já Carregados                                                                                                                   Solução: Tarifa de Ocupação Ociosa Dinâmica: O motorista informa o horário de saída pelo app. Se o carro carregar antes e continuar na vaga após o horário tolerado, o sistema inicia uma cobrança por minuto ocioso.

Aplicação do Pensamento Computacional

Decomposição:Divisão da expansão comercial em subproblemas (Hardware/Grid, Comunicação, Financeiro e IA).
Reconhecimento de Padrões: Identificação de horários de pico em ambientes comerciais (ex: 11h às 14h em shoppings).
Abstração: Foco apenas nos dados vitais do veículo (Estado da Carga, kWh da bateria e potência aceita), ignorando marca ou cor.

 Conclusão

O ChargeGrid Intelligence viabiliza a transição para a mobilidade elétrica comercial ao pensar a infraestrutura de forma sistêmica. Unindo energia solar, armazenamento e inteligência de dados, o sistema protege a rede elétrica e gera um modelo de negócios altamente rentável e sustentável.

 O que esse código faz?
 
Esse script simula o funcionamento do ChargeGrid Intelligence na vida real. Ele funciona como o "cérebro" de um carregador inteligente da GoodWe instalado em um local como um shopping. O objetivo dele é equilibrar três coisas: a pressa do motorista, a conta de energia e a segurança da rede elétrica do prédio. 
é um código feito para garantir que o carro carregue com segurança, sem derrubar a energia do shopping e cobrando o valor justo de cada um.
