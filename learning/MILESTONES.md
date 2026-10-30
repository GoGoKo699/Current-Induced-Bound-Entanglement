# Thirty milestones

This is the common project-defined understanding map. It contains **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The first phase progresses from individual states and noise operations to the channel-level question. The second joins local proof ingredients to the reversibility/current distinction and its operational meaning. This allocation follows the scientific story; it does not depend on a reader's assessed knowledge.

Book and preprint references always mean the one selected **Rivas–Huelga** anchor; see the [edition map](ANCHOR_BRIDGE.md). The project supplies the specialized entanglement bridge and attributes research ingredients separately. No personal teaching or assessment procedure is part of this map.

## Background/preliminaries

### M01 — States and coherences

**Central question:** What information does a density matrix contain?

**Understanding target:** Distinguish populations, coherences, positivity and unit trace without confusing a coherence with bipartite entanglement.

**Dependencies:** None; objects are introduced here.

**Connection and story role:** Establishes the local objects on which the channel acts.

**Sources:** Book 2–3 / preprint 3–4; [model](../science/model.md).

### M02 — A system and its reference

**Central question:** Why study a reference that the noise never touches?

**Understanding target:** Explain how correlations with an untouched reference test information that a single-system marginal cannot reveal.

**Dependencies:** M01

**Connection and story role:** Moves from local states to the bipartite task.

**Sources:** Book 3.1–3.2 / preprint 4.1–4.2; [tutorial](TUTORIAL.md).

### M03 — Dynamical maps

**Central question:** What makes one operation a channel for every input?

**Understanding target:** Distinguish a linear trace-preserving map from a map defined only for one prepared state.

**Dependencies:** M01, M02

**Connection and story role:** Identifies the all-input object whose threshold is sought.

**Sources:** Book 3.1–3.2 / preprint 4.1–4.2; [model](../science/model.md).

### M04 — Complete positivity

**Central question:** Why is positivity on the system alone insufficient?

**Understanding target:** Explain the need for positivity after adjoining an arbitrary idle reference.

**Dependencies:** M02, M03

**Connection and story role:** Connects physically allowed dynamics with Choi testing.

**Sources:** Book 3.2 / preprint 4.2; [model](../science/model.md).

### M05 — Time-homogeneous noise

**Central question:** How does a generator determine evolution at every time?

**Understanding target:** Use semigroup composition and a matrix exponential, while distinguishing this model from arbitrary time-dependent Markovian evolution.

**Dependencies:** M03, M04

**Connection and story role:** Builds the temporal structure that makes onset sets persistent.

**Sources:** Book 1.2–1.3, 3.5 / preprint 2.2–2.3, 4.5; [model](../science/model.md).

### M06 — Classical population flow

**Central question:** How is a transition rate encoded in a matrix?

**Understanding target:** Read a column-convention generator, its escape rates, and the no-jump probability.

**Dependencies:** M01, M05

**Connection and story role:** Isolates the population sector before adding coherence damping.

**Sources:** Book 4.1 / preprint 5.1; [model](../science/model.md).

### M07 — Stationarity and reversibility

**Central question:** Can a stationary state still carry a current?

**Understanding target:** Distinguish stationarity from detailed balance and interpret the faithful stationary distribution.

**Dependencies:** M06

**Connection and story role:** Introduces the physical distinction underlying the theorem.

**Sources:** Book 4.4 / preprint 5.4; [cycle](../science/cycle.md).

### M08 — Resolved jumps and dephasing

**Central question:** Which generator assumptions keep coherences independent?

**Understanding target:** Distinguish separate rank-one jumps and Hermitian diagonal noise from coherent combinations of transitions.

**Dependencies:** M05, M06

**Connection and story role:** Joins the population and coherence sectors without enlarging the model.

**Sources:** Book 4.2–4.3, 5.2 / preprint 5.2–5.3, 6.2; [model](../science/model.md).

### M09 — The channel as a state

**Central question:** How can one bipartite state encode a channel?

**Understanding target:** Track the normalized maximally entangled input, output-first ordering, and the factor relating the Choi operator and state.

**Dependencies:** M02, M04, M08

**Connection and story role:** Translates an all-input channel question into matrix structure.

**Sources:** Book 3.2 / preprint 4.2 for map foundations; [model](../science/model.md) supplies the Choi bridge.

