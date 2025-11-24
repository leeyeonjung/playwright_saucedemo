# tests/src/locator/login_locators.py
"""로그인 페이지 요소 locators"""

# 로그인 입력 필드
USERNAME_INPUT = "#user-name"  # 사용자명 입력 필드
PASSWORD_INPUT = "#password"  # 비밀번호 입력 필드
LOGIN_BUTTON = "#login-button"  # 로그인 버튼

# 에러 및 페이지 요소
ERROR_MESSAGE = "[data-test='error']"  # 로그인 에러 메시지
INVENTORY_TITLE = ".title"  # 인벤토리 페이지 타이틀 (로그인 후 표시)