# Wanderlight — World & Story Bible
*Maintained by Jordan (Narrative Designer)*

## Premise
You play a traveling messenger who has lost their way home. The game follows your route through a handful of small, distinct locations until you find your way back.

## Locations (in route order)

### Millbrook (starting location)
A quiet village with a general store. Home to a shopkeeper NPC who greets the player when they enter. Player buys a map here before they can move on.

### The Hollow Path
A forest trail connecting Millbrook to the coast. Atmospheric, mostly empty. Contains a lantern item the player needs later.

### Bramblegate
A small crossroads town with an innkeeper. First place the player can rest/save. A traveler here asks the player for help, branching the story - see "Bramblegate Branch" below.

### Coldharbor
A foggy, quiet coastal town. A second traveler here asks for help; helping them (on either attempt) provides the hint needed to reach the lighthouse, plus a money reward on one branch. Refusing both times leads to a beach scene with no way forward except turing back or attempting to swim.

### The Lighthouse (ending location)
Where the route home finally becomes clear. Win condition: arrive here by boat, carrying a lit lantern (from The Hollow Path) and with enough coin for the ferryman's fare.

## Bramlegate Branch (see issue #12 for full design + draft dialogue)
Bramblegate is where the player rests/saves, then is approached by a traveler asking for help. This choice branches the story:
- **Helped** -> the traveler is later revealed by the innkeeper to be a thief; the player's map and remaining coin are stolen; a long road leads to Coldharbor.
- **Refused** -> the traveler leaves angery; the map is instead lost crossing the river on the way to Coldharbor. The player's coin is untouched.

Both paths converge at Coldharbor: the player arrives without a map either way, and a second traveler there asks for help (twice, if refused the first time). Refusing both times sends the player to beach with no boat - the only options are drowning (game over) or turning back to reconsider helping.

Helping the Coldharbor traveler (on either attempt) gives the hint needed to find the lighthouse. If the player is on the "helped at Bramblegate" branch, they also recieve a small amount of money - slightly more than what was stolen - since the traveler reacts to hearing the player was robbed. On the "refused at Bramblegate" branch, no money is given, but the player still has whatever coin they started with (never stolen on this path).

Both branches require the same two things to actually reach the lighthouse: a lit lantern(for the fog) and enough coin for the ferryman's boat fare at the marina.

## Notes for engineering
Exits should connect these locations in the order listed above. Each
location needs at minimum a name, description, and exits — see the
Room class in wanderlight.py.

Implementation of the Bramblegate branch, the beach failure loop, and the marina/boat will be tracked as separate issues, split from the design work in #12.