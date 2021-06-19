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
    CronExp: Optional[str]
    EnableEventReplication: Optional[bool]
    Id: Optional[str]
    RepoKey: Optional[str]
    Replications: Optional[Sequence["_ReplicationsDefinition"]]

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
            CronExp=json_data.get("CronExp"),
            EnableEventReplication=json_data.get("EnableEventReplication"),
            Id=json_data.get("Id"),
            RepoKey=json_data.get("RepoKey"),
            Replications=deserialize_list(json_data.get("Replications"), ReplicationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReplicationsDefinition(BaseModel):
    Enabled: Optional[bool]
    Password: Optional[str]
    PathPrefix: Optional[str]
    SocketTimeoutMillis: Optional[float]
    SyncDeletes: Optional[bool]
    SyncProperties: Optional[bool]
    SyncStatistics: Optional[bool]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Password=json_data.get("Password"),
            PathPrefix=json_data.get("PathPrefix"),
            SocketTimeoutMillis=json_data.get("SocketTimeoutMillis"),
            SyncDeletes=json_data.get("SyncDeletes"),
            SyncProperties=json_data.get("SyncProperties"),
            SyncStatistics=json_data.get("SyncStatistics"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationsDefinition = ReplicationsDefinition


