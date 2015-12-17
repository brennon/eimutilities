import mongoengine

class Signal(mongoengine.DynamicDocument):
    """
    A class to hold documents from the ``eim.signals`` collection in the Emotion in Motion database.

    See :py:class:`mongoengine.Document` for more details on how to use mongoengine documents to query the database for
    signals.
    """
    meta = {
        'collection' : 'signals'
    }


class Trial(mongoengine.DynamicDocument):
    """
    A class to hold documents from the ``eim.trial`` collection in the Emotion in Motion database.

    See :py:class:`mongoengine.Document` for more details on how to use mongoengine documents to query the database for
    trials.

    Attributes
    ----------
    signals : :py:class:`mongoengine.fields.ListField` of :py:class:`Signal` instances
        A list of the signals (as :py:class:`Signal` instances) in the order in which they were recorded during
        the trial
    """
    meta = {
        'collection' : 'trials'
    }

    signals = mongoengine.ListField(mongoengine.ReferenceField(Signal))

