# tests/src/locator/product_detail_locators.py
"""상품 상세 페이지 요소 locators"""

# 상품 정보
PRODUCT_NAME = ".inventory_details_name"  # 상품 이름
PRODUCT_PRICE = ".inventory_details_price"  # 상품 가격
PRODUCT_DESCRIPTION = ".inventory_details_desc"  # 상품 설명
PRODUCT_IMAGE = ".inventory_details_img img"  # 상품 이미지

# 액션 버튼
ADD_TO_CART_BUTTON = "button[data-test*='add-to-cart']"  # 장바구니에 추가 버튼
REMOVE_BUTTON = "button[data-test*='remove']"  # 장바구니에서 제거 버튼
BACK_BUTTON = "[data-test='back-to-products']"  # 상품 목록으로 돌아가기 버튼