# PORTED

![](ZZZ/ZZZ.jpg)

* An interesting ctf challange where data is tranamitted in different parts
* There is no fix port of the server on which the server is running
* The port keeps changing according to the timing given
* Set a range of ports
* Set number of parts in which the message need to be split

## HOW TO USE
* `python3 ported.py <HOST> <SP> <EP> <FLAG> <SPLIT_PARTS>`
* SP = lower port limit
* EP = higher port limit
* FLAG =  secret message
* SPLITPARTS = no of splits of flag to be made
