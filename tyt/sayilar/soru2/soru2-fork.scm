;;; Copyright © 2026 Adam Faiz <adam.faiz@disroot.org>
;;;
;;; This program is free software: you can redistribute it and/or modify it under the terms of
;;; the GNU General Public License as published by the Free Software Foundation, either
;;; version 3 of the License, or (at your option) any later version.
;;;
;;; This program is distributed in the hope that it will be useful, but WITHOUT ANY
;;; WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
;;; A PARTICULAR PURPOSE. See the GNU General Public License for more details.
;;;
;;; You should have received a copy of the GNU General Public License along with this
;;; program. If not, see <https://www.gnu.org/licenses/>.

(use-modules (srfi srfi-1))

(define (solve-k n)
  (define (unique-pairs lst)
    (define (matches x lst) (cdr (memq x lst)))
    (define (pair x) (lambda (y) (list x y)))
    (append-map (lambda (x) (map (pair x) (matches x lst))) lst))
  (let* ((range (iota n))
	 (pairs (unique-pairs range))
	 (ks (delete-duplicates
	      (sort (map (lambda (args) (apply + args)) pairs) <))))
    (format #t "K values: ~a~%" ks)
    (format #t "K unique count: ~a~%" (length ks))))

(define (solve-k* n)
  ;; For any pair of distinct integers each in the range [0, N),
  ;; the min and max sum are 0+1=1 and (N-2)+(N-1)=2N-3 respectively.
  ;;
  ;; The set of K values is guaranteed to be contiguous,
  ;; since every K in [1, 2N-3] has at least one pair (X, Y) such
  ;; that 0 <= X < Y < N and X + Y = K.
  (let ((ks (iota (- (* 2 n) 3) 1)))
    (format #t "K values: ~a~%" ks)
    (format #t "K unique count: ~a~%" (length ks))))

(solve-k* 10)
