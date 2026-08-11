# Wanderlight — World & Story Bible
*Maintained by Jordan (Narrative Designer)*

## Premise
You play a traveling messenger who has lost their way home. The game
follows your route through a handful of small, distinct locations
until you find your way back.

## Locations (in route order)

### Millbrook (starting location)
A quiet village with a general store. Home to a shopkeeper NPC who
greets the player when they enter.

### The Hollow Path
A forest trail connecting Millbrook to the coast. Atmospheric, mostly
empty. Contains a lantern item the player needs later.

### Bramblegate
A small crossroads town with an innkeeper. First place the player can
rest/save.

### Coldharbor
A foggy, quiet coastal town. A second NPC here hints at the way home.

### The Lighthouse (ending location)
Where the route home finally becomes clear. Win condition: arrive
here while carrying the lantern from The Hollow Path.

## Notes for engineering
Exits should connect these locations in the order listed above. Each
location needs at minimum a name, description, and exits — see the
Room class in wanderlight.py.
