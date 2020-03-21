# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Connect: Optional[bool]
    Datacenter: Optional[str]
    Name: Optional[str]
    Near: Optional[str]
    OnlyPassing: Optional[bool]
    Service: Optional[str]
    Session: Optional[str]
    StoredToken: Optional[str]
    Tags: Optional[Sequence[str]]
    Token: Optional[str]
    Dns: Optional[Sequence["_Dns"]]
    Failover: Optional[Sequence["_Failover"]]
    Template: Optional[Sequence["_Template"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Connect=json_data.get("Connect"),
            Datacenter=json_data.get("Datacenter"),
            Name=json_data.get("Name"),
            Near=json_data.get("Near"),
            OnlyPassing=json_data.get("OnlyPassing"),
            Service=json_data.get("Service"),
            Session=json_data.get("Session"),
            StoredToken=json_data.get("StoredToken"),
            Tags=json_data.get("Tags"),
            Token=json_data.get("Token"),
            Dns=json_data.get("Dns"),
            Failover=json_data.get("Failover"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Dns:
    Ttl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dns"]:
        if not json_data:
            return None
        return cls(
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dns = Dns


@dataclass
class Failover:
    Datacenters: Optional[Sequence[str]]
    NearestN: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Failover"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Failover"]:
        if not json_data:
            return None
        return cls(
            Datacenters=json_data.get("Datacenters"),
            NearestN=json_data.get("NearestN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Failover = Failover


@dataclass
class Template:
    Regexp: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Template"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Template"]:
        if not json_data:
            return None
        return cls(
            Regexp=json_data.get("Regexp"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Template = Template


