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
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    AuthenticationPolicy: Optional[Sequence["_AuthenticationPolicyDefinition"]]
    AuthorizationPolicy: Optional[Sequence["_AuthorizationPolicyDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            AuthenticationPolicy=deserialize_list(json_data.get("AuthenticationPolicy"), AuthenticationPolicyDefinition),
            AuthorizationPolicy=deserialize_list(json_data.get("AuthorizationPolicy"), AuthorizationPolicyDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthenticationPolicyDefinition(BaseModel):
    DefaultAuthProfileRef: Optional[str]
    AuthnRules: Optional[Sequence["_AuthnRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultAuthProfileRef=json_data.get("DefaultAuthProfileRef"),
            AuthnRules=deserialize_list(json_data.get("AuthnRules"), AuthnRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationPolicyDefinition = AuthenticationPolicyDefinition


@dataclass
class AuthnRulesDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthnRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthnRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthnRulesDefinition = AuthnRulesDefinition


@dataclass
class ActionDefinition(BaseModel):
    StatusCode: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class MatchDefinition(BaseModel):
    AccessToken: Optional[Sequence["_AccessTokenDefinition"]]
    AttrMatches: Optional[Sequence["_AttrMatchesDefinition"]]
    HostHdr: Optional[Sequence["_HostHdrDefinition"]]
    Method: Optional[Sequence["_MethodDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=deserialize_list(json_data.get("AccessToken"), AccessTokenDefinition),
            AttrMatches=deserialize_list(json_data.get("AttrMatches"), AttrMatchesDefinition),
            HostHdr=deserialize_list(json_data.get("HostHdr"), HostHdrDefinition),
            Method=deserialize_list(json_data.get("Method"), MethodDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class AccessTokenDefinition(BaseModel):
    TokenName: Optional[str]
    Matches: Optional[Sequence["_MatchesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            TokenName=json_data.get("TokenName"),
            Matches=deserialize_list(json_data.get("Matches"), MatchesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessTokenDefinition = AccessTokenDefinition


@dataclass
class MatchesDefinition(BaseModel):
    BoolMatch: Optional[bool]
    IntMatch: Optional[float]
    IsMandatory: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]
    Validate: Optional[bool]
    StringMatch: Optional[Sequence["_StringMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchesDefinition"]:
        if not json_data:
            return None
        return cls(
            BoolMatch=json_data.get("BoolMatch"),
            IntMatch=json_data.get("IntMatch"),
            IsMandatory=json_data.get("IsMandatory"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Validate=json_data.get("Validate"),
            StringMatch=deserialize_list(json_data.get("StringMatch"), StringMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchesDefinition = MatchesDefinition


@dataclass
class StringMatchDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringMatchDefinition = StringMatchDefinition


@dataclass
class AttrMatchesDefinition(BaseModel):
    AttributeName: Optional[str]
    AttributeValueList: Optional[Sequence["_AttributeValueListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttrMatchesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttrMatchesDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeValueList=deserialize_list(json_data.get("AttributeValueList"), AttributeValueListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttrMatchesDefinition = AttrMatchesDefinition


@dataclass
class AttributeValueListDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeValueListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeValueListDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeValueListDefinition = AttributeValueListDefinition


@dataclass
class HostHdrDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HostHdrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostHdrDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostHdrDefinition = HostHdrDefinition


@dataclass
class MethodDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Methods: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Methods=json_data.get("Methods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodDefinition = MethodDefinition


@dataclass
class PathDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class AuthorizationPolicyDefinition(BaseModel):
    AuthzRules: Optional[Sequence["_AuthzRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthzRules=deserialize_list(json_data.get("AuthzRules"), AuthzRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationPolicyDefinition = AuthorizationPolicyDefinition


@dataclass
class AuthzRulesDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthzRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthzRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthzRulesDefinition = AuthzRulesDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


