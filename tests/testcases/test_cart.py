from pytest_check import check

from tests.actions.cart_actions import CartActions
from tests.actions.inventory_actions import InventoryActions


def test_add_single_product_to_cart(page):
    """단일 상품 장바구니 추가 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 첫 번째 상품 추가
    inventory.add_product_to_cart(0)
    
    # 장바구니 배지 확인
    cart_count = inventory.get_cart_badge_count()
    check.equal(cart_count, 1, "Cart badge should show 1 item")


def test_add_multiple_products_to_cart(page):
    """여러 상품 장바구니 추가 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 3개 상품 추가
    inventory.add_product_to_cart(0)
    inventory.add_product_to_cart(1)
    inventory.add_product_to_cart(2)
    
    # 장바구니 배지 확인
    cart_count = inventory.get_cart_badge_count()
    check.equal(cart_count, 3, "Cart badge should show 3 items")


def test_cart_page_displays_added_items(page):
    """장바구니 페이지에 추가된 상품 표시 확인"""
    cart = CartActions(page)
    cart.login_and_add_to_cart(product_count=2)
    
    # 장바구니 타이틀 확인
    cart_title = cart.get_cart_title()
    check.equal(cart_title, "Your Cart", "Cart page title should be 'Your Cart'")
    
    # 장바구니 아이템 개수 확인
    item_count = cart.get_cart_item_count()
    check.equal(item_count, 2, "Cart should contain 2 items")


def test_remove_item_from_cart(page):
    """장바구니에서 상품 제거 테스트"""
    cart = CartActions(page)
    cart.login_and_add_to_cart(product_count=2)
    
    # 초기 아이템 개수 확인
    initial_count = cart.get_cart_item_count()
    check.equal(initial_count, 2, "Cart should initially contain 2 items")
    
    # 첫 번째 아이템 제거
    cart.remove_item_from_cart(0)
    
    # 제거 후 아이템 개수 확인
    final_count = cart.get_cart_item_count()
    check.equal(final_count, 1, "Cart should contain 1 item after removal")


def test_continue_shopping_button(page):
    """계속 쇼핑하기 버튼 테스트"""
    cart = CartActions(page)
    cart.login_and_add_to_cart(product_count=1)
    
    # 계속 쇼핑하기 클릭
    cart.click_continue_shopping()
    
    # 인벤토리 페이지로 돌아왔는지 확인
    inventory = InventoryActions(page)
    inventory_title = inventory.get_inventory_title()
    check.equal(inventory_title, "Products", "Should return to inventory page")


def test_checkout_button_navigation(page):
    """체크아웃 버튼 클릭 테스트"""
    cart = CartActions(page)
    cart.login_and_add_to_cart(product_count=1)
    
    # 체크아웃 버튼 클릭
    cart.click_checkout()
    
    # 체크아웃 페이지로 이동했는지 확인 (URL 또는 타이틀 확인)
    current_url = page.url
    check.equal("checkout-step-one" in current_url, True, "Should navigate to checkout page")

