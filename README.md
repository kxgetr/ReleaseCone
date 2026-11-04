# ReleaseCone

Birden fazla dağıtım hedefi için gereken bileşen kümesini çıkarır.

## Girdi

graph ve targets.

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python releasecone.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
[
  "cache",
  "db",
  "disk"
]
```
