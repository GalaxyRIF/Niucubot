# Functions
- [x] Scrambles
- [ ] Competition List
- [ ] Registered competition
- [ ] PR 
- [ ] Local WCA data
- [ ] Comparisons
- [ ] Rank and records
# Instructions
 

## Scrambles: `.event ` ##
Randomly choose scrambles from WCA competition scrmables.
Event short codes: 2,222, 3, 333, 4, 444, 5, 555, 6, 666, 7, 777, 3bf, 333bf ,4bf, 444bf, 5bf, 555bf py, pyram, minx, mega, clock, cl, sq, sq1, sk, skewb.
Add space + number to get more scrambles:

### Example
Input:  \
`.3 2`

Ouptput :\
``1. L2 U R2 L' U' F2 R L2 D F R2 L2 F' R2 F L2 U2 D2 B D2``\
``2. U F2 R2 D' R2 B2 F2 U' R2 B' U R' B' U2 L' F L2 U' F R2``

## Competitions `.comp`##
Get competition information from WCA.\
Args:\
`-s`: Competition status, `o` for open for registration, `f` for fully registered, `p` for ongoing comps, `u` for upcoming compestitions.\
`-r`: region, defualt set to `"UK"`. Can be set to contry names or continent names.\
`-e`: Event short code, split by `/`.

### Example

`.comp -reu`\
`.comp -e3/4/5 -so -ruk` 
