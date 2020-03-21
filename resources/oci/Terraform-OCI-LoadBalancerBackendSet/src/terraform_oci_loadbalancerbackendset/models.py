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
    Backend: Optional[Sequence["_Backend"]]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    Policy: Optional[str]
    State: Optional[str]
    HealthChecker: Optional[Sequence["_HealthChecker"]]
    LbCookieSessionPersistenceConfiguration: Optional[Sequence["_LbCookieSessionPersistenceConfiguration"]]
    SessionPersistenceConfiguration: Optional[Sequence["_SessionPersistenceConfiguration"]]
    SslConfiguration: Optional[Sequence["_SslConfiguration"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            State=json_data.get("State"),
            HealthChecker=json_data.get("HealthChecker"),
            LbCookieSessionPersistenceConfiguration=json_data.get("LbCookieSessionPersistenceConfiguration"),
            SessionPersistenceConfiguration=json_data.get("SessionPersistenceConfiguration"),
            SslConfiguration=json_data.get("SslConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backend:
    Backup: Optional[bool]
    Drain: Optional[bool]
    IpAddress: Optional[str]
    Name: Optional[str]
    Offline: Optional[bool]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
        if not json_data:
            return None
        return cls(
            Backup=json_data.get("Backup"),
            Drain=json_data.get("Drain"),
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            Offline=json_data.get("Offline"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


@dataclass
class HealthChecker:
    IntervalMs: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    ResponseBodyRegex: Optional[str]
    Retries: Optional[float]
    ReturnCode: Optional[float]
    TimeoutInMillis: Optional[float]
    UrlPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthChecker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthChecker"]:
        if not json_data:
            return None
        return cls(
            IntervalMs=json_data.get("IntervalMs"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ResponseBodyRegex=json_data.get("ResponseBodyRegex"),
            Retries=json_data.get("Retries"),
            ReturnCode=json_data.get("ReturnCode"),
            TimeoutInMillis=json_data.get("TimeoutInMillis"),
            UrlPath=json_data.get("UrlPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthChecker = HealthChecker


@dataclass
class LbCookieSessionPersistenceConfiguration:
    CookieName: Optional[str]
    DisableFallback: Optional[bool]
    Domain: Optional[str]
    IsHttpOnly: Optional[bool]
    IsSecure: Optional[bool]
    MaxAgeInSeconds: Optional[float]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LbCookieSessionPersistenceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LbCookieSessionPersistenceConfiguration"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            DisableFallback=json_data.get("DisableFallback"),
            Domain=json_data.get("Domain"),
            IsHttpOnly=json_data.get("IsHttpOnly"),
            IsSecure=json_data.get("IsSecure"),
            MaxAgeInSeconds=json_data.get("MaxAgeInSeconds"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LbCookieSessionPersistenceConfiguration = LbCookieSessionPersistenceConfiguration


@dataclass
class SessionPersistenceConfiguration:
    CookieName: Optional[str]
    DisableFallback: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SessionPersistenceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionPersistenceConfiguration"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            DisableFallback=json_data.get("DisableFallback"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionPersistenceConfiguration = SessionPersistenceConfiguration


@dataclass
class SslConfiguration:
    CertificateName: Optional[str]
    VerifyDepth: Optional[float]
    VerifyPeerCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SslConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslConfiguration"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            VerifyDepth=json_data.get("VerifyDepth"),
            VerifyPeerCertificate=json_data.get("VerifyPeerCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslConfiguration = SslConfiguration


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


