from fatetime import datetime
from sqlachemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# Cria um registry, a variavel pode ter qualquer nome
table_registry = registry()


# esse table_registry mapped as dataclass serve para mostrar ao db q esta
# classe é a tabela users já definida
# e O @table_registry.mapped_as_dataclass regista a classe Python como uma
# tabela do banco de dados no SQLAlchemy e gera automaticamente o método
# __init__ para criar objetos facilmente.
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    # Mapped serve para converter os valores do python para os
    # equivalentes em sql, e mapped_column serve para definir coisas
    # especificas a aquela coluna, init=False serve para quando for criar
    # um usuario nao precise definir o item marcado como init=False.
    # Primary key é o identificador de cada registro em um banco de dados.
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        # func serve para executar comandos sql dentro do python, now serve
        # para capturar e retornar a data e a hora exatas do momento atual em
        # que o comando é executado no banco de dados
        init=False,
        server_default=func.now(),
    )
