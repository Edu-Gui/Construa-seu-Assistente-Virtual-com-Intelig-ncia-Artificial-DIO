from src.agent import load_data, local_answer, summary

DATA = load_data()

def test_summary():
    s = summary(DATA)
    assert s["entradas"] == 5000
    assert abs(s["saidas"] - 2488.9) < 0.001
    assert abs(s["saldo"] - 2511.1) < 0.001

def test_gastos_with_source():
    result, source = local_answer("Quais foram meus gastos?", DATA)
    assert "2.488,90" in result
    assert source == "data/transacoes.csv"

def test_reserva():
    result, source = local_answer("Quanto falta para minha reserva?", DATA)
    assert "5.000,00" in result
    assert source == "data/perfil_investidor.json"

def test_unknown_question_does_not_fabricate():
    result, source = local_answer("Qual é a cotação do dólar agora?", DATA)
    assert "informação suficiente" in result
    assert "insuficiente" in source

def test_prohibit_actions():
    result, _ = local_answer("Pode transferir dinheiro para mim?", DATA)
    assert "nem realizo operações" in result.lower()

def test_products_are_historical():
    result, _ = local_answer("Quais produtos tenho?", DATA)
    assert "não são taxas" in result.lower()
