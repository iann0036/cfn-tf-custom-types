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
    AvailabilityZone: Optional[str]
    CloudRef: Optional[str]
    ContainerMode: Optional[bool]
    ContainerType: Optional[str]
    ControllerCreated: Optional[bool]
    ControllerIp: Optional[str]
    EnableState: Optional[str]
    Flavor: Optional[str]
    HostRef: Optional[str]
    Hypervisor: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SeGroupRef: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    DataVnics: Optional[Sequence["_DataVnicsDefinition"]]
    MgmtVnic: Optional[Sequence["_MgmtVnicDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CloudRef=json_data.get("CloudRef"),
            ContainerMode=json_data.get("ContainerMode"),
            ContainerType=json_data.get("ContainerType"),
            ControllerCreated=json_data.get("ControllerCreated"),
            ControllerIp=json_data.get("ControllerIp"),
            EnableState=json_data.get("EnableState"),
            Flavor=json_data.get("Flavor"),
            HostRef=json_data.get("HostRef"),
            Hypervisor=json_data.get("Hypervisor"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SeGroupRef=json_data.get("SeGroupRef"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            DataVnics=deserialize_list(json_data.get("DataVnics"), DataVnicsDefinition),
            MgmtVnic=deserialize_list(json_data.get("MgmtVnic"), MgmtVnicDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DataVnicsDefinition(BaseModel):
    Adapter: Optional[str]
    AggregatorChgd: Optional[bool]
    CanSeDpTakeover: Optional[bool]
    Connected: Optional[bool]
    DelPending: Optional[bool]
    DeleteVnic: Optional[bool]
    DhcpEnabled: Optional[bool]
    DpDeletionDone: Optional[bool]
    Enabled: Optional[bool]
    IfName: Optional[str]
    Ip6AutocfgEnabled: Optional[bool]
    IsAsm: Optional[bool]
    IsAviInternalNetwork: Optional[bool]
    IsHsm: Optional[bool]
    IsMgmt: Optional[bool]
    IsPortchannel: Optional[bool]
    LinkUp: Optional[bool]
    LinuxName: Optional[str]
    MacAddress: Optional[str]
    Mtu: Optional[float]
    NetworkName: Optional[str]
    NetworkRef: Optional[str]
    PciId: Optional[str]
    PortUuid: Optional[str]
    VlanId: Optional[float]
    VrfId: Optional[float]
    VrfRef: Optional[str]
    Members: Optional[Sequence["_MembersDefinition"]]
    VlanInterfaces: Optional[Sequence["_VlanInterfacesDefinition"]]
    VnicNetworks: Optional[Sequence["_VnicNetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataVnicsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataVnicsDefinition"]:
        if not json_data:
            return None
        return cls(
            Adapter=json_data.get("Adapter"),
            AggregatorChgd=json_data.get("AggregatorChgd"),
            CanSeDpTakeover=json_data.get("CanSeDpTakeover"),
            Connected=json_data.get("Connected"),
            DelPending=json_data.get("DelPending"),
            DeleteVnic=json_data.get("DeleteVnic"),
            DhcpEnabled=json_data.get("DhcpEnabled"),
            DpDeletionDone=json_data.get("DpDeletionDone"),
            Enabled=json_data.get("Enabled"),
            IfName=json_data.get("IfName"),
            Ip6AutocfgEnabled=json_data.get("Ip6AutocfgEnabled"),
            IsAsm=json_data.get("IsAsm"),
            IsAviInternalNetwork=json_data.get("IsAviInternalNetwork"),
            IsHsm=json_data.get("IsHsm"),
            IsMgmt=json_data.get("IsMgmt"),
            IsPortchannel=json_data.get("IsPortchannel"),
            LinkUp=json_data.get("LinkUp"),
            LinuxName=json_data.get("LinuxName"),
            MacAddress=json_data.get("MacAddress"),
            Mtu=json_data.get("Mtu"),
            NetworkName=json_data.get("NetworkName"),
            NetworkRef=json_data.get("NetworkRef"),
            PciId=json_data.get("PciId"),
            PortUuid=json_data.get("PortUuid"),
            VlanId=json_data.get("VlanId"),
            VrfId=json_data.get("VrfId"),
            VrfRef=json_data.get("VrfRef"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            VlanInterfaces=deserialize_list(json_data.get("VlanInterfaces"), VlanInterfacesDefinition),
            VnicNetworks=deserialize_list(json_data.get("VnicNetworks"), VnicNetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataVnicsDefinition = DataVnicsDefinition


@dataclass
class MembersDefinition(BaseModel):
    Active: Optional[bool]
    IfName: Optional[str]
    MacAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            IfName=json_data.get("IfName"),
            MacAddress=json_data.get("MacAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class VlanInterfacesDefinition(BaseModel):
    DhcpEnabled: Optional[bool]
    Enabled: Optional[bool]
    IfName: Optional[str]
    Ip6AutocfgEnabled: Optional[bool]
    IsMgmt: Optional[bool]
    VlanId: Optional[float]
    VrfRef: Optional[str]
    VnicNetworks: Optional[Sequence["_VnicNetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VlanInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VlanInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            DhcpEnabled=json_data.get("DhcpEnabled"),
            Enabled=json_data.get("Enabled"),
            IfName=json_data.get("IfName"),
            Ip6AutocfgEnabled=json_data.get("Ip6AutocfgEnabled"),
            IsMgmt=json_data.get("IsMgmt"),
            VlanId=json_data.get("VlanId"),
            VrfRef=json_data.get("VrfRef"),
            VnicNetworks=deserialize_list(json_data.get("VnicNetworks"), VnicNetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VlanInterfacesDefinition = VlanInterfacesDefinition


@dataclass
class VnicNetworksDefinition(BaseModel):
    CtlrAlloc: Optional[bool]
    Mode: Optional[str]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VnicNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VnicNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            CtlrAlloc=json_data.get("CtlrAlloc"),
            Mode=json_data.get("Mode"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VnicNetworksDefinition = VnicNetworksDefinition


@dataclass
class IpDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class MgmtVnicDefinition(BaseModel):
    Adapter: Optional[str]
    AggregatorChgd: Optional[bool]
    CanSeDpTakeover: Optional[bool]
    Connected: Optional[bool]
    DelPending: Optional[bool]
    DeleteVnic: Optional[bool]
    DhcpEnabled: Optional[bool]
    DpDeletionDone: Optional[bool]
    Enabled: Optional[bool]
    IfName: Optional[str]
    Ip6AutocfgEnabled: Optional[bool]
    IsAsm: Optional[bool]
    IsAviInternalNetwork: Optional[bool]
    IsHsm: Optional[bool]
    IsMgmt: Optional[bool]
    IsPortchannel: Optional[bool]
    LinkUp: Optional[bool]
    LinuxName: Optional[str]
    MacAddress: Optional[str]
    Mtu: Optional[float]
    NetworkName: Optional[str]
    NetworkRef: Optional[str]
    PciId: Optional[str]
    PortUuid: Optional[str]
    VlanId: Optional[float]
    VrfId: Optional[float]
    VrfRef: Optional[str]
    Members: Optional[Sequence["_MembersDefinition"]]
    VlanInterfaces: Optional[Sequence["_VlanInterfacesDefinition"]]
    VnicNetworks: Optional[Sequence["_VnicNetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MgmtVnicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MgmtVnicDefinition"]:
        if not json_data:
            return None
        return cls(
            Adapter=json_data.get("Adapter"),
            AggregatorChgd=json_data.get("AggregatorChgd"),
            CanSeDpTakeover=json_data.get("CanSeDpTakeover"),
            Connected=json_data.get("Connected"),
            DelPending=json_data.get("DelPending"),
            DeleteVnic=json_data.get("DeleteVnic"),
            DhcpEnabled=json_data.get("DhcpEnabled"),
            DpDeletionDone=json_data.get("DpDeletionDone"),
            Enabled=json_data.get("Enabled"),
            IfName=json_data.get("IfName"),
            Ip6AutocfgEnabled=json_data.get("Ip6AutocfgEnabled"),
            IsAsm=json_data.get("IsAsm"),
            IsAviInternalNetwork=json_data.get("IsAviInternalNetwork"),
            IsHsm=json_data.get("IsHsm"),
            IsMgmt=json_data.get("IsMgmt"),
            IsPortchannel=json_data.get("IsPortchannel"),
            LinkUp=json_data.get("LinkUp"),
            LinuxName=json_data.get("LinuxName"),
            MacAddress=json_data.get("MacAddress"),
            Mtu=json_data.get("Mtu"),
            NetworkName=json_data.get("NetworkName"),
            NetworkRef=json_data.get("NetworkRef"),
            PciId=json_data.get("PciId"),
            PortUuid=json_data.get("PortUuid"),
            VlanId=json_data.get("VlanId"),
            VrfId=json_data.get("VrfId"),
            VrfRef=json_data.get("VrfRef"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            VlanInterfaces=deserialize_list(json_data.get("VlanInterfaces"), VlanInterfacesDefinition),
            VnicNetworks=deserialize_list(json_data.get("VnicNetworks"), VnicNetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MgmtVnicDefinition = MgmtVnicDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    CoresPerSocket: Optional[float]
    Disk: Optional[float]
    HyperThreading: Optional[bool]
    HypervisorMode: Optional[bool]
    Memory: Optional[float]
    NumDatapathProcesses: Optional[float]
    NumVcpus: Optional[float]
    Sockets: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            CoresPerSocket=json_data.get("CoresPerSocket"),
            Disk=json_data.get("Disk"),
            HyperThreading=json_data.get("HyperThreading"),
            HypervisorMode=json_data.get("HypervisorMode"),
            Memory=json_data.get("Memory"),
            NumDatapathProcesses=json_data.get("NumDatapathProcesses"),
            NumVcpus=json_data.get("NumVcpus"),
            Sockets=json_data.get("Sockets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


