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
    BootType: Optional[str]
    Bootscript: Optional[str]
    Cloudinit: Optional[str]
    DynamicIpRequired: Optional[bool]
    EnableIpv6: Optional[bool]
    Image: Optional[str]
    Name: Optional[str]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    PublicIpv6: Optional[str]
    SecurityGroup: Optional[str]
    State: Optional[str]
    StateDetail: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BootType=json_data.get("BootType"),
            Bootscript=json_data.get("Bootscript"),
            Cloudinit=json_data.get("Cloudinit"),
            DynamicIpRequired=json_data.get("DynamicIpRequired"),
            EnableIpv6=json_data.get("EnableIpv6"),
            Image=json_data.get("Image"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            PublicIpv6=json_data.get("PublicIpv6"),
            SecurityGroup=json_data.get("SecurityGroup"),
            State=json_data.get("State"),
            StateDetail=json_data.get("StateDetail"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Volume:
    SizeInGb: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            SizeInGb=json_data.get("SizeInGb"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


