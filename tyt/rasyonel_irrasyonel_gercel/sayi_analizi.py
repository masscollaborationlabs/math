"""
MIT License

Copyright (c) 2026-2027 Mass Collaboration Labs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import math
from fractions import Fraction
import sympy as sp

def sayi_kumesi_analiz_et(sayi_str, sembolik_deger):
    """
    Verilen sayının rasyonel, irrasyonel ve gerçel sayı 
    kümelerindeki durumunu analiz eder.
    """
    print(f"\n--- Analiz Edilen Sayı: {sayi_str} ---")
    
    # SymPy üzerinden rasyonellik kontrolü (Sembolik kesinlik)
    is_rational = sembolik_deger.is_rational
    
    if is_rational:
        print("Küme: Rasyonel Sayılar (Q)")
        # Kesir formatına dönüştürerek gösterelim
        try:
            kesir_hali = Fraction(str(sp.N(sembolik_deger)))
            print(f"Kesir Biçimi (a/b): {kesir_hali}")
        except:
            print(f"Kesir Biçimi (a/b): {sembolik_deger}")
    else:
        print("Küme: İrrasyonel Sayılar (Q')")
        print("Açıklama: İki tam sayının oranı şeklinde yazılamaz, virgülden sonrası düzensizdir.")
        # Yaklaşık ondalık değerini sonsuz basamağı göstermek adına yazdıralım
        print(f"Yaklaşık Ondalık Değeri: {float(sp.N(sembolik_deger)):.15f}...")

    # Her iki durum da gerçel sayı kümesine dahildir
    print("Küme: Gerçel Sayılar (R) -> EVET (Sayı doğrusunda bir noktadır.)")

# 1. Rasyonel Sayı Örnekleri
sayi_kumesi_analiz_et("0.75", sp.Rational(3, 4))
sayi_kumesi_analiz_et("-5", sp.Integer(-5))

# 2. İrrasyonel Sayı Örnekleri
sayi_kumesi_analiz_et("Kök 2 (sqrt(2))", sp.sqrt(2))
sayi_kumesi_analiz_et("Pi Sayısı (pi)", sp.pi)
