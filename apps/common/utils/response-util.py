from flask import request, jsonify, Response, make_response
import urllib.parse

class ResponseUtil:
    """
    Author: 김대광
    """

    _is_null = "{} is null"
    _is_null_or_empty = "{} is null or empty"

    @classmethod
    def get_encoded_file_name(cls, file_name: str) -> str:
        """브라우저에 따른 파일명 인코딩 설정 (Content-Disposition 값 생성)

        Args:
            file_name (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """

        if not file_name or not file_name.strip():
            raise ValueError(cls._is_null_or_empty.format("file_name"))
        
        # URL 인코딩 (공백은 %20으로 처리)
        return urllib.parse.quote(file_name)
    
    @classmethod
    def set_content_disposition(cls, response: Response, file_name: str) -> Response:
        """브라우저별로 최적화된 파일 다운로드 응답 헤더를 설정

        Args:
            response (Response): _description_
            file_name (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            Response: _description_
        """

        if not response:
            raise ValueError(cls._is_null.format("response"))
        
        if not file_name or not file_name.strip():
            raise ValueError(cls._is_null_or_empty.format("file_name"))
        
        user_agent = request.headers.get('User-Agent', '')

        encoded_file_name = cls.get_encoded_file_name(request, file_name)

        response.headers['Content-Transfer-Encoding'] = 'binary'

        # IE / Edge (Old) 대응 및 최신 브라우저 대응
        if 'MSIE' in user_agent or 'Trident' in user_agent:
            response.headers['Content-Disposition'] = f'attachment; filename="{encoded_file_name}"'
        else:
            # 최신 브라우저는 RFC 5987 규격(filename*) 사용
            response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_file_name}"

        return response
    
    @classmethod
    def get_json_response(cls, message: str) -> Response:
        """JSON 응답 객체 반환

        Args:
            message (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            Response: _description_
        """

        if not message or not message.strip():
            raise ValueError(cls._is_null_or_empty.format("message"))
        
        return jsonify({"message": message})