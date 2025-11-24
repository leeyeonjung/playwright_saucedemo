# tests/src/locator/inventory_locators.py
"""인벤토리(상품 목록) 페이지 요소 locators"""

# 정렬 및 상품 목록
SORT_DROPDOWN = "[data-test='product-sort-container'], .product_sort_container"  # 상품 정렬 드롭다운 (이름/가격 정렬)
INVENTORY_ITEM = ".inventory_item"  # 개별 상품 아이템 컨테이너
INVENTORY_ITEM_NAME = ".inventory_item_name"  # 상품 이름
INVENTORY_ITEM_PRICE = ".inventory_item_price"  # 상품 가격
INVENTORY_ITEM_IMAGE = ".inventory_item_img img"  # 상품 이미지
INVENTORY_ITEM_LINK = ".inventory_item_name"  # 상품 상세 페이지로 이동하는 링크

# 장바구니 관련 버튼
ADD_TO_CART_BUTTON = "button[data-test*='add-to-cart']"  # 장바구니에 추가 버튼
REMOVE_BUTTON = "button[data-test*='remove']"  # 장바구니에서 제거 버튼

# 장바구니 UI 요소
CART_BADGE = ".shopping_cart_badge"  # 장바구니 아이템 개수 배지
CART_LINK = ".shopping_cart_link"  # 장바구니 페이지로 이동하는 링크

# 페이지 타이틀
INVENTORY_TITLE = ".title"  # 인벤토리 페이지 타이틀 ("Products")