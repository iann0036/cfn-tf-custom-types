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
    AuthnRequestUrl: Optional[str]
    Certificate: Optional[str]
    ConfigurationName: Optional[str]
    DebugMode: Optional[bool]
    DisableRequestedAuthnContext: Optional[bool]
    EmailAttribute: Optional[str]
    Id: Optional[str]
    IsRedirectBinding: Optional[bool]
    Issuer: Optional[str]
    LogoutEnabled: Optional[bool]
    LogoutUrl: Optional[str]
    RolesAttribute: Optional[str]
    SignAuthnRequest: Optional[bool]
    SpInitiatedLoginEnabled: Optional[bool]
    SpInitiatedLoginPath: Optional[str]
    X509cert1: Optional[str]
    X509cert2: Optional[str]
    X509cert3: Optional[str]
    OnDemandProvisioningEnabled: Optional[Sequence["_OnDemandProvisioningEnabledDefinition"]]

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
            AuthnRequestUrl=json_data.get("AuthnRequestUrl"),
            Certificate=json_data.get("Certificate"),
            ConfigurationName=json_data.get("ConfigurationName"),
            DebugMode=json_data.get("DebugMode"),
            DisableRequestedAuthnContext=json_data.get("DisableRequestedAuthnContext"),
            EmailAttribute=json_data.get("EmailAttribute"),
            Id=json_data.get("Id"),
            IsRedirectBinding=json_data.get("IsRedirectBinding"),
            Issuer=json_data.get("Issuer"),
            LogoutEnabled=json_data.get("LogoutEnabled"),
            LogoutUrl=json_data.get("LogoutUrl"),
            RolesAttribute=json_data.get("RolesAttribute"),
            SignAuthnRequest=json_data.get("SignAuthnRequest"),
            SpInitiatedLoginEnabled=json_data.get("SpInitiatedLoginEnabled"),
            SpInitiatedLoginPath=json_data.get("SpInitiatedLoginPath"),
            X509cert1=json_data.get("X509cert1"),
            X509cert2=json_data.get("X509cert2"),
            X509cert3=json_data.get("X509cert3"),
            OnDemandProvisioningEnabled=deserialize_list(json_data.get("OnDemandProvisioningEnabled"), OnDemandProvisioningEnabledDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OnDemandProvisioningEnabledDefinition(BaseModel):
    FirstNameAttribute: Optional[str]
    LastNameAttribute: Optional[str]
    OnDemandProvisioningRoles: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandProvisioningEnabledDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandProvisioningEnabledDefinition"]:
        if not json_data:
            return None
        return cls(
            FirstNameAttribute=json_data.get("FirstNameAttribute"),
            LastNameAttribute=json_data.get("LastNameAttribute"),
            OnDemandProvisioningRoles=json_data.get("OnDemandProvisioningRoles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandProvisioningEnabledDefinition = OnDemandProvisioningEnabledDefinition


