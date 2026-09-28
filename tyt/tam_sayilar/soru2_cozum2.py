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
def solve():
    valid_a = []
    # We can check a broad range of a to confirm
    for a in range(-1000, 1000):
        if a - 3 == 0 or 2*a + 15 == 0:
            continue
        num1 = 2*a + 15
        den1 = a - 3
        num2 = a - 3
        den2 = 2*a + 15
        
        if num1 % den1 == 0 and num2 % den2 == 0:
            valid_a.append(a)
    print("Valid a values:", valid_a)
    print("Sum of a:", sum(valid_a))

solve()
