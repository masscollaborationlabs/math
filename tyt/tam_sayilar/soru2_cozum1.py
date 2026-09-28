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
# a'nın alabileceği değerleri tutacak liste
degerler_a = []

# Geniş bir aralıkta a değerlerini test edelim
for a in range(-1000, 1000):
    # Paydaların sıfır olma durumunu kontrol edelim (Tanımsızlığı önlemek için)
    if (a - 3 == 0) or (2 * a + 15 == 0):
        continue
    
    pay = 2 * a + 15
    payda = a - 3
    
    # x ve y'nin tam sayı olması için kalanların 0 olması gerekir
    # (Hem pay paydaya tam bölünmeli, hem de payda paya tam bölünmeli)
    if (pay % payda == 0) and (payda % pay == 0):
        degerler_a.append(a)

# Sonuçları ekrana yazdırma
toplam_a = sum(degerler_a)
print(f"a'nın alabileceği değerler: {degerler_a}")
print(f"a'nın alabileceği değerlerin toplamı: {toplam_a}")
