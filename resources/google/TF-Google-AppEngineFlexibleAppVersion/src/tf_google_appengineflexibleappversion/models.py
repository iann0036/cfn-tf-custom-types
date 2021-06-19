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
    BetaSettings: Optional[Sequence["_BetaSettingsDefinition"]]
    DefaultExpiration: Optional[str]
    DeleteServiceOnDestroy: Optional[bool]
    EnvVariables: Optional[Sequence["_EnvVariablesDefinition"]]
    Id: Optional[str]
    InboundServices: Optional[Sequence[str]]
    InstanceClass: Optional[str]
    Name: Optional[str]
    NobuildFilesRegex: Optional[str]
    NoopOnDestroy: Optional[bool]
    Project: Optional[str]
    Runtime: Optional[str]
    RuntimeApiVersion: Optional[str]
    RuntimeChannel: Optional[str]
    RuntimeMainExecutablePath: Optional[str]
    Service: Optional[str]
    ServingStatus: Optional[str]
    VersionId: Optional[str]
    ApiConfig: Optional[Sequence["_ApiConfigDefinition"]]
    AutomaticScaling: Optional[Sequence["_AutomaticScalingDefinition"]]
    Deployment: Optional[Sequence["_DeploymentDefinition"]]
    EndpointsApiService: Optional[Sequence["_EndpointsApiServiceDefinition"]]
    Entrypoint: Optional[Sequence["_EntrypointDefinition"]]
    Handlers: Optional[Sequence["_HandlersDefinition"]]
    LivenessCheck: Optional[Sequence["_LivenessCheckDefinition"]]
    ManualScaling: Optional[Sequence["_ManualScalingDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    ReadinessCheck: Optional[Sequence["_ReadinessCheckDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VpcAccessConnector: Optional[Sequence["_VpcAccessConnectorDefinition"]]

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
            BetaSettings=deserialize_list(json_data.get("BetaSettings"), BetaSettingsDefinition),
            DefaultExpiration=json_data.get("DefaultExpiration"),
            DeleteServiceOnDestroy=json_data.get("DeleteServiceOnDestroy"),
            EnvVariables=deserialize_list(json_data.get("EnvVariables"), EnvVariablesDefinition),
            Id=json_data.get("Id"),
            InboundServices=json_data.get("InboundServices"),
            InstanceClass=json_data.get("InstanceClass"),
            Name=json_data.get("Name"),
            NobuildFilesRegex=json_data.get("NobuildFilesRegex"),
            NoopOnDestroy=json_data.get("NoopOnDestroy"),
            Project=json_data.get("Project"),
            Runtime=json_data.get("Runtime"),
            RuntimeApiVersion=json_data.get("RuntimeApiVersion"),
            RuntimeChannel=json_data.get("RuntimeChannel"),
            RuntimeMainExecutablePath=json_data.get("RuntimeMainExecutablePath"),
            Service=json_data.get("Service"),
            ServingStatus=json_data.get("ServingStatus"),
            VersionId=json_data.get("VersionId"),
            ApiConfig=deserialize_list(json_data.get("ApiConfig"), ApiConfigDefinition),
            AutomaticScaling=deserialize_list(json_data.get("AutomaticScaling"), AutomaticScalingDefinition),
            Deployment=deserialize_list(json_data.get("Deployment"), DeploymentDefinition),
            EndpointsApiService=deserialize_list(json_data.get("EndpointsApiService"), EndpointsApiServiceDefinition),
            Entrypoint=deserialize_list(json_data.get("Entrypoint"), EntrypointDefinition),
            Handlers=deserialize_list(json_data.get("Handlers"), HandlersDefinition),
            LivenessCheck=deserialize_list(json_data.get("LivenessCheck"), LivenessCheckDefinition),
            ManualScaling=deserialize_list(json_data.get("ManualScaling"), ManualScalingDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            ReadinessCheck=deserialize_list(json_data.get("ReadinessCheck"), ReadinessCheckDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VpcAccessConnector=deserialize_list(json_data.get("VpcAccessConnector"), VpcAccessConnectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BetaSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BetaSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BetaSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BetaSettingsDefinition = BetaSettingsDefinition


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
class ApiConfigDefinition(BaseModel):
    AuthFailAction: Optional[str]
    Login: Optional[str]
    Script: Optional[str]
    SecurityLevel: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthFailAction=json_data.get("AuthFailAction"),
            Login=json_data.get("Login"),
            Script=json_data.get("Script"),
            SecurityLevel=json_data.get("SecurityLevel"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiConfigDefinition = ApiConfigDefinition


@dataclass
class AutomaticScalingDefinition(BaseModel):
    CoolDownPeriod: Optional[str]
    MaxConcurrentRequests: Optional[float]
    MaxIdleInstances: Optional[float]
    MaxPendingLatency: Optional[str]
    MaxTotalInstances: Optional[float]
    MinIdleInstances: Optional[float]
    MinPendingLatency: Optional[str]
    MinTotalInstances: Optional[float]
    CpuUtilization: Optional[Sequence["_CpuUtilizationDefinition"]]
    DiskUtilization: Optional[Sequence["_DiskUtilizationDefinition"]]
    NetworkUtilization: Optional[Sequence["_NetworkUtilizationDefinition"]]
    RequestUtilization: Optional[Sequence["_RequestUtilizationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticScalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticScalingDefinition"]:
        if not json_data:
            return None
        return cls(
            CoolDownPeriod=json_data.get("CoolDownPeriod"),
            MaxConcurrentRequests=json_data.get("MaxConcurrentRequests"),
            MaxIdleInstances=json_data.get("MaxIdleInstances"),
            MaxPendingLatency=json_data.get("MaxPendingLatency"),
            MaxTotalInstances=json_data.get("MaxTotalInstances"),
            MinIdleInstances=json_data.get("MinIdleInstances"),
            MinPendingLatency=json_data.get("MinPendingLatency"),
            MinTotalInstances=json_data.get("MinTotalInstances"),
            CpuUtilization=deserialize_list(json_data.get("CpuUtilization"), CpuUtilizationDefinition),
            DiskUtilization=deserialize_list(json_data.get("DiskUtilization"), DiskUtilizationDefinition),
            NetworkUtilization=deserialize_list(json_data.get("NetworkUtilization"), NetworkUtilizationDefinition),
            RequestUtilization=deserialize_list(json_data.get("RequestUtilization"), RequestUtilizationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticScalingDefinition = AutomaticScalingDefinition


@dataclass
class CpuUtilizationDefinition(BaseModel):
    AggregationWindowLength: Optional[str]
    TargetUtilization: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuUtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuUtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregationWindowLength=json_data.get("AggregationWindowLength"),
            TargetUtilization=json_data.get("TargetUtilization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuUtilizationDefinition = CpuUtilizationDefinition


@dataclass
class DiskUtilizationDefinition(BaseModel):
    TargetReadBytesPerSecond: Optional[float]
    TargetReadOpsPerSecond: Optional[float]
    TargetWriteBytesPerSecond: Optional[float]
    TargetWriteOpsPerSecond: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DiskUtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskUtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetReadBytesPerSecond=json_data.get("TargetReadBytesPerSecond"),
            TargetReadOpsPerSecond=json_data.get("TargetReadOpsPerSecond"),
            TargetWriteBytesPerSecond=json_data.get("TargetWriteBytesPerSecond"),
            TargetWriteOpsPerSecond=json_data.get("TargetWriteOpsPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskUtilizationDefinition = DiskUtilizationDefinition


@dataclass
class NetworkUtilizationDefinition(BaseModel):
    TargetReceivedBytesPerSecond: Optional[float]
    TargetReceivedPacketsPerSecond: Optional[float]
    TargetSentBytesPerSecond: Optional[float]
    TargetSentPacketsPerSecond: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkUtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkUtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetReceivedBytesPerSecond=json_data.get("TargetReceivedBytesPerSecond"),
            TargetReceivedPacketsPerSecond=json_data.get("TargetReceivedPacketsPerSecond"),
            TargetSentBytesPerSecond=json_data.get("TargetSentBytesPerSecond"),
            TargetSentPacketsPerSecond=json_data.get("TargetSentPacketsPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkUtilizationDefinition = NetworkUtilizationDefinition


@dataclass
class RequestUtilizationDefinition(BaseModel):
    TargetConcurrentRequests: Optional[float]
    TargetRequestCountPerSecond: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestUtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestUtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetConcurrentRequests=json_data.get("TargetConcurrentRequests"),
            TargetRequestCountPerSecond=json_data.get("TargetRequestCountPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestUtilizationDefinition = RequestUtilizationDefinition


@dataclass
class DeploymentDefinition(BaseModel):
    CloudBuildOptions: Optional[Sequence["_CloudBuildOptionsDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Files: Optional[Sequence["_FilesDefinition"]]
    Zip: Optional[Sequence["_ZipDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudBuildOptions=deserialize_list(json_data.get("CloudBuildOptions"), CloudBuildOptionsDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Files=deserialize_list(json_data.get("Files"), FilesDefinition),
            Zip=deserialize_list(json_data.get("Zip"), ZipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentDefinition = DeploymentDefinition


@dataclass
class CloudBuildOptionsDefinition(BaseModel):
    AppYamlPath: Optional[str]
    CloudBuildTimeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudBuildOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudBuildOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AppYamlPath=json_data.get("AppYamlPath"),
            CloudBuildTimeout=json_data.get("CloudBuildTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudBuildOptionsDefinition = CloudBuildOptionsDefinition


@dataclass
class ContainerDefinition(BaseModel):
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class FilesDefinition(BaseModel):
    Name: Optional[str]
    Sha1Sum: Optional[str]
    SourceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Sha1Sum=json_data.get("Sha1Sum"),
            SourceUrl=json_data.get("SourceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilesDefinition = FilesDefinition


@dataclass
class ZipDefinition(BaseModel):
    FilesCount: Optional[float]
    SourceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZipDefinition"]:
        if not json_data:
            return None
        return cls(
            FilesCount=json_data.get("FilesCount"),
            SourceUrl=json_data.get("SourceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZipDefinition = ZipDefinition


@dataclass
class EndpointsApiServiceDefinition(BaseModel):
    ConfigId: Optional[str]
    DisableTraceSampling: Optional[bool]
    Name: Optional[str]
    RolloutStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsApiServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsApiServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigId=json_data.get("ConfigId"),
            DisableTraceSampling=json_data.get("DisableTraceSampling"),
            Name=json_data.get("Name"),
            RolloutStrategy=json_data.get("RolloutStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsApiServiceDefinition = EndpointsApiServiceDefinition


@dataclass
class EntrypointDefinition(BaseModel):
    Shell: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntrypointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntrypointDefinition"]:
        if not json_data:
            return None
        return cls(
            Shell=json_data.get("Shell"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntrypointDefinition = EntrypointDefinition


@dataclass
class HandlersDefinition(BaseModel):
    AuthFailAction: Optional[str]
    Login: Optional[str]
    RedirectHttpResponseCode: Optional[str]
    SecurityLevel: Optional[str]
    UrlRegex: Optional[str]
    Script: Optional[Sequence["_ScriptDefinition"]]
    StaticFiles: Optional[Sequence["_StaticFilesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HandlersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HandlersDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthFailAction=json_data.get("AuthFailAction"),
            Login=json_data.get("Login"),
            RedirectHttpResponseCode=json_data.get("RedirectHttpResponseCode"),
            SecurityLevel=json_data.get("SecurityLevel"),
            UrlRegex=json_data.get("UrlRegex"),
            Script=deserialize_list(json_data.get("Script"), ScriptDefinition),
            StaticFiles=deserialize_list(json_data.get("StaticFiles"), StaticFilesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HandlersDefinition = HandlersDefinition


@dataclass
class ScriptDefinition(BaseModel):
    ScriptPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptDefinition"]:
        if not json_data:
            return None
        return cls(
            ScriptPath=json_data.get("ScriptPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptDefinition = ScriptDefinition


@dataclass
class StaticFilesDefinition(BaseModel):
    ApplicationReadable: Optional[bool]
    Expiration: Optional[str]
    HttpHeaders: Optional[Sequence["_HttpHeadersDefinition"]]
    MimeType: Optional[str]
    Path: Optional[str]
    RequireMatchingFile: Optional[bool]
    UploadPathRegex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticFilesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticFilesDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationReadable=json_data.get("ApplicationReadable"),
            Expiration=json_data.get("Expiration"),
            HttpHeaders=deserialize_list(json_data.get("HttpHeaders"), HttpHeadersDefinition),
            MimeType=json_data.get("MimeType"),
            Path=json_data.get("Path"),
            RequireMatchingFile=json_data.get("RequireMatchingFile"),
            UploadPathRegex=json_data.get("UploadPathRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticFilesDefinition = StaticFilesDefinition


@dataclass
class HttpHeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeadersDefinition = HttpHeadersDefinition


@dataclass
class LivenessCheckDefinition(BaseModel):
    CheckInterval: Optional[str]
    FailureThreshold: Optional[float]
    Host: Optional[str]
    InitialDelay: Optional[str]
    Path: Optional[str]
    SuccessThreshold: Optional[float]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckInterval=json_data.get("CheckInterval"),
            FailureThreshold=json_data.get("FailureThreshold"),
            Host=json_data.get("Host"),
            InitialDelay=json_data.get("InitialDelay"),
            Path=json_data.get("Path"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessCheckDefinition = LivenessCheckDefinition


@dataclass
class ManualScalingDefinition(BaseModel):
    Instances: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManualScalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManualScalingDefinition"]:
        if not json_data:
            return None
        return cls(
            Instances=json_data.get("Instances"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManualScalingDefinition = ManualScalingDefinition


@dataclass
class NetworkDefinition(BaseModel):
    ForwardedPorts: Optional[Sequence[str]]
    InstanceTag: Optional[str]
    Name: Optional[str]
    SessionAffinity: Optional[bool]
    Subnetwork: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardedPorts=json_data.get("ForwardedPorts"),
            InstanceTag=json_data.get("InstanceTag"),
            Name=json_data.get("Name"),
            SessionAffinity=json_data.get("SessionAffinity"),
            Subnetwork=json_data.get("Subnetwork"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class ReadinessCheckDefinition(BaseModel):
    AppStartTimeout: Optional[str]
    CheckInterval: Optional[str]
    FailureThreshold: Optional[float]
    Host: Optional[str]
    Path: Optional[str]
    SuccessThreshold: Optional[float]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            AppStartTimeout=json_data.get("AppStartTimeout"),
            CheckInterval=json_data.get("CheckInterval"),
            FailureThreshold=json_data.get("FailureThreshold"),
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessCheckDefinition = ReadinessCheckDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Cpu: Optional[float]
    DiskGb: Optional[float]
    MemoryGb: Optional[float]
    Volumes: Optional[Sequence["_VolumesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            DiskGb=json_data.get("DiskGb"),
            MemoryGb=json_data.get("MemoryGb"),
            Volumes=deserialize_list(json_data.get("Volumes"), VolumesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class VolumesDefinition(BaseModel):
    Name: Optional[str]
    SizeGb: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SizeGb=json_data.get("SizeGb"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumesDefinition = VolumesDefinition


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


@dataclass
class VpcAccessConnectorDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcAccessConnectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcAccessConnectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcAccessConnectorDefinition = VpcAccessConnectorDefinition


