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
    DriverControlsFilesUri: Optional[str]
    DriverOutputResourceUri: Optional[str]
    ForceDelete: Optional[bool]
    Labels: Optional[Sequence["_Labels"]]
    Project: Optional[str]
    Region: Optional[str]
    Status: Optional[Sequence["_Status"]]
    HadoopConfig: Optional[Sequence["_HadoopConfig"]]
    HiveConfig: Optional[Sequence["_HiveConfig"]]
    PigConfig: Optional[Sequence["_PigConfig"]]
    Placement: Optional[Sequence["_Placement"]]
    PysparkConfig: Optional[Sequence["_PysparkConfig"]]
    Reference: Optional[Sequence["_Reference"]]
    Scheduling: Optional[Sequence["_Scheduling"]]
    SparkConfig: Optional[Sequence["_SparkConfig"]]
    SparksqlConfig: Optional[Sequence["_SparksqlConfig"]]
    Timeouts: Optional["_Timeouts"]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DriverControlsFilesUri=json_data.get("DriverControlsFilesUri"),
            DriverOutputResourceUri=json_data.get("DriverOutputResourceUri"),
            ForceDelete=json_data.get("ForceDelete"),
            Labels=json_data.get("Labels"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            HadoopConfig=json_data.get("HadoopConfig"),
            HiveConfig=json_data.get("HiveConfig"),
            PigConfig=json_data.get("PigConfig"),
            Placement=json_data.get("Placement"),
            PysparkConfig=json_data.get("PysparkConfig"),
            Reference=json_data.get("Reference"),
            Scheduling=json_data.get("Scheduling"),
            SparkConfig=json_data.get("SparkConfig"),
            SparksqlConfig=json_data.get("SparksqlConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            LoggingConfig=json_data.get("LoggingConfig"),
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
class Status:
    Details: Optional[str]
    State: Optional[str]
    StateStartTime: Optional[str]
    Substate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Status"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Status"]:
        if not json_data:
            return None
        return cls(
            Details=json_data.get("Details"),
            State=json_data.get("State"),
            StateStartTime=json_data.get("StateStartTime"),
            Substate=json_data.get("Substate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Status = Status


@dataclass
class HadoopConfig:
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainClass: Optional[str]
    MainJarFileUri: Optional[str]
    Properties: Optional[Sequence["_Properties"]]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_HadoopConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HadoopConfig"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainClass=json_data.get("MainClass"),
            MainJarFileUri=json_data.get("MainJarFileUri"),
            Properties=json_data.get("Properties"),
            LoggingConfig=json_data.get("LoggingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HadoopConfig = HadoopConfig


@dataclass
class Properties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


@dataclass
class LoggingConfig:
    DriverLogLevels: Optional[Sequence["_DriverLogLevels"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfig"]:
        if not json_data:
            return None
        return cls(
            DriverLogLevels=json_data.get("DriverLogLevels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfig = LoggingConfig


@dataclass
class DriverLogLevels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriverLogLevels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriverLogLevels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriverLogLevels = DriverLogLevels


@dataclass
class HiveConfig:
    ContinueOnFailure: Optional[bool]
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_Properties2"]]
    QueryFileUri: Optional[str]
    QueryList: Optional[Sequence[str]]
    ScriptVariables: Optional[Sequence["_ScriptVariables"]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveConfig"]:
        if not json_data:
            return None
        return cls(
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            JarFileUris=json_data.get("JarFileUris"),
            Properties=json_data.get("Properties"),
            QueryFileUri=json_data.get("QueryFileUri"),
            QueryList=json_data.get("QueryList"),
            ScriptVariables=json_data.get("ScriptVariables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveConfig = HiveConfig


@dataclass
class Properties2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties2 = Properties2


@dataclass
class ScriptVariables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptVariables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptVariables = ScriptVariables


@dataclass
class PigConfig:
    ContinueOnFailure: Optional[bool]
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_Properties3"]]
    QueryFileUri: Optional[str]
    QueryList: Optional[Sequence[str]]
    ScriptVariables: Optional[Sequence["_ScriptVariables2"]]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_PigConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PigConfig"]:
        if not json_data:
            return None
        return cls(
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            JarFileUris=json_data.get("JarFileUris"),
            Properties=json_data.get("Properties"),
            QueryFileUri=json_data.get("QueryFileUri"),
            QueryList=json_data.get("QueryList"),
            ScriptVariables=json_data.get("ScriptVariables"),
            LoggingConfig=json_data.get("LoggingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PigConfig = PigConfig


@dataclass
class Properties3:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties3"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties3 = Properties3


@dataclass
class ScriptVariables2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptVariables2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptVariables2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptVariables2 = ScriptVariables2


@dataclass
class Placement:
    ClusterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Placement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Placement"]:
        if not json_data:
            return None
        return cls(
            ClusterName=json_data.get("ClusterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Placement = Placement


@dataclass
class PysparkConfig:
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainPythonFileUri: Optional[str]
    Properties: Optional[Sequence["_Properties4"]]
    PythonFileUris: Optional[Sequence[str]]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_PysparkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PysparkConfig"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainPythonFileUri=json_data.get("MainPythonFileUri"),
            Properties=json_data.get("Properties"),
            PythonFileUris=json_data.get("PythonFileUris"),
            LoggingConfig=json_data.get("LoggingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PysparkConfig = PysparkConfig


@dataclass
class Properties4:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties4"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties4 = Properties4


@dataclass
class Reference:
    JobId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Reference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Reference"]:
        if not json_data:
            return None
        return cls(
            JobId=json_data.get("JobId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Reference = Reference


@dataclass
class Scheduling:
    MaxFailuresPerHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Scheduling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scheduling"]:
        if not json_data:
            return None
        return cls(
            MaxFailuresPerHour=json_data.get("MaxFailuresPerHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scheduling = Scheduling


@dataclass
class SparkConfig:
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainClass: Optional[str]
    MainJarFileUri: Optional[str]
    Properties: Optional[Sequence["_Properties5"]]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkConfig"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainClass=json_data.get("MainClass"),
            MainJarFileUri=json_data.get("MainJarFileUri"),
            Properties=json_data.get("Properties"),
            LoggingConfig=json_data.get("LoggingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkConfig = SparkConfig


@dataclass
class Properties5:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties5"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties5 = Properties5


@dataclass
class SparksqlConfig:
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_Properties6"]]
    QueryFileUri: Optional[str]
    QueryList: Optional[Sequence[str]]
    ScriptVariables: Optional[Sequence["_ScriptVariables3"]]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparksqlConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparksqlConfig"]:
        if not json_data:
            return None
        return cls(
            JarFileUris=json_data.get("JarFileUris"),
            Properties=json_data.get("Properties"),
            QueryFileUri=json_data.get("QueryFileUri"),
            QueryList=json_data.get("QueryList"),
            ScriptVariables=json_data.get("ScriptVariables"),
            LoggingConfig=json_data.get("LoggingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparksqlConfig = SparksqlConfig


@dataclass
class Properties6:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties6"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties6 = Properties6


@dataclass
class ScriptVariables3:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptVariables3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptVariables3"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptVariables3 = ScriptVariables3


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


