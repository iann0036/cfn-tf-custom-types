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
    Arn: Optional[str]
    AvailabilityZone: Optional[str]
    BlueprintId: Optional[str]
    BundleId: Optional[str]
    CpuCount: Optional[float]
    CreatedAt: Optional[str]
    Id: Optional[str]
    Ipv6Address: Optional[str]
    IsStaticIp: Optional[bool]
    KeyPairName: Optional[str]
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PublicIpAddress: Optional[str]
    RamSize: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    UserData: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BlueprintId=json_data.get("BlueprintId"),
            BundleId=json_data.get("BundleId"),
            CpuCount=json_data.get("CpuCount"),
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            Ipv6Address=json_data.get("Ipv6Address"),
            IsStaticIp=json_data.get("IsStaticIp"),
            KeyPairName=json_data.get("KeyPairName"),
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            RamSize=json_data.get("RamSize"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


