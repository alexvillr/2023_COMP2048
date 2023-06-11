# Question 1
## List all the differences between FSMs and computers we have today with the concept of Turing machines.
- FSM (As seen in [[FSM Tutorial]]) have no memory
- FSM cannot write information
- Turing machines are theoretical so have infinite tape. So computers are the real life adaptation using arbitrarily large tape
- TMs are a superset of FSMs

| FSMs        | PCs                              | TMs |
| ----------- | -------------------------------- | --- |
| States only | (Same transition options as TMs) | $\delta \set{S} \times \set{A}_{\text{tape read}} \implies \set{S} \times \set{A}_{\text{tape write}} \times \set{L, R}$    |

| Machine                  | Language               | Example                        | Implementation                                                  | 
| ------------------------ | ---------------------- | ------------------------------ | --------------------------------------------------------------- |
| Turing Machine           | Recursively enumerable | pretty much anything           | Infinite tape                                                   | 
| Linear-bounded Automaton | Context sensitive      | $\set{a^n b^n c^n \| n \ge 0}$ | Finite tape (arbitrary access; linear multiple of input length) | 
| Pushdown Automaton       | Context free           | $\set{a^n b^n \| n \ge 0}$     | Stack machine (push/pop only)                                   | 
| Finite State Machine     | Regular                | $\set{a^n \| n \ge 0}$         | Combinatoric logic with states                                  | 

FSM transition table vs TM transition table

| S_prev | a   | S_next |
| ------ | --- | ------ |
| S1     | 0   | S2     |
| S1     | 1   | S1     |

