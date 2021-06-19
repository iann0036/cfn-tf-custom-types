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
    CloudVendor: Optional[str]
    CreatedTime: Optional[str]
    Description: Optional[str]
    HideInCompliance: Optional[bool]
    Id: Optional[str]
    IsTemplate: Optional[bool]
    Language: Optional[str]
    MinFeatureTier: Optional[str]
    Name: Optional[str]
    UpdatedTime: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            CloudVendor=json_data.get("CloudVendor"),
            CreatedTime=json_data.get("CreatedTime"),
            Description=json_data.get("Description"),
            HideInCompliance=json_data.get("HideInCompliance"),
            Id=json_data.get("Id"),
            IsTemplate=json_data.get("IsTemplate"),
            Language=json_data.get("Language"),
            MinFeatureTier=json_data.get("MinFeatureTier"),
            Name=json_data.get("Name"),
            UpdatedTime=json_data.get("UpdatedTime"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RulesDefinition(BaseModel):
    ComplianceTag: Optional[str]
    ControlTitle: Optional[str]
    Description: Optional[str]
    Domain: Optional[str]
    IsDefault: Optional[bool]
    Logic: Optional[str]
    Name: Optional[str]
    Priority: Optional[str]
    Remediation: Optional[str]
    RuleId: Optional[str]
    Severity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            ComplianceTag=json_data.get("ComplianceTag"),
            ControlTitle=json_data.get("ControlTitle"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            IsDefault=json_data.get("IsDefault"),
            Logic=json_data.get("Logic"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Remediation=json_data.get("Remediation"),
            RuleId=json_data.get("RuleId"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


