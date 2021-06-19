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
    AccessPortSelectorDn: Optional[str]
    Annotation: Optional[str]
    Description: Optional[str]
    FromCard: Optional[str]
    FromPort: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    RelationInfraRsAccBndlSubgrp: Optional[str]
    ToCard: Optional[str]
    ToPort: Optional[str]

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
            AccessPortSelectorDn=json_data.get("AccessPortSelectorDn"),
            Annotation=json_data.get("Annotation"),
            Description=json_data.get("Description"),
            FromCard=json_data.get("FromCard"),
            FromPort=json_data.get("FromPort"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            RelationInfraRsAccBndlSubgrp=json_data.get("RelationInfraRsAccBndlSubgrp"),
            ToCard=json_data.get("ToCard"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


