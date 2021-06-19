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
    ApiEndpoints: Optional[Sequence[str]]
    Id: Optional[str]
    K8sVersion: Optional[str]
    Kubeconfig: Optional[str]
    Label: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    Pool: Optional[Sequence["_PoolDefinition"]]
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
            ApiEndpoints=json_data.get("ApiEndpoints"),
            Id=json_data.get("Id"),
            K8sVersion=json_data.get("K8sVersion"),
            Kubeconfig=json_data.get("Kubeconfig"),
            Label=json_data.get("Label"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Pool=deserialize_list(json_data.get("Pool"), PoolDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PoolDefinition(BaseModel):
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoolDefinition = PoolDefinition


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


