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
    Description: Optional[str]
    DisplayName: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    Conjunction: Optional[Sequence["_ConjunctionDefinition"]]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    ExtendedCriteria: Optional[Sequence["_ExtendedCriteriaDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            Conjunction=deserialize_list(json_data.get("Conjunction"), ConjunctionDefinition),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            ExtendedCriteria=deserialize_list(json_data.get("ExtendedCriteria"), ExtendedCriteriaDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConjunctionDefinition(BaseModel):
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConjunctionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConjunctionDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConjunctionDefinition = ConjunctionDefinition


@dataclass
class CriteriaDefinition(BaseModel):
    Condition: Optional[Sequence["_ConditionDefinition"]]
    IpaddressExpression: Optional[Sequence["_IpaddressExpressionDefinition"]]
    MacaddressExpression: Optional[Sequence["_MacaddressExpressionDefinition"]]
    PathExpression: Optional[Sequence["_PathExpressionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            IpaddressExpression=deserialize_list(json_data.get("IpaddressExpression"), IpaddressExpressionDefinition),
            MacaddressExpression=deserialize_list(json_data.get("MacaddressExpression"), MacaddressExpressionDefinition),
            PathExpression=deserialize_list(json_data.get("PathExpression"), PathExpressionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


@dataclass
class ConditionDefinition(BaseModel):
    Key: Optional[str]
    MemberType: Optional[str]
    Operator: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            MemberType=json_data.get("MemberType"),
            Operator=json_data.get("Operator"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class IpaddressExpressionDefinition(BaseModel):
    IpAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpaddressExpressionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpaddressExpressionDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddresses=json_data.get("IpAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpaddressExpressionDefinition = IpaddressExpressionDefinition


@dataclass
class MacaddressExpressionDefinition(BaseModel):
    MacAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MacaddressExpressionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacaddressExpressionDefinition"]:
        if not json_data:
            return None
        return cls(
            MacAddresses=json_data.get("MacAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacaddressExpressionDefinition = MacaddressExpressionDefinition


@dataclass
class PathExpressionDefinition(BaseModel):
    MemberPaths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathExpressionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathExpressionDefinition"]:
        if not json_data:
            return None
        return cls(
            MemberPaths=json_data.get("MemberPaths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathExpressionDefinition = PathExpressionDefinition


@dataclass
class ExtendedCriteriaDefinition(BaseModel):
    IdentityGroup: Optional[Sequence["_IdentityGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityGroup=deserialize_list(json_data.get("IdentityGroup"), IdentityGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedCriteriaDefinition = ExtendedCriteriaDefinition


@dataclass
class IdentityGroupDefinition(BaseModel):
    DistinguishedName: Optional[str]
    DomainBaseDistinguishedName: Optional[str]
    Sid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            DistinguishedName=json_data.get("DistinguishedName"),
            DomainBaseDistinguishedName=json_data.get("DomainBaseDistinguishedName"),
            Sid=json_data.get("Sid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityGroupDefinition = IdentityGroupDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


