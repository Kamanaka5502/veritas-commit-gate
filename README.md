
# Veritas Clinical Commit Gate v1.3.2

A bounded enforcement layer for clinical AI — decisions are only allowed to become real if they prove admissibility at the moment of execution.

## Flow

propose -> sign-off -> commit -> decision -> receipt -> replay

## Decision at commit

At the commit boundary:

- admissible → EXECUTE  
- not admissible → REFUSE (fail-closed)

Nothing becomes real unless it passes here.

## A bounded enforcement layer for clinical AI — decisions are only allowed to become real if they prove admissibility at the moment of execution.