### M10 — Two different boundaries

**Central question:** How do PPT and separability differ?

**Understanding target:** State which implications are valid and why PPT alone does not normally prove separability.

**Dependencies:** M09

**Connection and story role:** Makes the claimed coincidence scientifically nontrivial.

**Sources:** [model](../science/model.md); [research dependencies](../references/RELATED_WORK.md); anchor map foundations only.

### M11 — Witnesses and distillation

**Central question:** What can an entanglement witness or distillation theorem establish?

**Understanding target:** Separate witness detection, a separable decomposition, and conversion to singlets; recognize that an undetected state need not be separable.

**Dependencies:** M10

**Connection and story role:** Prepares the two different certificates used in the contrast.

**Sources:** [tutorial](TUTORIAL.md); [operational](../science/operational.md); research bridge beyond the anchor.

### M12 — Assembling the question

**Central question:** What is being compared at the channel level?

**Understanding target:** Explain the two onset times, their reference-assisted meaning, and the role of reversibility in one coherent account.

**Dependencies:** M05, M07, M08, M09, M10, M11

**Connection and story role:** Integrates the background into the precise project question.

**Sources:** [model](../science/model.md); [anchor bridge](ANCHOR_BRIDGE.md).

## Narrative/innovation

### M13 — Solving the matrix units

**Central question:** How do populations and coherences evolve in this model?

**Understanding target:** Derive the escape-rate and dephasing contributions and remove the diagonal Hamiltonian phase.

**Dependencies:** M08, M12

**Connection and story role:** Obtains the exact ingredients of the Choi matrix.

**Sources:** [model](../science/model.md); Book 4.2 / preprint 5.2.

### M14 — The pairwise PPT test

**Central question:** Why does partial transposition reduce to small blocks?

**Understanding target:** Identify each two-by-two block and derive its determinant inequality with the correct normalization.

**Dependencies:** M09, M10, M13

**Connection and story role:** Turns a global diagnostic into local inequalities.

**Sources:** [model](../science/model.md); [attribution](../references/RELATED_WORK.md).

### M15 — Nonnegative Gaussian factors

**Central question:** Why is positivity of a coherence matrix not enough?

**Understanding target:** Explain the stronger nonnegative Gram factorization and distinguish its matrix cone from completely positive quantum channels.

**Dependencies:** M13, M14

**Connection and story role:** Supplies the shared factorization needed to glue pairwise bounds together.

**Sources:** [reversible proof](../science/reversible_proof.md); matrix-cone research bridge beyond the anchor.

### M16 — The stationary-distribution tilt

**Central question:** How does reversibility choose one compatible product construction?

**Understanding target:** Follow the stationary-weight tilt and the diagonal-unitary average, including the once-counted aligned diagonal.

**Dependencies:** M07, M15

**Connection and story role:** Turns a nonnegative Gram factor into a separable operator.

**Sources:** [reversible proof](../science/reversible_proof.md).

### M17 — Paying for every population

**Central question:** Why are the remaining coefficients nonnegative?

**Understanding target:** Combine propagated detailed balance, PPT inequalities, and no-jump diagonal weights without division by zero.

**Dependencies:** M06, M14, M16

**Connection and story role:** Completes the constructive separability proof.

**Sources:** [reversible proof](../science/reversible_proof.md).

### M18 — The all-time reversible theorem

**Central question:** When can the shared threshold be infinite?

**Understanding target:** State the theorem with its full assumptions and explain irreducible and disconnected examples.

**Dependencies:** M12, M17

**Connection and story role:** Integrates the first part of the scientific contribution.

**Sources:** [model](../science/model.md); [boundaries](../science/limitations.md).

### M19 — A circulating three-level system

**Central question:** How can bias be changed without changing the outgoing rate?

**Understanding target:** Interpret forward and backward rates, normalized bias, stationary current and uniform dephasing.

**Dependencies:** M07, M08, M18

**Connection and story role:** Introduces the matched counterfamily.

**Sources:** [cycle](../science/cycle.md); Book 4.1 / preprint 5.1.

### M20 — Fixed damping, moving phases

**Central question:** Which population diagnostics stay unchanged under bias?

**Understanding target:** Distinguish singular-value decay from the full complex spectrum and derive the cyclic propagator.

**Dependencies:** M13, M19

