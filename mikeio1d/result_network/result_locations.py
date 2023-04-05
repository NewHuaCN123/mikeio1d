from ..dotnet import pythonnet_implementation as impl


class ResultLocations(dict):
    """
    A base class for a network locations (nodes, reaches)
    or a catchments wrapper class.

    Parameters
    ----------
    res1d : Res1D
        Res1D object the result location belongs to.

    Attributes
    ----------
    data : ResultData
        MIKE 1D ResultData object.
    data_items : IDataItems.
        MIKE 1D IDataItems object.
    """

    def __init__(self, res1d):
        self.res1d = res1d
        self.data = res1d.data
        self.data_items = res1d.data.DataItems

    def set_res1d_object_to_dict(self, dict_key, obj):
        """
        Create a dict entry from a key name to an object
        or a list of objects.
        """
        obj = impl(obj)
        if dict_key in self:
            value = self[dict_key]
            if not isinstance(value, list):
                self[dict_key] = [value]

            self[dict_key].append(obj)
        else:
            self[dict_key] = obj
