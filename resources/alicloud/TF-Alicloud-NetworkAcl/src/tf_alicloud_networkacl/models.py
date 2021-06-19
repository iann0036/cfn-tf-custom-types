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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NetworkAclName: Optional[str]
    Status: Optional[str]
    VpcId: Optional[str]
    EgressAclEntries: Optional[Sequence["_EgressAclEntriesDefinition"]]
    IngressAclEntries: Optional[Sequence["_IngressAclEntriesDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkAclName=json_data.get("NetworkAclName"),
            Status=json_data.get("Status"),
            VpcId=json_data.get("VpcId"),
            EgressAclEntries=deserialize_list(json_data.get("EgressAclEntries"), EgressAclEntriesDefinition),
            IngressAclEntries=deserialize_list(json_data.get("IngressAclEntries"), IngressAclEntriesDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EgressAclEntriesDefinition(BaseModel):
    Description: Optional[str]
    DestinationCidrIp: Optional[str]
    NetworkAclEntryName: Optional[str]
    Policy: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EgressAclEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressAclEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DestinationCidrIp=json_data.get("DestinationCidrIp"),
            NetworkAclEntryName=json_data.get("NetworkAclEntryName"),
            Policy=json_data.get("Policy"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressAclEntriesDefinition = EgressAclEntriesDefinition


@dataclass
class IngressAclEntriesDefinition(BaseModel):
    Description: Optional[str]
    NetworkAclEntryName: Optional[str]
    Policy: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
    SourceCidrIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngressAclEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressAclEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            NetworkAclEntryName=json_data.get("NetworkAclEntryName"),
            Policy=json_data.get("Policy"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SourceCidrIp=json_data.get("SourceCidrIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressAclEntriesDefinition = IngressAclEntriesDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    ResourceId: Optional[str]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


