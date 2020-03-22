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
    Address: Optional[str]
    AddressIpVersion: Optional[str]
    AddressType: Optional[str]
    Bandwidth: Optional[float]
    DeleteProtection: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    Internet: Optional[bool]
    InternetChargeType: Optional[str]
    MasterZoneId: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    ResourceGroupId: Optional[str]
    SlaveZoneId: Optional[str]
    Specification: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VswitchId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Address=json_data.get("Address"),
            AddressIpVersion=json_data.get("AddressIpVersion"),
            AddressType=json_data.get("AddressType"),
            Bandwidth=json_data.get("Bandwidth"),
            DeleteProtection=json_data.get("DeleteProtection"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            Internet=json_data.get("Internet"),
            InternetChargeType=json_data.get("InternetChargeType"),
            MasterZoneId=json_data.get("MasterZoneId"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SlaveZoneId=json_data.get("SlaveZoneId"),
            Specification=json_data.get("Specification"),
            Tags=json_data.get("Tags"),
            VswitchId=json_data.get("VswitchId"),
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


