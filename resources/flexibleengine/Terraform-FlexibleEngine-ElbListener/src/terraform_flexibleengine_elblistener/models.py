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
    BackendPort: Optional[float]
    BackendProtocol: Optional[str]
    CertificateId: Optional[str]
    CookieTimeout: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    LbAlgorithm: Optional[str]
    LoadbalancerId: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ProtocolPort: Optional[float]
    Region: Optional[str]
    SessionSticky: Optional[bool]
    SessionStickyType: Optional[str]
    SslCiphers: Optional[str]
    SslProtocols: Optional[str]
    TcpDraining: Optional[bool]
    TcpDrainingTimeout: Optional[float]
    TcpTimeout: Optional[float]
    UdpTimeout: Optional[float]
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
            BackendPort=json_data.get("BackendPort"),
            BackendProtocol=json_data.get("BackendProtocol"),
            CertificateId=json_data.get("CertificateId"),
            CookieTimeout=json_data.get("CookieTimeout"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LbAlgorithm=json_data.get("LbAlgorithm"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ProtocolPort=json_data.get("ProtocolPort"),
            Region=json_data.get("Region"),
            SessionSticky=json_data.get("SessionSticky"),
            SessionStickyType=json_data.get("SessionStickyType"),
            SslCiphers=json_data.get("SslCiphers"),
            SslProtocols=json_data.get("SslProtocols"),
            TcpDraining=json_data.get("TcpDraining"),
            TcpDrainingTimeout=json_data.get("TcpDrainingTimeout"),
            TcpTimeout=json_data.get("TcpTimeout"),
            UdpTimeout=json_data.get("UdpTimeout"),
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


