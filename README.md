# chess-pgn-compression

4.3 bits/mv current best, using an opening tree generated from a game database, and a 1ply -> eval func for move ordering. Then maps ranks to huffman codes.

Improvements possible:
 - Arithmetic encoding, or multiple huffman codes based on the mean of the probability distribution of the next move played (still precomputed codes).
 - Use a 3ply chess engine for move ordering (rather than 1ply). Prohibitively slow if done all in python.

I suspect <4bits/mv is doable.
