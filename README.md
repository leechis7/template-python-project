# 개발환경 설정

## 가상환경 만들기
파이썬에서 가상 환경(virtual environment)은 하나의 PC에서 프로젝트 별로 독룁된 파이썬 실행 환경(runtime/interpreter)을 사용할 수 있도록 해준다.

1. 가상환경 생성
```bash
$ python3 -m venv .venv
```
2. 가상환경은 버전관리 필요없으므로 .gitignore에 추가
```bash
$ echo '.venv' >> .gitignor준
```
3. 가상환경 활성화 (활성화하고 패키지를 설치하면된다.)
```bash
$ source .venv/bin/activate
(.venv) $
```
4. 가상환경 비활성화
```bash
(.venv) $ deactivate
```

## Code Styler
**Black** (or autopep8, yapf)를 사용한다. (Star수가 가장 많은 Black을 선택함)

1. 단축키 Ctrl + P를 이용해서 settings.json을 열어준다.
```json
{  
  .... //아래 추가
  "python.pythonPath": "test\\Scripts\\python.exe"
}
```

## Linter
**Pylint**를 사용한다.

1. Ctrl + Shift + P로 커맨드 명령 프롬프트을 연 이후에 Python: Select Linter 타이핑하거나 선택한다.  
아래의 옵션들이 settings.json에 자동으로 생성된다
```json
"python.linting.pylintEnabled": true,
"python.linting.enabled": true
```
1. lintOnSave 옵션을 이용해서 저장 시에 자동으로 검사하도록 설정한다.
```json
"python.linting.lintOnSave": true
```
