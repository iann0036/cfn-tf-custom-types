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
    Id: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    Cpu: Optional[Sequence["_CpuDefinition"]]
    Memory: Optional[Sequence["_MemoryDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Cpu=deserialize_list(json_data.get("Cpu"), CpuDefinition),
            Memory=deserialize_list(json_data.get("Memory"), MemoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CpuDefinition(BaseModel):
    CoresPerSocket: Optional[str]
    Count: Optional[str]
    LimitInMhz: Optional[str]
    ReservationGuarantee: Optional[str]
    Shares: Optional[str]
    SpeedInMhz: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CpuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuDefinition"]:
        if not json_data:
            return None
        return cls(
            CoresPerSocket=json_data.get("CoresPerSocket"),
            Count=json_data.get("Count"),
            LimitInMhz=json_data.get("LimitInMhz"),
            ReservationGuarantee=json_data.get("ReservationGuarantee"),
            Shares=json_data.get("Shares"),
            SpeedInMhz=json_data.get("SpeedInMhz"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuDefinition = CpuDefinition


@dataclass
class MemoryDefinition(BaseModel):
    LimitInMb: Optional[str]
    ReservationGuarantee: Optional[str]
    Shares: Optional[str]
    SizeInMb: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryDefinition"]:
        if not json_data:
            return None
        return cls(
            LimitInMb=json_data.get("LimitInMb"),
            ReservationGuarantee=json_data.get("ReservationGuarantee"),
            Shares=json_data.get("Shares"),
            SizeInMb=json_data.get("SizeInMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryDefinition = MemoryDefinition


