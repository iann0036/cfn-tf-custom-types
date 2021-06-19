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
    Action: Optional[str]
    Comments: Optional[str]
    DstNegate: Optional[str]
    DynamicSortSubtable: Optional[str]
    EndPort: Optional[float]
    EndSourcePort: Optional[float]
    Gateway: Optional[str]
    Id: Optional[str]
    InputDeviceNegate: Optional[str]
    OutputDevice: Optional[str]
    Protocol: Optional[float]
    SeqNum: Optional[float]
    SrcNegate: Optional[str]
    StartPort: Optional[float]
    StartSourcePort: Optional[float]
    Status: Optional[str]
    Tos: Optional[str]
    TosMask: Optional[str]
    Vdomparam: Optional[str]
    Dst: Optional[Sequence["_DstDefinition"]]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    InputDevice: Optional[Sequence["_InputDeviceDefinition"]]
    InternetServiceCustom: Optional[Sequence["_InternetServiceCustomDefinition"]]
    InternetServiceId: Optional[Sequence["_InternetServiceIdDefinition"]]
    Src: Optional[Sequence["_SrcDefinition"]]
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
            Action=json_data.get("Action"),
            Comments=json_data.get("Comments"),
            DstNegate=json_data.get("DstNegate"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EndPort=json_data.get("EndPort"),
            EndSourcePort=json_data.get("EndSourcePort"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            InputDeviceNegate=json_data.get("InputDeviceNegate"),
            OutputDevice=json_data.get("OutputDevice"),
            Protocol=json_data.get("Protocol"),
            SeqNum=json_data.get("SeqNum"),
            SrcNegate=json_data.get("SrcNegate"),
            StartPort=json_data.get("StartPort"),
            StartSourcePort=json_data.get("StartSourcePort"),
            Status=json_data.get("Status"),
            Tos=json_data.get("Tos"),
            TosMask=json_data.get("TosMask"),
            Vdomparam=json_data.get("Vdomparam"),
            Dst=deserialize_list(json_data.get("Dst"), DstDefinition),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            InputDevice=deserialize_list(json_data.get("InputDevice"), InputDeviceDefinition),
            InternetServiceCustom=deserialize_list(json_data.get("InternetServiceCustom"), InternetServiceCustomDefinition),
            InternetServiceId=deserialize_list(json_data.get("InternetServiceId"), InternetServiceIdDefinition),
            Src=deserialize_list(json_data.get("Src"), SrcDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DstDefinition(BaseModel):
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstDefinition"]:
        if not json_data:
            return None
        return cls(
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstDefinition = DstDefinition


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
class InputDeviceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDeviceDefinition = InputDeviceDefinition


@dataclass
class InternetServiceCustomDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCustomDefinition = InternetServiceCustomDefinition


@dataclass
class InternetServiceIdDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceIdDefinition = InternetServiceIdDefinition


@dataclass
class SrcDefinition(BaseModel):
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcDefinition"]:
        if not json_data:
            return None
        return cls(
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcDefinition = SrcDefinition


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


