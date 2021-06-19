# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Action: Optional[str]
    Color: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Observables: Optional[Sequence["_ObservablesDefinition"]]
    ProfileOverrides: Optional[Sequence["_ProfileOverridesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Observables=deserialize_list(json_data.get("Observables"), ObservablesDefinition),
            ProfileOverrides=deserialize_list(json_data.get("ProfileOverrides"), ProfileOverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ObservablesDefinition(BaseModel):
    Confidence: Optional[str]
    Domain: Optional[str]
    IpAddress: Optional[str]
    IpAddressFirst: Optional[str]
    IpAddressLast: Optional[str]
    MailCc: Optional[str]
    MailFrom: Optional[str]
    MailReplyTo: Optional[str]
    MailSubject: Optional[str]
    MailTo: Optional[str]
    Md5: Optional[str]
    Name: Optional[str]
    Product: Optional[str]
    Severity: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObservablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObservablesDefinition"]:
        if not json_data:
            return None
        return cls(
            Confidence=json_data.get("Confidence"),
            Domain=json_data.get("Domain"),
            IpAddress=json_data.get("IpAddress"),
            IpAddressFirst=json_data.get("IpAddressFirst"),
            IpAddressLast=json_data.get("IpAddressLast"),
            MailCc=json_data.get("MailCc"),
            MailFrom=json_data.get("MailFrom"),
            MailReplyTo=json_data.get("MailReplyTo"),
            MailSubject=json_data.get("MailSubject"),
            MailTo=json_data.get("MailTo"),
            Md5=json_data.get("Md5"),
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Severity=json_data.get("Severity"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObservablesDefinition = ObservablesDefinition


@dataclass
class ProfileOverridesDefinition(BaseModel):
    Action: Optional[str]
    Profile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProfileOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfileOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Profile=json_data.get("Profile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfileOverridesDefinition = ProfileOverridesDefinition


