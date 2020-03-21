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
    ContainerId: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    StartAction: Optional[str]
    StartDelay: Optional[float]
    StartOrder: Optional[float]
    StopAction: Optional[str]
    StopDelay: Optional[float]
    Tags: Optional[Sequence[str]]
    TargetId: Optional[str]
    WaitForGuest: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ContainerId=json_data.get("ContainerId"),
            CustomAttributes=json_data.get("CustomAttributes"),
            StartAction=json_data.get("StartAction"),
            StartDelay=json_data.get("StartDelay"),
            StartOrder=json_data.get("StartOrder"),
            StopAction=json_data.get("StopAction"),
            StopDelay=json_data.get("StopDelay"),
            Tags=json_data.get("Tags"),
            TargetId=json_data.get("TargetId"),
            WaitForGuest=json_data.get("WaitForGuest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributes = CustomAttributes


