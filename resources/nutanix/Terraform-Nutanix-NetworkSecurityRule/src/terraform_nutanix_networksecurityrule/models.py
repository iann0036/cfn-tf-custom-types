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
    TPSCode: Optional[str]
    Title: Optional[str]
    CoverSheetIncluded: Optional[bool]
    DueDate: Optional[str]
    ApprovalDate: Optional[str]
    Memo: Optional["_Memo"]
    SecondCopyOfMemo: Optional["_Memo"]
    TestCode: Optional[str]
    Authors: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            TPSCode=json_data.get("TPSCode"),
            Title=json_data.get("Title"),
            CoverSheetIncluded=json_data.get("CoverSheetIncluded"),
            DueDate=json_data.get("DueDate"),
            ApprovalDate=json_data.get("ApprovalDate"),
            Memo=Memo._deserialize(json_data.get("Memo")),
            SecondCopyOfMemo=Memo._deserialize(json_data.get("SecondCopyOfMemo")),
            TestCode=json_data.get("TestCode"),
            Authors=json_data.get("Authors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Memo:
    Heading: Optional[str]
    Body: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Memo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Memo"]:
        if not json_data:
            return None
        return cls(
            Heading=json_data.get("Heading"),
            Body=json_data.get("Body"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Memo = Memo


