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
    AdminUsers: Optional[Sequence[str]]
    BackupBlobContainerUri: Optional[str]
    EnablePowerBiService: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    QuerypoolConnectionMode: Optional[str]
    ResourceGroupName: Optional[str]
    ServerFullName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Ipv4FirewallRule: Optional[Sequence["_Ipv4FirewallRuleDefinition"]]
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
            AdminUsers=json_data.get("AdminUsers"),
            BackupBlobContainerUri=json_data.get("BackupBlobContainerUri"),
            EnablePowerBiService=json_data.get("EnablePowerBiService"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            QuerypoolConnectionMode=json_data.get("QuerypoolConnectionMode"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServerFullName=json_data.get("ServerFullName"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Ipv4FirewallRule=deserialize_list(json_data.get("Ipv4FirewallRule"), Ipv4FirewallRuleDefinition),
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
class Ipv4FirewallRuleDefinition(BaseModel):
    Name: Optional[str]
    RangeEnd: Optional[str]
    RangeStart: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4FirewallRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4FirewallRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RangeEnd=json_data.get("RangeEnd"),
            RangeStart=json_data.get("RangeStart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4FirewallRuleDefinition = Ipv4FirewallRuleDefinition


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


