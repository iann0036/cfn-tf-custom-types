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
    AcctAllServers: Optional[str]
    AcctInterimInterval: Optional[float]
    AllUsergroup: Optional[str]
    AuthType: Optional[str]
    DynamicSortSubtable: Optional[str]
    GroupOverrideAttrType: Optional[str]
    H3cCompatibility: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    Name: Optional[str]
    NasIp: Optional[str]
    PasswordEncoding: Optional[str]
    PasswordRenewal: Optional[str]
    RadiusCoa: Optional[str]
    RadiusPort: Optional[float]
    Rsso: Optional[str]
    RssoContextTimeout: Optional[float]
    RssoEndpointAttribute: Optional[str]
    RssoEndpointBlockAttribute: Optional[str]
    RssoEpOneIpOnly: Optional[str]
    RssoFlushIpSession: Optional[str]
    RssoLogFlags: Optional[str]
    RssoLogPeriod: Optional[float]
    RssoRadiusResponse: Optional[str]
    RssoRadiusServerPort: Optional[float]
    RssoSecret: Optional[str]
    RssoValidateRequestSecret: Optional[str]
    SecondarySecret: Optional[str]
    SecondaryServer: Optional[str]
    Secret: Optional[str]
    Server: Optional[str]
    SourceIp: Optional[str]
    SsoAttribute: Optional[str]
    SsoAttributeKey: Optional[str]
    SsoAttributeValueOverride: Optional[str]
    SwitchControllerAcctFastFramedipDetect: Optional[float]
    SwitchControllerServiceType: Optional[str]
    TertiarySecret: Optional[str]
    TertiaryServer: Optional[str]
    Timeout: Optional[float]
    UseManagementVdom: Optional[str]
    UsernameCaseSensitive: Optional[str]
    Vdomparam: Optional[str]
    AccountingServer: Optional[Sequence["_AccountingServerDefinition"]]
    Class: Optional[Sequence["_ClassDefinition"]]

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
            AcctAllServers=json_data.get("AcctAllServers"),
            AcctInterimInterval=json_data.get("AcctInterimInterval"),
            AllUsergroup=json_data.get("AllUsergroup"),
            AuthType=json_data.get("AuthType"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GroupOverrideAttrType=json_data.get("GroupOverrideAttrType"),
            H3cCompatibility=json_data.get("H3cCompatibility"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            Name=json_data.get("Name"),
            NasIp=json_data.get("NasIp"),
            PasswordEncoding=json_data.get("PasswordEncoding"),
            PasswordRenewal=json_data.get("PasswordRenewal"),
            RadiusCoa=json_data.get("RadiusCoa"),
            RadiusPort=json_data.get("RadiusPort"),
            Rsso=json_data.get("Rsso"),
            RssoContextTimeout=json_data.get("RssoContextTimeout"),
            RssoEndpointAttribute=json_data.get("RssoEndpointAttribute"),
            RssoEndpointBlockAttribute=json_data.get("RssoEndpointBlockAttribute"),
            RssoEpOneIpOnly=json_data.get("RssoEpOneIpOnly"),
            RssoFlushIpSession=json_data.get("RssoFlushIpSession"),
            RssoLogFlags=json_data.get("RssoLogFlags"),
            RssoLogPeriod=json_data.get("RssoLogPeriod"),
            RssoRadiusResponse=json_data.get("RssoRadiusResponse"),
            RssoRadiusServerPort=json_data.get("RssoRadiusServerPort"),
            RssoSecret=json_data.get("RssoSecret"),
            RssoValidateRequestSecret=json_data.get("RssoValidateRequestSecret"),
            SecondarySecret=json_data.get("SecondarySecret"),
            SecondaryServer=json_data.get("SecondaryServer"),
            Secret=json_data.get("Secret"),
            Server=json_data.get("Server"),
            SourceIp=json_data.get("SourceIp"),
            SsoAttribute=json_data.get("SsoAttribute"),
            SsoAttributeKey=json_data.get("SsoAttributeKey"),
            SsoAttributeValueOverride=json_data.get("SsoAttributeValueOverride"),
            SwitchControllerAcctFastFramedipDetect=json_data.get("SwitchControllerAcctFastFramedipDetect"),
            SwitchControllerServiceType=json_data.get("SwitchControllerServiceType"),
            TertiarySecret=json_data.get("TertiarySecret"),
            TertiaryServer=json_data.get("TertiaryServer"),
            Timeout=json_data.get("Timeout"),
            UseManagementVdom=json_data.get("UseManagementVdom"),
            UsernameCaseSensitive=json_data.get("UsernameCaseSensitive"),
            Vdomparam=json_data.get("Vdomparam"),
            AccountingServer=deserialize_list(json_data.get("AccountingServer"), AccountingServerDefinition),
            Class=deserialize_list(json_data.get("Class"), ClassDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountingServerDefinition(BaseModel):
    Id: Optional[float]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    Port: Optional[float]
    Secret: Optional[str]
    Server: Optional[str]
    SourceIp: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountingServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountingServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            Port=json_data.get("Port"),
            Secret=json_data.get("Secret"),
            Server=json_data.get("Server"),
            SourceIp=json_data.get("SourceIp"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountingServerDefinition = AccountingServerDefinition


@dataclass
class ClassDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassDefinition = ClassDefinition


