# tests/src/actions/checkout_actions.py
import logging
from tests.src.locator import checkout_locators
from tests.src.actions.cart_actions import CartActions

logger = logging.getLogger(__name__)


class CheckoutActions:
    """체크아웃 페이지 관련 액션 클래스"""
    
    def __init__(self, page):
        """CheckoutActions 초기화
        
        Args:
            page: Playwright 페이지 객체
        """
        self.page = page
        logger.debug("CheckoutActions 초기화 완료")

    def navigate_to_checkout_step_one(self, product_count: int = 1, username: str = "standard_user", password: str = "secret_sauce"):
        """로그인 후 상품을 장바구니에 추가하고 체크아웃 1단계로 이동"""
        logger.info(f"체크아웃 1단계 이동 시작: product_count={product_count}, username={username}")
        cart = CartActions(self.page)
        cart.login_and_add_to_cart(username, password, product_count)
        cart.click_checkout()
        logger.info("체크아웃 1단계 이동 완료")


    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        """체크아웃 정보 입력"""
        logger.info(f"체크아웃 정보 입력: first_name={first_name}, last_name={last_name}, postal_code={postal_code}")
        self.page.locator(checkout_locators.FIRST_NAME_INPUT).fill(first_name)
        logger.debug("이름 입력 완료")
        self.page.locator(checkout_locators.LAST_NAME_INPUT).fill(last_name)
        logger.debug("성 입력 완료")
        self.page.locator(checkout_locators.POSTAL_CODE_INPUT).fill(postal_code)
        logger.debug("우편번호 입력 완료")
        logger.info("체크아웃 정보 입력 완료")


    def click_continue(self):
        """계속하기 버튼 클릭"""
        logger.info("계속하기 버튼 클릭")
        self.page.locator(checkout_locators.CONTINUE_BUTTON).click()
        logger.debug("계속하기 버튼 클릭 완료")


    def get_checkout_step_one_error(self) -> str:
        """체크아웃 1단계 에러 메시지 반환"""
        logger.debug("체크아웃 1단계 에러 메시지 조회")
        error = self.page.locator(checkout_locators.ERROR_MESSAGE)
        if error.count() > 0:
            error_text = error.inner_text()
            logger.warning(f"체크아웃 에러 메시지: {error_text}")
            return error_text
        logger.debug("에러 메시지 없음")
        return ""


    def get_checkout_step_one_title(self) -> str:
        """체크아웃 1단계 타이틀 반환"""
        logger.debug("체크아웃 1단계 타이틀 조회")
        title = self.page.locator(checkout_locators.TITLE).inner_text()
        logger.debug(f"체크아웃 1단계 타이틀: {title}")
        return title


    def get_subtotal(self) -> float:
        """소계 금액 반환"""
        logger.debug("소계 금액 조회")
        subtotal_text = self.page.locator(checkout_locators.SUBTOTAL_LABEL).inner_text()
        # "Item total: $29.99" 형식에서 숫자 추출
        subtotal = float(subtotal_text.split("$")[1])
        logger.info(f"소계: ${subtotal:.2f}")
        return subtotal


    def get_tax(self) -> float:
        """세금 반환"""
        logger.debug("세금 조회")
        tax_text = self.page.locator(checkout_locators.TAX_LABEL).inner_text()
        # "Tax: $2.40" 형식에서 숫자 추출
        tax = float(tax_text.split("$")[1])
        logger.info(f"세금: ${tax:.2f}")
        return tax


    def get_total(self) -> float:
        """총합 반환"""
        logger.debug("총합 조회")
        total_text = self.page.locator(checkout_locators.TOTAL_LABEL).inner_text()
        # "Total: $32.39" 형식에서 숫자 추출
        total = float(total_text.split("$")[1])
        logger.info(f"총합: ${total:.2f}")
        return total


    def calculate_expected_total(self) -> float:
        """예상 총합 계산 (소계 + 세금)"""
        logger.debug("예상 총합 계산")
        expected = round(self.get_subtotal() + self.get_tax(), 2)
        logger.debug(f"예상 총합: ${expected:.2f}")
        return expected


    def get_cart_items_in_checkout(self) -> list[dict]:
        """체크아웃 2단계의 장바구니 아이템 정보 반환"""
        logger.debug("체크아웃 2단계 장바구니 아이템 정보 조회 시작")
        items = []
        cart_items = self.page.locator(checkout_locators.CART_ITEM).all()

        for item in cart_items:
            name = item.locator(checkout_locators.CART_ITEM_NAME).inner_text()
            price_text = item.locator(checkout_locators.CART_ITEM_PRICE).inner_text()
            price = float(price_text.replace("$", ""))
            quantity = item.locator(checkout_locators.CART_ITEM_QUANTITY).inner_text()

            items.append({
                "name": name,
                "price": price,
                "quantity": int(quantity)
            })

        logger.info(f"체크아웃 아이템 개수: {len(items)}개")
        logger.debug(f"체크아웃 아이템: {items}")
        return items


    def click_finish(self):
        """주문 완료 버튼 클릭"""
        logger.info("주문 완료 버튼 클릭")
        self.page.locator(checkout_locators.FINISH_BUTTON).click()
        logger.debug("주문 완료 버튼 클릭 완료")


    def get_checkout_complete_header(self) -> str:
        """주문 완료 헤더 반환"""
        logger.debug("주문 완료 헤더 조회")
        header = self.page.locator(checkout_locators.COMPLETE_HEADER).inner_text()
        logger.info(f"주문 완료 헤더: {header}")
        return header


    def get_checkout_complete_text(self) -> str:
        """주문 완료 텍스트 반환"""
        logger.debug("주문 완료 텍스트 조회")
        text = self.page.locator(checkout_locators.COMPLETE_TEXT).inner_text()
        logger.debug(f"주문 완료 텍스트 길이: {len(text)}자")
        return text


    def get_checkout_complete_title(self) -> str:
        """주문 완료 페이지 타이틀 반환"""
        logger.debug("주문 완료 페이지 타이틀 조회")
        title = self.page.locator(checkout_locators.TITLE).inner_text()
        logger.debug(f"주문 완료 페이지 타이틀: {title}")
        return title

