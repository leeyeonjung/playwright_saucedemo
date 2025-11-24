# tests/testcases/test_sorting.py
from pytest_check import check

from tests.src.actions.inventory_actions import InventoryActions


def test_sort_by_name_az(page):
    """이름 A-Z 정렬 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    # 기본 정렬 상태의 상품 이름 가져오기
    inventory.select_sort_option("az")
    sorted_names = inventory.get_product_names()
    
    # 정렬 확인: A-Z 순서
    expected_sorted = sorted(sorted_names)
    check.equal(sorted_names, expected_sorted, "Products should be sorted A-Z")


def test_sort_by_name_za(page):
    """이름 Z-A 정렬 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    inventory.select_sort_option("za")
    sorted_names = inventory.get_product_names()
    
    # 정렬 확인: Z-A 순서
    expected_sorted = sorted(sorted_names, reverse=True)
    check.equal(sorted_names, expected_sorted, "Products should be sorted Z-A")


def test_sort_by_price_low_to_high(page):
    """가격 낮은 순 정렬 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    inventory.select_sort_option("lohi")
    sorted_prices = inventory.get_product_prices()
    
    # 정렬 확인: 낮은 가격부터
    expected_sorted = sorted(sorted_prices)
    check.equal(sorted_prices, expected_sorted, "Products should be sorted by price low to high")


def test_sort_by_price_high_to_low(page):
    """가격 높은 순 정렬 테스트"""
    inventory = InventoryActions(page)
    inventory.login_and_navigate_to_inventory()
    
    inventory.select_sort_option("hilo")
    sorted_prices = inventory.get_product_prices()
    
    # 정렬 확인: 높은 가격부터
    expected_sorted = sorted(sorted_prices, reverse=True)
    check.equal(sorted_prices, expected_sorted, "Products should be sorted by price high to low")

