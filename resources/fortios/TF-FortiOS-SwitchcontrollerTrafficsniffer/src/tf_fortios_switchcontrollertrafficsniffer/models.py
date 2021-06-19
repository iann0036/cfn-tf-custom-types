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
    ErspanIp: Optional[str]
    Id: Optional[str]
    Mode: Optional[str]
    Vdomparam: Optional[str]
    TargetIp: Optional[Sequence["_TargetIpDefinition"]]
    TargetMac: Optional[Sequence["_TargetMacDefinition"]]
    TargetPort: Optional[Sequence["_TargetPortDefinition"]]

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
            ErspanIp=json_data.get("ErspanIp"),
            Id=json_data.get("Id"),
            Mode=json_data.get("Mode"),
            Vdomparam=json_data.get("Vdomparam"),
            TargetIp=deserialize_list(json_data.get("TargetIp"), TargetIpDefinition),
            TargetMac=deserialize_list(json_data.get("TargetMac"), TargetMacDefinition),
            TargetPort=deserialize_list(json_data.get("TargetPort"), TargetPortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TargetIpDefinition(BaseModel):
    Description: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetIpDefinition = TargetIpDefinition


@dataclass
class TargetMacDefinition(BaseModel):
    Description: Optional[str]
    Mac: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetMacDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetMacDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Mac=json_data.get("Mac"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetMacDefinition = TargetMacDefinition


@dataclass
class TargetPortDefinition(BaseModel):
    Description: Optional[str]
    SwitchId: Optional[str]
    InPorts: Optional[Sequence["_InPortsDefinition"]]
    OutPorts: Optional[Sequence["_OutPortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            SwitchId=json_data.get("SwitchId"),
            InPorts=deserialize_list(json_data.get("InPorts"), InPortsDefinition),
            OutPorts=deserialize_list(json_data.get("OutPorts"), OutPortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetPortDefinition = TargetPortDefinition


@dataclass
class InPortsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InPortsDefinition = InPortsDefinition


@dataclass
class OutPortsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutPortsDefinition = OutPortsDefinition


