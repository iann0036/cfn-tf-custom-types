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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    FrontendIpConfiguration: Optional[Sequence["_FrontendIpConfigurationDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            FrontendIpConfiguration=deserialize_list(json_data.get("FrontendIpConfiguration"), FrontendIpConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class FrontendIpConfigurationDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PrivateIpAddressVersion: Optional[str]
    PublicIpAddressId: Optional[str]
    PublicIpPrefixId: Optional[str]
    SubnetId: Optional[str]
    Zones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendIpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendIpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddressAllocation=json_data.get("PrivateIpAddressAllocation"),
            PrivateIpAddressVersion=json_data.get("PrivateIpAddressVersion"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            PublicIpPrefixId=json_data.get("PublicIpPrefixId"),
            SubnetId=json_data.get("SubnetId"),
            Zones=json_data.get("Zones"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendIpConfigurationDefinition = FrontendIpConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


