# Lab Work
**all programs must be written in `{cpp}C++`

**Important: the deadline for completing and defending this work is 16 of december of 2025 till 16:00**

---

1. Pi is undoubtedly one of the fundamental constants, the value of which was known even in ancient times. It is used in everything from cutting and sewing to calculating harmonic oscillations in physics and radio engineering. But what is it equal to? Does this number have some internal structure, some unknown pattern? Many people wanted to know. The simplest and most obvious way is to measure it. This is probably what they did in ancient times, although the accuracy was naturally low. Even in ancient Babylon, the value of Pi was known as 25/8. Then Archimedes proposed the first mathematical method for calculating Pi, by calculating polygons inscribed in a circle. This allowed the value to be calculated not "directly," with a compass and ruler, but mathematically, which ensured much greater accuracy. Finally, in the 3rd century AD, the Chinese mathematician Liu Hui devised the first iterative algorithm—an algorithm in which a number is calculated not by a single formula, but by a sequence of steps (iterations), with each subsequent iteration increasing precision. Furthermore, pi is irrational: it cannot be expressed as a fraction of the form m/n. This was only proven in 1761. Pi is transcendental: it is not the root of any equation with integer coefficients. This was proven in 1882. Pi is infinite. An interesting consequence of the previous point: practically any number can be found in pi, for example, your own phone number; the only question is the length of the sequence you have to search through.

Let's move on to formulas for calculating π:

Madhava-Leibniz formula (15th century):

$$\frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - ... = \frac{\pi}{4}$$

Wallis formula (17th century):

$$\frac{2}{1} * \frac{2}{3} * \frac{4}{3} * \frac{4}{5} * \frac{6}{5} * \frac{6}{7} * \frac{8}{7} * \frac{8}{9} ... = \frac{\pi}{2}$$

**Write a program that calculates the value of $\pi$ using these formulas for the first n iterations. Print all iterations and the current value of $\pi$ to 10 decimal places in the following format:**

`Iteration number of F. Madhava-Leibniz F. Wallis`

---

2. Write a program that determines all Pythagorean triples (x,y,z) of integers no greater than n that satisfy the expression:

$$ x^2 + y^2 = z^2 $$

---

3. Given an integer **at least 2**, print its smallest natural divisor other than 1. Write the program in two versions: one using a `for` loop and one using a `while` loop.

4. There is an explicit formula for the nth term in the Fibonacci sequence:

$$x_n = \frac{1}{\sqrt{5}}\left[\left( \frac{1 + \sqrt{5}}{2} \right)^{n} - \left( \frac{1 - \sqrt{5}}{2} \right)^{n} \right] $$

Since operations with real numbers occur with finite precision, as n increases, the result of the calculation using this formula will increasingly deviate from the true Fibonacci number. Find the n starting at which the deviation from the true value exceeds 0.001.

5. Write a program that determines the result of a logical expression that is true if and only if the coordinates (x,y) belong to the shaded region.

![[lab6z3.png]]
