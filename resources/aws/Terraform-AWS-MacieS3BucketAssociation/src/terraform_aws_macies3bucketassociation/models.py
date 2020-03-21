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
    BucketName: Optional[str]
    Id: Optional[str]
    MemberAccountId: Optional[str]
    Prefix: Optional[str]
    ClassificationType: Optional[Sequence["_ClassificationType"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BucketName=json_data.get("BucketName"),
            Id=json_data.get("Id"),
            MemberAccountId=json_data.get("MemberAccountId"),
            Prefix=json_data.get("Prefix"),
            ClassificationType=json_data.get("ClassificationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClassificationType:
    Continuous: Optional[str]
    OneTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClassificationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassificationType"]:
        if not json_data:
            return None
        return cls(
            Continuous=json_data.get("Continuous"),
            OneTime=json_data.get("OneTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassificationType = ClassificationType


