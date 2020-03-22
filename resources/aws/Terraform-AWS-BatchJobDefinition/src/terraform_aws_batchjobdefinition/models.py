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
    Arn: Optional[str]
    ContainerProperties: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]
    Revision: Optional[float]
    Type: Optional[str]
    RetryStrategy: Optional[Sequence["_RetryStrategy"]]
    Timeout: Optional[Sequence["_Timeout"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            ContainerProperties=json_data.get("ContainerProperties"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
            Revision=json_data.get("Revision"),
            Type=json_data.get("Type"),
            RetryStrategy=json_data.get("RetryStrategy"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Parameters:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class RetryStrategy:
    Attempts: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryStrategy"]:
        if not json_data:
            return None
        return cls(
            Attempts=json_data.get("Attempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryStrategy = RetryStrategy


@dataclass
class Timeout:
    AttemptDurationSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Timeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeout"]:
        if not json_data:
            return None
        return cls(
            AttemptDurationSeconds=json_data.get("AttemptDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeout = Timeout


