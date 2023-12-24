<div align="center">

[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]

  <h2>SquadUtils</h2>
  <p>
      SquadUtils, the tiling powerhouse behind SquadMaps!
      <br />
      <a href="https://discord.mahto.id/">Join Discord</a>
  </p>
</div>

---

## About

SquadUtils is the home of imagery used in SquadMaps. This repostitory contains the exported Minimaps from Squads SDK (exported as 'TGA'), which we then use to tile and display using SquadMaps. 

<p align="right">(<a href="#top">back to top</a>)</p>

---

## How do I tile the maps?

<details><summary>Prerequisites - Install Python & Docker</summary>
Install python & docker kthx
</details>

1. To get started, you first will need to clone the repository.

```sh
git clone https://github.com/mahtoid/SquadUtils
```

2. Once you have the project cloned, edit `tiles.py` in `SquadUtils/script`

```py
the_path = "CHANGE/TO/INPUT/PATH"
the_other_path = "CHANGE/TO/OUTPUT/PATH"
```

`the_path` should be the full input path to where the `TGA`'s are. <br/>
`the_other_path` should be the full output path.

**If you are trying to set up SquadMaps locally, this will be to `SquadMaps/public/assets/maps` directory.*

3. Run the `tiles.py` script

```sh
python -m tiles.py
```

**Please note that the script can take a long time to complete.**

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Attributions

- _This project borrows tiling logic originally found from [SquadLanes](https://github.com/w4rum/SquadLanes) repository._
- _This project borrows imagery from [Squad](https://joinsquad.com)'s SDK._

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LINK DUMP -->

[stars-shield]: https://img.shields.io/github/stars/mahtoid/SquadUtils?style=for-the-badge
[stars-url]: https://github.com/mahtoid/SquadUtils/stargazers
[issues-shield]: https://img.shields.io/github/issues/mahtoid/SquadUtils?style=for-the-badge
[issues-url]: https://github.com/mahtoid/SquadUtils/issues
[license-shield]: https://img.shields.io/github/license/mahtoid/SquadUtils?style=for-the-badge
[license-url]: https://github.com/mahtoid/SquadUtils/blob/master/LICENSE
[github-url]: https://github.com/mahtoid/SquadUtils/
