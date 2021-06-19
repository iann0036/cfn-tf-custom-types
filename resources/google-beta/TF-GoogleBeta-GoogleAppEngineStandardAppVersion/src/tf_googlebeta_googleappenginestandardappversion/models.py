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
    DeleteServiceOnDestroy: Optional[bool]
    EnvVariables: Optional[Sequence["_EnvVariablesDefinition"]]
    Id: Optional[str]
    InboundServices: Optional[Sequence[str]]
    InstanceClass: Optional[str]
    Name: Optional[str]
    NoopOnDestroy: Optional[bool]
    Project: Optional[str]
    Runtime: Optional[str]
    RuntimeApiVersion: Optional[str]
    Service: Optional[str]
    Threadsafe: Optional[bool]
    VersionId: Optional[str]
    AutomaticScaling: Optional[Sequence["_AutomaticScalingDefinition"]]
    BasicScaling: Optional[Sequence["_BasicScalingDefinition"]]
    Deployment: Optional[Sequence["_DeploymentDefinition"]]
    Entrypoint: Optional[Sequence["_EntrypointDefinition"]]
    Handlers: Optional[Sequence["_HandlersDefinition"]]
    Libraries: Optional[Sequence["_LibrariesDefinition"]]
    ManualScaling: Optional[Sequence["_ManualScalingDefinition"]]
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
            DeleteServiceOnDestroy=json_data.get("DeleteServiceOnDestroy"),
            EnvVariables=deserialize_list(json_data.get("EnvVariables"), EnvVariablesDefinition),
            Id=json_data.get("Id"),
            InboundServices=json_data.get("InboundServices"),
            InstanceClass=json_data.get("InstanceClass"),
            Name=json_data.get("Name"),
            NoopOnDestroy=json_data.get("NoopOnDestroy"),
            Project=json_data.get("Project"),
            Runtime=json_data.get("Runtime"),
            RuntimeApiVersion=json_data.get("RuntimeApiVersion"),
            Service=json_data.get("Service"),
            Threadsafe=json_data.get("Threadsafe"),
            VersionId=json_data.get("VersionId"),
            AutomaticScaling=deserialize_list(json_data.get("AutomaticScaling"), AutomaticScalingDefinition),
            BasicScaling=deserialize_list(json_data.get("BasicScaling"), BasicScalingDefinition),
            Deployment=deserialize_list(json_data.get("Deployment"), DeploymentDefinition),
            Entrypoint=deserialize_list(json_data.get("Entrypoint"), EntrypointDefinition),
            Handlers=deserialize_list(json_data.get("Handlers"), HandlersDefinition),
            Libraries=deserialize_list(json_data.get("Libraries"), LibrariesDefinition),
            ManualScaling=deserialize_list(json_data.get("ManualScaling"), ManualScalingDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VpcAccessConnector=deserialize_list(json_data.get("VpcAccessConnector"), VpcAccessConnectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AutomaticScalingDefinition(BaseModel):
    MaxConcurrentRequests: Optional[float]
    MaxIdleInstances: Optional[float]
    MaxPendingLatency: Optional[str]
    MinIdleInstances: Optional[float]
    MinPendingLatency: Optional[str]
    StandardSchedulerSettings: Optional[Sequence["_StandardSchedulerSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticScalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticScalingDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentRequests=json_data.get("MaxConcurrentRequests"),
            MaxIdleInstances=json_data.get("MaxIdleInstances"),
            MaxPendingLatency=json_data.get("MaxPendingLatency"),
            MinIdleInstances=json_data.get("MinIdleInstances"),
            MinPendingLatency=json_data.get("MinPendingLatency"),
            StandardSchedulerSettings=deserialize_list(json_data.get("StandardSchedulerSettings"), StandardSchedulerSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticScalingDefinition = AutomaticScalingDefinition


@dataclass
class StandardSchedulerSettingsDefinition(BaseModel):
    MaxInstances: Optional[float]
    MinInstances: Optional[float]
    TargetCpuUtilization: Optional[float]
    TargetThroughputUtilization: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StandardSchedulerSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StandardSchedulerSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxInstances=json_data.get("MaxInstances"),
            MinInstances=json_data.get("MinInstances"),
            TargetCpuUtilization=json_data.get("TargetCpuUtilization"),
            TargetThroughputUtilization=json_data.get("TargetThroughputUtilization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StandardSchedulerSettingsDefinition = StandardSchedulerSettingsDefinition


@dataclass
class BasicScalingDefinition(BaseModel):
    IdleTimeout: Optional[str]
    MaxInstances: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BasicScalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicScalingDefinition"]:
        if not json_data:
            return None
        return cls(
            IdleTimeout=json_data.get("IdleTimeout"),
            MaxInstances=json_data.get("MaxInstances"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicScalingDefinition = BasicScalingDefinition


@dataclass
class DeploymentDefinition(BaseModel):
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
            Files=deserialize_list(json_data.get("Files"), FilesDefinition),
            Zip=deserialize_list(json_data.get("Zip"), ZipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentDefinition = DeploymentDefinition


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
class LibrariesDefinition(BaseModel):
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LibrariesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LibrariesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LibrariesDefinition = LibrariesDefinition


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


