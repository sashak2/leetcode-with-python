# leetcode-with-python

## Environment Setup

### venv

```cmd
python -m venv venv
```

```cmd
.\venv\Scripts\activate
```

```cmd
deactivate
```

### Install python package

Install package

```cmd
pip install [package_name]
pip install [package_name==1.2.3]
pip install --upgrade package_name
```

Output installing packages to requirements.txt

```cmd
pip freeze > requirements.txt
```

Install requirements.txt

```cmd
pip install -r requirements.txt
```

### Execute

```cmd
.\venv\Scripts\activate
```

```cmd
python .\src\main.py
```

```cmd
python .\src\main.py 13
```

## Git Note

### Git commit message

#### Common Types

- feat: new feature
- fix: bug fix
- docs: documentation changes
- style: formatting (no code change)
- refactor: code restructuring
- test: adding tests
- chore: maintenance tasks

#### Key Principles

1. Be specific: "Fix login bug" → "Fix null pointer error in login validation"
1. Atomic commits: One logical change per commit
1. Present tense: Write as if giving commands to the codebase
1. Context matters: Future you (or teammates) should understand why this change was made
