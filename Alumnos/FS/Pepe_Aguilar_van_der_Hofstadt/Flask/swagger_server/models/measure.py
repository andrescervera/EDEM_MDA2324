# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Measure(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, fechamuestreo: str=None, unidad: str=None, medicion: float=None):  # noqa: E501
        """Measure - a model defined in Swagger

        :param code: The code of this Measure.  # noqa: E501
        :type code: str
        :param fechamuestreo: The fechamuestreo of this Measure.  # noqa: E501
        :type fechamuestreo: str
        :param unidad: The unidad of this Measure.  # noqa: E501
        :type unidad: str
        :param medicion: The medicion of this Measure.  # noqa: E501
        :type medicion: float
        """
        self.swagger_types = {
            'code': str,
            'fechamuestreo': str,
            'unidad': str,
            'medicion': float
        }

        self.attribute_map = {
            'code': 'code',
            'fechamuestreo': 'fechamuestreo',
            'unidad': 'unidad',
            'medicion': 'medicion'
        }
        self._code = code
        self._fechamuestreo = fechamuestreo
        self._unidad = unidad
        self._medicion = medicion

    @classmethod
    def from_dict(cls, dikt) -> 'Measure':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Measure of this Measure.  # noqa: E501
        :rtype: Measure
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this Measure.

        ID of the sensor  # noqa: E501

        :return: The code of this Measure.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Measure.

        ID of the sensor  # noqa: E501

        :param code: The code of this Measure.
        :type code: str
        """

        self._code = code

    @property
    def fechamuestreo(self) -> str:
        """Gets the fechamuestreo of this Measure.

        Sampling date  # noqa: E501

        :return: The fechamuestreo of this Measure.
        :rtype: str
        """
        return self._fechamuestreo

    @fechamuestreo.setter
    def fechamuestreo(self, fechamuestreo: str):
        """Sets the fechamuestreo of this Measure.

        Sampling date  # noqa: E501

        :param fechamuestreo: The fechamuestreo of this Measure.
        :type fechamuestreo: str
        """

        self._fechamuestreo = fechamuestreo

    @property
    def unidad(self) -> str:
        """Gets the unidad of this Measure.

        Unit of measurement  # noqa: E501

        :return: The unidad of this Measure.
        :rtype: str
        """
        return self._unidad

    @unidad.setter
    def unidad(self, unidad: str):
        """Sets the unidad of this Measure.

        Unit of measurement  # noqa: E501

        :param unidad: The unidad of this Measure.
        :type unidad: str
        """
        allowed_values = ["Celsius", "Fahrenheit", "Kelvin"]  # noqa: E501
        if unidad not in allowed_values:
            raise ValueError(
                "Invalid value for `unidad` ({0}), must be one of {1}"
                .format(unidad, allowed_values)
            )

        self._unidad = unidad

    @property
    def medicion(self) -> float:
        """Gets the medicion of this Measure.

        Temperature measurement  # noqa: E501

        :return: The medicion of this Measure.
        :rtype: float
        """
        return self._medicion

    @medicion.setter
    def medicion(self, medicion: float):
        """Sets the medicion of this Measure.

        Temperature measurement  # noqa: E501

        :param medicion: The medicion of this Measure.
        :type medicion: float
        """

        self._medicion = medicion
