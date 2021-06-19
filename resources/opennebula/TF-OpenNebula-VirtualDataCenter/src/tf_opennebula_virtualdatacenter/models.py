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
    GroupIds: Optional[Sequence[float]]
    Id: Optional[str]
    Name: Optional[str]
    Zones: Optional[Sequence["_ZonesDefinition"]]

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
            GroupIds=json_data.get("GroupIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Zones=deserialize_list(json_data.get("Zones"), ZonesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ZonesDefinition(BaseModel):
    ClusterIds: Optional[Sequence[float]]
    DatastoreIds: Optional[Sequence[float]]
    HostIds: Optional[Sequence[float]]
    Id: Optional[float]
    VnetIds: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ZonesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZonesDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterIds=json_data.get("ClusterIds"),
            DatastoreIds=json_data.get("DatastoreIds"),
            HostIds=json_data.get("HostIds"),
            Id=json_data.get("Id"),
            VnetIds=json_data.get("VnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZonesDefinition = ZonesDefinition


