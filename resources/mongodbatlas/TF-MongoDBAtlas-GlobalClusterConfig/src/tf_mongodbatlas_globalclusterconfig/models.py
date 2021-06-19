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
    ClusterName: Optional[str]
    CustomZoneMapping: Optional[Sequence["_CustomZoneMappingDefinition"]]
    Id: Optional[str]
    ProjectId: Optional[str]
    CustomZoneMappings: Optional[Sequence["_CustomZoneMappingsDefinition"]]
    ManagedNamespaces: Optional[Sequence["_ManagedNamespacesDefinition"]]

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
            ClusterName=json_data.get("ClusterName"),
            CustomZoneMapping=deserialize_list(json_data.get("CustomZoneMapping"), CustomZoneMappingDefinition),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            CustomZoneMappings=deserialize_list(json_data.get("CustomZoneMappings"), CustomZoneMappingsDefinition),
            ManagedNamespaces=deserialize_list(json_data.get("ManagedNamespaces"), ManagedNamespacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomZoneMappingDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomZoneMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomZoneMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomZoneMappingDefinition = CustomZoneMappingDefinition


@dataclass
class CustomZoneMappingsDefinition(BaseModel):
    Location: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomZoneMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomZoneMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomZoneMappingsDefinition = CustomZoneMappingsDefinition


@dataclass
class ManagedNamespacesDefinition(BaseModel):
    Collection: Optional[str]
    CustomShardKey: Optional[str]
    Db: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedNamespacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedNamespacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Collection=json_data.get("Collection"),
            CustomShardKey=json_data.get("CustomShardKey"),
            Db=json_data.get("Db"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedNamespacesDefinition = ManagedNamespacesDefinition


