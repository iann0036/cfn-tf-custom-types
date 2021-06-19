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
    Autolasthop: Optional[str]
    FullPath: Optional[str]
    Id: Optional[str]
    Mirror: Optional[str]
    Name: Optional[str]
    Partition: Optional[str]
    Snatpool: Optional[str]
    Sourceport: Optional[str]
    Translation: Optional[str]
    Vlans: Optional[Sequence[str]]
    Vlansdisabled: Optional[bool]
    Origins: Optional[Sequence["_OriginsDefinition"]]

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
            Autolasthop=json_data.get("Autolasthop"),
            FullPath=json_data.get("FullPath"),
            Id=json_data.get("Id"),
            Mirror=json_data.get("Mirror"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            Snatpool=json_data.get("Snatpool"),
            Sourceport=json_data.get("Sourceport"),
            Translation=json_data.get("Translation"),
            Vlans=json_data.get("Vlans"),
            Vlansdisabled=json_data.get("Vlansdisabled"),
            Origins=deserialize_list(json_data.get("Origins"), OriginsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OriginsDefinition(BaseModel):
    AppService: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginsDefinition"]:
        if not json_data:
            return None
        return cls(
            AppService=json_data.get("AppService"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginsDefinition = OriginsDefinition


