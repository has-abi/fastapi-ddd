import logging
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session, declarative_base

from src.settings import Settings

logger = logging.getLogger(__name__)

Base = declarative_base()

engine = create_engine(Settings().DATABASE_URL, echo=True)


class Database:
    def __init__(self) -> None:
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=engine,
            ),
        )

    @contextmanager  # type: ignore
    def session(self) -> Callable[..., AbstractContextManager[Session]]:  # type: ignore
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
