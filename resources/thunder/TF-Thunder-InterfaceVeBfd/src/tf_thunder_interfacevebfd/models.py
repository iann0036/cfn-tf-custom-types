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
    Demand: Optional[float]
    Echo: Optional[float]
    Id: Optional[str]
    Ifnum: Optional[float]
    Uuid: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    IntervalCfg: Optional[Sequence["_IntervalCfgDefinition"]]

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
            Demand=json_data.get("Demand"),
            Echo=json_data.get("Echo"),
            Id=json_data.get("Id"),
            Ifnum=json_data.get("Ifnum"),
            Uuid=json_data.get("Uuid"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            IntervalCfg=deserialize_list(json_data.get("IntervalCfg"), IntervalCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthenticationDefinition(BaseModel):
    Encrypted: Optional[str]
    KeyId: Optional[float]
    Method: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            KeyId=json_data.get("KeyId"),
            Method=json_data.get("Method"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class IntervalCfgDefinition(BaseModel):
    Interval: Optional[float]
    MinRx: Optional[float]
    Multiplier: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntervalCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntervalCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            MinRx=json_data.get("MinRx"),
            Multiplier=json_data.get("Multiplier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntervalCfgDefinition = IntervalCfgDefinition


