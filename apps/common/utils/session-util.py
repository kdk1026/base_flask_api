from flask import session
from typing import Any, Optional

class SessionUtil:
    """
    Author: 김대광
    """

    _is_null = "{} is null"
    _is_null_or_empty = "{} is null or empty"
    _is_negative = "{} is negative"

    @classmethod
    def set_attribute(cls, key: str, value: Any, timeout: Optional[int] = None) -> None:
        """세션에 데이터 저장

        Args:
            key (str): _description_
            value (Any): _description_
            timeout (Optional[int], optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """

        if not key or not key.strip():
            raise ValueError(cls._is_null_or_empty.format("key"))
        
        if value is None:
            raise ValueError(cls._is_null.format("value"))
        
        session[key] = value

        if timeout is not None:
            if timeout < 1:
                raise ValueError(cls._is_negative.format("timeout"))
            session.permanent = True
    
    @classmethod
    def get_attribute(cls, key: str) -> Any:
        """세션에서 데이터 가져오기

        Args:
            key (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            Any: _description_
        """

        if not key or not key.strip():
            raise ValueError(cls._is_null_or_empty.format("key"))
        
        return session.get(key)
    
    @classmethod
    def remove_attribute(cls, key: str) -> None:
        """특정 세션 키 삭제

        Args:
            key (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        if not key or not key.strip():
            raise ValueError(cls._is_null_or_empty.format("key"))
        
        session.pop(key, None)

    @staticmethod
    def clear_all() -> None:
        """모든 세션 데이터 삭제
        """
        session.clear()