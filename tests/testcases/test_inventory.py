# tests/testcases/test_inventory.py
from pytest_check import check

from tests.src.actions.inventory_actions import InventoryActions
from tests.src.actions.product_detail_actions import ProductDetailActions


def test_product_images_loaded(page):
    """상품 목록 페이지의 이미지 로딩 확인"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 모든 상품 이미지가 로드되었는지 확인
    product_count = len(inventory.get_product_names())
    for i in range(product_count):
        is_loaded = inventory.check_product_image_loaded(i)
        check.equal(is_loaded, True, f"Product image {i} should be loaded")


def test_navigate_to_product_detail(page):
    """상품 상세 페이지 이동 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 첫 번째 상품의 이름과 가격 저장
    product_name = inventory.get_product_name_by_index(0)
    product_price = inventory.get_product_price_by_index(0)
    
    # 상품 상세 페이지로 이동
    inventory.click_product_by_index(0)
    
    # 상세 페이지에서 이름과 가격 확인
    detail = ProductDetailActions(page)
    detail_name = detail.get_product_name()
    detail_price = detail.get_product_price()
    
    check.equal(detail_name, product_name, "Product name should match between list and detail page")
    check.equal(detail_price, product_price, "Product price should match between list and detail page")


def test_product_name_string_comparison(page):
    """상품 이름 문자열 비교 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 모든 상품 이름 가져오기
    product_names = inventory.get_product_names()
    
    # 상품 이름이 비어있지 않은지 확인
    for name in product_names:
        check.equal(len(name) > 0, True, "Product name should not be empty")
        check.equal(isinstance(name, str), True, "Product name should be a string")


def test_product_price_string_comparison(page):
    """상품 가격 문자열 비교 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 모든 상품 가격 가져오기
    product_count = len(inventory.get_product_names())
    
    for i in range(product_count):
        price_string = inventory.get_product_price_by_index(i)
        # 가격 형식 확인 ($ 포함)
        check.equal(price_string.startswith("$"), True, f"Price {i} should start with $")
        # 숫자 부분 추출하여 유효성 확인
        price_value = float(price_string.replace("$", ""))
        check.equal(price_value > 0, True, f"Price {i} should be greater than 0")


def test_product_detail_page_image_loaded(page):
    """상품 상세 페이지 이미지 로딩 확인"""
    detail = ProductDetailActions(page)
    detail.navigate_to_product_detail(0)
    
    is_loaded = detail.check_product_image_loaded()
    import logging
    logging.info(f"Product detail image loaded: {is_loaded}")
    check.equal(is_loaded, True, "Product detail image should be loaded")


def test_back_to_products_from_detail(page):
    """상품 상세 페이지에서 목록으로 돌아가기"""
    detail = ProductDetailActions(page)
    detail.navigate_to_product_detail(0)
    
    # 상세 페이지에서 뒤로가기
    detail.click_back_to_products()
    
    # 인벤토리 페이지로 돌아왔는지 확인
    inventory = InventoryActions(page)
    inventory_title = inventory.get_inventory_title()
    check.equal(inventory_title, "Products", "Should return to inventory page from detail page")

