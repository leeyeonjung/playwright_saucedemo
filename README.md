# Sauce Demo Playwright Tests

Sauce Demo 웹 앱을 검증하기 위한 Playwright + Pytest 기반 테스트 프로젝트입니다.  
로그인, 장바구니, 체크아웃 등 핵심 사용자 플로우를 브라우저 수준에서 검증하고, 실행 결과를 HTML 리포트로 남깁니다.

## 📁 프로젝트 구조

```
saucedemo/
├── pytest.ini                      # 공통 Pytest 옵션
├── requirements.txt                # Python 패키지 의존성
├── README.md                       # 프로젝트 가이드
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Playwright/pytest fixture와 리포트 경로 설정
│   ├── src/
│   │   ├── actions/                # 페이지 동작을 캡슐화한 액션 클래스
│   │   └── locator/                # 테스트에 사용하는 CSS/XPath locator 모음
│   └── testcases/                  # 실제 시나리오 테스트 (pytest 함수)
│
└── tests/Results/                  # pytest-html 리포트 저장 폴더 (자동 생성)
    └── report_YYYY-MM-DD_HH-MM-SS.html
```

## 🚀 설치 방법

1. 의존성 설치
   ```bash
   pip install -r requirements.txt
   ```
2. Playwright 브라우저 설치(최초 1회)
   ```bash
   python -m playwright install chromium
   ```

## 📖 사용 방법

### 전체 테스트 실행
```bash
pytest -v
```

### 개별 테스트 실행 예시
```bash
pytest tests/testcases/test_login.py::test_successful_login -v
```

### HTML 리포트
테스트 실행 시마다 `tests/Results/report_YYYY-MM-DD_HH-MM-SS.html` 파일이 자동 생성됩니다.  
`pytest.ini`의 `--html` 옵션 대신 `conftest.py`에서 경로를 동적으로 지정합니다.

## 🧩 주요 구성 요소

- **`tests/src/actions/`**  
  - `LoginActions`, `InventoryActions`, `CartActions`, `CheckoutActions`, `ProductDetailActions` 등  
  - Playwright `page` 객체를 받아 로그인, 상품 정렬, 장바구니 제어, 체크아웃 등 반복 동작을 재사용 가능하게 캡슐화
- **`tests/src/locator/`**  
  - 모든 locator를 중앙에서 관리해 변경 시 영향 범위를 최소화
- **`tests/testcases/`**  
  - `pytest-check`를 활용하여 여러 검증을 한 테스트 내에서 연속적으로 수행
  - 로그인, 장바구니, 상품 정렬, 체크아웃 등 사용자 여정을 커버
- **`tests/conftest.py`**  
  - Playwright 브라우저/페이지 fixture 제공  
  - 실행 시각 기반으로 HTML 리포트 경로 생성

## 🧪 주요 테스트 시나리오

- **Login**: 정상 로그인, 에러 메시지 확인
- **Cart**: 단일/복수 상품 추가, 수량 및 금액 확인
- **Checkout**: 사용자 정보 입력, 주문 합계 검증, 완료 메시지 확인
- **Inventory & Sorting**: 정렬 옵션(A-Z, Z-A, 가격순)별 결과 검증
- **Product Detail**: 상세 페이지 진입, 정보/이미지 검증

## 🔧 자주 사용하는 옵션

| 옵션 | 설명 |
|------|------|
| `-v` | 상세 출력(Verbose) |
| `--maxfail=1` | 첫 실패 시 중단 |
| `-k "keyword"` | 테스트 이름 필터 |
| `--headed` | 브라우저 UI 표시 (Playwright CLI 옵션) |

## 🐛 문제 해결 가이드

- **브라우저가 설치되지 않았다는 에러**  
  `python -m playwright install chromium`을 다시 실행합니다.
- **HTML 리포트가 생성되지 않는 경우**  
  `tests/Results` 폴더에 쓰기 권한이 있는지 확인하세요. 폴더가 없다면 테스트 실행 시 자동 생성됩니다.
- **테스트 중 브라우저 동작을 눈으로 보고 싶을 때**  
  `pytest -v --headed`로 실행하거나 `tests/src/actions/*`에서 `headless=False`로 유지합니다.

## 📦 의존성

- Playwright 1.55.0
- Pytest 8.3.4
- pytest-check 2.5.3
- pytest-html 4.1.1

필요 시 `pip install -r requirements.txt`로 한 번에 설치하세요.

## 📋 참고 사항

- `.pytest_cache/` 및 `__pycache__/`는 `.gitignore`에 포함되어 있어 Git에 올라가지 않습니다.
- 각 테스트 실행 후 브라우저 세션과 컨텍스트를 안전하게 정리하도록 fixture에서 관리하고 있습니다.
