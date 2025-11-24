import logging
from tests.locator import cart_locators
from tests.actions.inventory_actions import InventoryActions

logger = logging.getLogger(__name__)


class CartActions:
    """장바구니 페이지 관련 액션 클래스"""
    
    def __init__(self, page):
        """CartActions 초기화
        
        Args:
            page: Playwright 페이지 객체
        """
        self.page = page
        logger.debug("CartActions 초기화 완료")

    def login_and_add_to_cart(self, username: str = "standard_user", password: str = "secret_sauce", product_count: int = 1):
        """로그인 후 상품을 장바구니에 추가하고 장바구니로 이동"""
        logger.info(f"로그인 및 장바구니 추가 시작: username={username}, product_count={product_count}")
        inventory = InventoryActions(self.page)
        inventory.login_and_navigate_to_inventory(username, password)
        
        # 상품 추가
        logger.info(f"{product_count}개 상품을 장바구니에 추가 중")
        for i in range(product_count):
            inventory.add_product_to_cart(i)
        
        # 장바구니로 이동
        inventory.go_to_cart()
        logger.info("로그인 및 장바구니 추가 완료")


    def get_cart_items(self) -> list[dict]:
        """장바구니의 모든 아이템 정보 반환"""
        logger.debug("장바구니 아이템 정보 조회 시작")
        items = []
        cart_items = self.page.locator(cart_locators.CART_ITEM).all()
        
        for item in cart_items:
            name = item.locator(cart_locators.CART_ITEM_NAME).inner_text()
            price_text = item.locator(cart_locators.CART_ITEM_PRICE).inner_text()
            price = float(price_text.replace("$", ""))
            quantity = item.locator(cart_locators.CART_ITEM_QUANTITY).inner_text()
            
            items.append({
                "name": name,
                "price": price,
                "quantity": int(quantity)
            })
        
        logger.info(f"장바구니 아이템 개수: {len(items)}개")
        logger.debug(f"장바구니 아이템: {items}")
        return items


    def get_cart_item_count(self) -> int:
        """장바구니 아이템 개수 반환"""
        logger.debug("장바구니 아이템 개수 조회")
        count = self.page.locator(cart_locators.CART_ITEM).count()
        logger.debug(f"장바구니 아이템 개수: {count}")
        return count


    def remove_item_from_cart(self, item_index: int = 0):
        """특정 인덱스의 아이템을 장바구니에서 제거"""
        logger.info(f"장바구니에서 아이템 제거: index={item_index}")
        remove_buttons = self.page.locator(cart_locators.REMOVE_BUTTON).all()
        if item_index < len(remove_buttons):
            remove_buttons[item_index].click()
            logger.info(f"아이템 인덱스 {item_index} 제거 완료")
        else:
            logger.warning(f"아이템 인덱스 {item_index}가 범위를 벗어남 (총 {len(remove_buttons)}개 아이템)")


    def click_continue_shopping(self):
        """계속 쇼핑하기 버튼 클릭"""
        logger.info("계속 쇼핑하기 버튼 클릭")
        self.page.locator(cart_locators.CONTINUE_SHOPPING_BUTTON).click()
        logger.debug("계속 쇼핑하기 버튼 클릭 완료")


    def click_checkout(self):
        """체크아웃 버튼 클릭"""
        logger.info("체크아웃 버튼 클릭")
        self.page.locator(cart_locators.CHECKOUT_BUTTON).click()
        logger.debug("체크아웃 버튼 클릭 완료")


    def get_cart_title(self) -> str:
        """장바구니 페이지 타이틀 반환"""
        logger.debug("장바구니 페이지 타이틀 조회")
        title = self.page.locator(cart_locators.CART_TITLE).inner_text()
        logger.debug(f"장바구니 페이지 타이틀: {title}")
        return title

