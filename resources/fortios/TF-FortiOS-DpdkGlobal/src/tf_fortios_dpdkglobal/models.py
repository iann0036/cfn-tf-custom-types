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
    DynamicSortSubtable: Optional[str]
    Elasticbuffer: Optional[str]
    HugepagePercentage: Optional[float]
    Id: Optional[str]
    MbufpoolPercentage: Optional[float]
    Multiqueue: Optional[str]
    PerSessionAccounting: Optional[str]
    SleepOnIdle: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Elasticbuffer=json_data.get("Elasticbuffer"),
            HugepagePercentage=json_data.get("HugepagePercentage"),
            Id=json_data.get("Id"),
            MbufpoolPercentage=json_data.get("MbufpoolPercentage"),
            Multiqueue=json_data.get("Multiqueue"),
            PerSessionAccounting=json_data.get("PerSessionAccounting"),
            SleepOnIdle=json_data.get("SleepOnIdle"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterfaceDefinition(BaseModel):
    InterfaceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            InterfaceName=json_data.get("InterfaceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


