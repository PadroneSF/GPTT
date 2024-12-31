![alt text](https://i.imgur.com/cWCpCOE.png)

# Gradual Progression Tech Tree
A KSP tech tree designed with 3 main goals:

-	Take better advantage of some major part packs, in particular BDB and Nertea’s mods, without being held back by concerns over compatibility with different mod combinations.
- Make tech progression a bit more “rational”, focusing on increased capabilities rather than arbitrary distinctions of size that inconvenience the player without substantially affecting what they can achieve.
-	Give an RP-1-like feeling of early progression, advancing gradually from early sounding rockets to first satellites to crewed spaceflight, while still working with the actual gameplay balance rather than getting caught up in historical reenactment.

Aside from start, the tree is created using completely new nodes, meaning that only supported mods will appear on the tree, though as a fallback option there is a Lost and Found node that should contain all unsupported parts. The supported mods list is recorded in the mods spreadsheet and [here](https://docs.google.com/spreadsheets/d/1WkyJGPV0f5Y8t63Xq7FFZ4kE2LeNk-n0lTpThED6hso/edit?usp=sharing), but to start out with these mods are highly recommended to properly fill out the tree and play as intended:
- Airplane Plus
- Bluedog Design Bureau
- Cryo Engines
- Far Future
- Heat Control
- Kerbal Atomics
- Near Future Collection
- Restock and Restock Plus
- Station Parts Expansion Redux
- USI-LS
- USI Sounding Rockets


These mods also integrate quite well with the tree:
- Civilian Popuation Modernized
- Coatl Aerospace Probes Plus
- Deep Freeze
- Dmagic
- Feline Utility Rovers
- Kerbal Planetary Base Systems
- Malemute
- Mk2 Expansion
- MkIV Spaceplane System
- OSE Workshop Reworked
- Planetside Exploration Technologies MMSEV
- SCANsat
- Supplementary Electric Engines
- System Heat
- WaterDrinker


And these mods are also variously well supported:
- Artemis Construction Kit
- Blueshift
- Bon Voyage
- Boring Crew Services
- Breaking Ground
- Buffalo 2
- Bumblebee
- Completely NonAggressive Rocketry
- CryoEngines Extensions
- Extraplanetary Launchpads
- Firespitter
- Fuji
- GemstoneLV
- Ground Construction
- HabTech2
- HullcamVDS Continued
- Internal RCS
- JX2 Antenna
- KAS
- Kerbal Foundries 2
- Kerbal Reusability Expansion
- KIS
- Knes
- Making History
- Mechjeb2
- Missing History
- Mk3 Stockalike Expansion
- MKS
- Mk-X
- MOLE
- NRAP
- QuizTech Aero Pack Continued
- Radial Heat Shields
- Rational Resources
- RealChute
- Research Bodies
- RLA Reborn
- Sandcastle
- Simple Adjustable Fairings
- Smart Parts Continued
- SpaceY Heavy Lifters
- SSR Microsat
- Sterling Systems
- SXT Continued
- TAC Life Support
- Taerobee
- Tantares
- TantaresLV
- TantaresSAF
- TantaresSP
- Tarsier Space Technology
- Throttle Controlled Avionics
- Tundra Exploration
- Universal Storage 2

Again, see the spreadsheet for links and details

There are no extra parts or modifications added except that there are two tweaks to science value returns:
- stock_magnetometer_nerf.cfg reduces the stock magnetometer science return from 45 to 5 to be more in line with stock magnetometers, because it seemed silly to split them up
- usi_science_nerf.cfg reduces the return of the USI sounding rockets science parts from 25 to 4, to be more balanced as entry-level science parts.

GPTT was created using ksp-techtree-edit (https://github.com/linuxgurugamer/ksp-techtree-edit), but modified to use ModuleManager instead to remove the dependency on the YongeTech plugin (which has issues with Kerbal Construction Time), by saving the tech nodes as a stock tree, adding a patch to hide the stock nodes, and converting the part unlocks into a single MM patch using the make_gptt_patch.py python script; admittedly a somewhat clunky approach but it makes it easier to keep editing the tree with the editor. The Additional Patches folder holds (in addition to the 2 scripts above) various patches to cover parts added as MM patches, which don't appear in the editor, and part upgrades for at least a few mods.

GPTT is distributed under a CC-BY-NC-SA license (and redistributes tech icons made by Nertea for CTT under the same license), meaning variants or derivatives can be made so long as any previous authors are credited, the use is non-commercial, and the same license is used--and in fact I actively encourage this, because there's every chance I may move on to other projects in the future, and the tree has to be actively maintained to keep or expand mod support. I've added a design document to give a sense of my original intentions for the tree layout to guide any such efforts, though don't feel bound by that if you want to go in a different direction. In the meantime though, you can use pull requests to add any patches, and I am open to adding support for any requested mods.

Notes for future adjustments:
- GPPT_yonge.cfg is the yongetech version of the tree, containing all tech nodes and most part unlocks and editable in ksp-techtree-edit.
  - To add or move parts, edit in ksp-techtree-edit, save as a yongetech tree, and then use the make_gptt_patch.py script, which will read all the part unlocks and save them as a new version of the zzzGPTT_base_parts.cfg patch.
  - To save any changes to the tech nodes themselves, save the tree as a stock tree to replace GPTT.cfg, and then edit the first line to read @TechTree:FIRST (this is critical for KCT compatibility); you may still want to save it as a yongetech tree as well for ease of future editing.
  - If you want to suggest any changes or new mod compatibility, though, it's easier to send me the yongetech tree and I'll handle making the other files and merging together different versions from different people. Broadly speaking adding extra branch techs for unique functionality in specific mods is fine, just not anything intermediate with the existing techs (though if you wanna propose a rework to some of the weaker parts of the tree I'm open to that). And I may tweak things for balance.
- Part upgrades and any parts added by modulemanager patches won't appear in the editor and must be handled with MM patches, which is most of what's in Additional Patches
- All tech nodes should have ids starting with "gptt", anything else (except for start, which seems to cause a lot of issues if renamed) will have its contents moved to Lost and Found and be hidden by the zzzzstock_nodes.cfg patch
- The gptt_exclude node in the upper right is intended to hold any parts like deprecated parts or the stock comet parts that you do not want to end up in Lost and Found or anywhere else in the tree, and is removed before the game starts
