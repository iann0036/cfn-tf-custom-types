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
    CreateTime: Optional[str]
    Description: Optional[str]
    Ipv4Count: Optional[float]
    Ipv4Info: Optional[Sequence["_Ipv4Info"]]
    Mac: Optional[str]
    Name: Optional[str]
    Primary: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    State: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    Ipv4s: Optional[Sequence["_Ipv4s"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Ipv4Count=json_data.get("Ipv4Count"),
            Ipv4Info=json_data.get("Ipv4Info"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Primary=json_data.get("Primary"),
            SecurityGroups=json_data.get("SecurityGroups"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            Ipv4s=json_data.get("Ipv4s"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ipv4Info:
    Description: Optional[str]
    Ip: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4Info"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4Info"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Ip=json_data.get("Ip"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4Info = Ipv4Info


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Ipv4s:
    Description: Optional[str]
    Ip: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4s"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4s"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Ip=json_data.get("Ip"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4s = Ipv4s