| S_prev | a_in | S_next | a_out | direction |
| ------ | ---- | ------ | ----- | --------- |
| S1     | 0    | S2     | X     | L         |
| S1     | 1    | S2     | X     | R         |
# Question 2
## Write down the formal description for the Turing machine that decides the language A. You may use a transition table or diagram to describe the transition rules for the machine.
$$
A = \{\text{w } \\# \text{ w } | \text{ w} \in \{0, 1\} ∗\}
$$
- Note. Any unspecified transitions are considered a rejection
see [[turing_q2.py]]
### Transition table
| $S_{\text{prev}}$ | $a_{\text{in}}$    | $S_{\text{next}}$ | $a_{\text{out}}$ | $\text{direction}$ |
| ------ | ------- | ------ | ----- | --------- |
| q1     | 0       | q2     | X     | R         |
| q1     | 1       | q3     | X     | R         |
| q1     | #       | q8     |       | R         |
| q2     | 0, 1    | q2     |       | R         |
| q2     | #       | q4     |       | R         |
| q3     | 0, 1    | q3     |       | R         |
| q3     | #       | q5     |       | R         |
| q4     | X       | q4     |       | R         |
| q4     | 0       | q6     | X     | L         |
| q5     | X       | q5     |       | R         |
| q5     | 1       | q6     | X     | L         |
| q6     | 0, 1, X | q6     |       | L         |
| q6     | #       | q7     |       | L         |
| q7     | 0, 1    | q7     |       | L         |
| q7     | X       | q1     |       | R         |
| q8     | X       | q8     |       | R         |
| q8     | else    | accept |       | R          |
### Diagram
![](./images/TM_tute_q2.svg)


# Question 3
## Design and formally describe a Turing machine that decides $B = \set{0^{2^n} | n \ge 0}$, the language consisting of all strings of 0s whose length is a power of 2
see [[turing_q3.py]]
#### a) a high-level description of its algorithm
use the binary representation of the input length to keep track of the number of zeros read by the Turing machine. Specifically, the Turing machine uses the binary representation of the input length as a "counter" to count the number of zeros read so far. So count to the right crossing out every second 0 and keep doing that until either there are only crosses on the tape to accept, or there are some 0s on the tape still so reject

#### b) a formal description of the Turing machine
$\text{Turing Machine } M = \set{Q, \Sigma, \Gamma, \delta, Q_0, Q_{accept}, Q_{reject}}$
- $Q = \set{q_0, q_1, q_2, q_3, q_4, q_a, q_r}$
- $\Sigma = \set{0, X}$
- $\Gamma = \set{0, X, B}\text{ Where B represents the blank symbol}$
- $\delta \text{ Transition function where: }$
	1. $\delta(q_0, 0) = (q_1, B, R)$
	2. $\delta(q_0, B) = (q_r, B, R)$
	3. $\delta(q_0, X) = (q_r, X, R)$
	4. $\delta(q_1, 0) = (q_2, X, R)$
	5. $\delta(q_1, B) = (q_a, B, R)$
	6. $\delta(q_1, X) = (q_1, X, R)$
	7. $\delta(q_2, 0) = (q_3, 0, R)$
	8. $\delta(q_2, B) = (q_4, B, L)$
	9. $\delta(q_2, X) = (q_2, X, R)$
	10. $\delta(q_3, 0) = (q_2, X, R)$
	11. $\delta(q_3, B) = (q_r, B, R)$
	12. $\delta(q_3, X) = (q_3, X, R)$
	13. $\delta(q_4, 0) = (q_4, 0, L)$
	14. $\delta(q_4, B) = (q_1, B, R)$
	15. $\delta(q_4, X) = (q_4, X, L)$
- $Q_0 = q_0 \in Q$
- $Q_{accept} = q_a \in Q$
#### c) a transition/state diagram of the Turing machine
###### Transition table
| $S_{prev}$ | $a_{in}$ | $S_{next}$ | $a_{out}$ | $\text{direction}$ |
|:----------:|:--------:|:----------:|:---------:|:------------------:|
|   $q_0$    |    0     |   $q_1$    |     B     |         R          |
|   $q_0$    |    B     |   $q_r$    |     B     |         R          |
|   $q_0$    |    X     |   $q_r$    |     X     |         R          |
|   $q_1$    |    0     |   $q_2$    |     X     |         R          |
|   $q_1$    |    B     |   $q_a$    |     B     |         R          |
|   $q_1$    |    X     |   $q_1$    |     X     |         R          |
|   $q_2$    |    0     |   $q_3$    |     0     |         R          |
|   $q_2$    |    B     |   $q_4$    |     B     |         L          |
|   $q_2$    |    X     |   $q_2$    |     X     |         R          |
|   $q_3$    |    0     |   $q_2$    |     X     |         R          |
|   $q_3$    |    B     |   $q_r$    |     B     |         R          |
|   $q_3$    |    X     |   $q_3$    |     X     |         R          |
|   $q_4$    |    0     |   $q_4$    |     0     |         L          |
|   $q_4$    |    B     |   $q_1$    |     B     |         R          |
|   $q_4$    |    X     |   $q_4$    |     X     |         L          |

###### State diagram
![](./images/TM_q3.svg)

#### d) a sample run of the machine on the string 0000 noting its configuration at each step
	See turing_machine.py and turing_q3.py to get this output yourself
``` zsh
> Please enter the number of 0s to see if machine accepts: 4
q0                             _[0]000
q1                             __[0]00
q2                             __X[0]0
q3                             __X0[0]
q2                             __X0X[_]
q4                             __X0[X]_
q4                             __X[0]X_
q4                             __[X]0X_
q4                             _[_]X0X_
q1                             __[X]0X_
q1                             __X[0]X_
q2                             __XX[X]_
q2                             __XXX[_]
q4                             __XX[X]_
q4                             __X[X]X_
q4                             __[X]XX_
q4                             _[_]XXX_
q1                             __[X]XX_
q1                             __X[X]X_
q1                             __XX[X]_
q1                             __XXX[_]
qa                             __XXX_[_]

```
# Question 4
## Show that the language $C = \set{a^ib^jc^k | i \times j = k \land i, j, k \ge 1}$ cannot be recognisable by a finite state machine by designing a turing machine that decides it
see [[turing_q4.py]]
#### a) a high-level description of its algorithm
Psuedo code implementation of turing machine
```python
for a in As:
	# Replace 'a' with an 'x'
	for b in Bs:
		# Replace 'b' with a 'y'
		# Replace next available (leftmost) 'c' with a 'z'
		if (!c in Cs):
			reject
	# Replace all 'y's with 'b's again
# Iterate through the string to check there's no remaining 'c's or anything else
```
#### b) a formal description of the Turing machine
- $Q = \set{q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_a}$
- $\Sigma = \set{a, b, c, x, y, z, \text{␣}}\text{ Where ␣ represents the blank symbol}$
- $\Gamma = \Sigma$
- $\delta\text{ = Transition function where:}$
	1. $\delta(q_0, a) = (q_1, x, R)$
	2. $\delta(q_1, a) = (q_1, a, R)$
	3. $\delta(q_1, b) = (q_2, y, R)$
	4. $\delta(q_1, z) = (q_4, z, L)$
	5. $\delta(q_2, b) = (q_2, b, R)$
	6. $\delta(q_2, c) = (q_3, z, L)$
	7. $\delta(q_2, z) = (q_2, z, R)$
	8. $\delta(q_3, b) = (q_3, b, L)$
	9. $\delta(q_3, y) = (q_1, y, R)$
	10. $\delta(q_3, z) = (q_3, z, L)$
	11. $\delta(q_4, a) = (q_5, a, L)$
	12. $\delta(q_4, x) = (q_6, x, R)$
	13. $\delta(q_4, y) = (q_4, b, L)$
	14. $\delta(q_5, a) = (q_5, a, L)$
	15. $\delta(q_5, x) = (q_0, x, R)$
	16. $\delta(q_6, \text{␣}) = (q_a, \text{␣}, L)$
- $Q_0 = q_0 \in Q$
- $Q_{accept} = q_a \in Q$
#### c) a transition/state diagram of the Turing machine
###### Transition table
| $S_{prev}$ | $a_{in}$ | $S_{next}$ | $a_{out}$ | $\text{direction}$ |
|:----------:|:--------:|:----------:|:---------:|:------------------:|
|   $q_0$    |   $a$    |   $q_1$    |    $x$    |        $R$         |
|   $q_1$    |   $a$    |   $q_1$    |    $a$    |        $R$         |
|   $q_1$    |   $b$    |   $q_2$    |    $y$    |        $R$         |
|   $q_1$    |   $z$    |   $q_4$    |    $z$    |        $L$         |
|   $q_2$    |   $b$    |   $q_2$    |    $b$    |        $R$         |
|   $q_2$    |   $c$    |   $q_3$    |    $z$    |        $L$         |
|   $q_2$    |   $z$    |   $q_2$    |    $z$    |        $R$         |
|   $q_3$    |   $b$    |   $q_3$    |    $b$    |        $L$         |
|   $q_3$    |   $y$    |   $q_1$    |    $y$    |        $R$         |
|   $q_3$    |   $z$    |   $q_3$    |    $z$    |        $L$         |
|   $q_4$    |   $a$    |   $q_5$    |    $a$    |        $L$         |
|   $q_4$    |   $x$    |   $q_6$    |    $x$    |        $R$         |
|   $q_4$    |   $y$    |   $q_4$    |    $b$    |        $L$         |
|   $q_5$    |   $a$    |   $q_5$    |    $a$    |        $L$         |
|   $q_5$    |   $x$    |   $q_0$    |    $x$    |        $R$         |
|   $q_6$    |   ␣   |   $q_a$    |   ␣    |        $L$         |
###### State diagram
![](./images/TM_q4.svg)
#### d) a sample run of the machine on the string 0000 noting its configuration at each step
```zsh
Please enter your string to see if it is accepted by language C = {a^i b^j c^k | i * j = k && i, j, k >= 1}: aabcc

q0                             _[a]abcc
q1                             _x[a]bcc
q1                             _xa[b]cc
q2                             _xay[c]c
q3                             _xa[y]zc
q1                             _xay[z]c
q4                             _xa[y]zc
q4                             _x[a]bzc
q5                             _[x]abzc
q0                             _x[a]bzc
q1                             _xx[b]zc
q2                             _xxy[z]c
q2                             _xxyz[c]
q3                             _xxy[z]z
q3                             _xx[y]zz
q1                             _xxy[z]z
q4                             _xx[y]zz
q4                             _x[x]bzz
q6                             _xx[b]zz
q6                             _xxb[z]z
q6                             _xxbz[z]
q6                             _xxbzz[_]
qa                             _xxbz[z]_
```

continued in [[Turing Machine Tutorial 2]]


