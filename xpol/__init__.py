"""xpol — cross-pollination sampler: draw a genuinely random foreign topic and
build a prompt that transfers its mechanisms into a STEM problem."""
from .frame import Frame, LEVELS
from .sampler import Sampler, Seed

__all__ = ["Frame", "LEVELS", "Sampler", "Seed"]
