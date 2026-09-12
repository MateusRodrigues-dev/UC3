class ProcessadorDePagamento:
    
    def _conectar_banco(self):
        self._conectar_banco = _conectar_banco
        print("Conectando ao banco de dados...")
    
    def _autenticar_token(self):
        self._autenticar_token = _autenticar_token
        print("Autenticando transação")
    
    def _deduzir_saldo(self,valor):
        self._deduzir_saldo = _deduzir_saldo
        self.valor = valor 
        print("Deduzindo R$ [valor] do saldo...")
    
    def _processar_compra(self,valor):
        self._processar_compra = _processar_compra
        self.valor = valor 
        print("Compra finalizada com sucesso")

