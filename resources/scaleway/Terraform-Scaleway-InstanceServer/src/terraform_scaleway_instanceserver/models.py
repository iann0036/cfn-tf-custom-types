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
    AdditionalVolumeIds: Optional[Sequence[str]]
    BootType: Optional[str]
    CloudInit: Optional[str]
    DisableDynamicIp: Optional[bool]
    DisablePublicIp: Optional[bool]
    EnableDynamicIp: Optional[bool]
    EnableIpv6: Optional[bool]
    Id: Optional[str]
    Image: Optional[str]
    IpId: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6Gateway: Optional[str]
    Ipv6PrefixLength: Optional[float]
    Name: Optional[str]
    OrganizationId: Optional[str]
    PlacementGroupId: Optional[str]
    PlacementGroupPolicyRespected: Optional[bool]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    SecurityGroupId: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    Zone: Optional[str]
    RootVolume: Optional[Sequence["_RootVolume"]]
    UserData: Optional[Sequence["_UserData"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalVolumeIds=json_data.get("AdditionalVolumeIds"),
            BootType=json_data.get("BootType"),
            CloudInit=json_data.get("CloudInit"),
            DisableDynamicIp=json_data.get("DisableDynamicIp"),
            DisablePublicIp=json_data.get("DisablePublicIp"),
            EnableDynamicIp=json_data.get("EnableDynamicIp"),
            EnableIpv6=json_data.get("EnableIpv6"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            IpId=json_data.get("IpId"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Gateway=json_data.get("Ipv6Gateway"),
            Ipv6PrefixLength=json_data.get("Ipv6PrefixLength"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            PlacementGroupPolicyRespected=json_data.get("PlacementGroupPolicyRespected"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Zone=json_data.get("Zone"),
            RootVolume=json_data.get("RootVolume"),
            UserData=json_data.get("UserData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RootVolume:
    DeleteOnTermination: Optional[bool]
    SizeInGb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RootVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootVolume"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            SizeInGb=json_data.get("SizeInGb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootVolume = RootVolume


@dataclass
class UserData:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserData"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserData = UserData


