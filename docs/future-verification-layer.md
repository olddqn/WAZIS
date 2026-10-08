# Possible future capability: a verification layer

Status: **concept only. Nothing described here is implemented.**

## What this is

A second description of WAZIS was written in the owner's brand material in July 2026. It
described WAZIS as two things at once:

- a **verification layer** that lets anyone check that records kept by other systems have not
  been altered, and
- a **public deliberation space** that uses those verified records as shared facts.

Its central idea: a discussion only moves forward when the facts under it can be checked by
everyone taking part.

## Decision

On 2026-10-08 the owner decided that this is **not** the canonical definition of WAZIS.
WAZIS is the open-needs commons described in the [README](../README.md).

The idea is kept here, not deleted, as a capability that may be built later. It must not
redefine WAZIS.

## Where it would belong

If it is built, it is associated with these concerns, which today live outside WAZIS:

- **Asset** — a result of work that can be pointed to.
- **Attribution** — who contributed to it.
- **Provenance** — where it came from and how it changed.
- **Release** — the explicit human decision to make it public.
- **Verification** — a way for a third party to check the above.

## How it could meet WAZIS

The one place the two ideas touch today is Reality Feedback. A Reality Feedback entry is a
reply carrying an external link, and WAZIS does not check that link. A verification
capability could let a reader confirm that the linked result is the one that was released
and has not changed since.

## Constraints that would apply

- Verification is optional. A Need and its Reality Feedback are valid without it.
- An NFT public reference is one possible mechanism among several. It is never required.
- Wallet ownership is not identity.
- Blockchain is not required for WAZIS.
- Nothing is released publicly without explicit human approval.
- Verification must not become a score, a rank, or a way to close a Need.
