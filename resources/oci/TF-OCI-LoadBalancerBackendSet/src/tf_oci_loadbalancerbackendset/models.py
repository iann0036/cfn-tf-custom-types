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
    Backend: Optional[Sequence["_BackendDefinition"]]
    Id: Optional[str]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    Policy: Optional[str]
    State: Optional[str]
    HealthChecker: Optional[Sequence["_HealthCheckerDefinition"]]
    LbCookieSessionPersistenceConfiguration: Optional[Sequence["_LbCookieSessionPersistenceConfigurationDefinition"]]
    SessionPersistenceConfiguration: Optional[Sequence["_SessionPersistenceConfigurationDefinition"]]
    SslConfiguration: Optional[Sequence["_SslConfigurationDefinition"]]
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
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            State=json_data.get("State"),
            HealthChecker=deserialize_list(json_data.get("HealthChecker"), HealthCheckerDefinition),
            LbCookieSessionPersistenceConfiguration=deserialize_list(json_data.get("LbCookieSessionPersistenceConfiguration"), LbCookieSessionPersistenceConfigurationDefinition),
            SessionPersistenceConfiguration=deserialize_list(json_data.get("SessionPersistenceConfiguration"), SessionPersistenceConfigurationDefinition),
            SslConfiguration=deserialize_list(json_data.get("SslConfiguration"), SslConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendDefinition(BaseModel):
    Backup: Optional[bool]
    Drain: Optional[bool]
    IpAddress: Optional[str]
    Name: Optional[str]
    Offline: Optional[bool]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
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
_BackendDefinition = BackendDefinition


@dataclass
class HealthCheckerDefinition(BaseModel):
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
        cls: Type["_HealthCheckerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckerDefinition"]:
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
_HealthCheckerDefinition = HealthCheckerDefinition


@dataclass
class LbCookieSessionPersistenceConfigurationDefinition(BaseModel):
    CookieName: Optional[str]
    DisableFallback: Optional[bool]
    Domain: Optional[str]
    IsHttpOnly: Optional[bool]
    IsSecure: Optional[bool]
    MaxAgeInSeconds: Optional[float]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LbCookieSessionPersistenceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LbCookieSessionPersistenceConfigurationDefinition"]:
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
_LbCookieSessionPersistenceConfigurationDefinition = LbCookieSessionPersistenceConfigurationDefinition


@dataclass
class SessionPersistenceConfigurationDefinition(BaseModel):
    CookieName: Optional[str]
    DisableFallback: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SessionPersistenceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionPersistenceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            DisableFallback=json_data.get("DisableFallback"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionPersistenceConfigurationDefinition = SessionPersistenceConfigurationDefinition


@dataclass
class SslConfigurationDefinition(BaseModel):
    CertificateName: Optional[str]
    CipherSuiteName: Optional[str]
    Protocols: Optional[Sequence[str]]
    ServerOrderPreference: Optional[str]
    VerifyDepth: Optional[float]
    VerifyPeerCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SslConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            CipherSuiteName=json_data.get("CipherSuiteName"),
            Protocols=json_data.get("Protocols"),
            ServerOrderPreference=json_data.get("ServerOrderPreference"),
            VerifyDepth=json_data.get("VerifyDepth"),
            VerifyPeerCertificate=json_data.get("VerifyPeerCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslConfigurationDefinition = SslConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


