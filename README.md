# Fast-API - Aprendo sobre Fast API

## Instalaçao
Necessário instalar a biblioteca <strong>Fast API.</strong>
  ```sh
  pip install fastapi 
  ```
Necessário instalar servidor local <strong>Unicorn</strong>
  ```sh
  pip install unicorn 
  ```
### GET HOME
```
http://127.0.0.1:8000/
```
### REQUEST
```
{
  "Vendas": 4
}
```
![Captura de tela de 2023-05-09 22-53-50](https://github.com/diegomarqueszs/Fast-API/assets/90580148/da79f4eb-d4d3-442d-a0ab-4f544fd5c294)

---

### GET VENDAS
```
http://127.0.0.1:8000/vendas/{id_vendas}?id_venda=1
```
### REQUEST
```
{
  "item": "lata",
  "preco-unitario": 4,
  "quantidade": 5
}
```
![Captura de tela de 2023-05-09 22-56-03](https://github.com/diegomarqueszs/Fast-API/assets/90580148/34be67d8-fdbf-404f-a03b-776fb92d2cc0)
