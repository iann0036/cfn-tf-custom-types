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
    Priority: Optional[float]
    Project: Optional[str]
    Region: Optional[str]
    CollectorIlb: Optional[Sequence["_CollectorIlbDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    MirroredResources: Optional[Sequence["_MirroredResourcesDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
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
            Priority=json_data.get("Priority"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            CollectorIlb=deserialize_list(json_data.get("CollectorIlb"), CollectorIlbDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            MirroredResources=deserialize_list(json_data.get("MirroredResources"), MirroredResourcesDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CollectorIlbDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CollectorIlbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CollectorIlbDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CollectorIlbDefinition = CollectorIlbDefinition


@dataclass
class FilterDefinition(BaseModel):
    CidrRanges: Optional[Sequence[str]]
    Direction: Optional[str]
    IpProtocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrRanges=json_data.get("CidrRanges"),
            Direction=json_data.get("Direction"),
            IpProtocols=json_data.get("IpProtocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class MirroredResourcesDefinition(BaseModel):
    Tags: Optional[Sequence[str]]
    Instances: Optional[Sequence["_InstancesDefinition"]]
    Subnetworks: Optional[Sequence["_SubnetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MirroredResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MirroredResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Tags=json_data.get("Tags"),
            Instances=deserialize_list(json_data.get("Instances"), InstancesDefinition),
            Subnetworks=deserialize_list(json_data.get("Subnetworks"), SubnetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MirroredResourcesDefinition = MirroredResourcesDefinition


@dataclass
class InstancesDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesDefinition = InstancesDefinition


@dataclass
class SubnetworksDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetworksDefinition = SubnetworksDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


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


