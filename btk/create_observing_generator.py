from btk.obs_conditions import WLDObsConditions, all_surveys


class ObservingGenerator:
    def __init__(
        self,
        surveys,
        obs_conds=None,
        verbose=False,
        stamp_size=24,
    ):
        """Generates class with observing conditions in each band.

        Args:
             surveys (str or list): Name(s) of the survey which should be available
                                    in descwl. May either be a string for single survey
                                    or a list of strings for several surveys. See
                                    obs_conditions.py for a list of available surveys.
             obs_conds: Class (not object) that returns observing conditions for
                             a given survey and band. If not provided, then the default
                             `descwl.survey.Survey` values for the corresponding
                             survey_name are used to create the observing_generator.
        """
        if isinstance(surveys, str):
            self.surveys = [all_surveys[surveys]]
        elif isinstance(surveys, list):
            self.surveys = []
            for s in surveys:
                if isinstance(s, str):
                    if s not in all_surveys:
                        raise KeyError("Survey not implemented.")
                    self.surveys.append(all_surveys[s])
                elif isinstance(s, dict):
                    self.surveys.append(s)
                else:
                    raise TypeError("surveys is not in the right format")
        else:
            raise TypeError("surveys is not in the right format")

        self.verbose = verbose

        # create default observing conditions
        if obs_conds is None:
            self.obs_conds = WLDObsConditions(stamp_size)
        else:
            if not obs_conds.stamp_size == stamp_size:
                raise ValueError(
                    "Observing conditions stamp_size does not match "
                    "stamp_size given."
                )
            self.obs_conds = obs_conds

    def __iter__(self):
        return self

    def __next__(self):
        observing_generator = {}
        for s in self.surveys:
            observing_generator[s["name"]] = []
            for band in s["bands"]:
                cutout = self.obs_conds(s, band)
                observing_generator[s["name"]].append(cutout)
        return observing_generator
