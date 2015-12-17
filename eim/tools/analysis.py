import numpy as np

def bioemo_readings_to_volts(readings):
    """
    Convert readings from the BioEmo sensor range to voltages.

    Parameters
    ----------
    readings : array_like
        The readings to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted reading(s) as voltage(s)

    Raises
    ------
    TypeError
        If ``readings`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> midrange = bioemo_readings_to_volts(512)
    >>> np.abs(midrange - 2.5024437927663734) < 0.001
    True
    """

    return (np.asarray(readings) / 1023.) * 5.


def bioemo_volts_to_ohms(volts):
    """
    Convert voltages from the BioEmo sensor to resistances in ohms. This mapping was empirically verified and is
    governed by the relationship:

    .. math::

        \\begin{eqnarray}
            \\ln{V} &=& -1.17 \\times 10^{-3} R + 0.861 \\\\
            \\ln{V} - 0.861 &=& -0.00117R \\\\
            R &=& \\frac{\ln{V} - 0.861}{-0.00117} \\\\
            R &=& \\frac{0.861 - \ln{V}}{0.00117} \\\\
            R &=& \\frac{0.861}{0.00117} - \\frac{\\ln{V}}{0.00117}
        \\end{eqnarray}

    Parameters
    ----------
    volts : array_like
        The voltages to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted voltage(s) as resistance(s)

    Raises
    ------
    TypeError
        If ``volts`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> two_volts = bioemo_volts_to_ohms(2)
    >>> np.abs(two_volts - 143463.94823936306) < 0.001
    True
    """

    volts = np.asarray(volts)
    left = 0.861 / 0.00117
    right = 1. / 0.00117
    right = right * np.log(volts)
    return (left - right) * 1000


def bioemo_volts_to_siemens(volts):
    """
    Convert voltages from the BioEmo sensor to conductances in siemens.

    Parameters
    ----------
    volts : array_like
        The voltages to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted voltage(s) as conductance(s)

    Raises
    ------
    TypeError
        If ``volts`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> two_volts = bioemo_volts_to_siemens(2)
    >>> np.abs(two_volts - 6.9703922990572208e-06) < 0.001
    True
    """

    ohms = bioemo_volts_to_ohms(volts)
    siemens = ohms_to_siemens(ohms)
    return siemens


def bioemo_readings_to_siemens(readings):
    """
    Convert readings from the BioEmo sensor to conductances in siemens.

    Parameters
    ----------
    readings : array_like
        The voltages to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted reading(s) as conductance(s)

    Raises
    ------
    TypeError
        If ``readings`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> midrange = bioemo_readings_to_siemens(512)
    >>> np.abs(midrange - -2.0793430561630236e-05) < 0.001
    True
    """

    readings = np.asarray(readings)
    volts = bioemo_readings_to_volts(readings)
    return bioemo_volts_to_siemens(volts)


def ohms_to_siemens(ohms):
    """
    Convert resistances in ohms to conductances in siemens.

    Parameters
    ----------
    ohms : array_like
        The resistances to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted resistance(s) as conductance(s)

    Raises
    ------
    TypeError
        If ``ohms`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> ohms_to_siemens(512) == 1. / 512
    True
    """

    return 1. / np.asarray(ohms)


def siemens_to_ohms(siemens):
    """
    Convert conductances in siemens to resistances in ohms.

    Parameters
    ----------
    siemens : array_like
        The conductances to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted conductance(s) as resistance(s)

    Raises
    ------
    TypeError
        If ``siemens`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> siemens_to_ohms(512) == 1. / 512
    True
    """

    return ohms_to_siemens(siemens)

def unit_to_kilounit(measure):
    """
    Convert measures in whole units to thousands of units.

    Parameters
    ----------
    measure : array_like
        The measure(s) to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted measure(s)

    Raises
    ------
    TypeError
        If ``measure`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> unit_to_kilounit(1) == 1. / 1000
    True
    """

    return measure / 1000.


def unit_to_megaunit(measure):
    """
    Convert measures in whole units to millions of units.

    Parameters
    ----------
    measure : array_like
        The measure(s) to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted measure(s)

    Raises
    ------
    TypeError
        If ``measure`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> unit_to_megaunit(1) == 1. / 1000000
    True
    """

    return measure / 1000000.


def unit_to_gigaunit(measure):
    """
    Convert measures in whole units to billions of units.

    Parameters
    ----------
    measure : array_like
        The measure(s) to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted measure(s)

    Raises
    ------
    TypeError
        If ``measure`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> unit_to_gigaunit(1) == 1. / 1000000000
    True
    """

    return measure / 1000000000.

def unit_to_milliunit(measure):
    """
    Convert measures in whole units to thousandths of units.

    Parameters
    ----------
    measure : array_like
        The measure(s) to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted measure(s)

    Raises
    ------
    TypeError
        If ``measure`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> unit_to_milliunit(1) == 1. * 1000
    True
    """

    return measure * 1000.


def unit_to_microunit(measure):
    """
    Convert measures in whole units to millionths of units.

    Parameters
    ----------
    measure : array_like
        The measure(s) to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted measure(s)

    Raises
    ------
    TypeError
        If ``measure`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> unit_to_microunit(1) == 1. * 1000000
    True
    """

    return measure * 1000000.


def unit_to_nanounit(measure):
    """
    Convert measures in whole units to billionths of units.

    Parameters
    ----------
    measure : array_like
        The measure(s) to be converted

    Returns
    -------
    out : float or :py:class:`numpy.ndarray`
        The converted measure(s)

    Raises
    ------
    TypeError
        If ``measure`` cannot be converted to a :py:class:`numpy.ndarray`

    Examples
    --------
    >>> unit_to_nanounit(1) == 1. * 1000000000
    True
    """

    return measure * 1000000000.




