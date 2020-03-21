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
    Created: Optional[str]
    Datastore: Optional[Sequence["_Datastore"]]
    EnableHttps: Optional[bool]
    Endpoint: Optional[str]
    ExpectNodeNum: Optional[float]
    Name: Optional[str]
    Nodes: Optional[Sequence["_Nodes"]]
    Updated: Optional[str]
    NodeConfig: Optional[Sequence["_NodeConfig"]]
    Timeouts: Optional["_Timeouts"]
    NetworkInfo: Optional[Sequence["_NetworkInfo"]]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Created=json_data.get("Created"),
            Datastore=json_data.get("Datastore"),
            EnableHttps=json_data.get("EnableHttps"),
            Endpoint=json_data.get("Endpoint"),
            ExpectNodeNum=json_data.get("ExpectNodeNum"),
            Name=json_data.get("Name"),
            Nodes=json_data.get("Nodes"),
            Updated=json_data.get("Updated"),
            NodeConfig=json_data.get("NodeConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            NetworkInfo=json_data.get("NetworkInfo"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Datastore:
    Type: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Datastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Datastore"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Datastore = Datastore


@dataclass
class Nodes:
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


@dataclass
class NodeConfig:
    AvailabilityZone: Optional[str]
    Flavor: Optional[str]
    NetworkInfo: Optional[Sequence["_NetworkInfo"]]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Flavor=json_data.get("Flavor"),
            NetworkInfo=json_data.get("NetworkInfo"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfig = NodeConfig


@dataclass
class NetworkInfo:
    NetworkId: Optional[str]
    SecurityGroupId: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInfo"]:
        if not json_data:
            return None
        return cls(
            NetworkId=json_data.get("NetworkId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInfo = NetworkInfo


@dataclass
class Volume:
    EncryptionKey: Optional[str]
    Size: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            EncryptionKey=json_data.get("EncryptionKey"),
            Size=json_data.get("Size"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class Timeouts:
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


