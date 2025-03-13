프로젝트 설정 가이드
Git에서 프로젝트 Pull 받은 후 환경 설정 방법
이 가이드는 Git에서 프로젝트를 처음 Pull 받은 후 개발 환경을 설정하는 방법을 안내합니다.
### 1. 프로젝트 클론
```bash
git clone https://github.com/papooo-dev/chat-api.git
cd chat-api
```

### 2. Poetry를 통한 의존성 설치
본 프로젝트는 Poetry를 사용하여 의존성을 관리합니다. Poetry가 설치되어 있지 않다면 먼저 설치해주세요.
- Poetry 설치 방법
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. 의존성 설치
프로젝트 디렉토리에서 다음 명령어를 실행하여 필요한 모든 패키지를 설치합니다:
```bash
poetry install
```

개발 의존성까지 모두 설치하려면:
```bash
poetry install --with dev
```

### 4. 가상 환경 활성화
Poetry 가상 환경을 활성화합니다:
```bash
poetry shell
```
또는 가상 환경을 활성화하지 않고 명령어를 실행하려면:
```bash
poetry run python app/main.py
```

### 5. 환경 변수 설정
.env.example 파일을 복사하여 .env 파일을 생성하고 필요한 환경 변수를 설정합니다:
```bash
cp .env.example .env
```
텍스트 편집기로 .env 파일을 열고 필요한 값을 입력하세요.

### 6. 데이터베이스 설정 (필요한 경우)
데이터베이스 마이그레이션을 실행합니다:
```bash
poetry run python manage.py migrate
```

### 7. 개발 서버 실행
개발 서버를 시작합니다:
```bash
./run.sh
```
