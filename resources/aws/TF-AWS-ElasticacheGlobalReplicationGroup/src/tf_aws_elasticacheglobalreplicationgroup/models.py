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
    ActualEngineVersion: Optional[str]
    Arn: Optional[str]
    AtRestEncryptionEnabled: Optional[bool]
    AuthTokenEnabled: Optional[bool]
    CacheNodeType: Optional[str]
    ClusterEnabled: Optional[bool]
    Engine: Optional[str]
    EngineVersionActual: Optional[str]
    GlobalReplicationGroupDescription: Optional[str]
    GlobalReplicationGroupId: Optional[str]
    GlobalReplicationGroupIdSuffix: Optional[str]
    Id: Optional[str]
    PrimaryReplicationGroupId: Optional[str]
    TransitEncryptionEnabled: Optional[bool]

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
            ActualEngineVersion=json_data.get("ActualEngineVersion"),
            Arn=json_data.get("Arn"),
            AtRestEncryptionEnabled=json_data.get("AtRestEncryptionEnabled"),
            AuthTokenEnabled=json_data.get("AuthTokenEnabled"),
            CacheNodeType=json_data.get("CacheNodeType"),
            ClusterEnabled=json_data.get("ClusterEnabled"),
            Engine=json_data.get("Engine"),
            EngineVersionActual=json_data.get("EngineVersionActual"),
            GlobalReplicationGroupDescription=json_data.get("GlobalReplicationGroupDescription"),
            GlobalReplicationGroupId=json_data.get("GlobalReplicationGroupId"),
            GlobalReplicationGroupIdSuffix=json_data.get("GlobalReplicationGroupIdSuffix"),
            Id=json_data.get("Id"),
            PrimaryReplicationGroupId=json_data.get("PrimaryReplicationGroupId"),
            TransitEncryptionEnabled=json_data.get("TransitEncryptionEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


