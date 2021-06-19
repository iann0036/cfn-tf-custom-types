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
    EnableUserId: Optional[bool]
    ExcludeAcls: Optional[Sequence[str]]
    Id: Optional[str]
    IncludeAcls: Optional[Sequence[str]]
    Interfaces: Optional[Sequence[str]]
    LogSetting: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    Vsys: Optional[str]
    ZoneProfile: Optional[str]

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
            EnableUserId=json_data.get("EnableUserId"),
            ExcludeAcls=json_data.get("ExcludeAcls"),
            Id=json_data.get("Id"),
            IncludeAcls=json_data.get("IncludeAcls"),
            Interfaces=json_data.get("Interfaces"),
            LogSetting=json_data.get("LogSetting"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            Vsys=json_data.get("Vsys"),
            ZoneProfile=json_data.get("ZoneProfile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


