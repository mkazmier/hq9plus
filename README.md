#HQ9+ and HQ9++
A Python implementation of the HQ9+ language and its object-oriented extension, HQ9++. The language is known for its very simple and clear syntax. The available commands are:
- **H**: the classic "Hello, world!"
- **Q**: print the program source, aka quine
- **9**: print all the verses of "99 beers on the wall"
- **+**: increment the accumulator

Additionally, HQ9++ supports the following keyword as a part of its object-oriented interface:
- **++**: instantiate an object of the Generic SuperClass

Running either program without arguments starts the REPL. Additionally, the interpreters accept .hq9 or .hq9pp source files respectively.

Unfortunately, I could not produce a proof of Turing-completeness of the language. If you do have one, feel free to share.

HQ9+ was created by Cliff L. Biffle, while the object-oriented extension is due to David Morgan-Mar. More info: 
- [HQ9+](https://esolangs.org/wiki/HQ9+)
- [HQ9++](https://esolangs.org/wiki/HQ9%2B%2B)

This implementation is a product of one hungover morning during the winter holidays. Therefore, it _might_ contain some (minor) bugs or oversights. The reader is invited to improve and build upon the project.
