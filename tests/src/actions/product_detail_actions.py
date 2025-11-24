# tests/src/actions/product_detail_actions.py
import logging
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from tests.src.locator import product_detail_locators
from tests.src.actions.inventory_actions import InventoryActions

logger = logging.getLogger(__name__)


class ProductDetailActions:
    """상품 상세 페이지 관련 액션 클래스"""
    
    def __init__(self, page):
        """ProductDetailActions 초기화
        
        Args:
            page: Playwright 페이지 객체
        """
        self.page = page
        logger.debug("ProductDetailActions 초기화 완료")

    def navigate_to_product_detail(self, product_index: int = 0, username: str = "standard_user", password: str = "secret_sauce"):
        """로그인 후 특정 상품 상세 페이지로 이동"""
        logger.info(f"상품 상세 페이지 이동 시작: product_index={product_index}, username={username}")
        inventory = InventoryActions(self.page)
        inventory.login_and_navigate_to_inventory(username, password)
        inventory.click_product_by_index(product_index)
        # 상세 페이지가 완전히 로드될 때까지 대기
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector(
            product_detail_locators.PRODUCT_IMAGE,
            state="visible",
            timeout=10000,
        )
        logger.info("상품 상세 페이지 이동 완료")


    def get_product_name(self) -> str:
        """상품 상세 페이지의 상품 이름 반환"""
        logger.debug("상품 이름 조회")
        name = self.page.locator(product_detail_locators.PRODUCT_NAME).inner_text()
        logger.debug(f"상품 이름: {name}")
        return name


    def get_product_price(self) -> str:
        """상품 상세 페이지의 상품 가격 반환"""
        logger.debug("상품 가격 조회")
        price = self.page.locator(product_detail_locators.PRODUCT_PRICE).inner_text()
        logger.debug(f"상품 가격: {price}")
        return price


    def get_product_description(self) -> str:
        """상품 상세 페이지의 상품 설명 반환"""
        logger.debug("상품 설명 조회")
        description = self.page.locator(product_detail_locators.PRODUCT_DESCRIPTION).inner_text()
        logger.debug(f"상품 설명 길이: {len(description)}자")
        return description


    def check_product_image_loaded(self) -> bool:
        """상품 이미지가 로드되었는지 확인"""
        logger.debug("상품 이미지 로드 확인")

        image_element = self.page.wait_for_selector(
            product_detail_locators.PRODUCT_IMAGE,
            state="visible",
            timeout=10000,
        )

        self.page.wait_for_function(
            """
            img => img && img.complete && img.naturalWidth > 0
            """,
            arg=image_element,
            timeout=10000,
        )
        logger.debug("상품 이미지 로드 완료 확인")
        return True


    def click_back_to_products(self):
        """상품 목록으로 돌아가기"""
        logger.info("상품 목록으로 돌아가기 버튼 클릭")
        self.page.locator(product_detail_locators.BACK_BUTTON).click()
        logger.debug("상품 목록으로 돌아가기 완료")


    def add_to_cart_from_detail(self):
        """상세 페이지에서 장바구니에 추가"""
        logger.info("상세 페이지에서 장바구니에 추가")
        self.page.locator(product_detail_locators.ADD_TO_CART_BUTTON).click()
        logger.debug("장바구니 추가 완료")