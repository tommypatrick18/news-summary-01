# World News Summary - November 11, 2026

This program performs a byte-exact, deterministic copy of a one-day world news summary for November 11, 2026, from `summary.txt` to a specified output directory. It reads the environment variable `MAKEFUN_OUTPUT_DIR` (defaulting to `/output`) to determine the destination for `entry.txt`.

The summary provides neutral coverage of the following twelve stories from Wednesday, November 11, 2026:
* **US shutdown ends**: President Trump signs a bill ending the record 43-day shutdown after a 222-209 House vote, funding the government through January 30.
* **Abu Dhabi talks**: Russia and Ukraine agree to a major prisoner swap of up to 1,500 each during US-brokered negotiations.
* **COP31 Antalya**: 102 heads of state open a summit where the UN chief warns of a climate "path to mutually assured destruction."
* **Baltic drone alerts**: NATO jets scramble as drones from Ukrainian strikes on Russia enter Baltic airspace, closing airports in Lithuania.
* **Wang Yi-Rubio call**: Top US and Chinese diplomats hold a positive call ahead of an expected Xi-Trump meeting in Shenzhen.
* **Iran-Argentina designations**: Iran designates Argentina’s navy and air force as terrorist entities in a reciprocal move.
* **Gaza storms**: Heavy rain floods camps for over 940,000 displaced people, with charities warning 150,000 tents are needed.
* **DR Congo Ebola**: The Bundibugyo outbreak is confirmed as the deadliest ever, killing 5,387 out of 11,042 cases.
* **Nvidia H200**: Records reveal a Chinese university with military ties bought two blacklisted AI chips for $123,000.
* **Anthropic IPO**: High demand may raise the IPO price above $78, valuing the AI firm at $1.5 trillion.
* **US inflation/Fed**: Hot 0.4% consumer inflation in October makes a December Federal Reserve rate hike nearly certain.
* **Paraguay rating watch**: Fitch places the BB+ rating on watch after the ueno collapse froze the savings of nearly 3 million customers.

The script uses raw binary mode to ensure that running it twice produces byte-identical output, maintaining the integrity of the summary text across different environments.
