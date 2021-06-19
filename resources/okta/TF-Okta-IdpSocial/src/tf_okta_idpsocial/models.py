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
    AccountLinkAction: Optional[str]
    AccountLinkGroupInclude: Optional[Sequence[str]]
    AuthorizationBinding: Optional[str]
    AuthorizationUrl: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    DeprovisionedAction: Optional[str]
    GroupsAction: Optional[str]
    GroupsAssignment: Optional[Sequence[str]]
    GroupsAttribute: Optional[str]
    GroupsFilter: Optional[Sequence[str]]
    Id: Optional[str]
    IssuerMode: Optional[str]
    MatchAttribute: Optional[str]
    MatchType: Optional[str]
    MaxClockSkew: Optional[float]
    Name: Optional[str]
    ProfileMaster: Optional[bool]
    ProtocolType: Optional[str]
    ProvisioningAction: Optional[str]
    RequestSignatureAlgorithm: Optional[str]
    RequestSignatureScope: Optional[str]
    ResponseSignatureAlgorithm: Optional[str]
    ResponseSignatureScope: Optional[str]
    Scopes: Optional[Sequence[str]]
    Status: Optional[str]
    SubjectMatchAttribute: Optional[str]
    SubjectMatchType: Optional[str]
    SuspendedAction: Optional[str]
    TokenBinding: Optional[str]
    TokenUrl: Optional[str]
    Type: Optional[str]
    UsernameTemplate: Optional[str]

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
            AccountLinkAction=json_data.get("AccountLinkAction"),
            AccountLinkGroupInclude=json_data.get("AccountLinkGroupInclude"),
            AuthorizationBinding=json_data.get("AuthorizationBinding"),
            AuthorizationUrl=json_data.get("AuthorizationUrl"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            DeprovisionedAction=json_data.get("DeprovisionedAction"),
            GroupsAction=json_data.get("GroupsAction"),
            GroupsAssignment=json_data.get("GroupsAssignment"),
            GroupsAttribute=json_data.get("GroupsAttribute"),
            GroupsFilter=json_data.get("GroupsFilter"),
            Id=json_data.get("Id"),
            IssuerMode=json_data.get("IssuerMode"),
            MatchAttribute=json_data.get("MatchAttribute"),
            MatchType=json_data.get("MatchType"),
            MaxClockSkew=json_data.get("MaxClockSkew"),
            Name=json_data.get("Name"),
            ProfileMaster=json_data.get("ProfileMaster"),
            ProtocolType=json_data.get("ProtocolType"),
            ProvisioningAction=json_data.get("ProvisioningAction"),
            RequestSignatureAlgorithm=json_data.get("RequestSignatureAlgorithm"),
            RequestSignatureScope=json_data.get("RequestSignatureScope"),
            ResponseSignatureAlgorithm=json_data.get("ResponseSignatureAlgorithm"),
            ResponseSignatureScope=json_data.get("ResponseSignatureScope"),
            Scopes=json_data.get("Scopes"),
            Status=json_data.get("Status"),
            SubjectMatchAttribute=json_data.get("SubjectMatchAttribute"),
            SubjectMatchType=json_data.get("SubjectMatchType"),
            SuspendedAction=json_data.get("SuspendedAction"),
            TokenBinding=json_data.get("TokenBinding"),
            TokenUrl=json_data.get("TokenUrl"),
            Type=json_data.get("Type"),
            UsernameTemplate=json_data.get("UsernameTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


