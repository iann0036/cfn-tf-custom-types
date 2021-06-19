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
    Ami: Optional[str]
    AvailabilityZone: Optional[str]
    BootstrapCfg: Optional[str]
    CloudProvider: Optional[str]
    Cnps: Optional[str]
    HaRtrId: Optional[str]
    Id: Optional[str]
    InternalRtTableId: Optional[Sequence[str]]
    IntfName: Optional[Sequence[str]]
    IntfPrivateIp: Optional[Sequence[str]]
    IntfType: Optional[Sequence[str]]
    IsRr: Optional[bool]
    KeyName: Optional[str]
    PeerRoutetableId: Optional[Sequence[str]]
    Peerroutetableid1: Optional[Sequence[str]]
    PrivateRtTableId: Optional[Sequence[str]]
    PublicRtTableId: Optional[Sequence[str]]
    Region: Optional[str]
    Role: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TfId: Optional[str]
    TopologyName: Optional[str]
    VpcId: Optional[str]
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
            Ami=json_data.get("Ami"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BootstrapCfg=json_data.get("BootstrapCfg"),
            CloudProvider=json_data.get("CloudProvider"),
            Cnps=json_data.get("Cnps"),
            HaRtrId=json_data.get("HaRtrId"),
            Id=json_data.get("Id"),
            InternalRtTableId=json_data.get("InternalRtTableId"),
            IntfName=json_data.get("IntfName"),
            IntfPrivateIp=json_data.get("IntfPrivateIp"),
            IntfType=json_data.get("IntfType"),
            IsRr=json_data.get("IsRr"),
            KeyName=json_data.get("KeyName"),
            PeerRoutetableId=json_data.get("PeerRoutetableId"),
            Peerroutetableid1=json_data.get("Peerroutetableid1"),
            PrivateRtTableId=json_data.get("PrivateRtTableId"),
            PublicRtTableId=json_data.get("PublicRtTableId"),
            Region=json_data.get("Region"),
            Role=json_data.get("Role"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TfId=json_data.get("TfId"),
            TopologyName=json_data.get("TopologyName"),
            VpcId=json_data.get("VpcId"),
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
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


