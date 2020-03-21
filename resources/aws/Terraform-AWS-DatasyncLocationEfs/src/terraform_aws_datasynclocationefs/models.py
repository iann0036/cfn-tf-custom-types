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
    EfsFileSystemArn: Optional[str]
    Id: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Uri: Optional[str]
    Ec2Config: Optional[Sequence["_Ec2Config"]]

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
            EfsFileSystemArn=json_data.get("EfsFileSystemArn"),
            Id=json_data.get("Id"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            Ec2Config=json_data.get("Ec2Config"),
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
class Ec2Config:
    SecurityGroupArns: Optional[Sequence[str]]
    SubnetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2Config"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupArns=json_data.get("SecurityGroupArns"),
            SubnetArn=json_data.get("SubnetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2Config = Ec2Config


