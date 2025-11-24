"""장바구니 페이지 요소 locators"""

# 장바구니 아이템 정보
CART_ITEM = ".cart_item"  # 개별 장바구니 아이템 컨테이너
CART_ITEM_NAME = ".inventory_item_name"  # 장바구니 아이템 이름
CART_ITEM_PRICE = ".inventory_item_price"  # 장바구니 아이템 가격
CART_ITEM_QUANTITY = ".cart_quantity"  # 장바구니 아이템 수량

# 액션 버튼
REMOVE_BUTTON = "button[data-test*='remove']"  # 장바구니에서 아이템 제거 버튼
CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"  # 계속 쇼핑하기 버튼
CHECKOUT_BUTTON = "[data-test='checkout']"  # 체크아웃 버튼

# 페이지 타이틀
CART_TITLE = ".title"  # 장바구니 페이지 타이틀 ("Your Cart")