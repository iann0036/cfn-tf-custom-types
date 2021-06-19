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
    Id: Optional[str]
    Note: Optional[str]
    PgpKey: Optional[str]
    Precedence: Optional[str]
    Resource: Optional[str]
    ResourceAkas: Optional[Sequence[str]]
    Template: Optional[str]
    TemplateInput: Optional[str]
    Type: Optional[str]
    ValidFromTimestamp: Optional[str]
    ValidToTimestamp: Optional[str]
    Value: Optional[str]
    ValueKeyFingerprint: Optional[str]
    ValueSource: Optional[str]
    ValueSourceKeyFingerprint: Optional[str]
    ValueSourceUsed: Optional[bool]

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
            Id=json_data.get("Id"),
            Note=json_data.get("Note"),
            PgpKey=json_data.get("PgpKey"),
            Precedence=json_data.get("Precedence"),
            Resource=json_data.get("Resource"),
            ResourceAkas=json_data.get("ResourceAkas"),
            Template=json_data.get("Template"),
            TemplateInput=json_data.get("TemplateInput"),
            Type=json_data.get("Type"),
            ValidFromTimestamp=json_data.get("ValidFromTimestamp"),
            ValidToTimestamp=json_data.get("ValidToTimestamp"),
            Value=json_data.get("Value"),
            ValueKeyFingerprint=json_data.get("ValueKeyFingerprint"),
            ValueSource=json_data.get("ValueSource"),
            ValueSourceKeyFingerprint=json_data.get("ValueSourceKeyFingerprint"),
            ValueSourceUsed=json_data.get("ValueSourceUsed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


