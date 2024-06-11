# Como usar o script:
Este guia explica como usar o script convert_trader_config.py para converter o arquivo TraderConfig.txt para o formato TraderPlusPriceConfig.json esperado pelo mod TraderPlus.

## Passos para usar o script:
Salve o script como convert_trader_config.py:

Prepare o arquivo TraderConfig.txt:

Certifique-se de que o arquivo TraderConfig.txt está no mesmo diretório que o script convert_trader_config.py. Caso contrário, ajuste o caminho do arquivo no script.
Execute o script usando Python:

Abra o terminal ou prompt de comando.
Navegue até o diretório onde o script e o arquivo TraderConfig.txt estão localizados.
Execute o seguinte comando:
sh
```
$ python convert_trader_config.py
```
Resultado:
O script irá gerar um arquivo chamado TraderPlusPriceConfig.json no mesmo diretório. Esse arquivo conterá as configurações convertidas no formato esperado pelo mod TraderPlus.
Exemplo de execução:
```
$ python convert_trader_config.py
```
Conversão completa. JSON salvo em TraderPlusPriceConfig.json
Observações:
Certifique-se de ter o Python instalado em seu sistema.
Caso encontre problemas, verifique se o arquivo TraderConfig.txt está no formato esperado e se não há erros de sintaxe no script.
