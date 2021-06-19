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
    ApprovedPatches: Optional[Sequence[str]]
    ApprovedPatchesComplianceLevel: Optional[str]
    ApprovedPatchesEnableNonSecurity: Optional[bool]
    Arn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OperatingSystem: Optional[str]
    RejectedPatches: Optional[Sequence[str]]
    RejectedPatchesAction: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ApprovalRule: Optional[Sequence["_ApprovalRuleDefinition"]]
    GlobalFilter: Optional[Sequence["_GlobalFilterDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]

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
            ApprovedPatches=json_data.get("ApprovedPatches"),
            ApprovedPatchesComplianceLevel=json_data.get("ApprovedPatchesComplianceLevel"),
            ApprovedPatchesEnableNonSecurity=json_data.get("ApprovedPatchesEnableNonSecurity"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OperatingSystem=json_data.get("OperatingSystem"),
            RejectedPatches=json_data.get("RejectedPatches"),
            RejectedPatchesAction=json_data.get("RejectedPatchesAction"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ApprovalRule=deserialize_list(json_data.get("ApprovalRule"), ApprovalRuleDefinition),
            GlobalFilter=deserialize_list(json_data.get("GlobalFilter"), GlobalFilterDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class ApprovalRuleDefinition(BaseModel):
    ApproveAfterDays: Optional[float]
    ApproveUntilDate: Optional[str]
    ComplianceLevel: Optional[str]
    EnableNonSecurity: Optional[bool]
    PatchFilter: Optional[Sequence["_PatchFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApprovalRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApprovalRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ApproveAfterDays=json_data.get("ApproveAfterDays"),
            ApproveUntilDate=json_data.get("ApproveUntilDate"),
            ComplianceLevel=json_data.get("ComplianceLevel"),
            EnableNonSecurity=json_data.get("EnableNonSecurity"),
            PatchFilter=deserialize_list(json_data.get("PatchFilter"), PatchFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApprovalRuleDefinition = ApprovalRuleDefinition


@dataclass
class PatchFilterDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PatchFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchFilterDefinition = PatchFilterDefinition


@dataclass
class GlobalFilterDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalFilterDefinition = GlobalFilterDefinition


@dataclass
class SourceDefinition(BaseModel):
    Configuration: Optional[str]
    Name: Optional[str]
    Products: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Configuration=json_data.get("Configuration"),
            Name=json_data.get("Name"),
            Products=json_data.get("Products"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


