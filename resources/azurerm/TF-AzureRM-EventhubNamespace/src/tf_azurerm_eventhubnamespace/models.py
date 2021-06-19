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
    AutoInflateEnabled: Optional[bool]
    Capacity: Optional[float]
    DedicatedClusterId: Optional[str]
    DefaultPrimaryConnectionString: Optional[str]
    DefaultPrimaryConnectionStringAlias: Optional[str]
    DefaultPrimaryKey: Optional[str]
    DefaultSecondaryConnectionString: Optional[str]
    DefaultSecondaryConnectionStringAlias: Optional[str]
    DefaultSecondaryKey: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MaximumThroughputUnits: Optional[float]
    Name: Optional[str]
    NetworkRulesets: Optional[Sequence["_NetworkRulesetsDefinition3"]]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ZoneRedundant: Optional[bool]
    Identity: Optional[Sequence["_IdentityDefinition"]]
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
            AutoInflateEnabled=json_data.get("AutoInflateEnabled"),
            Capacity=json_data.get("Capacity"),
            DedicatedClusterId=json_data.get("DedicatedClusterId"),
            DefaultPrimaryConnectionString=json_data.get("DefaultPrimaryConnectionString"),
            DefaultPrimaryConnectionStringAlias=json_data.get("DefaultPrimaryConnectionStringAlias"),
            DefaultPrimaryKey=json_data.get("DefaultPrimaryKey"),
            DefaultSecondaryConnectionString=json_data.get("DefaultSecondaryConnectionString"),
            DefaultSecondaryConnectionStringAlias=json_data.get("DefaultSecondaryConnectionStringAlias"),
            DefaultSecondaryKey=json_data.get("DefaultSecondaryKey"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MaximumThroughputUnits=json_data.get("MaximumThroughputUnits"),
            Name=json_data.get("Name"),
            NetworkRulesets=deserialize_list(json_data.get("NetworkRulesets"), NetworkRulesetsDefinition3),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ZoneRedundant=json_data.get("ZoneRedundant"),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkRulesetsDefinition3(BaseModel):
    DefaultAction: Optional[str]
    IpRule: Optional[Sequence["_NetworkRulesetsDefinition"]]
    TrustedServiceAccessEnabled: Optional[bool]
    VirtualNetworkRule: Optional[Sequence["_NetworkRulesetsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRulesetsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRulesetsDefinition3"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            IpRule=deserialize_list(json_data.get("IpRule"), NetworkRulesetsDefinition),
            TrustedServiceAccessEnabled=json_data.get("TrustedServiceAccessEnabled"),
            VirtualNetworkRule=deserialize_list(json_data.get("VirtualNetworkRule"), NetworkRulesetsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRulesetsDefinition3 = NetworkRulesetsDefinition3


@dataclass
class NetworkRulesetsDefinition(BaseModel):
    Action: Optional[str]
    IpMask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRulesetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRulesetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpMask=json_data.get("IpMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRulesetsDefinition = NetworkRulesetsDefinition


@dataclass
class NetworkRulesetsDefinition2(BaseModel):
    IgnoreMissingVirtualNetworkServiceEndpoint: Optional[bool]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRulesetsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRulesetsDefinition2"]:
        if not json_data:
            return None
        return cls(
            IgnoreMissingVirtualNetworkServiceEndpoint=json_data.get("IgnoreMissingVirtualNetworkServiceEndpoint"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRulesetsDefinition2 = NetworkRulesetsDefinition2


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
class IdentityDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


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


