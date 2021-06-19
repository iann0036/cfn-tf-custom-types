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
    Arn: Optional[str]
    DatabaseName: Optional[str]
    DeletionProtection: Optional[bool]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    ForceDestroy: Optional[bool]
    GlobalClusterIdentifier: Optional[str]
    GlobalClusterMembers: Optional[Sequence["_GlobalClusterMembersDefinition"]]
    GlobalClusterResourceId: Optional[str]
    Id: Optional[str]
    SourceDbClusterIdentifier: Optional[str]
    StorageEncrypted: Optional[bool]

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
            Arn=json_data.get("Arn"),
            DatabaseName=json_data.get("DatabaseName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            ForceDestroy=json_data.get("ForceDestroy"),
            GlobalClusterIdentifier=json_data.get("GlobalClusterIdentifier"),
            GlobalClusterMembers=deserialize_list(json_data.get("GlobalClusterMembers"), GlobalClusterMembersDefinition),
            GlobalClusterResourceId=json_data.get("GlobalClusterResourceId"),
            Id=json_data.get("Id"),
            SourceDbClusterIdentifier=json_data.get("SourceDbClusterIdentifier"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GlobalClusterMembersDefinition(BaseModel):
    DbClusterArn: Optional[str]
    IsWriter: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalClusterMembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalClusterMembersDefinition"]:
        if not json_data:
            return None
        return cls(
            DbClusterArn=json_data.get("DbClusterArn"),
            IsWriter=json_data.get("IsWriter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalClusterMembersDefinition = GlobalClusterMembersDefinition


