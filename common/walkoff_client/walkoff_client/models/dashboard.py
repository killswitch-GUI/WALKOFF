# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Dashboard(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id_': 'str',
        'name': 'str',
        'widgets': 'list[Widget]'
    }

    attribute_map = {
        'id_': 'id_',
        'name': 'name',
        'widgets': 'widgets'
    }

    def __init__(self, id_=None, name=None, widgets=None):  # noqa: E501
        """Dashboard - a model defined in OpenAPI"""  # noqa: E501

        self._id_ = None
        self._name = None
        self._widgets = None
        self.discriminator = None

        if id_ is not None:
            self.id_ = id_
        self.name = name
        if widgets is not None:
            self.widgets = widgets

    @property
    def id_(self):
        """Gets the id_ of this Dashboard.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The id_ of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._id_

    @id_.setter
    def id_(self, id_):
        """Sets the id_ of this Dashboard.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param id_: The id_ of this Dashboard.  # noqa: E501
        :type: str
        """

        self._id_ = id_

    @property
    def name(self):
        """Gets the name of this Dashboard.  # noqa: E501

        Name of the dashboard  # noqa: E501

        :return: The name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dashboard.

        Name of the dashboard  # noqa: E501

        :param name: The name of this Dashboard.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def widgets(self):
        """Gets the widgets of this Dashboard.  # noqa: E501

        List of widgets contained in the dashboard  # noqa: E501

        :return: The widgets of this Dashboard.  # noqa: E501
        :rtype: list[Widget]
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """Sets the widgets of this Dashboard.

        List of widgets contained in the dashboard  # noqa: E501

        :param widgets: The widgets of this Dashboard.  # noqa: E501
        :type: list[Widget]
        """

        self._widgets = widgets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
