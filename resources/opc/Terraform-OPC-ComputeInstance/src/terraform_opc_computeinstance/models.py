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
    Attributes: Optional[str]
    AvailabilityDomain: Optional[str]
    BootOrder: Optional[Sequence[float]]
    DesiredState: Optional[str]
    Domain: Optional[str]
    Entry: Optional[float]
    Fingerprint: Optional[str]
    Fqdn: Optional[str]
    Hostname: Optional[str]
    ImageFormat: Optional[str]
    ImageList: Optional[str]
    InstanceAttributes: Optional[str]
    IpAddress: Optional[str]
    Label: Optional[str]
    Name: Optional[str]
    PlacementRequirements: Optional[Sequence[str]]
    Platform: Optional[str]
    Priority: Optional[str]
    QuotaReservation: Optional[str]
    Relationships: Optional[Sequence[str]]
    Resolvers: Optional[Sequence[str]]
    ReverseDns: Optional[bool]
    Shape: Optional[str]
    Site: Optional[str]
    SshKeys: Optional[Sequence[str]]
    StartTime: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence[str]]
    Vcable: Optional[str]
    Virtio: Optional[bool]
    VncAddress: Optional[str]
    NetworkingInfo: Optional[Sequence["_NetworkingInfo"]]
    Storage: Optional[Sequence["_Storage"]]
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
            Attributes=json_data.get("Attributes"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BootOrder=json_data.get("BootOrder"),
            DesiredState=json_data.get("DesiredState"),
            Domain=json_data.get("Domain"),
            Entry=json_data.get("Entry"),
            Fingerprint=json_data.get("Fingerprint"),
            Fqdn=json_data.get("Fqdn"),
            Hostname=json_data.get("Hostname"),
            ImageFormat=json_data.get("ImageFormat"),
            ImageList=json_data.get("ImageList"),
            InstanceAttributes=json_data.get("InstanceAttributes"),
            IpAddress=json_data.get("IpAddress"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            PlacementRequirements=json_data.get("PlacementRequirements"),
            Platform=json_data.get("Platform"),
            Priority=json_data.get("Priority"),
            QuotaReservation=json_data.get("QuotaReservation"),
            Relationships=json_data.get("Relationships"),
            Resolvers=json_data.get("Resolvers"),
            ReverseDns=json_data.get("ReverseDns"),
            Shape=json_data.get("Shape"),
            Site=json_data.get("Site"),
            SshKeys=json_data.get("SshKeys"),
            StartTime=json_data.get("StartTime"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Vcable=json_data.get("Vcable"),
            Virtio=json_data.get("Virtio"),
            VncAddress=json_data.get("VncAddress"),
            NetworkingInfo=json_data.get("NetworkingInfo"),
            Storage=json_data.get("Storage"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkingInfo:
    Dns: Optional[Sequence[str]]
    Index: Optional[float]
    IpAddress: Optional[str]
    IpNetwork: Optional[str]
    IsDefaultGateway: Optional[bool]
    MacAddress: Optional[str]
    NameServers: Optional[Sequence[str]]
    Nat: Optional[Sequence[str]]
    SearchDomains: Optional[Sequence[str]]
    SecLists: Optional[Sequence[str]]
    SharedNetwork: Optional[bool]
    Vnic: Optional[str]
    VnicSets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkingInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkingInfo"]:
        if not json_data:
            return None
        return cls(
            Dns=json_data.get("Dns"),
            Index=json_data.get("Index"),
            IpAddress=json_data.get("IpAddress"),
            IpNetwork=json_data.get("IpNetwork"),
            IsDefaultGateway=json_data.get("IsDefaultGateway"),
            MacAddress=json_data.get("MacAddress"),
            NameServers=json_data.get("NameServers"),
            Nat=json_data.get("Nat"),
            SearchDomains=json_data.get("SearchDomains"),
            SecLists=json_data.get("SecLists"),
            SharedNetwork=json_data.get("SharedNetwork"),
            Vnic=json_data.get("Vnic"),
            VnicSets=json_data.get("VnicSets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkingInfo = NetworkingInfo


@dataclass
class Storage:
    Index: Optional[float]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Storage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Storage"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Storage = Storage


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


