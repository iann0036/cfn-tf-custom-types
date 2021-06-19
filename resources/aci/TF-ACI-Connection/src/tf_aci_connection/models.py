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
    AdjType: Optional[str]
    Annotation: Optional[str]
    ConnDir: Optional[str]
    ConnType: Optional[str]
    Description: Optional[str]
    DirectConnect: Optional[str]
    Id: Optional[str]
    L4L7ServiceGraphTemplateDn: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    RelationVnsRsAbsConnectionConns: Optional[Sequence[str]]
    RelationVnsRsAbsCopyConnection: Optional[Sequence[str]]
    UnicastRoute: Optional[str]

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
            AdjType=json_data.get("AdjType"),
            Annotation=json_data.get("Annotation"),
            ConnDir=json_data.get("ConnDir"),
            ConnType=json_data.get("ConnType"),
            Description=json_data.get("Description"),
            DirectConnect=json_data.get("DirectConnect"),
            Id=json_data.get("Id"),
            L4L7ServiceGraphTemplateDn=json_data.get("L4L7ServiceGraphTemplateDn"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            RelationVnsRsAbsConnectionConns=json_data.get("RelationVnsRsAbsConnectionConns"),
            RelationVnsRsAbsCopyConnection=json_data.get("RelationVnsRsAbsCopyConnection"),
            UnicastRoute=json_data.get("UnicastRoute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


