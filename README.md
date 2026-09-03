# Constellations

A project to compute the surface areas of the constellations.

## Constellation Boundaries

The official constellation boundaries are from http://cdsarc.u-strasbg.fr/viz-bin/cat/VI/49,
and are due to Davenhall, Leggett.  Extremely useful additions by Bill Gray are specifically
used here to get closed, counter-clockwise integration paths.  See ```VI_49/consbnd.txt``` and
```VI_49/constbnd.dat```.

## Method

Stoke's theorem is employed to turn the surface integral into a line integral along the
constellations' boundaries.  See the document in the ```docs``` folder for some of the
mathematical details.
