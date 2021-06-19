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
    AcsBinding: Optional[str]
    AcsType: Optional[str]
    Audience: Optional[str]
    DeprovisionedAction: Optional[str]
    GroupsAction: Optional[str]
    GroupsAssignment: Optional[Sequence[str]]
    GroupsAttribute: Optional[str]
    GroupsFilter: Optional[Sequence[str]]
    Id: Optional[str]
    Issuer: Optional[str]
    IssuerMode: Optional[str]
    Kid: Optional[str]
    MaxClockSkew: Optional[float]
    Name: Optional[str]
    NameFormat: Optional[str]
    ProfileMaster: Optional[bool]
    ProvisioningAction: Optional[str]
    RequestSignatureAlgorithm: Optional[str]
    RequestSignatureScope: Optional[str]
    ResponseSignatureAlgorithm: Optional[str]
    ResponseSignatureScope: Optional[str]
    SsoBinding: Optional[str]
    SsoDestination: Optional[str]
    SsoUrl: Optional[str]
    Status: Optional[str]
    SubjectFilter: Optional[str]
    SubjectFormat: Optional[Sequence[str]]
    SubjectMatchAttribute: Optional[str]
    SubjectMatchType: Optional[str]
    SuspendedAction: Optional[str]
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
            AcsBinding=json_data.get("AcsBinding"),
            AcsType=json_data.get("AcsType"),
            Audience=json_data.get("Audience"),
            DeprovisionedAction=json_data.get("DeprovisionedAction"),
            GroupsAction=json_data.get("GroupsAction"),
            GroupsAssignment=json_data.get("GroupsAssignment"),
            GroupsAttribute=json_data.get("GroupsAttribute"),
            GroupsFilter=json_data.get("GroupsFilter"),
            Id=json_data.get("Id"),
            Issuer=json_data.get("Issuer"),
            IssuerMode=json_data.get("IssuerMode"),
            Kid=json_data.get("Kid"),
            MaxClockSkew=json_data.get("MaxClockSkew"),
            Name=json_data.get("Name"),
            NameFormat=json_data.get("NameFormat"),
            ProfileMaster=json_data.get("ProfileMaster"),
            ProvisioningAction=json_data.get("ProvisioningAction"),
            RequestSignatureAlgorithm=json_data.get("RequestSignatureAlgorithm"),
            RequestSignatureScope=json_data.get("RequestSignatureScope"),
            ResponseSignatureAlgorithm=json_data.get("ResponseSignatureAlgorithm"),
            ResponseSignatureScope=json_data.get("ResponseSignatureScope"),
            SsoBinding=json_data.get("SsoBinding"),
            SsoDestination=json_data.get("SsoDestination"),
            SsoUrl=json_data.get("SsoUrl"),
            Status=json_data.get("Status"),
            SubjectFilter=json_data.get("SubjectFilter"),
            SubjectFormat=json_data.get("SubjectFormat"),
            SubjectMatchAttribute=json_data.get("SubjectMatchAttribute"),
            SubjectMatchType=json_data.get("SubjectMatchType"),
            SuspendedAction=json_data.get("SuspendedAction"),
            Type=json_data.get("Type"),
            UsernameTemplate=json_data.get("UsernameTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


