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
    Annotation: Optional[str]
    Description: Optional[str]
    DhcpOptionIds: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    TenantDn: Optional[str]
    DhcpOption: Optional[Sequence["_DhcpOptionDefinition"]]

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
            Annotation=json_data.get("Annotation"),
            Description=json_data.get("Description"),
            DhcpOptionIds=json_data.get("DhcpOptionIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            TenantDn=json_data.get("TenantDn"),
            DhcpOption=deserialize_list(json_data.get("DhcpOption"), DhcpOptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DhcpOptionDefinition(BaseModel):
    Annotation: Optional[str]
    Data: Optional[str]
    DhcpOptionId: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotation=json_data.get("Annotation"),
            Data=json_data.get("Data"),
            DhcpOptionId=json_data.get("DhcpOptionId"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpOptionDefinition = DhcpOptionDefinition


