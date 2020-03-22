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
    AssignIpv6AddressOnCreation: Optional[bool]
    AvailabilityZone: Optional[str]
    AvailabilityZoneId: Optional[str]
    CidrBlock: Optional[str]
    Id: Optional[str]
    Ipv6CidrBlock: Optional[str]
    Ipv6CidrBlockAssociationId: Optional[str]
    MapPublicIpOnLaunch: Optional[bool]
    OwnerId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    Timeouts: Optional["_Timeouts"]

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
            AssignIpv6AddressOnCreation=json_data.get("AssignIpv6AddressOnCreation"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AvailabilityZoneId=json_data.get("AvailabilityZoneId"),
            CidrBlock=json_data.get("CidrBlock"),
            Id=json_data.get("Id"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            Ipv6CidrBlockAssociationId=json_data.get("Ipv6CidrBlockAssociationId"),
            MapPublicIpOnLaunch=json_data.get("MapPublicIpOnLaunch"),
            OwnerId=json_data.get("OwnerId"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


