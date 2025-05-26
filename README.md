# Jakość kodu, Mit, czy Hit?

## Zadanie 1 - przygotowanie środowiska

Prosty setup środowiska Pythonowego z przykładową funkcją i testami przy użyciu `pytest`.

### 📁 Struktura katalogów

```
zadania/
├── src/
│   └── powitanie.py
├── tests/
├── setup.py
└── venv/
```

---

## ✅ Krok po kroku

### 1. Utwórz katalog projektu

```bash
mkdir ./zadania
cd zadania
```

### 2. Utwórz katalog na kod źródłowy

```bash
mkdir ./src
```

### 3. Dodaj przykładowy moduł

```bash
nvim ./src/powitanie.py
```

Wklej zawartość:

```python
def przywitaj(jak="Hello", kogo="World"):
    return f"{jak}, {kogo}"
```

### 4. Utwórz plik `setup.py`

```bash
nvim ./setup.py
```

Zawartość:

```python
from setuptools import find_packages, setup

setup(
    name="zadania",
    version="0.7",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
```

### 5. Utwórz i aktywuj środowisko wirtualne

```bash
python3 -m venv venv
source ./venv/bin/activate
```

### 6. Zainstaluj projekt lokalnie (editable mode)

```bash
pip install -e .
```

### 7. Przetestuj importowanie i działanie funkcji

```bash
python3
>>> import powitanie
>>> powitanie.przywitaj(jak="Siemka", kogo="ziomek")
'Siemka, ziomek'
```

---

## 🧪 Testowanie

### 8. Utwórz katalog na testy

```bash
mkdir tests
```

### 9. Zainstaluj pytest

```bash
pip install pytest
```

### 10. Dodaj przykładowy test

Plik: `tests/test_powitanie.py`

```python
import powitanie

def test_powitanie():
    res = powitanie.przywitaj()
    assert "Siemka" in res
```

### 11. Uruchom testy

```bash
pytest
```

## Zadanie 2 – Kalkulator

Napisz prostą aplikację kalkulatora, w której każde działanie (dodawanie, odejmowanie, mnożenie, dzielenie) zostanie zaimplementowane jako osobna funkcja. 

Następnie napisz testy jednostkowe sprawdzające poprawność działania każdej z funkcji.

**Wymagania:**
- Działania muszą być zaimplementowane jako oddzielne funkcje.
- Muszą zostać napisane testy jednostkowe do każdego działania.
- Należy uwzględnić zabezpieczenie przed dzieleniem przez zero.

---

## Zadanie 3 – Analiza błędów w pliku `3zad.py`

Przeanalizuj kod zawarty w pliku `3zad.py` i postaraj się odnaleźć oraz opisać błędy znajdujące się w funkcjach.
Napisz testy jednostkowe obnażające te niedociągnięcia.

W funkcji `to_roman()` spróbuj znaleźć 3 błędy.

Funkcja `price_of_shipment()` ma w sobie 2 błędy.

`factorial()` wcale nie jest tak silnie napisana. Też ma w sobie 3 błędy.

---

## Zadanie 4 – Typowanie funkcji

Zmień funkcję podaną niżej tak, aby zawierała adnotacje typów wejściowych oraz zwracanego wyniku, zgodnie z zaleceniami modułu `typing`.

**Dodatkowe wymagania:**
- Jeśli użytkownik nie poda wieku, informacja o wieku nie powinna być wyświetlana.
- Należy użyć odpowiednich typów z modułu `typing`, np. `Optional`.

Funkcja do poprawy:

```python
def powitanie(imie, wiek):
    return f'Cześć {imie}, masz {wiek} lat.'
