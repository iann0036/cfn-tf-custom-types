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
    DeletionWindowInDays: Optional[float]
    Description: Optional[str]
    Enabled: Optional[bool]
    ExpirationModel: Optional[str]
    Id: Optional[str]
    KeyMaterialBase64: Optional[str]
    KeyState: Optional[str]
    KeyUsage: Optional[str]
    Policy: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ValidTo: Optional[str]

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
            DeletionWindowInDays=json_data.get("DeletionWindowInDays"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ExpirationModel=json_data.get("ExpirationModel"),
            Id=json_data.get("Id"),
            KeyMaterialBase64=json_data.get("KeyMaterialBase64"),
            KeyState=json_data.get("KeyState"),
            KeyUsage=json_data.get("KeyUsage"),
            Policy=json_data.get("Policy"),
            Tags=json_data.get("Tags"),
            ValidTo=json_data.get("ValidTo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


