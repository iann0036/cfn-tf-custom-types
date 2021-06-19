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
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ConfigDefinition(BaseModel):
    NodeCount: Optional[float]
    NodeConfig: Optional[Sequence["_NodeConfigDefinition"]]
    PrivateEnvironmentConfig: Optional[Sequence["_PrivateEnvironmentConfigDefinition"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeCount=json_data.get("NodeCount"),
            NodeConfig=deserialize_list(json_data.get("NodeConfig"), NodeConfigDefinition),
            PrivateEnvironmentConfig=deserialize_list(json_data.get("PrivateEnvironmentConfig"), PrivateEnvironmentConfigDefinition),
            SoftwareConfig=deserialize_list(json_data.get("SoftwareConfig"), SoftwareConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class NodeConfigDefinition(BaseModel):
    DiskSizeGb: Optional[float]
    IpAllocationPolicy: Optional[Sequence["_IpAllocationPolicyDefinition"]]
    MachineType: Optional[str]
    Network: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    ServiceAccount: Optional[str]
    Subnetwork: Optional[str]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            IpAllocationPolicy=deserialize_list(json_data.get("IpAllocationPolicy"), IpAllocationPolicyDefinition),
            MachineType=json_data.get("MachineType"),
            Network=json_data.get("Network"),
            OauthScopes=json_data.get("OauthScopes"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Subnetwork=json_data.get("Subnetwork"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDefinition = NodeConfigDefinition


@dataclass
class IpAllocationPolicyDefinition(BaseModel):
    ClusterIpv4CidrBlock: Optional[str]
    ClusterSecondaryRangeName: Optional[str]
    ServicesIpv4CidrBlock: Optional[str]
    ServicesSecondaryRangeName: Optional[str]
    UseIpAliases: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IpAllocationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAllocationPolicyDefinition"]:
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
_IpAllocationPolicyDefinition = IpAllocationPolicyDefinition


@dataclass
class PrivateEnvironmentConfigDefinition(BaseModel):
    CloudSqlIpv4CidrBlock: Optional[str]
    EnablePrivateEndpoint: Optional[bool]
    MasterIpv4CidrBlock: Optional[str]
    WebServerIpv4CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateEnvironmentConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateEnvironmentConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudSqlIpv4CidrBlock=json_data.get("CloudSqlIpv4CidrBlock"),
            EnablePrivateEndpoint=json_data.get("EnablePrivateEndpoint"),
            MasterIpv4CidrBlock=json_data.get("MasterIpv4CidrBlock"),
            WebServerIpv4CidrBlock=json_data.get("WebServerIpv4CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateEnvironmentConfigDefinition = PrivateEnvironmentConfigDefinition


@dataclass
class SoftwareConfigDefinition(BaseModel):
    AirflowConfigOverrides: Optional[Sequence["_AirflowConfigOverridesDefinition"]]
    EnvVariables: Optional[Sequence["_EnvVariablesDefinition"]]
    ImageVersion: Optional[str]
    PypiPackages: Optional[Sequence["_PypiPackagesDefinition"]]
    PythonVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AirflowConfigOverrides=deserialize_list(json_data.get("AirflowConfigOverrides"), AirflowConfigOverridesDefinition),
            EnvVariables=deserialize_list(json_data.get("EnvVariables"), EnvVariablesDefinition),
            ImageVersion=json_data.get("ImageVersion"),
            PypiPackages=deserialize_list(json_data.get("PypiPackages"), PypiPackagesDefinition),
            PythonVersion=json_data.get("PythonVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareConfigDefinition = SoftwareConfigDefinition


@dataclass
class AirflowConfigOverridesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AirflowConfigOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AirflowConfigOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AirflowConfigOverridesDefinition = AirflowConfigOverridesDefinition


@dataclass
class EnvVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvVariablesDefinition = EnvVariablesDefinition


@dataclass
class PypiPackagesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PypiPackagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PypiPackagesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PypiPackagesDefinition = PypiPackagesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


