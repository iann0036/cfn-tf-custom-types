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
    AppProtocols: Optional[Sequence[str]]
    AppType: Optional[str]
    CreateTime: Optional[str]
    HasAbroad: Optional[str]
    HasInitiateTcp: Optional[str]
    HasInitiateUdp: Optional[str]
    HasVpn: Optional[str]
    Id: Optional[str]
    MaxTcpPackageLen: Optional[str]
    MaxUdpPackageLen: Optional[str]
    MinTcpPackageLen: Optional[str]
    MinUdpPackageLen: Optional[str]
    Name: Optional[str]
    PeerTcpPort: Optional[str]
    PeerUdpPort: Optional[str]
    PlatformTypes: Optional[Sequence[str]]
    ResourceType: Optional[str]
    SceneId: Optional[str]
    TcpEndPort: Optional[str]
    TcpFootprint: Optional[str]
    TcpStartPort: Optional[str]
    UdpEndPort: Optional[str]
    UdpFootprint: Optional[str]
    UdpStartPort: Optional[str]
    WebApiUrls: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppProtocols=json_data.get("AppProtocols"),
            AppType=json_data.get("AppType"),
            CreateTime=json_data.get("CreateTime"),
            HasAbroad=json_data.get("HasAbroad"),
            HasInitiateTcp=json_data.get("HasInitiateTcp"),
            HasInitiateUdp=json_data.get("HasInitiateUdp"),
            HasVpn=json_data.get("HasVpn"),
            Id=json_data.get("Id"),
            MaxTcpPackageLen=json_data.get("MaxTcpPackageLen"),
            MaxUdpPackageLen=json_data.get("MaxUdpPackageLen"),
            MinTcpPackageLen=json_data.get("MinTcpPackageLen"),
            MinUdpPackageLen=json_data.get("MinUdpPackageLen"),
            Name=json_data.get("Name"),
            PeerTcpPort=json_data.get("PeerTcpPort"),
            PeerUdpPort=json_data.get("PeerUdpPort"),
            PlatformTypes=json_data.get("PlatformTypes"),
            ResourceType=json_data.get("ResourceType"),
            SceneId=json_data.get("SceneId"),
            TcpEndPort=json_data.get("TcpEndPort"),
            TcpFootprint=json_data.get("TcpFootprint"),
            TcpStartPort=json_data.get("TcpStartPort"),
            UdpEndPort=json_data.get("UdpEndPort"),
            UdpFootprint=json_data.get("UdpFootprint"),
            UdpStartPort=json_data.get("UdpStartPort"),
            WebApiUrls=json_data.get("WebApiUrls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


