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
    Description: Optional[str]
    MacAddress: Optional[str]
    PrivateDnsName: Optional[str]
    PrivateIp: Optional[str]
    PrivateIps: Optional[Sequence[str]]
    PrivateIpsCount: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SourceDestCheck: Optional[bool]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Attachment: Optional[Sequence["_Attachment"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            MacAddress=json_data.get("MacAddress"),
            PrivateDnsName=json_data.get("PrivateDnsName"),
            PrivateIp=json_data.get("PrivateIp"),
            PrivateIps=json_data.get("PrivateIps"),
            PrivateIpsCount=json_data.get("PrivateIpsCount"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SourceDestCheck=json_data.get("SourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            Attachment=json_data.get("Attachment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class Attachment:
    DeviceIndex: Optional[float]
    Instance: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attachment"]:
        if not json_data:
            return None
        return cls(
            DeviceIndex=json_data.get("DeviceIndex"),
            Instance=json_data.get("Instance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attachment = Attachment


