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
    Comments: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    Name: Optional[str]
    Policyid: Optional[float]
    Status: Optional[str]
    Vdomparam: Optional[str]
    Anomaly: Optional[Sequence["_AnomalyDefinition"]]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]

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
            Comments=json_data.get("Comments"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Name=json_data.get("Name"),
            Policyid=json_data.get("Policyid"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            Anomaly=deserialize_list(json_data.get("Anomaly"), AnomalyDefinition),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnomalyDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    Name: Optional[str]
    Quarantine: Optional[str]
    QuarantineExpiry: Optional[str]
    QuarantineLog: Optional[str]
    Status: Optional[str]
    Threshold: Optional[float]
    Thresholddefault: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AnomalyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnomalyDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Quarantine=json_data.get("Quarantine"),
            QuarantineExpiry=json_data.get("QuarantineExpiry"),
            QuarantineLog=json_data.get("QuarantineLog"),
            Status=json_data.get("Status"),
            Threshold=json_data.get("Threshold"),
            Thresholddefault=json_data.get("Thresholddefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnomalyDefinition = AnomalyDefinition


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class ServiceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


