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
    DnsServers: Optional[Sequence[str]]
    FirewallPolicyId: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrivateIpRanges: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    SkuTier: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ThreatIntelMode: Optional[str]
    Zones: Optional[Sequence[str]]
    IpConfiguration: Optional[Sequence["_IpConfigurationDefinition"]]
    ManagementIpConfiguration: Optional[Sequence["_ManagementIpConfigurationDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VirtualHub: Optional[Sequence["_VirtualHubDefinition"]]

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
            DnsServers=json_data.get("DnsServers"),
            FirewallPolicyId=json_data.get("FirewallPolicyId"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrivateIpRanges=json_data.get("PrivateIpRanges"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            SkuTier=json_data.get("SkuTier"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ThreatIntelMode=json_data.get("ThreatIntelMode"),
            Zones=json_data.get("Zones"),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), IpConfigurationDefinition),
            ManagementIpConfiguration=deserialize_list(json_data.get("ManagementIpConfiguration"), ManagementIpConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VirtualHub=deserialize_list(json_data.get("VirtualHub"), VirtualHubDefinition),
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
class IpConfigurationDefinition(BaseModel):
    Name: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigurationDefinition = IpConfigurationDefinition


@dataclass
class ManagementIpConfigurationDefinition(BaseModel):
    Name: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementIpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementIpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementIpConfigurationDefinition = ManagementIpConfigurationDefinition


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


@dataclass
class VirtualHubDefinition(BaseModel):
    PublicIpCount: Optional[float]
    VirtualHubId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualHubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualHubDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicIpCount=json_data.get("PublicIpCount"),
            VirtualHubId=json_data.get("VirtualHubId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualHubDefinition = VirtualHubDefinition


