-- We need to make this frequency equal to the probability that the sequence
-- of letters is actually draw (assuming nothing about what has been played).
-- That involes some N choose K logic which I've forgotten.

CREATE FUNCTION distance (word varchar, other varchar)
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

  total = 98;

  wordcopy = word;

  // Remove characters that the words have in common
  for (char of wordcopy) {
    if (other.includes(char)) {
      other = other.replace(char, '')
      word = word.replace(char, '')
    }
  };

  // Letters that are more rare raise the distance between words. This should
  // be improved to use the relative probability of the letters appearing

  distance = 0;;
  for (char of other) {
    freq = frequencies[char]
    if (freq) {
      f = 1 / (freq / total)
      distance += f
    }
  }

  return distance;
$$ LANGUAGE plv8
