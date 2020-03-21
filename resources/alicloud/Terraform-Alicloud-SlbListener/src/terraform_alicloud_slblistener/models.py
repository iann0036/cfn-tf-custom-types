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
    AclId: Optional[str]
    AclStatus: Optional[str]
    AclType: Optional[str]
    BackendPort: Optional[float]
    Bandwidth: Optional[float]
    Cookie: Optional[str]
    CookieTimeout: Optional[float]
    DeleteProtectionValidation: Optional[bool]
    Description: Optional[str]
    EnableHttp2: Optional[str]
    EstablishedTimeout: Optional[float]
    ForwardPort: Optional[float]
    FrontendPort: Optional[float]
    Gzip: Optional[bool]
    HealthCheck: Optional[str]
    HealthCheckConnectPort: Optional[float]
    HealthCheckDomain: Optional[str]
    HealthCheckHttpCode: Optional[str]
    HealthCheckInterval: Optional[float]
    HealthCheckMethod: Optional[str]
    HealthCheckTimeout: Optional[float]
    HealthCheckType: Optional[str]
    HealthCheckUri: Optional[str]
    HealthyThreshold: Optional[float]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    InstancePort: Optional[float]
    LbPort: Optional[float]
    LbProtocol: Optional[str]
    ListenerForward: Optional[str]
    LoadBalancerId: Optional[str]
    MasterSlaveServerGroupId: Optional[str]
    PersistenceTimeout: Optional[float]
    Protocol: Optional[str]
    RequestTimeout: Optional[float]
    Scheduler: Optional[str]
    ServerCertificateId: Optional[str]
    ServerGroupId: Optional[str]
    SslCertificateId: Optional[str]
    StickySession: Optional[str]
    StickySessionType: Optional[str]
    TlsCipherPolicy: Optional[str]
    UnhealthyThreshold: Optional[float]
    XForwardedFor: Optional[Sequence["_XForwardedFor"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AclId=json_data.get("AclId"),
            AclStatus=json_data.get("AclStatus"),
            AclType=json_data.get("AclType"),
            BackendPort=json_data.get("BackendPort"),
            Bandwidth=json_data.get("Bandwidth"),
            Cookie=json_data.get("Cookie"),
            CookieTimeout=json_data.get("CookieTimeout"),
            DeleteProtectionValidation=json_data.get("DeleteProtectionValidation"),
            Description=json_data.get("Description"),
            EnableHttp2=json_data.get("EnableHttp2"),
            EstablishedTimeout=json_data.get("EstablishedTimeout"),
            ForwardPort=json_data.get("ForwardPort"),
            FrontendPort=json_data.get("FrontendPort"),
            Gzip=json_data.get("Gzip"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckConnectPort=json_data.get("HealthCheckConnectPort"),
            HealthCheckDomain=json_data.get("HealthCheckDomain"),
            HealthCheckHttpCode=json_data.get("HealthCheckHttpCode"),
            HealthCheckInterval=json_data.get("HealthCheckInterval"),
            HealthCheckMethod=json_data.get("HealthCheckMethod"),
            HealthCheckTimeout=json_data.get("HealthCheckTimeout"),
            HealthCheckType=json_data.get("HealthCheckType"),
            HealthCheckUri=json_data.get("HealthCheckUri"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            InstancePort=json_data.get("InstancePort"),
            LbPort=json_data.get("LbPort"),
            LbProtocol=json_data.get("LbProtocol"),
            ListenerForward=json_data.get("ListenerForward"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            MasterSlaveServerGroupId=json_data.get("MasterSlaveServerGroupId"),
            PersistenceTimeout=json_data.get("PersistenceTimeout"),
            Protocol=json_data.get("Protocol"),
            RequestTimeout=json_data.get("RequestTimeout"),
            Scheduler=json_data.get("Scheduler"),
            ServerCertificateId=json_data.get("ServerCertificateId"),
            ServerGroupId=json_data.get("ServerGroupId"),
            SslCertificateId=json_data.get("SslCertificateId"),
            StickySession=json_data.get("StickySession"),
            StickySessionType=json_data.get("StickySessionType"),
            TlsCipherPolicy=json_data.get("TlsCipherPolicy"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            XForwardedFor=json_data.get("XForwardedFor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class XForwardedFor:
    RetriveSlbId: Optional[bool]
    RetriveSlbIp: Optional[bool]
    RetriveSlbProto: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_XForwardedFor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XForwardedFor"]:
        if not json_data:
            return None
        return cls(
            RetriveSlbId=json_data.get("RetriveSlbId"),
            RetriveSlbIp=json_data.get("RetriveSlbIp"),
            RetriveSlbProto=json_data.get("RetriveSlbProto"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XForwardedFor = XForwardedFor


