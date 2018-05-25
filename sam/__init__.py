import numpy as np

from streamlines import Streamlines


def clean_bundle(streamlines: Streamlines) -> Streamlines:
    """Cleans a bundle by removing 'outlier' streamlines

    Cleans a bundle by removing streamlines that are too long or too short
    and those that do not start or end close to the others. It then smooths
    the streamlines.

    Args:
        streamlines: The streamlines to clean.

    Returns:
        cleaned: The cleaned streamlines.

    """

    # Reorient all the streamlines.
    streamlines.reorient()

    # Remove streamlines that have an uncommon length.
    lengths = streamlines.lengths
    to_keep = np.abs(lengths - np.mean(lengths)) < 2 * np.std(lengths)
    streamlines = streamlines[to_keep]

    # Remove streamlines that do not end near the others.
    starts = [s[0] for s in streamlines]
    to_keep = np.all(
        np.abs(starts - np.mean(starts, 0)) < 3 * np.std(starts, 0),
        1)
    streamlines = streamlines[to_keep]

    ends = [s[0] for s in streamlines]
    to_keep = np.all(
        np.abs(ends - np.mean(ends, 0)) < 3 * np.std(ends, 0),
        1)
    streamlines = streamlines[to_keep]

    # Make the streamlines prettier by smoothing them.
    streamlines.smooth()

    return streamlines
