# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AuthType: Optional[str]
    CertBaseUrl: Optional[str]
    CertEnableHashAndUrl: Optional[bool]
    CertEnableStrictValidation: Optional[bool]
    CertPermitPayloadMismatch: Optional[bool]
    CertProfile: Optional[str]
    CertUseManagementAsSource: Optional[bool]
    DeadPeerDetectionInterval: Optional[float]
    DeadPeerDetectionRetry: Optional[float]
    Disabled: Optional[bool]
    EnableDeadPeerDetection: Optional[bool]
    EnableFragmentation: Optional[bool]
    EnableIpv6: Optional[bool]
    EnableLivenessCheck: Optional[bool]
    EnableNatTraversal: Optional[bool]
    EnablePassiveMode: Optional[bool]
    Ikev1CryptoProfile: Optional[str]
    Ikev1ExchangeMode: Optional[str]
    Ikev2CookieValidation: Optional[bool]
    Ikev2CryptoProfile: Optional[str]
    Interface: Optional[str]
    LivenessCheckInterval: Optional[float]
    LocalCert: Optional[str]
    LocalIdType: Optional[str]
    LocalIdValue: Optional[str]
    LocalIpAddressType: Optional[str]
    LocalIpAddressValue: Optional[str]
    Name: Optional[str]
    NatTraversalEnableUdpChecksum: Optional[bool]
    NatTraversalKeepAlive: Optional[float]
    PeerIdCheck: Optional[str]
    PeerIdType: Optional[str]
    PeerIdValue: Optional[str]
    PeerIpType: Optional[str]
    PeerIpValue: Optional[str]
    PreSharedKey: Optional[str]
    PreSharedKeyEnc: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthType=json_data.get("AuthType"),
            CertBaseUrl=json_data.get("CertBaseUrl"),
            CertEnableHashAndUrl=json_data.get("CertEnableHashAndUrl"),
            CertEnableStrictValidation=json_data.get("CertEnableStrictValidation"),
            CertPermitPayloadMismatch=json_data.get("CertPermitPayloadMismatch"),
            CertProfile=json_data.get("CertProfile"),
            CertUseManagementAsSource=json_data.get("CertUseManagementAsSource"),
            DeadPeerDetectionInterval=json_data.get("DeadPeerDetectionInterval"),
            DeadPeerDetectionRetry=json_data.get("DeadPeerDetectionRetry"),
            Disabled=json_data.get("Disabled"),
            EnableDeadPeerDetection=json_data.get("EnableDeadPeerDetection"),
            EnableFragmentation=json_data.get("EnableFragmentation"),
            EnableIpv6=json_data.get("EnableIpv6"),
            EnableLivenessCheck=json_data.get("EnableLivenessCheck"),
            EnableNatTraversal=json_data.get("EnableNatTraversal"),
            EnablePassiveMode=json_data.get("EnablePassiveMode"),
            Ikev1CryptoProfile=json_data.get("Ikev1CryptoProfile"),
            Ikev1ExchangeMode=json_data.get("Ikev1ExchangeMode"),
            Ikev2CookieValidation=json_data.get("Ikev2CookieValidation"),
            Ikev2CryptoProfile=json_data.get("Ikev2CryptoProfile"),
            Interface=json_data.get("Interface"),
            LivenessCheckInterval=json_data.get("LivenessCheckInterval"),
            LocalCert=json_data.get("LocalCert"),
            LocalIdType=json_data.get("LocalIdType"),
            LocalIdValue=json_data.get("LocalIdValue"),
            LocalIpAddressType=json_data.get("LocalIpAddressType"),
            LocalIpAddressValue=json_data.get("LocalIpAddressValue"),
            Name=json_data.get("Name"),
            NatTraversalEnableUdpChecksum=json_data.get("NatTraversalEnableUdpChecksum"),
            NatTraversalKeepAlive=json_data.get("NatTraversalKeepAlive"),
            PeerIdCheck=json_data.get("PeerIdCheck"),
            PeerIdType=json_data.get("PeerIdType"),
            PeerIdValue=json_data.get("PeerIdValue"),
            PeerIpType=json_data.get("PeerIpType"),
            PeerIpValue=json_data.get("PeerIpValue"),
            PreSharedKey=json_data.get("PreSharedKey"),
            PreSharedKeyEnc=json_data.get("PreSharedKeyEnc"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


