"""Resolve DEVIL_HOME for standalone skill scripts.

Skill scripts may run outside the Hermes process (e.g. system Python,
nix env, CI) where ``devil_constants`` is not importable.  This module
provides the same ``get_devil_home()`` and ``display_devil_home()``
contracts as ``devil_constants`` without requiring it on ``sys.path``.

When ``devil_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``devil_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``DEVIL_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from devil_constants import display_devil_home as display_devil_home
    from devil_constants import get_devil_home as get_devil_home
except (ModuleNotFoundError, ImportError):

    def get_devil_home() -> Path:
        """Return the Hermes home directory (default: ~/.devil).

        Mirrors ``devil_constants.get_devil_home()``."""
        val = os.environ.get("DEVIL_HOME", "").strip()
        return Path(val) if val else Path.home() / ".devil"

    def display_devil_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``devil_constants.display_devil_home()``."""
        home = get_devil_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
