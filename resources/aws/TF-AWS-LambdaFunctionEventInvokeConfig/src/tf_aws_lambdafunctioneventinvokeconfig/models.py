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
    FunctionName: Optional[str]
    Id: Optional[str]
    MaximumEventAgeInSeconds: Optional[float]
    MaximumRetryAttempts: Optional[float]
    Qualifier: Optional[str]
    DestinationConfig: Optional[Sequence["_DestinationConfigDefinition"]]

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
            FunctionName=json_data.get("FunctionName"),
            Id=json_data.get("Id"),
            MaximumEventAgeInSeconds=json_data.get("MaximumEventAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            Qualifier=json_data.get("Qualifier"),
            DestinationConfig=deserialize_list(json_data.get("DestinationConfig"), DestinationConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationConfigDefinition(BaseModel):
    OnFailure: Optional[Sequence["_OnFailureDefinition"]]
    OnSuccess: Optional[Sequence["_OnSuccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            OnFailure=deserialize_list(json_data.get("OnFailure"), OnFailureDefinition),
            OnSuccess=deserialize_list(json_data.get("OnSuccess"), OnSuccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfigDefinition = DestinationConfigDefinition


@dataclass
class OnFailureDefinition(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailureDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailureDefinition = OnFailureDefinition


@dataclass
class OnSuccessDefinition(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnSuccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnSuccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnSuccessDefinition = OnSuccessDefinition


