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
    ApiManagementId: Optional[str]
    Id: Optional[str]
    DeveloperPortal: Optional[Sequence["_DeveloperPortalDefinition"]]
    Management: Optional[Sequence["_ManagementDefinition"]]
    Portal: Optional[Sequence["_PortalDefinition"]]
    Proxy: Optional[Sequence["_ProxyDefinition"]]
    Scm: Optional[Sequence["_ScmDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            ApiManagementId=json_data.get("ApiManagementId"),
            Id=json_data.get("Id"),
            DeveloperPortal=deserialize_list(json_data.get("DeveloperPortal"), DeveloperPortalDefinition),
            Management=deserialize_list(json_data.get("Management"), ManagementDefinition),
            Portal=deserialize_list(json_data.get("Portal"), PortalDefinition),
            Proxy=deserialize_list(json_data.get("Proxy"), ProxyDefinition),
            Scm=deserialize_list(json_data.get("Scm"), ScmDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeveloperPortalDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeveloperPortalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeveloperPortalDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeveloperPortalDefinition = DeveloperPortalDefinition


@dataclass
class ManagementDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementDefinition = ManagementDefinition


@dataclass
class PortalDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PortalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortalDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortalDefinition = PortalDefinition


@dataclass
class ProxyDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    DefaultSslBinding: Optional[bool]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            DefaultSslBinding=json_data.get("DefaultSslBinding"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyDefinition = ProxyDefinition


@dataclass
class ScmDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ScmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScmDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScmDefinition = ScmDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


