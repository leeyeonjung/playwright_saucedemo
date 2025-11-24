from pytest_check import check

from tests.actions.checkout_actions import CheckoutActions


def test_checkout_step_one_title(page):
    """체크아웃 1단계 타이틀 확인"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one()
    
    title = checkout.get_checkout_step_one_title()
    check.equal(title, "Checkout: Your Information", "Checkout step one title should be correct")


def test_checkout_with_valid_information(page):
    """유효한 정보로 체크아웃 진행"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one()
    
    # 사용자 정보 입력
    checkout.fill_checkout_information("John", "Doe", "12345")
    checkout.click_continue()
    
    # 체크아웃 2단계로 이동했는지 확인 (URL 또는 타이틀)
    current_url = page.url
    check.equal("checkout-step-two" in current_url, True, "Should navigate to checkout step two")


def test_checkout_with_empty_first_name(page):
    """빈 이름으로 체크아웃 시도"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one()
    
    checkout.fill_checkout_information("", "Doe", "12345")
    checkout.click_continue()
    
    error_message = checkout.get_checkout_step_one_error()
    check.equal("First Name is required" in error_message, True, "Should show error for empty first name")


def test_checkout_with_empty_last_name(page):
    """빈 성으로 체크아웃 시도"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one()
    
    checkout.fill_checkout_information("John", "", "12345")
    checkout.click_continue()
    
    error_message = checkout.get_checkout_step_one_error()
    check.equal("Last Name is required" in error_message, True, "Should show error for empty last name")


def test_checkout_with_empty_postal_code(page):
    """빈 우편번호로 체크아웃 시도"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one()
    
    checkout.fill_checkout_information("John", "Doe", "")
    checkout.click_continue()
    
    error_message = checkout.get_checkout_step_one_error()
    check.equal("Postal Code is required" in error_message, True, "Should show error for empty postal code")


def test_checkout_total_calculation_with_single_item(page):
    """단일 상품 체크아웃 총합 계산 테스트"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one(product_count=1)
    
    # 사용자 정보 입력 및 2단계로 이동
    checkout.fill_checkout_information("John", "Doe", "12345")
    checkout.click_continue()
    
    # 소계, 세금, 총합 가져오기
    subtotal = checkout.get_subtotal()
    tax = checkout.get_tax()
    total = checkout.get_total()
    
    # 총합 계산 검증 (소계 + 세금)
    expected_total = checkout.calculate_expected_total()
    check.equal(round(total, 2), round(expected_total, 2), "Total should equal subtotal + tax")
    
    # 가격이 양수인지 확인
    check.equal(subtotal > 0, True, "Subtotal should be greater than 0")
    check.equal(tax >= 0, True, "Tax should be greater than or equal to 0")
    check.equal(total > 0, True, "Total should be greater than 0")


def test_checkout_total_calculation_with_multiple_items(page):
    """여러 상품 체크아웃 총합 계산 테스트"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one(product_count=3)
    
    # 사용자 정보 입력 및 2단계로 이동
    checkout.fill_checkout_information("John", "Doe", "12345")
    checkout.click_continue()
    
    # 장바구니 아이템 가격 합계 계산
    cart_items = checkout.get_cart_items_in_checkout()
    expected_subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    
    # 실제 소계와 비교
    actual_subtotal = checkout.get_subtotal()
    check.equal(round(actual_subtotal, 2), round(expected_subtotal, 2), "Subtotal should match sum of item prices")
    
    # 총합 계산 검증
    tax = checkout.get_tax()
    total = checkout.get_total()
    expected_total = round(expected_subtotal + tax, 2)
    
    check.equal(round(total, 2), round(expected_total, 2), "Total should equal subtotal + tax")


def test_checkout_price_verification(page):
    """체크아웃 가격 검증 테스트"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one(product_count=2)
    
    # 사용자 정보 입력 및 2단계로 이동
    checkout.fill_checkout_information("John", "Doe", "12345")
    checkout.click_continue()
    
    # 장바구니 아이템 가격 확인
    cart_items = checkout.get_cart_items_in_checkout()
    
    # 각 아이템의 가격이 양수인지 확인
    for item in cart_items:
        check.equal(item["price"] > 0, True, f"Item {item['name']} price should be greater than 0")
        check.equal(item["quantity"] > 0, True, f"Item {item['name']} quantity should be greater than 0")
    
    # 소계가 모든 아이템 가격의 합과 일치하는지 확인
    expected_subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    actual_subtotal = checkout.get_subtotal()
    check.equal(round(actual_subtotal, 2), round(expected_subtotal, 2), "Subtotal should match sum of all items")


def test_checkout_complete_order(page):
    """주문 완료 페이지 테스트"""
    checkout = CheckoutActions(page)
    checkout.navigate_to_checkout_step_one(product_count=1)
    
    # 사용자 정보 입력 및 주문 완료
    checkout.fill_checkout_information("John", "Doe", "12345")
    checkout.click_continue()
    checkout.click_finish()
    
    # 주문 완료 페이지 확인
    complete_header = checkout.get_checkout_complete_header()
    complete_text = checkout.get_checkout_complete_text()
    complete_title = checkout.get_checkout_complete_title()
    
    check.equal(complete_header, "Thank you for your order!", "Complete header should be correct")
    check.equal(
        "Your order has been dispatched" in complete_text,
        True,
        "Complete text should contain dispatch message"
    )
    check.equal(complete_title, "Checkout: Complete!", "Complete page title should be correct")

