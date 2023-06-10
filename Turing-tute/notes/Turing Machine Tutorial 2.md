continuation of [[Turing Machine Tutorial 1]]
# Question 1
#### Using diagrams, mathematical definitions and equations where appropriate:  
###### a) Define a Turing machine in at least two different ways

1. A Turing machine is a mathematical model of computation that consists of a tape of infinite length divided into discrete cells, a read/write head that can read and write symbols on the tape, and a finite set of states that the machine can be in at any given time. The machine operates by following a set of rules that tell it how to move the tape and change its state based on the symbol it reads from the tape.

2. See previous tutorial for mathematical definition of
$$TM = \set{Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject}}$$

###### b) Define a universal Turing machine and give an example of one in a modern-day context

A universal Turing machine is a Turing machine that can simulate any other Turing machine. It takes as input the description of another Turing machine, and simulates its operation on an input tape. The concept of a universal Turing machine is important because it shows that all Turing machines are equivalent in their computational power, and any computation that can be done by one Turing machine can be done by another.

One modern-day example of a universal Turing machine is a computer program that emulates a virtual machine. A virtual machine is a software program that simulates a computer system, and allows other programs to run on it as if they were running on a real computer. A virtual machine is essentially a Turing machine that can simulate any other computer system, making it a universal computing platform.

###### c) How Alan Turing used it to prove that the Halting problem is undecidable

Alan Turing used the concept of a Turing machine to prove that the Halting problem is undecidable. The Halting problem is the problem of determining, given a description of a program and an input, whether the program will eventually halt (terminate) when run on that input, or whether it will run forever. Turing showed that there is no algorithmic procedure that can solve the Halting problem for all possible programs and inputs.

###### d) How this also proves that the decision problem in mathematics (sometimes referred to as the ‘Entscheidungsproblem’) is undecidable

Turing's proof of the undecidability of the Halting problem also implies that the decision problem in mathematics, which asks whether a given mathematical statement is provable from a given set of axioms, is undecidable. This is sometimes referred to as the Entscheidungsproblem, or the decision problem in German. The proof works by showing that the Halting problem can be reduced to the decision problem, which means that if we had an algorithmic procedure for solving the decision problem, we could use it to solve the Halting problem as well. Since the Halting problem is undecidable, this implies that the decision problem is also undecidable.

# Question 2
#### Given the differences between finite state machines and Turing machines, and the definition of a Turing machine. In no more than one page (12pt, normal 2.54 cm margins), argue either for or against why a Turing machine can or cannot obtain artificial intelligence (AI). Discuss what needs to be added or removed to ensure that AI can result or can’t result. If an AI can result, what restrictions or safe guards do you need in place to protect human-kind from becoming obsolete? If an AI can’t result, how will computers and advancements in computing help human-kind in the future?

Turing machines are more powerful than finite state machines, as they can compute any algorithm that can be computed by a computer, while finite state machines can only recognize regular languages. This raises the question of whether a Turing machine can obtain artificial intelligence.

Arguments for a Turing machine being able to obtain AI are based on the fact that a Turing machine can simulate any computation that can be performed by a computer. If the process of intelligence can be defined algorithmically, a Turing machine could be programmed to perform that algorithm and therefore exhibit intelligent behavior.

However, it is important to note that intelligence is not just a matter of computation, but also involves qualities such as creativity, empathy, and self-awareness. It is currently unclear whether these qualities can be defined algorithmically and implemented on a Turing machine. Furthermore, even if we were able to program a Turing machine to exhibit intelligent behavior, there would still be ethical and safety concerns about the potential consequences of creating an artificial general intelligence.

To ensure that AI can result in a safe and responsible manner, we need to have ethical guidelines and regulatory frameworks in place to prevent the misuse of AI and protect human safety. Additionally, research should be focused on developing AI that is aligned with human values and can be controlled by humans.

If a Turing machine cannot obtain AI, advancements in computing can still have a profound impact on human-kind. They can be used to improve medical diagnosis and treatment, assist with scientific research, and automate tedious and dangerous tasks. However, it is important to recognize that these advancements may also have unintended consequences and potential risks, and we need to approach them with caution and careful consideration.