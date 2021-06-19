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
    CloudRef: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    VcenterCredentialsRef: Optional[str]
    VcenterUrl: Optional[str]
    ContentLib: Optional[Sequence["_ContentLibDefinition"]]

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
            CloudRef=json_data.get("CloudRef"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            VcenterCredentialsRef=json_data.get("VcenterCredentialsRef"),
            VcenterUrl=json_data.get("VcenterUrl"),
            ContentLib=deserialize_list(json_data.get("ContentLib"), ContentLibDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContentLibDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentLibDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentLibDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentLibDefinition = ContentLibDefinition


