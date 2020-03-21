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
    ClbId: Optional[str]
    IsAutoRewrite: Optional[bool]
    SourceListenerId: Optional[str]
    SourceRuleId: Optional[str]
    TargetListenerId: Optional[str]
    TargetRuleId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClbId=json_data.get("ClbId"),
            IsAutoRewrite=json_data.get("IsAutoRewrite"),
            SourceListenerId=json_data.get("SourceListenerId"),
            SourceRuleId=json_data.get("SourceRuleId"),
            TargetListenerId=json_data.get("TargetListenerId"),
            TargetRuleId=json_data.get("TargetRuleId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


