import time
from datetime import datetime, timedelta


def simular_chargegrid():
    print("=" * 50)
    print("     CHARGEGRID INTELLIGENCE - SIMULADOR PoC     ")
    print("=" * 50)


    DEMANDA_CONTRATADA = 150.0
    CONSUMO_ATUAL_PREDIO = 95.0
    POTENCIA_MAX_CARREGADOR = 22.0
    VALOR_KWH_NORMAL = 0.85
    VALOR_KWH_PICO = 1.40
    TAXA_OCIOSIDADE_MINUTO = 0.50

    print(f"Status do Prédio: Consumo Atual = {CONSUMO_ATUAL_PREDIO}kW | Limite = {DEMANDA_CONTRATADA}kW")
    print(f"Margem disponível para carregadores: {DEMANDA_CONTRATADA - CONSUMO_ATUAL_PREDIO}kW\n")


    try:
        soc_atual = float(input("Digite a porcentagem ATUAL da bateria do VE (0-100): "))
        soc_desejado = float(input("Digite a porcentagem DESEJADA da bateria (0-100): "))
        capacidade_bateria = float(input("Digite a capacidade total da bateria do VE (em kWh, ex: 60): "))
        tempo_permanencia_horas = float(input("Quantas horas o veículo ficará estacionado? (ex: 2): "))
    except ValueError:
        print("\n[Erro] Por favor, insira apenas números válidos.")
        return

    energia_necessaria_kwh = ((soc_desejado - soc_atual) / 100) * capacidade_bateria

    if energia_necessaria_kwh <= 0:
        print("\nO veículo já possui a carga desejada ou um valor superior.")
        return

    tempo_minimo_recarga_horas = energia_necessaria_kwh / POTENCIA_MAX_CARREGADOR

    print("\n" + "-" * 30)
    print("ANALISANDO PRIORIDADE VIA IA...")
    time.sleep(1)

    if tempo_permanencia_horas <= (tempo_minimo_recarga_horas * 1.2):
        prioridade = "ALTA"
        potencia_alocada = POTENCIA_MAX_CARREGADOR
    else:
        prioridade = "BAIXA"
        potencia_alocada = POTENCIA_MAX_CARREGADOR * 0.6

    consumo_futuro_total = CONSUMO_ATUAL_PREDIO + potencia_alocada

    if consumo_futuro_total > DEMANDA_CONTRATADA:
        print("\n[ALERTA] Risco de sobrecarga detectado! Ativando controle dinâmico.")
        potencia_alocada = DEMANDA_CONTRATADA - CONSUMO_ATUAL_PREDIO
        print(f"-> Potência do carregador limitada dinamicamente para: {potencia_alocada:.2f} kW")
        tempo_minimo_recarga_horas = energia_necessaria_kwh / potencia_alocada
    else:
        print(f"-> Rede estável. Potência alocada: {potencia_alocada:.2f} kW (Prioridade: {prioridade})")

    hora_atual = datetime.now().hour
    if 18 <= hora_atual <= 21:
        custo_energia = energia_necessaria_kwh * VALOR_KWH_PICO
        tipo_tarifa = "Tarifa de Pico (Mais cara)"
    else:
        custo_energia = energia_necessaria_kwh * VALOR_KWH_NORMAL
        tipo_tarifa = "Tarifa Normal (Econômica)"
    print("\n" + "-" * 30)
    print("SIMULANDO FIM DA SESSÃO DE RECARGA...")
    time.sleep(1)
    minutos_atraso = 15
    custo_ociosidade = minutos_atraso * TAXA_OCIOSIDADE_MINUTO
    custo_total = custo_energia + custo_ociosidade

    print("\n==================================================")
    print("            RECIBO DE RECARGA - GOODWE            ")
    print("==================================================")
    print(f"Energia Entregue:........ {energia_necessaria_kwh:.2f} kWh")
    print(f"Tempo de Recarga Ativo:.. {tempo_minimo_recarga_horas:.2f} horas")
    print(f"Modelo de Tarifação:..... {tipo_tarifa}")
    print(f"Custo da Energia:........ R$ {custo_energia:.2f}")
    print(f"Tempo Ocioso na Vaga:.... {minutos_atraso} minutos")
    print(f"Taxa de Ocupação Ociosa:. R$ {custo_ociosidade:.2f}")
    print("-" * 50)
    print(f"VALOR TOTAL A PAGAR:..... R$ {custo_total:.2f}")
    print("==================================================")


if __name__ == "__main__":
    simular_chargegrid()
