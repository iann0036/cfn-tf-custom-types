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
    BucketId: Optional[str]
    EnvironmentId: Optional[str]
    Id: Optional[str]
    Interval: Optional[str]
    Note: Optional[str]
    TestId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BucketId=json_data.get("BucketId"),
            EnvironmentId=json_data.get("EnvironmentId"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Note=json_data.get("Note"),
            TestId=json_data.get("TestId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


