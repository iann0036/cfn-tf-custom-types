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
    ApiserverPort: Optional[float]
    ClusterDistro: Optional[str]
    Coe: Optional[str]
    CreatedAt: Optional[str]
    DnsNameserver: Optional[str]
    DockerStorageDriver: Optional[str]
    DockerVolumeSize: Optional[float]
    ExternalNetworkId: Optional[str]
    FixedNetwork: Optional[str]
    FixedSubnet: Optional[str]
    Flavor: Optional[str]
    FloatingIpEnabled: Optional[bool]
    HttpProxy: Optional[str]
    HttpsProxy: Optional[str]
    Image: Optional[str]
    InsecureRegistry: Optional[str]
    KeypairId: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MasterFlavor: Optional[str]
    MasterLbEnabled: Optional[bool]
    Name: Optional[str]
    NetworkDriver: Optional[str]
    NoProxy: Optional[str]
    ProjectId: Optional[str]
    Public: Optional[bool]
    Region: Optional[str]
    RegistryEnabled: Optional[bool]
    ServerType: Optional[str]
    TlsDisabled: Optional[bool]
    UpdatedAt: Optional[str]
    UserId: Optional[str]
    VolumeDriver: Optional[str]
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
            ApiserverPort=json_data.get("ApiserverPort"),
            ClusterDistro=json_data.get("ClusterDistro"),
            Coe=json_data.get("Coe"),
            CreatedAt=json_data.get("CreatedAt"),
            DnsNameserver=json_data.get("DnsNameserver"),
            DockerStorageDriver=json_data.get("DockerStorageDriver"),
            DockerVolumeSize=json_data.get("DockerVolumeSize"),
            ExternalNetworkId=json_data.get("ExternalNetworkId"),
            FixedNetwork=json_data.get("FixedNetwork"),
            FixedSubnet=json_data.get("FixedSubnet"),
            Flavor=json_data.get("Flavor"),
            FloatingIpEnabled=json_data.get("FloatingIpEnabled"),
            HttpProxy=json_data.get("HttpProxy"),
            HttpsProxy=json_data.get("HttpsProxy"),
            Image=json_data.get("Image"),
            InsecureRegistry=json_data.get("InsecureRegistry"),
            KeypairId=json_data.get("KeypairId"),
            Labels=json_data.get("Labels"),
            MasterFlavor=json_data.get("MasterFlavor"),
            MasterLbEnabled=json_data.get("MasterLbEnabled"),
            Name=json_data.get("Name"),
            NetworkDriver=json_data.get("NetworkDriver"),
            NoProxy=json_data.get("NoProxy"),
            ProjectId=json_data.get("ProjectId"),
            Public=json_data.get("Public"),
            Region=json_data.get("Region"),
            RegistryEnabled=json_data.get("RegistryEnabled"),
            ServerType=json_data.get("ServerType"),
            TlsDisabled=json_data.get("TlsDisabled"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UserId=json_data.get("UserId"),
            VolumeDriver=json_data.get("VolumeDriver"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


