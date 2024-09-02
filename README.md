# wf-fs-test-server

## install

1. clone the repo
2. install env

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

3. run dev server

```bash
fastapi dev main.py
```

## dev server

```bash
curl http://127.0.0.1:8000/items
```