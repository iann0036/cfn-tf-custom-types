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
    CreateMode: Optional[float]
    CreateTime: Optional[str]
    PolicyId: Optional[str]
    PolicyName: Optional[str]
    PolicyType: Optional[str]
    RoleId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateMode=json_data.get("CreateMode"),
            CreateTime=json_data.get("CreateTime"),
            PolicyId=json_data.get("PolicyId"),
            PolicyName=json_data.get("PolicyName"),
            PolicyType=json_data.get("PolicyType"),
            RoleId=json_data.get("RoleId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


