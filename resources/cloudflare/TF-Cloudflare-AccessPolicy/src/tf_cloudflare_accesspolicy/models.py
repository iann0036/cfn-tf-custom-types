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
    AccountId: Optional[str]
    ApplicationId: Optional[str]
    Decision: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Precedence: Optional[float]
    ZoneId: Optional[str]
    Exclude: Optional[Sequence["_ExcludeDefinition"]]
    Include: Optional[Sequence["_IncludeDefinition"]]
    Require: Optional[Sequence["_RequireDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            ApplicationId=json_data.get("ApplicationId"),
            Decision=json_data.get("Decision"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Precedence=json_data.get("Precedence"),
            ZoneId=json_data.get("ZoneId"),
            Exclude=deserialize_list(json_data.get("Exclude"), ExcludeDefinition),
            Include=deserialize_list(json_data.get("Include"), IncludeDefinition),
            Require=deserialize_list(json_data.get("Require"), RequireDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExcludeDefinition(BaseModel):
    AnyValidServiceToken: Optional[bool]
    AuthMethod: Optional[str]
    Certificate: Optional[bool]
    CommonName: Optional[str]
    DevicePosture: Optional[Sequence[str]]
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Geo: Optional[Sequence[str]]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]
    LoginMethod: Optional[Sequence[str]]
    ServiceToken: Optional[Sequence[str]]
    Azure: Optional[Sequence["_AzureDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gsuite: Optional[Sequence["_GsuiteDefinition"]]
    Okta: Optional[Sequence["_OktaDefinition"]]
    Saml: Optional[Sequence["_SamlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyValidServiceToken=json_data.get("AnyValidServiceToken"),
            AuthMethod=json_data.get("AuthMethod"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            DevicePosture=json_data.get("DevicePosture"),
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Geo=json_data.get("Geo"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
            LoginMethod=json_data.get("LoginMethod"),
            ServiceToken=json_data.get("ServiceToken"),
            Azure=deserialize_list(json_data.get("Azure"), AzureDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gsuite=deserialize_list(json_data.get("Gsuite"), GsuiteDefinition),
            Okta=deserialize_list(json_data.get("Okta"), OktaDefinition),
            Saml=deserialize_list(json_data.get("Saml"), SamlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeDefinition = ExcludeDefinition


@dataclass
class AzureDefinition(BaseModel):
    Id: Optional[Sequence[str]]
    IdentityProviderId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDefinition = AzureDefinition


@dataclass
class GithubDefinition(BaseModel):
    IdentityProviderId: Optional[str]
    Name: Optional[str]
    Teams: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GithubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityProviderId=json_data.get("IdentityProviderId"),
            Name=json_data.get("Name"),
            Teams=json_data.get("Teams"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubDefinition = GithubDefinition


@dataclass
class GsuiteDefinition(BaseModel):
    Email: Optional[Sequence[str]]
    IdentityProviderId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GsuiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GsuiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GsuiteDefinition = GsuiteDefinition


@dataclass
class OktaDefinition(BaseModel):
    IdentityProviderId: Optional[str]
    Name: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OktaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OktaDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityProviderId=json_data.get("IdentityProviderId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OktaDefinition = OktaDefinition


@dataclass
class SamlDefinition(BaseModel):
    AttributeName: Optional[str]
    AttributeValue: Optional[str]
    IdentityProviderId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamlDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeValue=json_data.get("AttributeValue"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamlDefinition = SamlDefinition


@dataclass
class IncludeDefinition(BaseModel):
    AnyValidServiceToken: Optional[bool]
    AuthMethod: Optional[str]
    Certificate: Optional[bool]
    CommonName: Optional[str]
    DevicePosture: Optional[Sequence[str]]
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Geo: Optional[Sequence[str]]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]
    LoginMethod: Optional[Sequence[str]]
    ServiceToken: Optional[Sequence[str]]
    Azure: Optional[Sequence["_AzureDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gsuite: Optional[Sequence["_GsuiteDefinition"]]
    Okta: Optional[Sequence["_OktaDefinition"]]
    Saml: Optional[Sequence["_SamlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncludeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludeDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyValidServiceToken=json_data.get("AnyValidServiceToken"),
            AuthMethod=json_data.get("AuthMethod"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            DevicePosture=json_data.get("DevicePosture"),
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Geo=json_data.get("Geo"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
            LoginMethod=json_data.get("LoginMethod"),
            ServiceToken=json_data.get("ServiceToken"),
            Azure=deserialize_list(json_data.get("Azure"), AzureDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gsuite=deserialize_list(json_data.get("Gsuite"), GsuiteDefinition),
            Okta=deserialize_list(json_data.get("Okta"), OktaDefinition),
            Saml=deserialize_list(json_data.get("Saml"), SamlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludeDefinition = IncludeDefinition


@dataclass
class RequireDefinition(BaseModel):
    AnyValidServiceToken: Optional[bool]
    AuthMethod: Optional[str]
    Certificate: Optional[bool]
    CommonName: Optional[str]
    DevicePosture: Optional[Sequence[str]]
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Geo: Optional[Sequence[str]]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]
    LoginMethod: Optional[Sequence[str]]
    ServiceToken: Optional[Sequence[str]]
    Azure: Optional[Sequence["_AzureDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gsuite: Optional[Sequence["_GsuiteDefinition"]]
    Okta: Optional[Sequence["_OktaDefinition"]]
    Saml: Optional[Sequence["_SamlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequireDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequireDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyValidServiceToken=json_data.get("AnyValidServiceToken"),
            AuthMethod=json_data.get("AuthMethod"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            DevicePosture=json_data.get("DevicePosture"),
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Geo=json_data.get("Geo"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
            LoginMethod=json_data.get("LoginMethod"),
            ServiceToken=json_data.get("ServiceToken"),
            Azure=deserialize_list(json_data.get("Azure"), AzureDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gsuite=deserialize_list(json_data.get("Gsuite"), GsuiteDefinition),
            Okta=deserialize_list(json_data.get("Okta"), OktaDefinition),
            Saml=deserialize_list(json_data.get("Saml"), SamlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequireDefinition = RequireDefinition


