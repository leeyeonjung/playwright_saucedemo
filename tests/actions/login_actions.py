import logging
from tests.locator import login_locators

logger = logging.getLogger(__name__)


class LoginActions:
    """로그인 페이지 관련 액션 클래스"""
    
    def __init__(self, page):
        """LoginActions 초기화
        
        Args:
            page: Playwright 페이지 객체
        """
        self.page = page
        logger.debug(f"LoginActions 초기화 완료")

    def load(self):
        """로그인 페이지 로드"""
        logger.info("로그인 페이지 로드 시작")
        self.page.goto("/")
        logger.info("로그인 페이지 로드 완료")


    def login(self, username: str, password: str):
        """로그인 수행
        
        Args:
            username: 사용자명
            password: 비밀번호
        """
        logger.info(f"로그인 시도: username={username}")
        self.page.locator(login_locators.USERNAME_INPUT).fill(username)
        logger.debug("사용자명 입력 완료")
        self.page.locator(login_locators.PASSWORD_INPUT).fill(password)
        logger.debug("비밀번호 입력 완료")
        self.page.locator(login_locators.LOGIN_BUTTON).click()
        logger.info("로그인 버튼 클릭 완료")


    def get_error_message(self) -> str:
        """로그인 에러 메시지 조회
        
        Returns:
            str: 에러 메시지 텍스트
        """
        logger.debug("에러 메시지 조회 시작")
        error_text = self.page.locator(login_locators.ERROR_MESSAGE).inner_text()
        logger.info(f"에러 메시지: {error_text}")
        return error_text


    def get_inventory_title(self) -> str:
        """인벤토리 페이지 타이틀 조회 (로그인 성공 확인용)
        
        Returns:
            str: 인벤토리 페이지 타이틀
        """
        logger.debug("인벤토리 타이틀 조회 시작")
        title = self.page.locator(login_locators.INVENTORY_TITLE).inner_text()
        logger.debug(f"인벤토리 타이틀: {title}")
        return title

