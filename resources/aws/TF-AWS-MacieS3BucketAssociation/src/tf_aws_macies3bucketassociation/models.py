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
    BucketName: Optional[str]
    Id: Optional[str]
    MemberAccountId: Optional[str]
    Prefix: Optional[str]
    ClassificationType: Optional[Sequence["_ClassificationTypeDefinition"]]

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
            BucketName=json_data.get("BucketName"),
            Id=json_data.get("Id"),
            MemberAccountId=json_data.get("MemberAccountId"),
            Prefix=json_data.get("Prefix"),
            ClassificationType=deserialize_list(json_data.get("ClassificationType"), ClassificationTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClassificationTypeDefinition(BaseModel):
    Continuous: Optional[str]
    OneTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClassificationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassificationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Continuous=json_data.get("Continuous"),
            OneTime=json_data.get("OneTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassificationTypeDefinition = ClassificationTypeDefinition


