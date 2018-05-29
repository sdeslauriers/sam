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

    # Remove streamlines whose points are far from the distribution of the
    # rest of the bundle.
    streamlines.resample(nb_points=100)
    to_keep = np.ones((len(streamlines),))
    for i in range(3):
        x = [s.points[:, i] for s in streamlines]
        to_keep = np.logical_and(
            np.all(np.abs(x - np.mean(x, 0)) < 2.5 * np.std(x, 0), 1),
            to_keep)

    streamlines = streamlines[to_keep]

    # Make the streamlines prettier by smoothing them.
    streamlines.smooth()

    return streamlines
