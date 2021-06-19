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
    DefaultAction: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    DeviceList: Optional[Sequence["_DeviceListDefinition"]]

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
            DefaultAction=json_data.get("DefaultAction"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            DeviceList=deserialize_list(json_data.get("DeviceList"), DeviceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeviceListDefinition(BaseModel):
    Action: Optional[str]
    Device: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Device=json_data.get("Device"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceListDefinition = DeviceListDefinition


