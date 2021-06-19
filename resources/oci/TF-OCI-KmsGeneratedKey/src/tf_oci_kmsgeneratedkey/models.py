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
    AssociatedData: Optional[Sequence["_AssociatedDataDefinition"]]
    Ciphertext: Optional[str]
    CryptoEndpoint: Optional[str]
    Id: Optional[str]
    IncludePlaintextKey: Optional[bool]
    KeyId: Optional[str]
    LoggingContext: Optional[Sequence["_LoggingContextDefinition"]]
    Plaintext: Optional[str]
    PlaintextChecksum: Optional[str]
    KeyShape: Optional[Sequence["_KeyShapeDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AssociatedData=deserialize_list(json_data.get("AssociatedData"), AssociatedDataDefinition),
            Ciphertext=json_data.get("Ciphertext"),
            CryptoEndpoint=json_data.get("CryptoEndpoint"),
            Id=json_data.get("Id"),
            IncludePlaintextKey=json_data.get("IncludePlaintextKey"),
            KeyId=json_data.get("KeyId"),
            LoggingContext=deserialize_list(json_data.get("LoggingContext"), LoggingContextDefinition),
            Plaintext=json_data.get("Plaintext"),
            PlaintextChecksum=json_data.get("PlaintextChecksum"),
            KeyShape=deserialize_list(json_data.get("KeyShape"), KeyShapeDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssociatedDataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociatedDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociatedDataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociatedDataDefinition = AssociatedDataDefinition


@dataclass
class LoggingContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingContextDefinition = LoggingContextDefinition


@dataclass
class KeyShapeDefinition(BaseModel):
    Algorithm: Optional[str]
    CurveId: Optional[str]
    Length: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_KeyShapeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyShapeDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            CurveId=json_data.get("CurveId"),
            Length=json_data.get("Length"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyShapeDefinition = KeyShapeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


