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
    Mode: Optional[str]
    PollingInterval: Optional[float]
    PortalUrl: Optional[str]
    UseSplitProxy: Optional[bool]
    UseTls: Optional[bool]
    Uuid: Optional[str]
    AppSignatureConfig: Optional[Sequence["_AppSignatureConfigDefinition"]]
    AssetContact: Optional[Sequence["_AssetContactDefinition"]]
    FeatureOptInStatus: Optional[Sequence["_FeatureOptInStatusDefinition"]]
    IpReputationConfig: Optional[Sequence["_IpReputationConfigDefinition"]]
    ProactiveSupportDefaults: Optional[Sequence["_ProactiveSupportDefaultsDefinition"]]
    SplitProxyConfiguration: Optional[Sequence["_SplitProxyConfigurationDefinition"]]

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
            Mode=json_data.get("Mode"),
            PollingInterval=json_data.get("PollingInterval"),
            PortalUrl=json_data.get("PortalUrl"),
            UseSplitProxy=json_data.get("UseSplitProxy"),
            UseTls=json_data.get("UseTls"),
            Uuid=json_data.get("Uuid"),
            AppSignatureConfig=deserialize_list(json_data.get("AppSignatureConfig"), AppSignatureConfigDefinition),
            AssetContact=deserialize_list(json_data.get("AssetContact"), AssetContactDefinition),
            FeatureOptInStatus=deserialize_list(json_data.get("FeatureOptInStatus"), FeatureOptInStatusDefinition),
            IpReputationConfig=deserialize_list(json_data.get("IpReputationConfig"), IpReputationConfigDefinition),
            ProactiveSupportDefaults=deserialize_list(json_data.get("ProactiveSupportDefaults"), ProactiveSupportDefaultsDefinition),
            SplitProxyConfiguration=deserialize_list(json_data.get("SplitProxyConfiguration"), SplitProxyConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppSignatureConfigDefinition(BaseModel):
    AppSignatureSyncInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AppSignatureConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppSignatureConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AppSignatureSyncInterval=json_data.get("AppSignatureSyncInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppSignatureConfigDefinition = AppSignatureConfigDefinition


@dataclass
class AssetContactDefinition(BaseModel):
    AccountId: Optional[str]
    AccountName: Optional[str]
    Email: Optional[str]
    Name: Optional[str]
    Phone: Optional[str]
    ManagedAccounts: Optional[Sequence["_ManagedAccountsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AssetContactDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetContactDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            AccountName=json_data.get("AccountName"),
            Email=json_data.get("Email"),
            Name=json_data.get("Name"),
            Phone=json_data.get("Phone"),
            ManagedAccounts=deserialize_list(json_data.get("ManagedAccounts"), ManagedAccountsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetContactDefinition = AssetContactDefinition


@dataclass
class ManagedAccountsDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Users: Optional[Sequence["_UsersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedAccountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedAccountsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedAccountsDefinition = ManagedAccountsDefinition


@dataclass
class UsersDefinition(BaseModel):
    Email: Optional[str]
    Name: Optional[str]
    Phone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Name=json_data.get("Name"),
            Phone=json_data.get("Phone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


@dataclass
class FeatureOptInStatusDefinition(BaseModel):
    EnableAppsignatureSync: Optional[bool]
    EnableAutoCaseCreationOnSeFailure: Optional[bool]
    EnableAutoCaseCreationOnSystemFailure: Optional[bool]
    EnableAutoDownloadWafSignatures: Optional[bool]
    EnableIpReputation: Optional[bool]
    EnableWafSignaturesNotifications: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureOptInStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureOptInStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableAppsignatureSync=json_data.get("EnableAppsignatureSync"),
            EnableAutoCaseCreationOnSeFailure=json_data.get("EnableAutoCaseCreationOnSeFailure"),
            EnableAutoCaseCreationOnSystemFailure=json_data.get("EnableAutoCaseCreationOnSystemFailure"),
            EnableAutoDownloadWafSignatures=json_data.get("EnableAutoDownloadWafSignatures"),
            EnableIpReputation=json_data.get("EnableIpReputation"),
            EnableWafSignaturesNotifications=json_data.get("EnableWafSignaturesNotifications"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureOptInStatusDefinition = FeatureOptInStatusDefinition


@dataclass
class IpReputationConfigDefinition(BaseModel):
    IpReputationFileObjectExpiryDuration: Optional[float]
    IpReputationSyncInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpReputationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpReputationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IpReputationFileObjectExpiryDuration=json_data.get("IpReputationFileObjectExpiryDuration"),
            IpReputationSyncInterval=json_data.get("IpReputationSyncInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpReputationConfigDefinition = IpReputationConfigDefinition


@dataclass
class ProactiveSupportDefaultsDefinition(BaseModel):
    AttachCoreDump: Optional[bool]
    AttachTechSupport: Optional[bool]
    CaseSeverity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProactiveSupportDefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProactiveSupportDefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            AttachCoreDump=json_data.get("AttachCoreDump"),
            AttachTechSupport=json_data.get("AttachTechSupport"),
            CaseSeverity=json_data.get("CaseSeverity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProactiveSupportDefaultsDefinition = ProactiveSupportDefaultsDefinition


@dataclass
class SplitProxyConfigurationDefinition(BaseModel):
    Host: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplitProxyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplitProxyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplitProxyConfigurationDefinition = SplitProxyConfigurationDefinition


