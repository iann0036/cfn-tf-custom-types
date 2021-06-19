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
    ClusterId: Optional[str]
    ClusterMemberIds: Optional[Sequence["_ClusterMemberIdsDefinition"]]
    EcuMap: Optional[Sequence["_EcuMapDefinition"]]
    Id: Optional[str]
    InstanceIds: Optional[Sequence[str]]
    StatusMap: Optional[Sequence["_StatusMapDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            ClusterMemberIds=deserialize_list(json_data.get("ClusterMemberIds"), ClusterMemberIdsDefinition),
            EcuMap=deserialize_list(json_data.get("EcuMap"), EcuMapDefinition),
            Id=json_data.get("Id"),
            InstanceIds=json_data.get("InstanceIds"),
            StatusMap=deserialize_list(json_data.get("StatusMap"), StatusMapDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterMemberIdsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterMemberIdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterMemberIdsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterMemberIdsDefinition = ClusterMemberIdsDefinition


@dataclass
class EcuMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcuMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcuMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcuMapDefinition = EcuMapDefinition


@dataclass
class StatusMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StatusMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusMapDefinition = StatusMapDefinition


