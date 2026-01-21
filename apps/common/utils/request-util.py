from flask import request

class RequestUtil:
    """
    Author: 김대광
    """

    @staticmethod
    def get_request_ip_address() -> str:
        """IP 주소 가져오기

        Returns:
            str: _description_
        """

        x_forwarded_for = request.headers.get('X-Forwarded-For')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.remote_addr

        return ip
    
    @staticmethod
    def get_request_domain() -> str:
        """포트와 컨텍스트 경로를 포함한 전체 베이스 URL 가져오기

        Args:
            request (HttpRequest): _description_

        Returns:
            str: _description_
        """
        
        return request.host_url.rstrip('/')
    
    @staticmethod
    def get_base_domain() -> str:
        """기본 도메인 가져오기 (포트 미포함, 호스트명만)

        Args:
            request (HttpRequest): _description_

        Returns:
            str: _description_
        """

        scheme = request.is_secure and "https" or "http"
        host = request.host.split(':')[0]

        return f"{scheme}://{host}"
    
    @staticmethod
    def get_browser_info() -> str:
        """브라우저 User-Agent 가져오기

        Args:
            request (HttpRequest): _description_

        Returns:
            str: _description_
        """
        
        user_agent = request.headers.get('User-Agent', 'User-Agent 정보 없음')
        return user_agent
