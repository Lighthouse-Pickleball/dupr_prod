# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExternalInviteRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'str',
        'full_name': 'str',
        'identifier': 'str',
        'iso_code': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'email',
        'full_name': 'fullName',
        'identifier': 'identifier',
        'iso_code': 'isoCode',
        'phone': 'phone'
    }

    def __init__(self, email=None, full_name=None, identifier=None, iso_code=None, phone=None):  # noqa: E501
        """ExternalInviteRequest - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._full_name = None
        self._identifier = None
        self._iso_code = None
        self._phone = None
        self.discriminator = None
        self.email = email
        if full_name is not None:
            self.full_name = full_name
        if identifier is not None:
            self.identifier = identifier
        if iso_code is not None:
            self.iso_code = iso_code
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this ExternalInviteRequest.  # noqa: E501


        :return: The email of this ExternalInviteRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ExternalInviteRequest.


        :param email: The email of this ExternalInviteRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this ExternalInviteRequest.  # noqa: E501


        :return: The full_name of this ExternalInviteRequest.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ExternalInviteRequest.


        :param full_name: The full_name of this ExternalInviteRequest.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def identifier(self):
        """Gets the identifier of this ExternalInviteRequest.  # noqa: E501


        :return: The identifier of this ExternalInviteRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExternalInviteRequest.


        :param identifier: The identifier of this ExternalInviteRequest.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def iso_code(self):
        """Gets the iso_code of this ExternalInviteRequest.  # noqa: E501


        :return: The iso_code of this ExternalInviteRequest.  # noqa: E501
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """Sets the iso_code of this ExternalInviteRequest.


        :param iso_code: The iso_code of this ExternalInviteRequest.  # noqa: E501
        :type: str
        """

        self._iso_code = iso_code

    @property
    def phone(self):
        """Gets the phone of this ExternalInviteRequest.  # noqa: E501


        :return: The phone of this ExternalInviteRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ExternalInviteRequest.


        :param phone: The phone of this ExternalInviteRequest.  # noqa: E501
        :type: str
        """

        self._phone = phone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ExternalInviteRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalInviteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
