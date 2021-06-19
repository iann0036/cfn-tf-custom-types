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
    AuthConcurrentOverride: Optional[str]
    AuthConcurrentValue: Optional[float]
    Authtimeout: Optional[float]
    EmailTo: Optional[str]
    Fortitoken: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    LdapServer: Optional[str]
    Name: Optional[str]
    Passwd: Optional[str]
    PasswdPolicy: Optional[str]
    PasswdTime: Optional[str]
    PpkIdentity: Optional[str]
    PpkSecret: Optional[str]
    RadiusServer: Optional[str]
    SmsCustomServer: Optional[str]
    SmsPhone: Optional[str]
    SmsServer: Optional[str]
    Status: Optional[str]
    TacacsServer: Optional[str]
    TwoFactor: Optional[str]
    TwoFactorAuthentication: Optional[str]
    TwoFactorNotification: Optional[str]
    Type: Optional[str]
    UsernameCaseInsensitivity: Optional[str]
    UsernameCaseSensitivity: Optional[str]
    Vdomparam: Optional[str]
    Workstation: Optional[str]

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
            AuthConcurrentOverride=json_data.get("AuthConcurrentOverride"),
            AuthConcurrentValue=json_data.get("AuthConcurrentValue"),
            Authtimeout=json_data.get("Authtimeout"),
            EmailTo=json_data.get("EmailTo"),
            Fortitoken=json_data.get("Fortitoken"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            LdapServer=json_data.get("LdapServer"),
            Name=json_data.get("Name"),
            Passwd=json_data.get("Passwd"),
            PasswdPolicy=json_data.get("PasswdPolicy"),
            PasswdTime=json_data.get("PasswdTime"),
            PpkIdentity=json_data.get("PpkIdentity"),
            PpkSecret=json_data.get("PpkSecret"),
            RadiusServer=json_data.get("RadiusServer"),
            SmsCustomServer=json_data.get("SmsCustomServer"),
            SmsPhone=json_data.get("SmsPhone"),
            SmsServer=json_data.get("SmsServer"),
            Status=json_data.get("Status"),
            TacacsServer=json_data.get("TacacsServer"),
            TwoFactor=json_data.get("TwoFactor"),
            TwoFactorAuthentication=json_data.get("TwoFactorAuthentication"),
            TwoFactorNotification=json_data.get("TwoFactorNotification"),
            Type=json_data.get("Type"),
            UsernameCaseInsensitivity=json_data.get("UsernameCaseInsensitivity"),
            UsernameCaseSensitivity=json_data.get("UsernameCaseSensitivity"),
            Vdomparam=json_data.get("Vdomparam"),
            Workstation=json_data.get("Workstation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


