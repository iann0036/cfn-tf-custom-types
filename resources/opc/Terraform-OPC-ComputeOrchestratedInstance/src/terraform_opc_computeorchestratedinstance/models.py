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
    Description: Optional[str]
    DesiredState: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Version: Optional[float]
    Instance: Optional[Sequence["_Instance"]]
    Timeouts: Optional["_Timeouts"]
    NetworkingInfo: Optional[Sequence["_NetworkingInfo"]]
    Storage: Optional[Sequence["_Storage"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DesiredState=json_data.get("DesiredState"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            Instance=json_data.get("Instance"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            NetworkingInfo=json_data.get("NetworkingInfo"),
            Storage=json_data.get("Storage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Instance:
    BootOrder: Optional[Sequence[float]]
    Hostname: Optional[str]
    ImageList: Optional[str]
    InstanceAttributes: Optional[str]
    Label: Optional[str]
    Name: Optional[str]
    Persistent: Optional[bool]
    ReverseDns: Optional[bool]
    Shape: Optional[str]
    SshKeys: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    NetworkingInfo: Optional[Sequence["_NetworkingInfo"]]
    Storage: Optional[Sequence["_Storage"]]

    @classmethod
    def _deserialize(
        cls: Type["_Instance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Instance"]:
        if not json_data:
            return None
        return cls(
            BootOrder=json_data.get("BootOrder"),
            Hostname=json_data.get("Hostname"),
            ImageList=json_data.get("ImageList"),
            InstanceAttributes=json_data.get("InstanceAttributes"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            Persistent=json_data.get("Persistent"),
            ReverseDns=json_data.get("ReverseDns"),
            Shape=json_data.get("Shape"),
            SshKeys=json_data.get("SshKeys"),
            Tags=json_data.get("Tags"),
            NetworkingInfo=json_data.get("NetworkingInfo"),
            Storage=json_data.get("Storage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Instance = Instance


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


