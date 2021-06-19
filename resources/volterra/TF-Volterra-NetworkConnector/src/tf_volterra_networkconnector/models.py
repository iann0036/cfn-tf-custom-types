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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    DisableForwardProxy: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    SliToSloDr: Optional[bool]
    EnableForwardProxy: Optional[Sequence["_EnableForwardProxyDefinition"]]
    SliToGlobalDr: Optional[Sequence["_SliToGlobalDrDefinition"]]
    SliToGlobalSnat: Optional[Sequence["_SliToGlobalSnatDefinition"]]
    SliToSloSnat: Optional[Sequence["_SliToSloSnatDefinition"]]
    SloToGlobalDr: Optional[Sequence["_SloToGlobalDrDefinition"]]
    SloToGlobalSnat: Optional[Sequence["_SloToGlobalSnatDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DisableForwardProxy=json_data.get("DisableForwardProxy"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            SliToSloDr=json_data.get("SliToSloDr"),
            EnableForwardProxy=deserialize_list(json_data.get("EnableForwardProxy"), EnableForwardProxyDefinition),
            SliToGlobalDr=deserialize_list(json_data.get("SliToGlobalDr"), SliToGlobalDrDefinition),
            SliToGlobalSnat=deserialize_list(json_data.get("SliToGlobalSnat"), SliToGlobalSnatDefinition),
            SliToSloSnat=deserialize_list(json_data.get("SliToSloSnat"), SliToSloSnatDefinition),
            SloToGlobalDr=deserialize_list(json_data.get("SloToGlobalDr"), SloToGlobalDrDefinition),
            SloToGlobalSnat=deserialize_list(json_data.get("SloToGlobalSnat"), SloToGlobalSnatDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class EnableForwardProxyDefinition(BaseModel):
    ConnectionTimeout: Optional[float]
    MaxConnectAttempts: Optional[float]
    NoInterception: Optional[bool]
    WhiteListedPorts: Optional[Sequence[float]]
    WhiteListedPrefixes: Optional[Sequence[str]]
    TlsIntercept: Optional[Sequence["_TlsInterceptDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnableForwardProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableForwardProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            MaxConnectAttempts=json_data.get("MaxConnectAttempts"),
            NoInterception=json_data.get("NoInterception"),
            WhiteListedPorts=json_data.get("WhiteListedPorts"),
            WhiteListedPrefixes=json_data.get("WhiteListedPrefixes"),
            TlsIntercept=deserialize_list(json_data.get("TlsIntercept"), TlsInterceptDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableForwardProxyDefinition = EnableForwardProxyDefinition


@dataclass
class TlsInterceptDefinition(BaseModel):
    EnableForAllDomains: Optional[bool]
    TrustedCaUrl: Optional[str]
    VolterraCertificate: Optional[bool]
    VolterraTrustedCa: Optional[bool]
    CustomCertificate: Optional[Sequence["_CustomCertificateDefinition"]]
    Policy: Optional[Sequence["_PolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsInterceptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsInterceptDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableForAllDomains=json_data.get("EnableForAllDomains"),
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
            VolterraCertificate=json_data.get("VolterraCertificate"),
            VolterraTrustedCa=json_data.get("VolterraTrustedCa"),
            CustomCertificate=deserialize_list(json_data.get("CustomCertificate"), CustomCertificateDefinition),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsInterceptDefinition = TlsInterceptDefinition


@dataclass
class CustomCertificateDefinition(BaseModel):
    CertificateUrl: Optional[str]
    Description: Optional[str]
    PrivateKey: Optional[Sequence["_PrivateKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Description=json_data.get("Description"),
            PrivateKey=deserialize_list(json_data.get("PrivateKey"), PrivateKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCertificateDefinition = CustomCertificateDefinition


@dataclass
class PrivateKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretEncodingType=json_data.get("SecretEncodingType"),
            BlindfoldSecretInfo=deserialize_list(json_data.get("BlindfoldSecretInfo"), BlindfoldSecretInfoDefinition),
            BlindfoldSecretInfoInternal=deserialize_list(json_data.get("BlindfoldSecretInfoInternal"), BlindfoldSecretInfoInternalDefinition),
            ClearSecretInfo=deserialize_list(json_data.get("ClearSecretInfo"), ClearSecretInfoDefinition),
            VaultSecretInfo=deserialize_list(json_data.get("VaultSecretInfo"), VaultSecretInfoDefinition),
            WingmanSecretInfo=deserialize_list(json_data.get("WingmanSecretInfo"), WingmanSecretInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyDefinition = PrivateKeyDefinition


@dataclass
class BlindfoldSecretInfoDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoDefinition = BlindfoldSecretInfoDefinition


@dataclass
class BlindfoldSecretInfoInternalDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoInternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoInternalDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoInternalDefinition = BlindfoldSecretInfoInternalDefinition


@dataclass
class ClearSecretInfoDefinition(BaseModel):
    Provider: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClearSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClearSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Provider=json_data.get("Provider"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClearSecretInfoDefinition = ClearSecretInfoDefinition


@dataclass
class VaultSecretInfoDefinition(BaseModel):
    Key: Optional[str]
    Location: Optional[str]
    Provider: Optional[str]
    SecretEncoding: Optional[str]
    Version: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VaultSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Location=json_data.get("Location"),
            Provider=json_data.get("Provider"),
            SecretEncoding=json_data.get("SecretEncoding"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultSecretInfoDefinition = VaultSecretInfoDefinition


@dataclass
class WingmanSecretInfoDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WingmanSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WingmanSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WingmanSecretInfoDefinition = WingmanSecretInfoDefinition


@dataclass
class PolicyDefinition(BaseModel):
    InterceptionRules: Optional[Sequence["_InterceptionRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InterceptionRules=deserialize_list(json_data.get("InterceptionRules"), InterceptionRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class InterceptionRulesDefinition(BaseModel):
    DisableInterception: Optional[bool]
    EnableInterception: Optional[bool]
    DomainMatch: Optional[Sequence["_DomainMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterceptionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterceptionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableInterception=json_data.get("DisableInterception"),
            EnableInterception=json_data.get("EnableInterception"),
            DomainMatch=deserialize_list(json_data.get("DomainMatch"), DomainMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterceptionRulesDefinition = InterceptionRulesDefinition


@dataclass
class DomainMatchDefinition(BaseModel):
    ExactValue: Optional[str]
    RegexValue: Optional[str]
    SuffixValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValue=json_data.get("ExactValue"),
            RegexValue=json_data.get("RegexValue"),
            SuffixValue=json_data.get("SuffixValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainMatchDefinition = DomainMatchDefinition


@dataclass
class SliToGlobalDrDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SliToGlobalDrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliToGlobalDrDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliToGlobalDrDefinition = SliToGlobalDrDefinition


@dataclass
class GlobalVnDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalVnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalVnDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalVnDefinition = GlobalVnDefinition


@dataclass
class SliToGlobalSnatDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]
    SnatConfig: Optional[Sequence["_SnatConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SliToGlobalSnatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliToGlobalSnatDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
            SnatConfig=deserialize_list(json_data.get("SnatConfig"), SnatConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliToGlobalSnatDefinition = SliToGlobalSnatDefinition


@dataclass
class SnatConfigDefinition(BaseModel):
    DefaultGwSnat: Optional[bool]
    DynamicRouting: Optional[bool]
    InterfaceIp: Optional[bool]
    SnatPool: Optional[str]
    SnatPoolAllocator: Optional[Sequence["_SnatPoolAllocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnatConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultGwSnat=json_data.get("DefaultGwSnat"),
            DynamicRouting=json_data.get("DynamicRouting"),
            InterfaceIp=json_data.get("InterfaceIp"),
            SnatPool=json_data.get("SnatPool"),
            SnatPoolAllocator=deserialize_list(json_data.get("SnatPoolAllocator"), SnatPoolAllocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatConfigDefinition = SnatConfigDefinition


@dataclass
class SnatPoolAllocatorDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnatPoolAllocatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatPoolAllocatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatPoolAllocatorDefinition = SnatPoolAllocatorDefinition


@dataclass
class SliToSloSnatDefinition(BaseModel):
    DefaultGwSnat: Optional[bool]
    DynamicRouting: Optional[bool]
    InterfaceIp: Optional[bool]
    SnatPool: Optional[str]
    SnatPoolAllocator: Optional[Sequence["_SnatPoolAllocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SliToSloSnatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliToSloSnatDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultGwSnat=json_data.get("DefaultGwSnat"),
            DynamicRouting=json_data.get("DynamicRouting"),
            InterfaceIp=json_data.get("InterfaceIp"),
            SnatPool=json_data.get("SnatPool"),
            SnatPoolAllocator=deserialize_list(json_data.get("SnatPoolAllocator"), SnatPoolAllocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliToSloSnatDefinition = SliToSloSnatDefinition


@dataclass
class SloToGlobalDrDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SloToGlobalDrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SloToGlobalDrDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SloToGlobalDrDefinition = SloToGlobalDrDefinition


@dataclass
class SloToGlobalSnatDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]
    SnatConfig: Optional[Sequence["_SnatConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SloToGlobalSnatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SloToGlobalSnatDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
            SnatConfig=deserialize_list(json_data.get("SnatConfig"), SnatConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SloToGlobalSnatDefinition = SloToGlobalSnatDefinition


