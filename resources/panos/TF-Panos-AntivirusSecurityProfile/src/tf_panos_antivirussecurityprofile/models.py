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
    DeviceGroup: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PacketCapture: Optional[bool]
    ThreatExceptions: Optional[Sequence[str]]
    Vsys: Optional[str]
    ApplicationException: Optional[Sequence["_ApplicationExceptionDefinition"]]
    Decoder: Optional[Sequence["_DecoderDefinition"]]
    MachineLearningException: Optional[Sequence["_MachineLearningExceptionDefinition"]]
    MachineLearningModel: Optional[Sequence["_MachineLearningModelDefinition"]]

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
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PacketCapture=json_data.get("PacketCapture"),
            ThreatExceptions=json_data.get("ThreatExceptions"),
            Vsys=json_data.get("Vsys"),
            ApplicationException=deserialize_list(json_data.get("ApplicationException"), ApplicationExceptionDefinition),
            Decoder=deserialize_list(json_data.get("Decoder"), DecoderDefinition),
            MachineLearningException=deserialize_list(json_data.get("MachineLearningException"), MachineLearningExceptionDefinition),
            MachineLearningModel=deserialize_list(json_data.get("MachineLearningModel"), MachineLearningModelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationExceptionDefinition(BaseModel):
    Action: Optional[str]
    Application: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationExceptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationExceptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Application=json_data.get("Application"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationExceptionDefinition = ApplicationExceptionDefinition


@dataclass
class DecoderDefinition(BaseModel):
    Action: Optional[str]
    MachineLearningAction: Optional[str]
    Name: Optional[str]
    WildfireAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DecoderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecoderDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            MachineLearningAction=json_data.get("MachineLearningAction"),
            Name=json_data.get("Name"),
            WildfireAction=json_data.get("WildfireAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecoderDefinition = DecoderDefinition


@dataclass
class MachineLearningExceptionDefinition(BaseModel):
    Description: Optional[str]
    Filename: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineLearningExceptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineLearningExceptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Filename=json_data.get("Filename"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineLearningExceptionDefinition = MachineLearningExceptionDefinition


@dataclass
class MachineLearningModelDefinition(BaseModel):
    Action: Optional[str]
    Model: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineLearningModelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineLearningModelDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Model=json_data.get("Model"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineLearningModelDefinition = MachineLearningModelDefinition


