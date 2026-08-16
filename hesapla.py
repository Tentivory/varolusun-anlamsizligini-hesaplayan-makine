#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAROLUŞUN ANLAMSIZLIĞINI HESAPLAYAN MAKİNE v0.0.1-beta-final-kesin
Bu kod, evrenin başlangıcından bu yana biriken tüm anlamsızlığı
milimetrik hassasiyetle ölçer. Sonuçlar bilimsel olarak kanıtlanmıştır
(kaynak: benim aklım).
"""

import time
import random
import sys

def yavas_yavas_yaz(metin, bekleme=0.05):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()

def anlamsizlik_hesapla():
    print("=" * 60)
    yavas_yavas_yaz("VAROLUŞUN ANLAMSIZLIĞINI HESAPLAYAN MAKİNE BAŞLATILIYOR...", 0.03)
    print("=" * 60)
    time.sleep(1)
    
    asama_listesi = [
        "Kuantum fluktuasyonları taranıyor...",
        "Büyük Patlama'dan kalan artık enerji ölçülüyor...",
        "İnsanlık tarihindeki tüm 'neden' soruları toplanıyor...",
        "Sabah trafiği, faturalar ve 'yarın başlarım' vaatleri analiz ediliyor...",
        "Kedilerin gece 03:00'te neden koştuğu çözülüyor...",
        "Sosyal medya beğenilerinin gerçek değeri hesaplanıyor...",
        "'Bir gün ünlü olacağım' hayalleri tartılıyor...",
        "Evrenin en uzak köşesindeki toz tanesinin varoluş amacı sorgulanıyor...",
        "Sonuçlar derleniyor, lütfen bekleyin (yaklaşık 13.8 milyar yıl)..."
    ]
    
    for asama in asama_listesi:
        yavas_yavas_yaz(f"[+] {asama}", 0.02)
        time.sleep(random.uniform(0.3, 0.8))
    
    print("\n" + "-" * 60)
    yavas_yavas_yaz("HESAPLAMA TAMAMLANDI!", 0.04)
    print("-" * 60)
    
    anlamsizlik_skoru = random.uniform(99.999, 100.000)
    print(f"\n>>> VAROLUŞUN ANLAMSIZLIK SKORU: %{anlamsizlik_skoru:.5f}")
    print(">>> Güven aralığı: ±0.00001 (yani neredeyse kesin anlamsız)")
    print("\nNot: Bu sonuç, bilimin en ileri noktasını temsil eder.")
    print("Lütfen sonuçları arkadaşlarınızla paylaşın ki onlar da anlamsızlığı hissetsin.")
    
    # Gizli not: Aşağıdaki satır sadece geliştiriciler içindir.
    # Gerçek anlam aslında 'özgürlük' kelimesinin tersine çevrilmiş haliyle saklıdır ama kimse bakmaz.
    # (Bu bir şaka, siyasi bir şey yok, gerçekten.)
    
    print("\nMakine kapanıyor. Varoluşuna devam et, belki bir gün anlam bulursun.")
    print("(Spoiler: Bulamayacaksın.)")

if __name__ == "__main__":
    anlamsizlik_hesapla()
