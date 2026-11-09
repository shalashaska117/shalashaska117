# Hi, I'm Pietro

### Automated reasoning, formal verification, and AI for mathematics

I'm a CS student at the University of Naples Federico II and an AI researcher at [Project Numina](https://projectnumina.ai). I work on theorem proving and model checking, contribute to [Vampire](https://github.com/vprover/vampire), and build [Fang](https://github.com/shalashaska117/Fang), a first-order theorem prover in Rust with Lean 4 proof checking.

[![Portfolio](https://img.shields.io/badge/Portfolio-pietropellegrino.dev-2563eb?style=flat-square)](https://www.pietropellegrino.dev) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Pietro_Pellegrino-0A66C2?style=flat-square)](https://www.linkedin.com/in/ppellegrino2002/) [![Email](https://img.shields.io/badge/Email-Get_in_touch-7c3aed?style=flat-square&logo=protonmail&logoColor=white)](mailto:p.pellegrino2002@proton.me)

Open to internship and research opportunities.

## At Numina

I work on automating mathematics and autoformalization with [Numina Fuse](https://fuse.projectnumina.ai). I also worked on Numina's public [Lean 4 formalization of the three-dimensional Kakeya conjecture](https://github.com/project-numina/kakeya-3d).

[![Numina Fuse](https://img.shields.io/badge/Numina_Fuse-AI_for_formalization-7c3aed?style=for-the-badge)](https://fuse.projectnumina.ai) [![Kakeya in dimension three](https://img.shields.io/badge/Kakeya_3D-Lean_4-2563eb?style=for-the-badge)](https://github.com/project-numina/kakeya-3d)

## Open source

<a href="https://github.com/search?q=is%3Apr+is%3Amerged+is%3Apublic+author%3Ashalashaska117+-user%3Ashalashaska117&amp;type=pullrequests"><picture><source media="(prefers-color-scheme: dark)" srcset="profile/merged-prs-dark.svg"><img alt="Merged public pull requests, with counts for Vampire, Kakeya-3d, LiquidHaskell, and Apalache" src="profile/merged-prs-light.svg" width="400"></picture></a> <a href="https://github.com/shalashaska117?tab=overview"><picture><source media="(prefers-color-scheme: dark)" srcset="profile/stats-dark.svg"><img alt="Pietro's public GitHub statistics, generated with GitHub Stats Extended" src="profile/stats-light.svg" width="400"></picture></a>

The cards refresh daily. The PR card counts public PRs merged into repositories owned by other users or organizations; the stats card covers my public GitHub activity.

### Vampire

I contribute correctness fixes and refactors to the [Vampire theorem prover](https://github.com/vprover/vampire). My merged work includes:

- Fixing a wrong answer involving Boolean `$let` expressions ([#894](https://github.com/vprover/vampire/pull/894)) and Euclidean division in the Z3 integration ([#1025](https://github.com/vprover/vampire/pull/1025)).
- Making container hash functions explicit and removing `DefaultHash` ([#935](https://github.com/vprover/vampire/pull/935)).
- Fixing SMT proof reconstruction ([#971](https://github.com/vprover/vampire/pull/971)) and removing a timer-thread read of shared options ([#1027](https://github.com/vprover/vampire/pull/1027)).

[Browse my merged Vampire PRs →](https://github.com/vprover/vampire/pulls?q=is%3Apr+author%3Ashalashaska117+is%3Amerged)

### Other contributions

- [Kakeya-3d](https://github.com/project-numina/kakeya-3d): work on the Lean 4 formalization of the three-dimensional Kakeya conjecture at Numina. [Merged PRs](https://github.com/project-numina/kakeya-3d/pulls?q=is%3Apr+author%3Ashalashaska117+is%3Amerged).
- [LiquidHaskell](https://github.com/ucsd-progsys/liquidhaskell): recursive datatype autosize measures and validation of PLE annotations. [Merged PRs](https://github.com/ucsd-progsys/liquidhaskell/pulls?q=is%3Apr+author%3Ashalashaska117+is%3Amerged).
- [Apalache](https://github.com/apalache-mc/apalache): type checking, expression simplification, and module importing in the TLA+ model checker. [Merged PRs](https://github.com/apalache-mc/apalache/pulls?q=is%3Apr+author%3Ashalashaska117+is%3Amerged).
- [Lean Explore benchmarks](https://github.com/lean-explore/lean-explore-bench): offline benchmarks and candidate selection experiments for Lean 4 search. [Merged PRs](https://github.com/lean-explore/lean-explore-bench/pulls?q=is%3Apr+author%3Ashalashaska117+is%3Amerged).

## Personal projects

### Fang

<a href="https://github.com/shalashaska117/Fang"><picture><source media="(prefers-color-scheme: dark)" srcset="profile/fang-dark.svg"><img alt="Fang repository: a first-order theorem prover in Rust with Lean 4 proof checking" src="profile/fang-light.svg" width="500"></picture></a>

An experimental first-order theorem prover written in Rust. Fang reads TPTP problems and checks the proofs it finds with an independent Lean 4 checker before reporting success. It supports TSTP proof output; improving proof search is the current focus.

[Source and documentation →](https://github.com/shalashaska117/Fang)

### More projects

- [ATL Model Checker](https://github.com/shalashaska117/atl-model-checker): strategic verification of multi-agent systems with Alternating-time Temporal Logic. `Python`
- [Logic Evaluator](https://github.com/shalashaska117/logic-evaluator): propositional logic parser and Boolean minimizer with Quine-McCluskey, Petrick's method, and Karnaugh maps. `Python`
- [RegexRiddle](https://github.com/shalashaska117/RegexRiddle): a web game for practising regular expressions. `TypeScript · Vue · Express · PostgreSQL`
- [DietiEstates25](https://github.com/shalashaska117/DietiEstates25): a real estate platform with geospatial search. `Java · Spring Boot · React · PostGIS`
- [Labyrinth Game](https://github.com/shalashaska117/labyrinth-game): a multiplayer maze game with a TCP client-server architecture. `C · UNIX sockets`

More on my [portfolio](https://www.pietropellegrino.dev).

## Technologies I've used

### Programming languages

![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Scala](https://img.shields.io/badge/Scala-DC322F?style=flat-square&logo=scala&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-292929?style=flat-square&logo=rust&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Haskell](https://img.shields.io/badge/Haskell-5D4F85?style=flat-square&logo=haskell&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=222222) ![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)

### Proof assistants and verification tools

![Lean 4](https://img.shields.io/badge/Lean_4-5A4FCF?style=flat-square&logo=lean&logoColor=white) ![Vampire](https://img.shields.io/badge/Vampire-9F1239?style=flat-square) ![TPTP](https://img.shields.io/badge/TPTP-334155?style=flat-square) ![TLA+](https://img.shields.io/badge/TLA%2B-6D28D9?style=flat-square) ![Apalache](https://img.shields.io/badge/Apalache-6D28D9?style=flat-square) ![LiquidHaskell](https://img.shields.io/badge/LiquidHaskell-5D4F85?style=flat-square&logo=haskell&logoColor=white)

### Web frameworks and databases

![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![Vue](https://img.shields.io/badge/Vue-35495E?style=flat-square&logo=vuedotjs&logoColor=4FC08D) ![Node.js](https://img.shields.io/badge/Node.js-417E38?style=flat-square&logo=nodedotjs&logoColor=white) ![Express](https://img.shields.io/badge/Express-292929?style=flat-square&logo=express&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![PostGIS](https://img.shields.io/badge/PostGIS-4169E1?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white) ![Prisma](https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white)

### Development, testing, and writing

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=222222) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square) ![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)

<sub>Cards: <a href="https://github.com/stats-organization/github-stats-extended">GitHub Stats Extended</a>. <a href=".github/profile-cards.md">How the cards update</a>.</sub>
