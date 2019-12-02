-- We need to make this frequency equal to the probability that the sequence
-- of letters is actually draw (assuming nothing about what has been played).
-- That involes some N choose K logic which I've forgotten.

CREATE FUNCTION score (word varchar)
  RETURNS float
AS $$
  var frequencies = {
    'a': 9,
    'b': 2,
    'c': 2,
    'd': 4,
    'e': 12,
    'f': 2,
    'g': 3,
    'h': 2,
    'i': 9,
    'j': 1,
    'k': 1,
    'l': 4,
    'm': 2,
    'n': 6,
    'o': 8,
    'p': 2,
    'q': 1,
    'r': 6,
    's': 4,
    't': 6,
    'u': 4,
    'v': 2,
    'w': 2,
    'x': 1,
    'y': 2,
    'z': 1
  };

  val = 0;
  total = 98;
  for (char of word) {
    val += (frequencies[char] || 0);
  };

  return val / total;
$$ LANGUAGE plv8
