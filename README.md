﻿# alientools
#### Video Demo: https://youtu.be/jYqLi41qsrw
#### Description: 
The Apollo Interface is a tool made to assist players running Frea League Publishing's Alien RPG. This is primarily through generation of random objects, but differs from many online tools that are similar by allowing users to save the randomly generated objects and make notes about them for reference later.

The project is primarily written in Python using Flask and some JavaScript to generate a website. Although in many cases the use of SQL for storing and retrieving data would be more practical, I intend to eventually publish this project as a website and did not want to worry about protecting user data. As a result, JSON imports and exports are supported for the user to retain their data between sessions.

Although this is intended to aid players running sessions of the Alien RPG, the tools can be used in a system agnostic manor. 
-Some content is specific to the setting, found on the Factions tab. The factions included can be manually removed and replaced by the user to reflect their setting.
-Generated characters have stats based on the Mutant Year Zero system used by Alien. These can be ignored for system agnostic play.
-Generated ships are composed of modules that are used by ships within the core rulebook. Although module names are present, no stats or specifics are included. These modules also generate the rooms found aboard the ship, which is unique to this generator.

The generator can create characters, cats, star systems, and ships. It allows the user to manually add and remove factions, but will not randomly generate them.

##### Factions:
Factions can be referenced by characters, ships, and the planets and moons of a star system. A faction indicates the allegiance of that object. As factions can be removed and changed by players, the factions that load upon generating the website can be replaced. The only hard coded reference to any of the loaded factions are some ship names are only available to certain factions. For example, a ship named the USS Pennsylvania would only be possible for a faction titled United Americas, as that name wouldn't be appropriate to be generally available to any ship. It is also not possible to remove the Unaligned faction. If a faction is removed, any saved objects belonging to that faction will have their faction changed to Unaligned.

##### Characters: 
Characters are intended to be used as NPCs while running a game. They generate names based on namelists that are imported as needed. Factions can be associated with certain namelists, so if a character belongs to the faction United Americas, the name list may be from any of the North or South American countries that have a namelist available. While it would be nice to have a more robust source of names, collecting names is time consuming. An effort was made, where possible, to take name lists from the 1980's and 1990's to fit the cassette futurism vibe of the Alien franchise. 

Jobs are attributed based on the character's primary stat. The list of available jobs is not primarily based on the core rulebook, but inspired by it. This adds some variation. The primary stat also determines how the stats for a character are distributed, so that characters are more likely to have points in the stats that matter to them. Currently the "Kid" job from the core rulebook is not present as character age is not currently supported, and the faction associated with the character wouldn't make sense.

A glaring ommission in the character section is a lack of Talents and Skills. While it would be easy enough to include both, I'm not interested in including this type of rules content as I don't want a letter from anyone's legal team if this is ever hosted.

The character generator allows for a specific type of random character to be created via a toolbar at the top.

##### Cats:
Space ships have cats. What type of cat? A random one. Cats can also be generated via the ship generator already assigned to the ship.

##### System Generator
The system generator generates a star, its planets, and their moons. Where possible I attempted to use astronomy to inform the generation of space objects.

###### Stars
Stars choose a spectral class and then a spectral type. This informs all of their physical characteristics, such as color and temperature. Increasing or decreasing the number of planets will always add and subtract the last planet associated with the sun. Future plans include adding other celestial objects such as asteroid fields.

###### Planets and Moons
Planets and moons share a lot of the same generation code. While some tables exist within the core rulebook for planet generation, most of this was ignored to reference science instead. At some points science is ignored to make things more interesting to a roleplaying game. Features that are retained from the rulebook are limited to the atmosphere type list, as determining the atmospheric composition of exoplanets was taking too long.

In an attempt to organize the planets data, symbology is used along with tooltips. Expanding any planet can show more detailed content. Adding or removing moons works similar to a star's relationship to planets, where the last listed moon is the first to be removed if the moon count is lowered.

##### Ship Generator
Ship generation is more complicated than any of the other generators used on this project. Instead of simply generating a complete ship, the type of ship is chosen and fed in to a HullType class. That is then fed in to a HullModel class, which is then used to create the actual ship object. I would like to eventually make it possible for users to save different Hull Types and Hull Models, so the foundations are in place to make that possible. The thought would that the hull type corresponds to a base model, and the hull model would be similar to the trim level on a car. Finally the ship generation adds anything unique to that particular instance, such as name, crew members, the presence of a cat, the faction it belongs to, and a prefix for the name. Military ships do not generate cats.

It is currently not possible to change ship details within the editor as the module and room code was not interacting kindly with the UI. 

