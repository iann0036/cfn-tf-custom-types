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
    Id: Optional[str]
    MpskConcurrentClients: Optional[float]
    Name: Optional[str]
    Vdomparam: Optional[str]
    MpskGroup: Optional[Sequence["_MpskGroupDefinition"]]

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
            Id=json_data.get("Id"),
            MpskConcurrentClients=json_data.get("MpskConcurrentClients"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            MpskGroup=deserialize_list(json_data.get("MpskGroup"), MpskGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MpskGroupDefinition(BaseModel):
    Name: Optional[str]
    VlanId: Optional[float]
    VlanType: Optional[str]
    MpskKey: Optional[Sequence["_MpskKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MpskGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MpskGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            VlanId=json_data.get("VlanId"),
            VlanType=json_data.get("VlanType"),
            MpskKey=deserialize_list(json_data.get("MpskKey"), MpskKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MpskGroupDefinition = MpskGroupDefinition


@dataclass
class MpskKeyDefinition(BaseModel):
    Comment: Optional[str]
    ConcurrentClientLimitType: Optional[str]
    ConcurrentClients: Optional[float]
    Mac: Optional[str]
    Name: Optional[str]
    Passphrase: Optional[str]
    MpskSchedules: Optional[Sequence["_MpskSchedulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MpskKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MpskKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            ConcurrentClientLimitType=json_data.get("ConcurrentClientLimitType"),
            ConcurrentClients=json_data.get("ConcurrentClients"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Passphrase=json_data.get("Passphrase"),
            MpskSchedules=deserialize_list(json_data.get("MpskSchedules"), MpskSchedulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MpskKeyDefinition = MpskKeyDefinition


@dataclass
class MpskSchedulesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MpskSchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MpskSchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MpskSchedulesDefinition = MpskSchedulesDefinition


