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
    Description: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Policy: Optional[str]
    RecoveryWindowInDays: Optional[float]
    RotationEnabled: Optional[bool]
    RotationLambdaArn: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    RotationRules: Optional[Sequence["_RotationRules"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Policy=json_data.get("Policy"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            RotationEnabled=json_data.get("RotationEnabled"),
            RotationLambdaArn=json_data.get("RotationLambdaArn"),
            Tags=json_data.get("Tags"),
            RotationRules=json_data.get("RotationRules"),
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


@dataclass
class RotationRules:
    AutomaticallyAfterDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RotationRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RotationRules"]:
        if not json_data:
            return None
        return cls(
            AutomaticallyAfterDays=json_data.get("AutomaticallyAfterDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RotationRules = RotationRules


