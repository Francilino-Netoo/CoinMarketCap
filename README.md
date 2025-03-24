# WebSocket Scraping com Python

#### Este projeto realiza scraping de dados em tempo real utilizando WebSocket para capturar informações do mercado de criptomoedas.

## Tecnologias Utilizadas
- Python
- WebSocket (biblioteca websocket-client)
- JSON para manipulação dos dados
- Colorama para saída colorida no terminal
- OS para compatibilidade com Windows
- Time para controle de tempo de reconexão

## Instalação

#### Instale as dependências necessárias com o seguinte comando:
```
pip install -r requirements.txt
```

## Como Funciona
#### O script conecta-se ao WebSocket do CoinMarketCap e escuta atualizações de preços em tempo real. Ele filtra e exibe dados de criptoativos específicos, como Bitcoin (ID: 1975).

## Estrutura dos Dados Recebidos
#### O WebSocket envia mensagens JSON com a seguinte estrutura:
```
{
  "d": {
    "id": 1975,
    "p": "Preço Atual",
    "p24h": "Variação 24h",
    "p7d": "Variação 7 dias",
    "p30d": "Variação 30 dias",
    "p3m": "Variação 3 meses",
    "p1y": "Variação 1 ano",
    "pytd": "Variação YTD",
    "pall": "Preço Histórico Máximo",
    "as": "Oferta Circulante",
    "mc": "Market Cap",
    "fmc24hpc": "Mudança Percentual Market Cap 24h"
  },
  "t": "Timestamp",
  "c": "Canal de Origem"
}
```
## Para rodar o scraper, utilize o seguinte comando:
```
python scraping.py
```
#### O script irá conectar-se ao WebSocket, aguardar mensagens e exibir no terminal os preços e variações das criptomoedas monitoradas. Se a conexão for perdida, o script tenta reconectar automaticamente.

## Funções Principais
- conectar_websocket(): Estabelece a conexão WebSocket e inicia a escuta de mensagens.
- on_message(ws, message): Processa cada mensagem recebida e chama as funções valor1() e valor2() para extrair informações das criptomoedas monitoradas.
- on_open(ws): Envia uma mensagem de assinatura ao WebSocket para receber as atualizações desejadas.
- on_close(ws, close_status_code, close_msg): Aguarda um tempo e tenta reconectar em caso de desconexão.
- valor1(ws, message) e valor2(ws, message): Filtram e extraem os dados relevantes das mensagens JSON, verificando se o ID da cripto corresponde aos ativos monitorados.

## Observações
- Certifique-se de ter uma conexão estável com a internet para evitar falhas frequentes na conexão com o WebSocket.
- O script pode ser adaptado para monitorar outras criptomoedas, basta modificar os IDs filtrados.
- A origem e referência do WebSocket são definidas para evitar bloqueios de requisição.

##### Este projeto é uma ferramenta simples e eficaz para acompanhar variações de preços de criptomoedas em tempo real, podendo ser ampliado para incluir mais ativos e funcionalidades.