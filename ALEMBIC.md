# Alembic — guia rápido

O Alembic é a ferramenta de **migrations** do SQLAlchemy: ele guarda o histórico
de mudanças na **estrutura** do banco (tabelas, colunas, índices...) e aplica
essas mudanças em ordem, como se fosse um "git do banco de dados".

> Todos os comandos abaixo rodam na raiz do projeto. Se o ambiente virtual do
> Poetry não estiver ativado, coloque `poetry run` na frente
> (ex.: `poetry run alembic upgrade head`).

---

## Como está configurado neste projeto

| Arquivo | Para que serve |
|---|---|
| `alembic.ini` | Configuração geral (pasta das migrations, logs...). |
| `migrations/env.py` | Liga o Alembic ao projeto: pega a URL do banco de `Settings().DATABASE_URL` (arquivo `.env`) e os models de `table_registry.metadata`. |
| `migrations/versions/` | Uma migration por arquivo. Cada uma tem `upgrade()` (aplicar) e `downgrade()` (desfazer). |
| `migrations/script.py.mako` | Modelo usado para gerar novos arquivos de migration. |

> A linha `sqlalchemy.url` do `alembic.ini` é ignorada: o `env.py` sobrescreve
> com o `DATABASE_URL` do `.env`.

---

## Fluxo do dia a dia

```bash
# 1. Altere os models em fastapi_zero/models.py

# 2. Gere a migration com a diferença entre os models e o banco
alembic revision --autogenerate -m "add is_active to users"

# 3. ABRA E REVISE o arquivo gerado em migrations/versions/

# 4. Aplique no banco
alembic upgrade head

# 5. Faça commit do model + da migration juntos
```

---

## Comandos principais

### Criar migrations

```bash
# Gera a migration comparando os models com o banco (o mais usado)
alembic revision --autogenerate -m "mensagem"

# Gera uma migration vazia, para escrever na mão
# (útil para migrar dados ou fazer algo que o autogenerate não detecta)
alembic revision -m "mensagem"
```

### Aplicar migrations

```bash
alembic upgrade head        # aplica todas as pendentes (até a mais recente)
alembic upgrade +1          # aplica só a próxima
alembic upgrade <revision>  # aplica até uma revisão específica (ex.: c676ed5834cf)
```

### Desfazer migrations

```bash
alembic downgrade -1          # desfaz a última
alembic downgrade <revision>  # volta até uma revisão específica
alembic downgrade base        # desfaz TODAS (banco fica sem tabelas)
```

### Consultar o estado

```bash
alembic current             # em qual migration o banco está agora
alembic history             # lista todas as migrations
alembic history --verbose   # lista com detalhes
alembic heads               # mostra a(s) migration(s) mais recente(s)
alembic check               # avisa se há mudanças nos models sem migration
```

### Ver o SQL sem executar

```bash
alembic upgrade head --sql  # imprime o SQL que seria rodado (modo offline)
```

---

## Anatomia de uma migration

```python
revision = 'c676ed5834cf'  # id desta migration
down_revision = None  # id da anterior (None = primeira)


def upgrade() -> None:  # o que fazer ao aplicar
    op.create_table('users', ...)


def downgrade() -> None:  # como desfazer
    op.drop_table('users')
```

O `down_revision` encadeia as migrations: `None → c676ed5834cf → próxima → ...`.
O banco guarda em qual elo está na tabela `alembic_version`.

---

## Cuidados (sempre revise o que o autogenerate gerou!)

- **Renomear coluna/tabela:** o autogenerate entende como *apagar + criar* e
  **perde os dados**. Troque manualmente por
  `op.alter_column('users', 'antigo', new_column_name='novo')`.
- **Coluna obrigatória em tabela com dados:** sem valor padrão o `upgrade` falha.
  Use `server_default` no model (ex.: `server_default='1'`).
- **Nem tudo é detectado:** algumas mudanças de tipo e de `server_default`
  podem passar despercebidas.
- **SQLite:** tem `ALTER TABLE` limitado. Para alterar/remover colunas, ative o
  batch mode no `migrations/env.py`:
  ```python
  context.configure(
      connection=connection,
      target_metadata=target_metadata,
      render_as_batch=True,
  )
  ```
- **Dados não migram sozinhos:** a migration cuida da estrutura. Transformar
  dados existentes é código que você escreve dentro do `upgrade()`.
- **Nunca edite uma migration que já foi aplicada** em outro banco (de outra
  pessoa ou de produção). Crie uma nova migration corrigindo.
- **Teste `upgrade` e `downgrade`** localmente antes de aplicar em um banco com
  dados reais.

---

## Quando NÃO precisa de migration

Mudanças que não afetam as tabelas: rotas novas, schemas Pydantic, validações,
regras de negócio etc. Só precisa de migration quando `models.py` muda.
