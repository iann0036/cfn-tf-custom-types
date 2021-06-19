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
    Namespace: Optional[str]
    Policies: Optional[Sequence[str]]
    ServiceIdentities: Optional[Sequence["_ServiceIdentitiesDefinition"]]

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
            Namespace=json_data.get("Namespace"),
            Policies=json_data.get("Policies"),
            ServiceIdentities=deserialize_list(json_data.get("ServiceIdentities"), ServiceIdentitiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceIdentitiesDefinition(BaseModel):
    Datacenters: Optional[Sequence[str]]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIdentitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIdentitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenters=json_data.get("Datacenters"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIdentitiesDefinition = ServiceIdentitiesDefinition


