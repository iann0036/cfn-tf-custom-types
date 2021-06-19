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
    AddressFamily: Optional[str]
    Enable: Optional[bool]
    Id: Optional[str]
    Metric: Optional[float]
    Name: Optional[str]
    RouteTable: Optional[str]
    SetAsPathLimit: Optional[float]
    SetCommunities: Optional[Sequence[str]]
    SetExtendedCommunities: Optional[Sequence[str]]
    SetLocalPreference: Optional[str]
    SetMed: Optional[str]
    SetOrigin: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    VirtualRouter: Optional[str]

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
            AddressFamily=json_data.get("AddressFamily"),
            Enable=json_data.get("Enable"),
            Id=json_data.get("Id"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            RouteTable=json_data.get("RouteTable"),
            SetAsPathLimit=json_data.get("SetAsPathLimit"),
            SetCommunities=json_data.get("SetCommunities"),
            SetExtendedCommunities=json_data.get("SetExtendedCommunities"),
            SetLocalPreference=json_data.get("SetLocalPreference"),
            SetMed=json_data.get("SetMed"),
            SetOrigin=json_data.get("SetOrigin"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


