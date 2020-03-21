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
    AdminStateUp: Optional[bool]
    BackendPort: Optional[float]
    BackendProtocol: Optional[str]
    CertificateId: Optional[str]
    Certificates: Optional[Sequence[str]]
    CookieTimeout: Optional[float]
    CreateTime: Optional[str]
    Description: Optional[str]
    HealthcheckId: Optional[str]
    LbAlgorithm: Optional[str]
    LoadbalancerId: Optional[str]
    MemberNumber: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    SessionSticky: Optional[bool]
    SslCiphers: Optional[str]
    SslProtocols: Optional[str]
    Status: Optional[str]
    StickySessionType: Optional[str]
    TcpDraining: Optional[bool]
    TcpDrainingTimeout: Optional[float]
    TcpTimeout: Optional[float]
    UdpTimeout: Optional[float]
    UpdateTime: Optional[str]
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
            AdminStateUp=json_data.get("AdminStateUp"),
            BackendPort=json_data.get("BackendPort"),
            BackendProtocol=json_data.get("BackendProtocol"),
            CertificateId=json_data.get("CertificateId"),
            Certificates=json_data.get("Certificates"),
            CookieTimeout=json_data.get("CookieTimeout"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            HealthcheckId=json_data.get("HealthcheckId"),
            LbAlgorithm=json_data.get("LbAlgorithm"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            MemberNumber=json_data.get("MemberNumber"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SessionSticky=json_data.get("SessionSticky"),
            SslCiphers=json_data.get("SslCiphers"),
            SslProtocols=json_data.get("SslProtocols"),
            Status=json_data.get("Status"),
            StickySessionType=json_data.get("StickySessionType"),
            TcpDraining=json_data.get("TcpDraining"),
            TcpDrainingTimeout=json_data.get("TcpDrainingTimeout"),
            TcpTimeout=json_data.get("TcpTimeout"),
            UdpTimeout=json_data.get("UdpTimeout"),
            UpdateTime=json_data.get("UpdateTime"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


