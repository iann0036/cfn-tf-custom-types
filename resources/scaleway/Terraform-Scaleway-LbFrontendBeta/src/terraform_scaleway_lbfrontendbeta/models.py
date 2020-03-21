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
    BackendId: Optional[str]
    CertificateId: Optional[str]
    InboundPort: Optional[float]
    LbId: Optional[str]
    Name: Optional[str]
    TimeoutClient: Optional[str]
    Acl: Optional[Sequence["_Acl"]]
    Action: Optional[Sequence["_Action"]]
    Match: Optional[Sequence["_Match"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackendId=json_data.get("BackendId"),
            CertificateId=json_data.get("CertificateId"),
            InboundPort=json_data.get("InboundPort"),
            LbId=json_data.get("LbId"),
            Name=json_data.get("Name"),
            TimeoutClient=json_data.get("TimeoutClient"),
            Acl=json_data.get("Acl"),
            Action=json_data.get("Action"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Acl:
    Name: Optional[str]
    OrganizationId: Optional[str]
    Region: Optional[str]
    Action: Optional[Sequence["_Action"]]
    Match: Optional[Sequence["_Match"]]

    @classmethod
    def _deserialize(
        cls: Type["_Acl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Acl"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            Region=json_data.get("Region"),
            Action=json_data.get("Action"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Acl = Acl


@dataclass
class Action:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Match:
    HttpFilter: Optional[str]
    HttpFilterValue: Optional[Sequence[str]]
    Invert: Optional[bool]
    IpSubnet: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Match"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Match"]:
        if not json_data:
            return None
        return cls(
            HttpFilter=json_data.get("HttpFilter"),
            HttpFilterValue=json_data.get("HttpFilterValue"),
            Invert=json_data.get("Invert"),
            IpSubnet=json_data.get("IpSubnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Match = Match


