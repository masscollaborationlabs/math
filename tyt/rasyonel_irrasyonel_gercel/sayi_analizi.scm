;;; Copyright (C) 2026-2027 Mass Collaboration Labs
;;;
;;; This file is part of the custom software ecosystem project.
;;;
;;; This program is free software: you can redistribute it and/or modify
;;; it under the terms of the GNU Affero General Public License as published by
;;; the Free Software Foundation, either version 3 of the License, or
;;; (at your option) any later version.
;;;
;;; This program is distributed in the hope that it will be useful,
;;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;;; GNU Affero General Public License for more details.
;;;
;;; You should have received a copy of the GNU Affero General Public License
;;; along with this program.  If not, see <https://gnu.org>.

(use-modules (ice-9 format))

(define (sayi-kumesi-analiz-et isim deger)
  "Verilen sayinin Scheme veri tipine gore hangi sayi kumesinde oldugunu analiz eder."
  (format #t "~%--- Analiz Edilen Sayi: ~a ---~%" isim)
  
  ;; exact-rational? hatasını çözmek için yerleşik (and (rational? x) (exact? x)) yapısı kullanılmıştır.
  ;; Guile Scheme'de tam sayılar ve kesirler (3/4 gibi) hem rational hem de exact'tir.
  (if (and (rational? deger) (exact? deger))
      (begin
        (format #t "Kume: Rasyonel Sayilar (Q)~%")
        (format #t "Kesir / Tam Sayi Bicimi: ~a~%" deger))
      (begin
        (format #t "Kume: Irrasyonel Sayilar (Q')~%")
        (format #t "Aciklama: Kesir (a/b) olarak ifade edilemez. Virgulden sonrasi duzensizdir.~%")
        (format #t "Yaklasik Ondalik Degeri: ~,15f...~%" deger)))
  
  ;; Real? kontrolu sayi dogrusunda bir karsiligi olan (R) gerchel sayilari temsil eder.
  (if (real? deger)
      (format #t "Kume: Gercel Sayilar (R) -> EVET (Sayı doğrusunda bir noktadır.)~%")
      (format #t "Kume: Gercel Sayilar (R) -> HAYIR~%")))

;; --- Test Senaryolari ---

;; 1. Rasyonel Sayilar (Tam sayi ve Exact Kesir ifadesi)
(sayi-kumesi-analiz-et "Kesirli Sayi (3/4)" (/ 3 4))
(sayi-kumesi-analiz-et "Negatif Tam Sayi (-5)" -5)

;; 2. Irrasyonel Sayilar (Inexact kokenli koklu ve askin ifadeler)
(sayi-kumesi-analiz-et "Kok 2 (sqrt 2)" (sqrt 2))
(sayi-kumesi-analiz-et "Pi Sayisi" (* 4 (atan 1))) ; Scheme uzerinde pi sabiti hesabi
