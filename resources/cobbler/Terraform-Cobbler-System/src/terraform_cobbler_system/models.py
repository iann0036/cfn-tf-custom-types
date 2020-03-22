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
    BootFiles: Optional[str]
    Comment: Optional[str]
    EnableGpxe: Optional[bool]
    FetchableFiles: Optional[str]
    Gateway: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    Ipv6DefaultDevice: Optional[str]
    KernelOptions: Optional[str]
    KernelOptionsPost: Optional[str]
    Kickstart: Optional[str]
    KsMeta: Optional[str]
    LdapEnabled: Optional[bool]
    LdapType: Optional[str]
    MgmtClasses: Optional[Sequence[str]]
    MgmtParameters: Optional[str]
    MonitEnabled: Optional[bool]
    Name: Optional[str]
    NameServers: Optional[Sequence[str]]
    NameServersSearch: Optional[Sequence[str]]
    NetbootEnabled: Optional[bool]
    Owners: Optional[Sequence[str]]
    PowerAddress: Optional[str]
    PowerId: Optional[str]
    PowerPass: Optional[str]
    PowerType: Optional[str]
    PowerUser: Optional[str]
    Profile: Optional[str]
    Proxy: Optional[str]
    RedhatManagementKey: Optional[str]
    RedhatManagementServer: Optional[str]
    Status: Optional[str]
    TemplateFiles: Optional[str]
    TemplateRemoteKickstarts: Optional[float]
    VirtAutoBoot: Optional[str]
    VirtCpus: Optional[str]
    VirtDiskDriver: Optional[str]
    VirtFileSize: Optional[str]
    VirtPath: Optional[str]
    VirtPxeBoot: Optional[float]
    VirtRam: Optional[str]
    VirtType: Optional[str]
    Interface: Optional[Sequence["_Interface"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BootFiles=json_data.get("BootFiles"),
            Comment=json_data.get("Comment"),
            EnableGpxe=json_data.get("EnableGpxe"),
            FetchableFiles=json_data.get("FetchableFiles"),
            Gateway=json_data.get("Gateway"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Ipv6DefaultDevice=json_data.get("Ipv6DefaultDevice"),
            KernelOptions=json_data.get("KernelOptions"),
            KernelOptionsPost=json_data.get("KernelOptionsPost"),
            Kickstart=json_data.get("Kickstart"),
            KsMeta=json_data.get("KsMeta"),
            LdapEnabled=json_data.get("LdapEnabled"),
            LdapType=json_data.get("LdapType"),
            MgmtClasses=json_data.get("MgmtClasses"),
            MgmtParameters=json_data.get("MgmtParameters"),
            MonitEnabled=json_data.get("MonitEnabled"),
            Name=json_data.get("Name"),
            NameServers=json_data.get("NameServers"),
            NameServersSearch=json_data.get("NameServersSearch"),
            NetbootEnabled=json_data.get("NetbootEnabled"),
            Owners=json_data.get("Owners"),
            PowerAddress=json_data.get("PowerAddress"),
            PowerId=json_data.get("PowerId"),
            PowerPass=json_data.get("PowerPass"),
            PowerType=json_data.get("PowerType"),
            PowerUser=json_data.get("PowerUser"),
            Profile=json_data.get("Profile"),
            Proxy=json_data.get("Proxy"),
            RedhatManagementKey=json_data.get("RedhatManagementKey"),
            RedhatManagementServer=json_data.get("RedhatManagementServer"),
            Status=json_data.get("Status"),
            TemplateFiles=json_data.get("TemplateFiles"),
            TemplateRemoteKickstarts=json_data.get("TemplateRemoteKickstarts"),
            VirtAutoBoot=json_data.get("VirtAutoBoot"),
            VirtCpus=json_data.get("VirtCpus"),
            VirtDiskDriver=json_data.get("VirtDiskDriver"),
            VirtFileSize=json_data.get("VirtFileSize"),
            VirtPath=json_data.get("VirtPath"),
            VirtPxeBoot=json_data.get("VirtPxeBoot"),
            VirtRam=json_data.get("VirtRam"),
            VirtType=json_data.get("VirtType"),
            Interface=json_data.get("Interface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Interface:
    BondingOpts: Optional[str]
    BridgeOpts: Optional[str]
    Cnames: Optional[Sequence[str]]
    DhcpTag: Optional[str]
    DnsName: Optional[str]
    Gateway: Optional[str]
    InterfaceMaster: Optional[str]
    InterfaceType: Optional[str]
    IpAddress: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6DefaultGateway: Optional[str]
    Ipv6Mtu: Optional[str]
    Ipv6Secondaries: Optional[Sequence[str]]
    Ipv6StaticRoutes: Optional[Sequence[str]]
    MacAddress: Optional[str]
    Management: Optional[bool]
    Name: Optional[str]
    Netmask: Optional[str]
    Static: Optional[bool]
    StaticRoutes: Optional[Sequence[str]]
    VirtBridge: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface"]:
        if not json_data:
            return None
        return cls(
            BondingOpts=json_data.get("BondingOpts"),
            BridgeOpts=json_data.get("BridgeOpts"),
            Cnames=json_data.get("Cnames"),
            DhcpTag=json_data.get("DhcpTag"),
            DnsName=json_data.get("DnsName"),
            Gateway=json_data.get("Gateway"),
            InterfaceMaster=json_data.get("InterfaceMaster"),
            InterfaceType=json_data.get("InterfaceType"),
            IpAddress=json_data.get("IpAddress"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6DefaultGateway=json_data.get("Ipv6DefaultGateway"),
            Ipv6Mtu=json_data.get("Ipv6Mtu"),
            Ipv6Secondaries=json_data.get("Ipv6Secondaries"),
            Ipv6StaticRoutes=json_data.get("Ipv6StaticRoutes"),
            MacAddress=json_data.get("MacAddress"),
            Management=json_data.get("Management"),
            Name=json_data.get("Name"),
            Netmask=json_data.get("Netmask"),
            Static=json_data.get("Static"),
            StaticRoutes=json_data.get("StaticRoutes"),
            VirtBridge=json_data.get("VirtBridge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface = Interface


