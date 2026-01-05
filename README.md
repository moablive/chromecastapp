# Chromecast Manager 📺

Aplicação web para gerenciar dispositivos Chromecast na rede local via interface HTML.

## 🚀 Características

- Controle de Chromecast via rede local
- Interface web intuitiva
- Autenticação administrativa
- Containerizado com Docker

## 📋 Pré-requisitos

- Docker
- Docker Compose
- Chromecast na mesma rede local

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/moablive/chromecastapp.git
cd chromecastapp
```

### 2. Configure as credenciais de administrador

Edite o arquivo `docker-compose.yml` e defina suas credenciais:

```yaml
environment:
  - ADMIN_USER=seu_usuario
  - ADMIN_PASSWORD=sua_senha_segura
```

**⚠️ IMPORTANTE**: Altere as credenciais padrão antes de executar em produção!

## 🐳 Execução com Docker

### Iniciar o serviço

```bash
docker-compose up -d
```

### Parar o serviço

```bash
docker-compose down
```

### Ver logs

```bash
docker-compose logs -f
```

## 🌐 Acesso

Após iniciar o container, acesse:

```
http://localhost:5000
```

ou

```
http://SEU_IP_LOCAL:5000
```

## 📁 Estrutura do Projeto

```
.
├── app.py                 # Aplicação principal Flask
├── Dockerfile            # Imagem Docker
├── docker-compose.yml    # Configuração Docker Compose
└── templates/            # Templates HTML
```

## 🔒 Segurança

- Sempre altere as credenciais padrão
- Use senhas fortes
- Mantenha o Docker atualizado
- Execute apenas em redes confiáveis

## 🛠️ Desenvolvimento

Para executar localmente sem Docker:

```bash
pip install -r requirements.txt
python app.py
```

## 📝 Licença

Este projeto é de código aberto.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

Desenvolvido com ❤️ para facilitar o controle de Chromecast
