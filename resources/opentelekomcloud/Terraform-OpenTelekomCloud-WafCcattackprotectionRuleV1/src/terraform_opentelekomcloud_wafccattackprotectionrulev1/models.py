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
    ActionCategory: Optional[str]
    BlockContent: Optional[str]
    BlockContentType: Optional[str]
    Default: Optional[bool]
    LimitNum: Optional[float]
    LimitPeriod: Optional[float]
    LockTime: Optional[float]
    PolicyId: Optional[str]
    TagCategory: Optional[str]
    TagContents: Optional[Sequence[str]]
    TagIndex: Optional[str]
    TagType: Optional[str]
    Url: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActionCategory=json_data.get("ActionCategory"),
            BlockContent=json_data.get("BlockContent"),
            BlockContentType=json_data.get("BlockContentType"),
            Default=json_data.get("Default"),
            LimitNum=json_data.get("LimitNum"),
            LimitPeriod=json_data.get("LimitPeriod"),
            LockTime=json_data.get("LockTime"),
            PolicyId=json_data.get("PolicyId"),
            TagCategory=json_data.get("TagCategory"),
            TagContents=json_data.get("TagContents"),
            TagIndex=json_data.get("TagIndex"),
            TagType=json_data.get("TagType"),
            Url=json_data.get("Url"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


