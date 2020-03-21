# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    FunctionName: Optional[str]
    Id: Optional[str]
    MaximumEventAgeInSeconds: Optional[float]
    MaximumRetryAttempts: Optional[float]
    Qualifier: Optional[str]
    DestinationConfig: Optional[Sequence["_DestinationConfig"]]
    OnFailure: Optional[Sequence["_OnFailure"]]
    OnSuccess: Optional[Sequence["_OnSuccess"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            FunctionName=json_data.get("FunctionName"),
            Id=json_data.get("Id"),
            MaximumEventAgeInSeconds=json_data.get("MaximumEventAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            Qualifier=json_data.get("Qualifier"),
            DestinationConfig=json_data.get("DestinationConfig"),
            OnFailure=json_data.get("OnFailure"),
            OnSuccess=json_data.get("OnSuccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationConfig:
    OnFailure: Optional[Sequence["_OnFailure"]]
    OnSuccess: Optional[Sequence["_OnSuccess"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfig"]:
        if not json_data:
            return None
        return cls(
            OnFailure=json_data.get("OnFailure"),
            OnSuccess=json_data.get("OnSuccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfig = DestinationConfig


@dataclass
class OnFailure:
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailure"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailure"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailure = OnFailure


@dataclass
class OnSuccess:
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnSuccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnSuccess"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnSuccess = OnSuccess


