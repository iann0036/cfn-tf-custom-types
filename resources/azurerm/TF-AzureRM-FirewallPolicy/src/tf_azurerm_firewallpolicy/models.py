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
    BasePolicyId: Optional[str]
    ChildPolicies: Optional[Sequence[str]]
    Firewalls: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    RuleCollectionGroups: Optional[Sequence[str]]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ThreatIntelligenceMode: Optional[str]
    Dns: Optional[Sequence["_DnsDefinition"]]
    ThreatIntelligenceAllowlist: Optional[Sequence["_ThreatIntelligenceAllowlistDefinition"]]
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
            BasePolicyId=json_data.get("BasePolicyId"),
            ChildPolicies=json_data.get("ChildPolicies"),
            Firewalls=json_data.get("Firewalls"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RuleCollectionGroups=json_data.get("RuleCollectionGroups"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ThreatIntelligenceMode=json_data.get("ThreatIntelligenceMode"),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
            ThreatIntelligenceAllowlist=deserialize_list(json_data.get("ThreatIntelligenceAllowlist"), ThreatIntelligenceAllowlistDefinition),
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
class DnsDefinition(BaseModel):
    NetworkRuleFqdnEnabled: Optional[bool]
    ProxyEnabled: Optional[bool]
    Servers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRuleFqdnEnabled=json_data.get("NetworkRuleFqdnEnabled"),
            ProxyEnabled=json_data.get("ProxyEnabled"),
            Servers=json_data.get("Servers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


@dataclass
class ThreatIntelligenceAllowlistDefinition(BaseModel):
    Fqdns: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelligenceAllowlistDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelligenceAllowlistDefinition"]:
        if not json_data:
            return None
        return cls(
            Fqdns=json_data.get("Fqdns"),
            IpAddresses=json_data.get("IpAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelligenceAllowlistDefinition = ThreatIntelligenceAllowlistDefinition


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


