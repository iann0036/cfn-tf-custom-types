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
    Base64Encode: Optional[bool]
    Boundary: Optional[str]
    Gzip: Optional[bool]
    Id: Optional[str]
    Rendered: Optional[str]
    Part: Optional[Sequence["_PartDefinition"]]

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
            Base64Encode=json_data.get("Base64Encode"),
            Boundary=json_data.get("Boundary"),
            Gzip=json_data.get("Gzip"),
            Id=json_data.get("Id"),
            Rendered=json_data.get("Rendered"),
            Part=deserialize_list(json_data.get("Part"), PartDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PartDefinition(BaseModel):
    Content: Optional[str]
    ContentType: Optional[str]
    Filename: Optional[str]
    MergeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            ContentType=json_data.get("ContentType"),
            Filename=json_data.get("Filename"),
            MergeType=json_data.get("MergeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartDefinition = PartDefinition


