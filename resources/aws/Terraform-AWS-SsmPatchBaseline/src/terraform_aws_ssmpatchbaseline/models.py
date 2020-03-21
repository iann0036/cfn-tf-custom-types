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
    ApprovedPatches: Optional[Sequence[str]]
    ApprovedPatchesComplianceLevel: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    OperatingSystem: Optional[str]
    RejectedPatches: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    ApprovalRule: Optional[Sequence["_ApprovalRule"]]
    GlobalFilter: Optional[Sequence["_GlobalFilter"]]
    PatchFilter: Optional[Sequence["_PatchFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApprovedPatches=json_data.get("ApprovedPatches"),
            ApprovedPatchesComplianceLevel=json_data.get("ApprovedPatchesComplianceLevel"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            OperatingSystem=json_data.get("OperatingSystem"),
            RejectedPatches=json_data.get("RejectedPatches"),
            Tags=json_data.get("Tags"),
            ApprovalRule=json_data.get("ApprovalRule"),
            GlobalFilter=json_data.get("GlobalFilter"),
            PatchFilter=json_data.get("PatchFilter"),
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
class ApprovalRule:
    ApproveAfterDays: Optional[float]
    ComplianceLevel: Optional[str]
    EnableNonSecurity: Optional[bool]
    PatchFilter: Optional[Sequence["_PatchFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApprovalRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApprovalRule"]:
        if not json_data:
            return None
        return cls(
            ApproveAfterDays=json_data.get("ApproveAfterDays"),
            ComplianceLevel=json_data.get("ComplianceLevel"),
            EnableNonSecurity=json_data.get("EnableNonSecurity"),
            PatchFilter=json_data.get("PatchFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApprovalRule = ApprovalRule


@dataclass
class PatchFilter:
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PatchFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchFilter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchFilter = PatchFilter


@dataclass
class GlobalFilter:
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalFilter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalFilter = GlobalFilter


