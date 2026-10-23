# Learning_blockchain
## Offline demo and current completeness

The original repository is README-only. This is an educational hash chain, not a blockchain network.

Hash linked block learning exercise. The explicit mock uses synthetic local data, makes no network calls, and does not persist changes. It is separate from the original implementation.

Requirements: Python 3.9+ and Make for the local example; Docker Engine for its container. Run from this repository root:

```sh
make demo
make check
make build
make run
```

The container runs the demo once and exits; it does not expose an HTTP port. First Docker build needs access to the Python base image. For remaining implementation work and known gaps, see [TODO.md](TODO.md). Original dependencies, service integration, and container runtime require separate validation.
