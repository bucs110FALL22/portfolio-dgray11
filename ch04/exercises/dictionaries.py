article = "The Milky Way is 'rippling' like a pond, and scientists may finally know why                                                 Imagine the Milky Way's 100 billion stars as a flat, tranquil pool of water. Now, picture someone dropping a stone the size of 400 million suns into that water. The tranquility is shattered. Wave after wave of energy ripples across the galaxy's surface, jostling and bouncing its stars in a chaotic dance that takes eons to calm.                                        Astronomers suspect that something like this may have really happened — not just once, but several times over the past several billion years.                                          In a new paper published Sept. 15 in the Monthly Notices of the Royal Astronomical Society, researchers explain how a nearby mini-galaxy — the Sagittarius dwarf galaxy — appears to have crashed through the Milky Way on at least two separate occasions, causing stars all around the galaxy to mysteriously oscillate at different speeds.   "
#https://www.livescience.com/milky-way-galaxy-ripple

substitutions = {
  "Milky Way":"the Candy",
  "pond":"lake",
  "water":"H2O",
  "picture":"think of",
  "researchers":"the people who research stuff",
}

for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)