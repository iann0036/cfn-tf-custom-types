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
    Descriptor: Optional[str]
    DisplayName: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    Mail: Optional[str]
    Members: Optional[Sequence[str]]
    Origin: Optional[str]
    OriginId: Optional[str]
    PrincipalName: Optional[str]
    Scope: Optional[str]
    SubjectKind: Optional[str]
    Url: Optional[str]

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
            Descriptor=json_data.get("Descriptor"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Mail=json_data.get("Mail"),
            Members=json_data.get("Members"),
            Origin=json_data.get("Origin"),
            OriginId=json_data.get("OriginId"),
            PrincipalName=json_data.get("PrincipalName"),
            Scope=json_data.get("Scope"),
            SubjectKind=json_data.get("SubjectKind"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


