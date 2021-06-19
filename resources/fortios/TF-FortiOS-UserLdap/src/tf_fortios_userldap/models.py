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
    AccountKeyFilter: Optional[str]
    AccountKeyProcessing: Optional[str]
    CaCert: Optional[str]
    Cnid: Optional[str]
    Dn: Optional[str]
    GroupFilter: Optional[str]
    GroupMemberCheck: Optional[str]
    GroupObjectFilter: Optional[str]
    GroupSearchBase: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    MemberAttr: Optional[str]
    Name: Optional[str]
    ObtainUserInfo: Optional[str]
    Password: Optional[str]
    PasswordExpiryWarning: Optional[str]
    PasswordRenewal: Optional[str]
    Port: Optional[float]
    SearchType: Optional[str]
    SecondaryServer: Optional[str]
    Secure: Optional[str]
    Server: Optional[str]
    ServerIdentityCheck: Optional[str]
    SourceIp: Optional[str]
    SslMinProtoVersion: Optional[str]
    TertiaryServer: Optional[str]
    TwoFactor: Optional[str]
    TwoFactorAuthentication: Optional[str]
    TwoFactorNotification: Optional[str]
    Type: Optional[str]
    UserInfoExchangeServer: Optional[str]
    Username: Optional[str]
    Vdomparam: Optional[str]

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
            AccountKeyFilter=json_data.get("AccountKeyFilter"),
            AccountKeyProcessing=json_data.get("AccountKeyProcessing"),
            CaCert=json_data.get("CaCert"),
            Cnid=json_data.get("Cnid"),
            Dn=json_data.get("Dn"),
            GroupFilter=json_data.get("GroupFilter"),
            GroupMemberCheck=json_data.get("GroupMemberCheck"),
            GroupObjectFilter=json_data.get("GroupObjectFilter"),
            GroupSearchBase=json_data.get("GroupSearchBase"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            MemberAttr=json_data.get("MemberAttr"),
            Name=json_data.get("Name"),
            ObtainUserInfo=json_data.get("ObtainUserInfo"),
            Password=json_data.get("Password"),
            PasswordExpiryWarning=json_data.get("PasswordExpiryWarning"),
            PasswordRenewal=json_data.get("PasswordRenewal"),
            Port=json_data.get("Port"),
            SearchType=json_data.get("SearchType"),
            SecondaryServer=json_data.get("SecondaryServer"),
            Secure=json_data.get("Secure"),
            Server=json_data.get("Server"),
            ServerIdentityCheck=json_data.get("ServerIdentityCheck"),
            SourceIp=json_data.get("SourceIp"),
            SslMinProtoVersion=json_data.get("SslMinProtoVersion"),
            TertiaryServer=json_data.get("TertiaryServer"),
            TwoFactor=json_data.get("TwoFactor"),
            TwoFactorAuthentication=json_data.get("TwoFactorAuthentication"),
            TwoFactorNotification=json_data.get("TwoFactorNotification"),
            Type=json_data.get("Type"),
            UserInfoExchangeServer=json_data.get("UserInfoExchangeServer"),
            Username=json_data.get("Username"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


