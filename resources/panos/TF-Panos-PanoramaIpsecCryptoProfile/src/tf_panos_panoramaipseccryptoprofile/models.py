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
    Authentications: Optional[Sequence[str]]
    DhGroup: Optional[str]
    Encryptions: Optional[Sequence[str]]
    Id: Optional[str]
    LifesizeType: Optional[str]
    LifesizeValue: Optional[float]
    LifetimeType: Optional[str]
    LifetimeValue: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]

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
            Authentications=json_data.get("Authentications"),
            DhGroup=json_data.get("DhGroup"),
            Encryptions=json_data.get("Encryptions"),
            Id=json_data.get("Id"),
            LifesizeType=json_data.get("LifesizeType"),
            LifesizeValue=json_data.get("LifesizeValue"),
            LifetimeType=json_data.get("LifetimeType"),
            LifetimeValue=json_data.get("LifetimeValue"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


