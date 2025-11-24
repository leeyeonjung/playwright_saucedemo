"""체크아웃 페이지 요소 locators"""

# ========== Checkout Step One (사용자 정보 입력) ==========
FIRST_NAME_INPUT = "[data-test='firstName']"  # 이름 입력 필드
LAST_NAME_INPUT = "[data-test='lastName']"  # 성 입력 필드
POSTAL_CODE_INPUT = "[data-test='postalCode']"  # 우편번호 입력 필드
CONTINUE_BUTTON = "[data-test='continue']"  # 계속하기 버튼
CANCEL_BUTTON = "[data-test='cancel']"  # 취소 버튼
ERROR_MESSAGE = "[data-test='error']"  # 에러 메시지
TITLE = ".title"  # 페이지 타이틀 ("Checkout: Your Information")

# ========== Checkout Step Two (주문 확인 및 결제) ==========
CART_ITEM = ".cart_item"  # 체크아웃 페이지의 장바구니 아이템
CART_ITEM_NAME = ".inventory_item_name"  # 아이템 이름
CART_ITEM_PRICE = ".inventory_item_price"  # 아이템 가격
CART_ITEM_QUANTITY = ".cart_quantity"  # 아이템 수량
SUBTOTAL_LABEL = ".summary_subtotal_label"  # 소계 라벨 (예: "Item total: $29.99")
TAX_LABEL = ".summary_tax_label"  # 세금 라벨 (예: "Tax: $2.40")
TOTAL_LABEL = ".summary_total_label"  # 총합 라벨 (예: "Total: $32.39")
FINISH_BUTTON = "[data-test='finish']"  # 주문 완료 버튼

# ========== Checkout Complete (주문 완료) ==========
COMPLETE_HEADER = ".complete-header"  # 주문 완료 헤더 ("Thank you for your order!")
COMPLETE_TEXT = ".complete-text"  # 주문 완료 메시지 텍스트
BACK_HOME_BUTTON = "[data-test='back-to-products']"  # 홈으로 돌아가기 버튼

