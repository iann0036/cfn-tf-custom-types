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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Slug: Optional[str]
    Container: Optional[Sequence["_ContainerDefinition"]]
    ImagePullCredentials: Optional[Sequence["_ImagePullCredentialsDefinition"]]
    Instances: Optional[Sequence["_InstancesDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    Target: Optional[Sequence["_TargetDefinition"]]
    VirtualMachine: Optional[Sequence["_VirtualMachineDefinition"]]
    VolumeClaim: Optional[Sequence["_VolumeClaimDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Slug=json_data.get("Slug"),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            ImagePullCredentials=deserialize_list(json_data.get("ImagePullCredentials"), ImagePullCredentialsDefinition),
            Instances=deserialize_list(json_data.get("Instances"), InstancesDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
            VirtualMachine=deserialize_list(json_data.get("VirtualMachine"), VirtualMachineDefinition),
            VolumeClaim=deserialize_list(json_data.get("VolumeClaim"), VolumeClaimDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


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
class ContainerDefinition(BaseModel):
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    Name: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    LivenessProbe: Optional[Sequence["_LivenessProbeDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbeDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]
    VolumeMount: Optional[Sequence["_VolumeMountDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            Image=json_data.get("Image"),
            Name=json_data.get("Name"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            LivenessProbe=deserialize_list(json_data.get("LivenessProbe"), LivenessProbeDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            ReadinessProbe=deserialize_list(json_data.get("ReadinessProbe"), ReadinessProbeDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
            VolumeMount=deserialize_list(json_data.get("VolumeMount"), VolumeMountDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class EnvDefinition(BaseModel):
    Key: Optional[str]
    SecretValue: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            SecretValue=json_data.get("SecretValue"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvDefinition = EnvDefinition


@dataclass
class LivenessProbeDefinition(BaseModel):
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessProbeDefinition = LivenessProbeDefinition


@dataclass
class HttpGetDefinition(BaseModel):
    HttpHeaders: Optional[Sequence["_HttpHeadersDefinition2"]]
    Path: Optional[str]
    Port: Optional[float]
    Scheme: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGetDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpHeaders=deserialize_list(json_data.get("HttpHeaders"), HttpHeadersDefinition2),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Scheme=json_data.get("Scheme"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGetDefinition = HttpGetDefinition


@dataclass
class HttpHeadersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeadersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeadersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeadersDefinition2 = HttpHeadersDefinition2


@dataclass
class TcpSocketDefinition(BaseModel):
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TcpSocketDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpSocketDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpSocketDefinition = TcpSocketDefinition


@dataclass
class PortDefinition(BaseModel):
    EnableImplicitNetworkPolicy: Optional[bool]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableImplicitNetworkPolicy=json_data.get("EnableImplicitNetworkPolicy"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


@dataclass
class ReadinessProbeDefinition(BaseModel):
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessProbeDefinition = ReadinessProbeDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Requests: Optional[Sequence["_RequestsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Requests=deserialize_list(json_data.get("Requests"), RequestsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class RequestsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestsDefinition2 = RequestsDefinition2


@dataclass
class VolumeMountDefinition(BaseModel):
    MountPath: Optional[str]
    Slug: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeMountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeMountDefinition"]:
        if not json_data:
            return None
        return cls(
            MountPath=json_data.get("MountPath"),
            Slug=json_data.get("Slug"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeMountDefinition = VolumeMountDefinition


@dataclass
class ImagePullCredentialsDefinition(BaseModel):
    DockerRegistry: Optional[Sequence["_DockerRegistryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImagePullCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImagePullCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            DockerRegistry=deserialize_list(json_data.get("DockerRegistry"), DockerRegistryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImagePullCredentialsDefinition = ImagePullCredentialsDefinition


@dataclass
class DockerRegistryDefinition(BaseModel):
    Email: Optional[str]
    Password: Optional[str]
    Server: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DockerRegistryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerRegistryDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerRegistryDefinition = DockerRegistryDefinition


@dataclass
class InstancesDefinition(BaseModel):
    ExternalIpAddress: Optional[str]
    IpAddress: Optional[str]
    Message: Optional[str]
    Name: Optional[str]
    Phase: Optional[str]
    Reason: Optional[str]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Location: Optional[Sequence["_LocationDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    VirtualMachine: Optional[Sequence["_VirtualMachineDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalIpAddress=json_data.get("ExternalIpAddress"),
            IpAddress=json_data.get("IpAddress"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            Phase=json_data.get("Phase"),
            Reason=json_data.get("Reason"),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            VirtualMachine=deserialize_list(json_data.get("VirtualMachine"), VirtualMachineDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesDefinition = InstancesDefinition


@dataclass
class LocationDefinition(BaseModel):
    City: Optional[str]
    CityCode: Optional[str]
    Continent: Optional[str]
    ContinentCode: Optional[str]
    Country: Optional[str]
    CountryCode: Optional[str]
    Latitude: Optional[float]
    Longitude: Optional[float]
    Name: Optional[str]
    Region: Optional[str]
    RegionCode: Optional[str]
    Subdivision: Optional[str]
    SubdivisionCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationDefinition"]:
        if not json_data:
            return None
        return cls(
            City=json_data.get("City"),
            CityCode=json_data.get("CityCode"),
            Continent=json_data.get("Continent"),
            ContinentCode=json_data.get("ContinentCode"),
            Country=json_data.get("Country"),
            CountryCode=json_data.get("CountryCode"),
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RegionCode=json_data.get("RegionCode"),
            Subdivision=json_data.get("Subdivision"),
            SubdivisionCode=json_data.get("SubdivisionCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationDefinition = LocationDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition2"]]
    Labels: Optional[Sequence["_LabelsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition2),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AnnotationsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition2 = AnnotationsDefinition2


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    Gateway: Optional[str]
    IpAddress: Optional[str]
    IpAddressAliases: Optional[Sequence[str]]
    Network: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Gateway=json_data.get("Gateway"),
            IpAddress=json_data.get("IpAddress"),
            IpAddressAliases=json_data.get("IpAddressAliases"),
            Network=json_data.get("Network"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class VirtualMachineDefinition(BaseModel):
    Image: Optional[str]
    Name: Optional[str]
    UserData: Optional[str]
    LivenessProbe: Optional[Sequence["_LivenessProbeDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbeDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]
    VolumeMount: Optional[Sequence["_VolumeMountDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualMachineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualMachineDefinition"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
            Name=json_data.get("Name"),
            UserData=json_data.get("UserData"),
            LivenessProbe=deserialize_list(json_data.get("LivenessProbe"), LivenessProbeDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            ReadinessProbe=deserialize_list(json_data.get("ReadinessProbe"), ReadinessProbeDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
            VolumeMount=deserialize_list(json_data.get("VolumeMount"), VolumeMountDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualMachineDefinition = VirtualMachineDefinition


@dataclass
class TargetDefinition(BaseModel):
    DeploymentScope: Optional[str]
    MaxReplicas: Optional[float]
    MinReplicas: Optional[float]
    Name: Optional[str]
    ScaleSettings: Optional[Sequence["_ScaleSettingsDefinition"]]
    Selector: Optional[Sequence["_SelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            DeploymentScope=json_data.get("DeploymentScope"),
            MaxReplicas=json_data.get("MaxReplicas"),
            MinReplicas=json_data.get("MinReplicas"),
            Name=json_data.get("Name"),
            ScaleSettings=deserialize_list(json_data.get("ScaleSettings"), ScaleSettingsDefinition),
            Selector=deserialize_list(json_data.get("Selector"), SelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


@dataclass
class ScaleSettingsDefinition(BaseModel):
    Metrics: Optional[Sequence["_MetricsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Metrics=deserialize_list(json_data.get("Metrics"), MetricsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleSettingsDefinition = ScaleSettingsDefinition


@dataclass
class MetricsDefinition(BaseModel):
    AverageUtilization: Optional[float]
    AverageValue: Optional[str]
    Metric: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsDefinition"]:
        if not json_data:
            return None
        return cls(
            AverageUtilization=json_data.get("AverageUtilization"),
            AverageValue=json_data.get("AverageValue"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsDefinition = MetricsDefinition


@dataclass
class SelectorDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectorDefinition = SelectorDefinition


@dataclass
class VolumeClaimDefinition(BaseModel):
    Name: Optional[str]
    Slug: Optional[str]
    Resources: Optional[Sequence["_ResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeClaimDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeClaimDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Slug=json_data.get("Slug"),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeClaimDefinition = VolumeClaimDefinition


