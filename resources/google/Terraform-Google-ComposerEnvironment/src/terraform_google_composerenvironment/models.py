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
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Config: Optional[Sequence["_Config"]]
    Timeouts: Optional["_Timeouts"]
    NodeConfig: Optional[Sequence["_NodeConfig"]]
    PrivateEnvironmentConfig: Optional[Sequence["_PrivateEnvironmentConfig"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Config=json_data.get("Config"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            NodeConfig=json_data.get("NodeConfig"),
            PrivateEnvironmentConfig=json_data.get("PrivateEnvironmentConfig"),
            SoftwareConfig=json_data.get("SoftwareConfig"),
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
class Config:
    NodeCount: Optional[float]
    NodeConfig: Optional[Sequence["_NodeConfig"]]
    PrivateEnvironmentConfig: Optional[Sequence["_PrivateEnvironmentConfig"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            NodeCount=json_data.get("NodeCount"),
            NodeConfig=json_data.get("NodeConfig"),
            PrivateEnvironmentConfig=json_data.get("PrivateEnvironmentConfig"),
            SoftwareConfig=json_data.get("SoftwareConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class NodeConfig:
    DiskSizeGb: Optional[float]
    IpAllocationPolicy: Optional[Sequence["_IpAllocationPolicy"]]
    MachineType: Optional[str]
    Network: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    ServiceAccount: Optional[str]
    Subnetwork: Optional[str]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfig"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            IpAllocationPolicy=json_data.get("IpAllocationPolicy"),
            MachineType=json_data.get("MachineType"),
            Network=json_data.get("Network"),
            OauthScopes=json_data.get("OauthScopes"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Subnetwork=json_data.get("Subnetwork"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfig = NodeConfig


@dataclass
class IpAllocationPolicy:
    ClusterIpv4CidrBlock: Optional[str]
    ClusterSecondaryRangeName: Optional[str]
    ServicesIpv4CidrBlock: Optional[str]
    ServicesSecondaryRangeName: Optional[str]
    UseIpAliases: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IpAllocationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAllocationPolicy"]:
        if not json_data:
            return None
        return cls(
            ClusterIpv4CidrBlock=json_data.get("ClusterIpv4CidrBlock"),
            ClusterSecondaryRangeName=json_data.get("ClusterSecondaryRangeName"),
            ServicesIpv4CidrBlock=json_data.get("ServicesIpv4CidrBlock"),
            ServicesSecondaryRangeName=json_data.get("ServicesSecondaryRangeName"),
            UseIpAliases=json_data.get("UseIpAliases"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAllocationPolicy = IpAllocationPolicy


@dataclass
class PrivateEnvironmentConfig:
    EnablePrivateEndpoint: Optional[bool]
    MasterIpv4CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateEnvironmentConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateEnvironmentConfig"]:
        if not json_data:
            return None
        return cls(
            EnablePrivateEndpoint=json_data.get("EnablePrivateEndpoint"),
            MasterIpv4CidrBlock=json_data.get("MasterIpv4CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateEnvironmentConfig = PrivateEnvironmentConfig


@dataclass
class SoftwareConfig:
    AirflowConfigOverrides: Optional[Sequence["_AirflowConfigOverrides"]]
    EnvVariables: Optional[Sequence["_EnvVariables"]]
    ImageVersion: Optional[str]
    PypiPackages: Optional[Sequence["_PypiPackages"]]
    PythonVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareConfig"]:
        if not json_data:
            return None
        return cls(
            AirflowConfigOverrides=json_data.get("AirflowConfigOverrides"),
            EnvVariables=json_data.get("EnvVariables"),
            ImageVersion=json_data.get("ImageVersion"),
            PypiPackages=json_data.get("PypiPackages"),
            PythonVersion=json_data.get("PythonVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareConfig = SoftwareConfig


@dataclass
class AirflowConfigOverrides:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AirflowConfigOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AirflowConfigOverrides"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AirflowConfigOverrides = AirflowConfigOverrides


@dataclass
class EnvVariables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvVariables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvVariables = EnvVariables


@dataclass
class PypiPackages:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PypiPackages"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PypiPackages"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PypiPackages = PypiPackages


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