**Connection and story role:** Locates precisely what the comparison controls.

**Sources:** [cycle](../science/cycle.md); Book 1.2 / preprint 2.2.

### M21 — The cyclic PPT determinant

**Central question:** How do directed transfer probabilities affect PPT?

**Understanding target:** Reduce the general pair inequalities to one determinant and interpret its sign.

**Dependencies:** M14, M20

**Connection and story role:** Exposes the bias-sensitive boundary.

**Sources:** [cycle](../science/cycle.md).

### M22 — A bias-independent witness

**Central question:** Why does realignment ignore the circulation phase here?

**Understanding target:** Identify its population and scalar coherence blocks and use the trace-norm witness in the correct direction.

**Dependencies:** M11, M20

**Connection and story role:** Provides a separate entanglement certificate with fixed damping.

**Sources:** [cycle](../science/cycle.md); [attribution](../references/RELATED_WORK.md).

### M23 — The reversible reference crossing

**Central question:** Why does one scalar root locate both thresholds at zero bias?

**Understanding target:** Explain monotonicity, the reference equation and why reversibility is needed to turn a PPT crossing into an EB result.

**Dependencies:** M18, M21, M22

**Connection and story role:** Sets an exact benchmark rather than an assumed separability time.

**Sources:** [cycle](../science/cycle.md).

### M24 — Strict positivity opens an interval

**Central question:** Why does every nonzero bias suffice?

**Understanding target:** Use the factored determinant difference, dephasing bound and continuity to establish a nonempty PPT-entangled interval.

**Dependencies:** M21, M22, M23

**Connection and story role:** Connects microscopic circulation to the main contrasting effect.

**Sources:** [cycle](../science/cycle.md).

### M25 — The weak-current law

**Central question:** Why is the leading opening quadratic without extra dephasing?

**Understanding target:** Read the even expansion and implicit-function derivative, retaining the remainder and normalized units.

**Dependencies:** M23, M24

**Connection and story role:** Quantifies how the certified effect vanishes near reversibility.

**Sources:** [cycle](../science/cycle.md); [verification](../verification/README.md).

### M26 — A delicate endpoint

**Central question:** What changes at dephasing equal to one half?

**Understanding target:** Explain why the quadratic factor vanishes while strict positivity survives at fourth order, and why double precision can miss tiny gaps.

**Dependencies:** M24, M25

**Connection and story role:** Identifies a load-bearing limiting case instead of extrapolating a coefficient.

**Sources:** [cycle](../science/cycle.md); [verification](../verification/README.md).

### M27 — From a negative block to singlets

**Central question:** How does this particular non-PPT channel give positive two-way capacity?

**Understanding target:** Track the local two-level projection, its success probability and the imported two-qubit distillation theorem.

**Dependencies:** M11, M14

**Connection and story role:** Gives the threshold a communication meaning without assuming arbitrary NPT distillability.

**Sources:** [operational](../science/operational.md).

### M28 — Why adaptive use does not beat PPT

**Central question:** Why does a PPT channel have zero two-way quantum capacity?

**Understanding target:** Explain preservation across the sender-receiver cut and the maximally-entangled overlap bound.

**Dependencies:** M04, M10, M27

**Connection and story role:** Completes the exact positive-versus-zero operational distinction.

**Sources:** [operational](../science/operational.md).

### M29 — What the checks can certify

**Central question:** How can implementation errors be separated from proof and priority?

**Understanding target:** Interpret independent GKSL reconstruction, Gram checks and high-precision scaling tests, without treating finite agreement as universal proof.

**Dependencies:** M17, M24, M26, M28

**Connection and story role:** Connects the theorem and example to reproducible evidence and its limits.

**Sources:** [verification](../verification/README.md); [related work](../references/RELATED_WORK.md).

### M30 — The complete physical story

**Central question:** What does circulation change, and what remains unproved?

**Understanding target:** Integrate reversibility, matched damping, loss of distillability and residual bound entanglement while withholding an exact biased EB time or a lifetime-advantage claim.

**Dependencies:** M18, M24, M25, M26, M28, M29

**Connection and story role:** Synthesizes the whole contribution and its boundaries.

**Sources:** [science route](../science/README.md); [scope](../science/limitations.md); [anchor bridge](ANCHOR_BRIDGE.md).
