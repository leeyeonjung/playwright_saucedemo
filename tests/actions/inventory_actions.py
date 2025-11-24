import logging
from tests.locator import inventory_locators
from tests.actions.login_actions import LoginActions

logger = logging.getLogger(__name__)


class InventoryActions:
    """인벤토리(상품 목록) 페이지 관련 액션 클래스"""
    
    def __init__(self, page):
        """InventoryActions 초기화
        
        Args:
            page: Playwright 페이지 객체
        """
        self.page = page
        logger.debug("InventoryActions 초기화 완료")

    def login_and_navigate_to_inventory(self, username: str = "standard_user", password: str = "secret_sauce"):
        """로그인 후 인벤토리 페이지로 이동"""
        logger.info(f"로그인 및 인벤토리 페이지 이동 시작: username={username}")
        login = LoginActions(self.page)
        login.load()
        login.login(username, password)
        logger.info("로그인 및 인벤토리 페이지 이동 완료")


    def select_sort_option(self, sort_value: str):
        """정렬 옵션 선택 (az, za, lohi, hilo)"""
        logger.info(f"정렬 옵션 선택: {sort_value}")
        self.page.locator(inventory_locators.SORT_DROPDOWN).select_option(sort_value)
        logger.debug(f"정렬 옵션 '{sort_value}' 선택 완료")


    def get_selected_sort_option(self) -> str:
        """현재 선택된 정렬 옵션 반환"""
        logger.debug("선택된 정렬 옵션 조회")
        selected = self.page.locator(inventory_locators.SORT_DROPDOWN).input_value()
        logger.debug(f"선택된 정렬 옵션: {selected}")
        return selected


    def get_product_names(self) -> list[str]:
        """모든 상품 이름 리스트 반환"""
        logger.debug("상품 이름 리스트 조회 시작")
        names = [item.inner_text() for item in self.page.locator(inventory_locators.INVENTORY_ITEM_NAME).all()]
        logger.info(f"상품 개수: {len(names)}개")
        logger.debug(f"상품 이름: {names}")
        return names


    def get_product_prices(self) -> list[float]:
        """모든 상품 가격 리스트 반환 (숫자로 변환)"""
        logger.debug("상품 가격 리스트 조회 시작")
        prices = []
        for item in self.page.locator(inventory_locators.INVENTORY_ITEM_PRICE).all():
            price_text = item.inner_text()
            # "$29.99" 형식에서 숫자만 추출
            price = float(price_text.replace("$", ""))
            prices.append(price)
        logger.info(f"상품 가격 개수: {len(prices)}개")
        logger.debug(f"상품 가격: {prices}")
        return prices


    def add_product_to_cart(self, product_index: int = 0):
        """특정 인덱스의 상품을 장바구니에 추가"""
        logger.info(f"장바구니에 상품 추가 시도: index={product_index}")
        add_buttons = self.page.locator(inventory_locators.ADD_TO_CART_BUTTON).all()
        if product_index < len(add_buttons):
            add_buttons[product_index].click()
            logger.info(f"상품 인덱스 {product_index} 장바구니에 추가 완료")
        else:
            logger.warning(f"상품 인덱스 {product_index}가 범위를 벗어남 (총 {len(add_buttons)}개 상품)")


    def add_product_to_cart_by_name(self, product_name: str):
        """상품 이름으로 장바구니에 추가"""
        logger.info(f"장바구니에 상품 추가 시도: name={product_name}")
        items = self.page.locator(inventory_locators.INVENTORY_ITEM).all()
        for item in items:
            name = item.locator(inventory_locators.INVENTORY_ITEM_NAME).inner_text()
            if name == product_name:
                item.locator(inventory_locators.ADD_TO_CART_BUTTON).click()
                logger.info(f"상품 '{product_name}' 장바구니에 추가 완료")
                return
        logger.warning(f"상품 '{product_name}'을 찾을 수 없음")


    def get_cart_badge_count(self) -> int:
        """장바구니 배지에 표시된 상품 개수 반환"""
        logger.debug("장바구니 배지 개수 조회")
        badge = self.page.locator(inventory_locators.CART_BADGE)
        if badge.count() > 0:
            count = int(badge.inner_text())
            logger.debug(f"장바구니 배지 개수: {count}")
            return count
        logger.debug("장바구니 배지가 없음 (0개)")
        return 0


    def go_to_cart(self):
        """장바구니 페이지로 이동"""
        logger.info("장바구니 페이지로 이동")
        self.page.locator(inventory_locators.CART_LINK).click()
        logger.debug("장바구니 페이지 이동 완료")


    def get_inventory_title(self) -> str:
        """인벤토리 페이지 타이틀 반환"""
        logger.debug("인벤토리 페이지 타이틀 조회")
        title = self.page.locator(inventory_locators.INVENTORY_TITLE).inner_text()
        logger.debug(f"인벤토리 페이지 타이틀: {title}")
        return title


    def get_product_name_by_index(self, index: int) -> str:
        """특정 인덱스의 상품 이름 반환"""
        logger.debug(f"상품 이름 조회: index={index}")
        names = self.get_product_names()
        if index < len(names):
            name = names[index]
            logger.debug(f"상품 이름[{index}]: {name}")
            return name
        logger.warning(f"상품 인덱스 {index}가 범위를 벗어남")
        return ""


    def get_product_price_by_index(self, index: int) -> str:
        """특정 인덱스의 상품 가격 반환 (문자열 형식)"""
        logger.debug(f"상품 가격 조회: index={index}")
        items = self.page.locator(inventory_locators.INVENTORY_ITEM).all()
        if index < len(items):
            price = items[index].locator(inventory_locators.INVENTORY_ITEM_PRICE).inner_text()
            logger.debug(f"상품 가격[{index}]: {price}")
            return price
        logger.warning(f"상품 인덱스 {index}가 범위를 벗어남")
        return ""


    def check_product_image_loaded(self, index: int = 0) -> bool:
        """특정 인덱스의 상품 이미지가 로드되었는지 확인"""
        logger.debug(f"상품 이미지 로드 확인: index={index}")
        images = self.page.locator(inventory_locators.INVENTORY_ITEM_IMAGE).all()
        if index < len(images):
            # 이미지가 로드되었는지 확인 (naturalWidth > 0)
            is_loaded = images[index].evaluate("img => img.complete && img.naturalWidth > 0")
            logger.debug(f"상품 이미지[{index}] 로드 상태: {is_loaded}")
            return is_loaded
        logger.warning(f"상품 인덱스 {index}가 범위를 벗어남")
        return False


    def click_product_by_index(self, index: int):
        """특정 인덱스의 상품 클릭하여 상세 페이지로 이동"""
        logger.info(f"상품 상세 페이지 이동: index={index}")
        items = self.page.locator(inventory_locators.INVENTORY_ITEM).all()
        if index < len(items):
            items[index].locator(inventory_locators.INVENTORY_ITEM_LINK).click()
            logger.debug(f"상품 인덱스 {index} 클릭 완료")
        else:
            logger.warning(f"상품 인덱스 {index}가 범위를 벗어남")

