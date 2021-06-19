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
    ClosId: Optional[str]
    ClosName: Optional[str]
    CloudProvider: Optional[str]
    Cnps: Optional[str]
    Id: Optional[str]
    PeerRgName: Optional[str]
    PeerVnetId: Optional[str]
    PeerVnetName: Optional[str]
    PeerVpcCidr: Optional[str]
    PeerVpcId: Optional[str]
    Peervpcidr: Optional[str]
    Region: Optional[str]
    RgName: Optional[str]
    Role: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TfId: Optional[str]
    TopologyId: Optional[str]
    TopologyName: Optional[str]
    VnetName: Optional[str]
    WanId: Optional[str]
    WanName: Optional[str]
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
            ClosId=json_data.get("ClosId"),
            ClosName=json_data.get("ClosName"),
            CloudProvider=json_data.get("CloudProvider"),
            Cnps=json_data.get("Cnps"),
            Id=json_data.get("Id"),
            PeerRgName=json_data.get("PeerRgName"),
            PeerVnetId=json_data.get("PeerVnetId"),
            PeerVnetName=json_data.get("PeerVnetName"),
            PeerVpcCidr=json_data.get("PeerVpcCidr"),
            PeerVpcId=json_data.get("PeerVpcId"),
            Peervpcidr=json_data.get("Peervpcidr"),
            Region=json_data.get("Region"),
            RgName=json_data.get("RgName"),
            Role=json_data.get("Role"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TfId=json_data.get("TfId"),
            TopologyId=json_data.get("TopologyId"),
            TopologyName=json_data.get("TopologyName"),
            VnetName=json_data.get("VnetName"),
            WanId=json_data.get("WanId"),
            WanName=json_data.get("WanName"),
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


