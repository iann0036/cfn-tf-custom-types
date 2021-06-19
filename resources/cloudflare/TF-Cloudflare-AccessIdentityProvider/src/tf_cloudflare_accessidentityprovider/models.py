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
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    ZoneId: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            ZoneId=json_data.get("ZoneId"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    AppsDomain: Optional[str]
    Attributes: Optional[Sequence[str]]
    AuthUrl: Optional[str]
    CentrifyAccount: Optional[str]
    CentrifyAppId: Optional[str]
    CertsUrl: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    DirectoryId: Optional[str]
    EmailAttributeName: Optional[str]
    IdpPublicCert: Optional[str]
    IssuerUrl: Optional[str]
    OktaAccount: Optional[str]
    OneloginAccount: Optional[str]
    RedirectUrl: Optional[str]
    SignRequest: Optional[bool]
    SsoTargetUrl: Optional[str]
    SupportGroups: Optional[bool]
    TokenUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AppsDomain=json_data.get("AppsDomain"),
            Attributes=json_data.get("Attributes"),
            AuthUrl=json_data.get("AuthUrl"),
            CentrifyAccount=json_data.get("CentrifyAccount"),
            CentrifyAppId=json_data.get("CentrifyAppId"),
            CertsUrl=json_data.get("CertsUrl"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            DirectoryId=json_data.get("DirectoryId"),
            EmailAttributeName=json_data.get("EmailAttributeName"),
            IdpPublicCert=json_data.get("IdpPublicCert"),
            IssuerUrl=json_data.get("IssuerUrl"),
            OktaAccount=json_data.get("OktaAccount"),
            OneloginAccount=json_data.get("OneloginAccount"),
            RedirectUrl=json_data.get("RedirectUrl"),
            SignRequest=json_data.get("SignRequest"),
            SsoTargetUrl=json_data.get("SsoTargetUrl"),
            SupportGroups=json_data.get("SupportGroups"),
            TokenUrl=json_data.get("TokenUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


