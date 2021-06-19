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
    CreateTime: Optional[str]
    DagTimeout: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    UpdateTime: Optional[str]
    Version: Optional[float]
    Jobs: Optional[Sequence["_JobsDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    Placement: Optional[Sequence["_PlacementDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            DagTimeout=json_data.get("DagTimeout"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            UpdateTime=json_data.get("UpdateTime"),
            Version=json_data.get("Version"),
            Jobs=deserialize_list(json_data.get("Jobs"), JobsDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Placement=deserialize_list(json_data.get("Placement"), PlacementDefinition),
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
class JobsDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    PrerequisiteStepIds: Optional[Sequence[str]]
    StepId: Optional[str]
    HadoopJob: Optional[Sequence["_HadoopJobDefinition"]]
    HiveJob: Optional[Sequence["_HiveJobDefinition"]]
    PigJob: Optional[Sequence["_PigJobDefinition"]]
    PrestoJob: Optional[Sequence["_PrestoJobDefinition"]]
    PysparkJob: Optional[Sequence["_PysparkJobDefinition"]]
    Scheduling: Optional[Sequence["_SchedulingDefinition"]]
    SparkJob: Optional[Sequence["_SparkJobDefinition"]]
    SparkRJob: Optional[Sequence["_SparkRJobDefinition"]]
    SparkSqlJob: Optional[Sequence["_SparkSqlJobDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_JobsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobsDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            PrerequisiteStepIds=json_data.get("PrerequisiteStepIds"),
            StepId=json_data.get("StepId"),
            HadoopJob=deserialize_list(json_data.get("HadoopJob"), HadoopJobDefinition),
            HiveJob=deserialize_list(json_data.get("HiveJob"), HiveJobDefinition),
            PigJob=deserialize_list(json_data.get("PigJob"), PigJobDefinition),
            PrestoJob=deserialize_list(json_data.get("PrestoJob"), PrestoJobDefinition),
            PysparkJob=deserialize_list(json_data.get("PysparkJob"), PysparkJobDefinition),
            Scheduling=deserialize_list(json_data.get("Scheduling"), SchedulingDefinition),
            SparkJob=deserialize_list(json_data.get("SparkJob"), SparkJobDefinition),
            SparkRJob=deserialize_list(json_data.get("SparkRJob"), SparkRJobDefinition),
            SparkSqlJob=deserialize_list(json_data.get("SparkSqlJob"), SparkSqlJobDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobsDefinition = JobsDefinition


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
class HadoopJobDefinition(BaseModel):
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainClass: Optional[str]
    MainJarFileUri: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HadoopJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HadoopJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainClass=json_data.get("MainClass"),
            MainJarFileUri=json_data.get("MainJarFileUri"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HadoopJobDefinition = HadoopJobDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class LoggingConfigDefinition(BaseModel):
    DriverLogLevels: Optional[Sequence["_DriverLogLevelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DriverLogLevels=deserialize_list(json_data.get("DriverLogLevels"), DriverLogLevelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfigDefinition = LoggingConfigDefinition


@dataclass
class DriverLogLevelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriverLogLevelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriverLogLevelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriverLogLevelsDefinition = DriverLogLevelsDefinition


@dataclass
class HiveJobDefinition(BaseModel):
    ContinueOnFailure: Optional[bool]
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_PropertiesDefinition2"]]
    QueryFileUri: Optional[str]
    ScriptVariables: Optional[Sequence["_ScriptVariablesDefinition"]]
    QueryList: Optional[Sequence["_QueryListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            JarFileUris=json_data.get("JarFileUris"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition2),
            QueryFileUri=json_data.get("QueryFileUri"),
            ScriptVariables=deserialize_list(json_data.get("ScriptVariables"), ScriptVariablesDefinition),
            QueryList=deserialize_list(json_data.get("QueryList"), QueryListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveJobDefinition = HiveJobDefinition


@dataclass
class PropertiesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition2 = PropertiesDefinition2


@dataclass
class ScriptVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptVariablesDefinition = ScriptVariablesDefinition


@dataclass
class QueryListDefinition(BaseModel):
    Queries: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryListDefinition"]:
        if not json_data:
            return None
        return cls(
            Queries=json_data.get("Queries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryListDefinition = QueryListDefinition


@dataclass
class PigJobDefinition(BaseModel):
    ContinueOnFailure: Optional[bool]
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_PropertiesDefinition3"]]
    QueryFileUri: Optional[str]
    ScriptVariables: Optional[Sequence["_ScriptVariablesDefinition2"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]
    QueryList: Optional[Sequence["_QueryListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PigJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PigJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            JarFileUris=json_data.get("JarFileUris"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition3),
            QueryFileUri=json_data.get("QueryFileUri"),
            ScriptVariables=deserialize_list(json_data.get("ScriptVariables"), ScriptVariablesDefinition2),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
            QueryList=deserialize_list(json_data.get("QueryList"), QueryListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PigJobDefinition = PigJobDefinition


@dataclass
class PropertiesDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition3 = PropertiesDefinition3


@dataclass
class ScriptVariablesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptVariablesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptVariablesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptVariablesDefinition2 = ScriptVariablesDefinition2


@dataclass
class PrestoJobDefinition(BaseModel):
    ClientTags: Optional[Sequence[str]]
    ContinueOnFailure: Optional[bool]
    OutputFormat: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition4"]]
    QueryFileUri: Optional[str]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]
    QueryList: Optional[Sequence["_QueryListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrestoJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrestoJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientTags=json_data.get("ClientTags"),
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            OutputFormat=json_data.get("OutputFormat"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition4),
            QueryFileUri=json_data.get("QueryFileUri"),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
            QueryList=deserialize_list(json_data.get("QueryList"), QueryListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrestoJobDefinition = PrestoJobDefinition


@dataclass
class PropertiesDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition4 = PropertiesDefinition4


@dataclass
class PysparkJobDefinition(BaseModel):
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainPythonFileUri: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition5"]]
    PythonFileUris: Optional[Sequence[str]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PysparkJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PysparkJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainPythonFileUri=json_data.get("MainPythonFileUri"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition5),
            PythonFileUris=json_data.get("PythonFileUris"),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PysparkJobDefinition = PysparkJobDefinition


@dataclass
class PropertiesDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition5 = PropertiesDefinition5


@dataclass
class SchedulingDefinition(BaseModel):
    MaxFailuresPerHour: Optional[float]
    MaxFailuresTotal: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulingDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxFailuresPerHour=json_data.get("MaxFailuresPerHour"),
            MaxFailuresTotal=json_data.get("MaxFailuresTotal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulingDefinition = SchedulingDefinition


@dataclass
class SparkJobDefinition(BaseModel):
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainClass: Optional[str]
    MainJarFileUri: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition6"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparkJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainClass=json_data.get("MainClass"),
            MainJarFileUri=json_data.get("MainJarFileUri"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition6),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkJobDefinition = SparkJobDefinition


@dataclass
class PropertiesDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition6 = PropertiesDefinition6


@dataclass
class SparkRJobDefinition(BaseModel):
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    MainRFileUri: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition7"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparkRJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkRJobDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            MainRFileUri=json_data.get("MainRFileUri"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition7),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkRJobDefinition = SparkRJobDefinition


@dataclass
class PropertiesDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition7 = PropertiesDefinition7


@dataclass
class SparkSqlJobDefinition(BaseModel):
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_PropertiesDefinition8"]]
    QueryFileUri: Optional[str]
    ScriptVariables: Optional[Sequence["_ScriptVariablesDefinition3"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]
    QueryList: Optional[Sequence["_QueryListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparkSqlJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkSqlJobDefinition"]:
        if not json_data:
            return None
        return cls(
            JarFileUris=json_data.get("JarFileUris"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition8),
            QueryFileUri=json_data.get("QueryFileUri"),
            ScriptVariables=deserialize_list(json_data.get("ScriptVariables"), ScriptVariablesDefinition3),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
            QueryList=deserialize_list(json_data.get("QueryList"), QueryListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkSqlJobDefinition = SparkSqlJobDefinition


@dataclass
class PropertiesDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition8 = PropertiesDefinition8


@dataclass
class ScriptVariablesDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptVariablesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptVariablesDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptVariablesDefinition3 = ScriptVariablesDefinition3


@dataclass
class ParametersDefinition(BaseModel):
    Description: Optional[str]
    Fields: Optional[Sequence[str]]
    Name: Optional[str]
    Validation: Optional[Sequence["_ValidationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Fields=json_data.get("Fields"),
            Name=json_data.get("Name"),
            Validation=deserialize_list(json_data.get("Validation"), ValidationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class ValidationDefinition(BaseModel):
    Regex: Optional[Sequence["_RegexDefinition"]]
    Values: Optional[Sequence["_ValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationDefinition"]:
        if not json_data:
            return None
        return cls(
            Regex=deserialize_list(json_data.get("Regex"), RegexDefinition),
            Values=deserialize_list(json_data.get("Values"), ValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationDefinition = ValidationDefinition


@dataclass
class RegexDefinition(BaseModel):
    Regexes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RegexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexDefinition"]:
        if not json_data:
            return None
        return cls(
            Regexes=json_data.get("Regexes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexDefinition = RegexDefinition


@dataclass
class ValuesDefinition(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesDefinition = ValuesDefinition


@dataclass
class PlacementDefinition(BaseModel):
    ClusterSelector: Optional[Sequence["_ClusterSelectorDefinition"]]
    ManagedCluster: Optional[Sequence["_ManagedClusterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterSelector=deserialize_list(json_data.get("ClusterSelector"), ClusterSelectorDefinition),
            ManagedCluster=deserialize_list(json_data.get("ManagedCluster"), ManagedClusterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementDefinition = PlacementDefinition


@dataclass
class ClusterSelectorDefinition(BaseModel):
    ClusterLabels: Optional[Sequence["_ClusterLabelsDefinition"]]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterLabels=deserialize_list(json_data.get("ClusterLabels"), ClusterLabelsDefinition),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterSelectorDefinition = ClusterSelectorDefinition


@dataclass
class ClusterLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterLabelsDefinition = ClusterLabelsDefinition


@dataclass
class ManagedClusterDefinition(BaseModel):
    ClusterName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition3"]]
    Config: Optional[Sequence["_ConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterName=json_data.get("ClusterName"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition3),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedClusterDefinition = ManagedClusterDefinition


@dataclass
class LabelsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition3 = LabelsDefinition3


@dataclass
class ConfigDefinition(BaseModel):
    StagingBucket: Optional[str]
    TempBucket: Optional[str]
    AutoscalingConfig: Optional[Sequence["_AutoscalingConfigDefinition"]]
    EncryptionConfig: Optional[Sequence["_EncryptionConfigDefinition"]]
    EndpointConfig: Optional[Sequence["_EndpointConfigDefinition"]]
    GceClusterConfig: Optional[Sequence["_GceClusterConfigDefinition"]]
    GkeClusterConfig: Optional[Sequence["_GkeClusterConfigDefinition"]]
    InitializationActions: Optional[Sequence["_InitializationActionsDefinition"]]
    LifecycleConfig: Optional[Sequence["_LifecycleConfigDefinition"]]
    MasterConfig: Optional[Sequence["_MasterConfigDefinition"]]
    MetastoreConfig: Optional[Sequence["_MetastoreConfigDefinition"]]
    SecondaryWorkerConfig: Optional[Sequence["_SecondaryWorkerConfigDefinition"]]
    SecurityConfig: Optional[Sequence["_SecurityConfigDefinition"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfigDefinition"]]
    WorkerConfig: Optional[Sequence["_WorkerConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            StagingBucket=json_data.get("StagingBucket"),
            TempBucket=json_data.get("TempBucket"),
            AutoscalingConfig=deserialize_list(json_data.get("AutoscalingConfig"), AutoscalingConfigDefinition),
            EncryptionConfig=deserialize_list(json_data.get("EncryptionConfig"), EncryptionConfigDefinition),
            EndpointConfig=deserialize_list(json_data.get("EndpointConfig"), EndpointConfigDefinition),
            GceClusterConfig=deserialize_list(json_data.get("GceClusterConfig"), GceClusterConfigDefinition),
            GkeClusterConfig=deserialize_list(json_data.get("GkeClusterConfig"), GkeClusterConfigDefinition),
            InitializationActions=deserialize_list(json_data.get("InitializationActions"), InitializationActionsDefinition),
            LifecycleConfig=deserialize_list(json_data.get("LifecycleConfig"), LifecycleConfigDefinition),
            MasterConfig=deserialize_list(json_data.get("MasterConfig"), MasterConfigDefinition),
            MetastoreConfig=deserialize_list(json_data.get("MetastoreConfig"), MetastoreConfigDefinition),
            SecondaryWorkerConfig=deserialize_list(json_data.get("SecondaryWorkerConfig"), SecondaryWorkerConfigDefinition),
            SecurityConfig=deserialize_list(json_data.get("SecurityConfig"), SecurityConfigDefinition),
            SoftwareConfig=deserialize_list(json_data.get("SoftwareConfig"), SoftwareConfigDefinition),
            WorkerConfig=deserialize_list(json_data.get("WorkerConfig"), WorkerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class AutoscalingConfigDefinition(BaseModel):
    Policy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Policy=json_data.get("Policy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingConfigDefinition = AutoscalingConfigDefinition


@dataclass
class EncryptionConfigDefinition(BaseModel):
    GcePdKmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            GcePdKmsKeyName=json_data.get("GcePdKmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigDefinition = EncryptionConfigDefinition


@dataclass
class EndpointConfigDefinition(BaseModel):
    EnableHttpPortAccess: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableHttpPortAccess=json_data.get("EnableHttpPortAccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigDefinition = EndpointConfigDefinition


@dataclass
class GceClusterConfigDefinition(BaseModel):
    InternalIpOnly: Optional[bool]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Network: Optional[str]
    PrivateIpv6GoogleAccess: Optional[str]
    ServiceAccount: Optional[str]
    ServiceAccountScopes: Optional[Sequence[str]]
    Subnetwork: Optional[str]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]
    NodeGroupAffinity: Optional[Sequence["_NodeGroupAffinityDefinition"]]
    ReservationAffinity: Optional[Sequence["_ReservationAffinityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GceClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GceClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            InternalIpOnly=json_data.get("InternalIpOnly"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Network=json_data.get("Network"),
            PrivateIpv6GoogleAccess=json_data.get("PrivateIpv6GoogleAccess"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceAccountScopes=json_data.get("ServiceAccountScopes"),
            Subnetwork=json_data.get("Subnetwork"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
            NodeGroupAffinity=deserialize_list(json_data.get("NodeGroupAffinity"), NodeGroupAffinityDefinition),
            ReservationAffinity=deserialize_list(json_data.get("ReservationAffinity"), ReservationAffinityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GceClusterConfigDefinition = GceClusterConfigDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class NodeGroupAffinityDefinition(BaseModel):
    NodeGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeGroupAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeGroupAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeGroup=json_data.get("NodeGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeGroupAffinityDefinition = NodeGroupAffinityDefinition


@dataclass
class ReservationAffinityDefinition(BaseModel):
    ConsumeReservationType: Optional[str]
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ReservationAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReservationAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsumeReservationType=json_data.get("ConsumeReservationType"),
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReservationAffinityDefinition = ReservationAffinityDefinition


@dataclass
class GkeClusterConfigDefinition(BaseModel):
    NamespacedGkeDeploymentTarget: Optional[Sequence["_NamespacedGkeDeploymentTargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GkeClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GkeClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NamespacedGkeDeploymentTarget=deserialize_list(json_data.get("NamespacedGkeDeploymentTarget"), NamespacedGkeDeploymentTargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GkeClusterConfigDefinition = GkeClusterConfigDefinition


@dataclass
class NamespacedGkeDeploymentTargetDefinition(BaseModel):
    ClusterNamespace: Optional[str]
    TargetGkeCluster: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NamespacedGkeDeploymentTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespacedGkeDeploymentTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterNamespace=json_data.get("ClusterNamespace"),
            TargetGkeCluster=json_data.get("TargetGkeCluster"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespacedGkeDeploymentTargetDefinition = NamespacedGkeDeploymentTargetDefinition


@dataclass
class InitializationActionsDefinition(BaseModel):
    ExecutableFile: Optional[str]
    ExecutionTimeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitializationActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializationActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExecutableFile=json_data.get("ExecutableFile"),
            ExecutionTimeout=json_data.get("ExecutionTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializationActionsDefinition = InitializationActionsDefinition


@dataclass
class LifecycleConfigDefinition(BaseModel):
    AutoDeleteTime: Optional[str]
    AutoDeleteTtl: Optional[str]
    IdleDeleteTtl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoDeleteTime=json_data.get("AutoDeleteTime"),
            AutoDeleteTtl=json_data.get("AutoDeleteTtl"),
            IdleDeleteTtl=json_data.get("IdleDeleteTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleConfigDefinition = LifecycleConfigDefinition


@dataclass
class MasterConfigDefinition(BaseModel):
    Image: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Preemptibility: Optional[str]
    Accelerators: Optional[Sequence["_AcceleratorsDefinition"]]
    DiskConfig: Optional[Sequence["_DiskConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Preemptibility=json_data.get("Preemptibility"),
            Accelerators=deserialize_list(json_data.get("Accelerators"), AcceleratorsDefinition),
            DiskConfig=deserialize_list(json_data.get("DiskConfig"), DiskConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterConfigDefinition = MasterConfigDefinition


@dataclass
class AcceleratorsDefinition(BaseModel):
    AcceleratorCount: Optional[float]
    AcceleratorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceleratorCount=json_data.get("AcceleratorCount"),
            AcceleratorType=json_data.get("AcceleratorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorsDefinition = AcceleratorsDefinition


@dataclass
class DiskConfigDefinition(BaseModel):
    BootDiskSizeGb: Optional[float]
    BootDiskType: Optional[str]
    NumLocalSsds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DiskConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BootDiskSizeGb=json_data.get("BootDiskSizeGb"),
            BootDiskType=json_data.get("BootDiskType"),
            NumLocalSsds=json_data.get("NumLocalSsds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskConfigDefinition = DiskConfigDefinition


@dataclass
class MetastoreConfigDefinition(BaseModel):
    DataprocMetastoreService: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetastoreConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetastoreConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DataprocMetastoreService=json_data.get("DataprocMetastoreService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetastoreConfigDefinition = MetastoreConfigDefinition


@dataclass
class SecondaryWorkerConfigDefinition(BaseModel):
    Image: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Preemptibility: Optional[str]
    Accelerators: Optional[Sequence["_AcceleratorsDefinition"]]
    DiskConfig: Optional[Sequence["_DiskConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryWorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryWorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Preemptibility=json_data.get("Preemptibility"),
            Accelerators=deserialize_list(json_data.get("Accelerators"), AcceleratorsDefinition),
            DiskConfig=deserialize_list(json_data.get("DiskConfig"), DiskConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryWorkerConfigDefinition = SecondaryWorkerConfigDefinition


@dataclass
class SecurityConfigDefinition(BaseModel):
    KerberosConfig: Optional[Sequence["_KerberosConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            KerberosConfig=deserialize_list(json_data.get("KerberosConfig"), KerberosConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityConfigDefinition = SecurityConfigDefinition


@dataclass
class KerberosConfigDefinition(BaseModel):
    CrossRealmTrustAdminServer: Optional[str]
    CrossRealmTrustKdc: Optional[str]
    CrossRealmTrustRealm: Optional[str]
    CrossRealmTrustSharedPassword: Optional[str]
    EnableKerberos: Optional[bool]
    KdcDbKey: Optional[str]
    KeyPassword: Optional[str]
    Keystore: Optional[str]
    KeystorePassword: Optional[str]
    KmsKey: Optional[str]
    Realm: Optional[str]
    RootPrincipalPassword: Optional[str]
    TgtLifetimeHours: Optional[float]
    Truststore: Optional[str]
    TruststorePassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CrossRealmTrustAdminServer=json_data.get("CrossRealmTrustAdminServer"),
            CrossRealmTrustKdc=json_data.get("CrossRealmTrustKdc"),
            CrossRealmTrustRealm=json_data.get("CrossRealmTrustRealm"),
            CrossRealmTrustSharedPassword=json_data.get("CrossRealmTrustSharedPassword"),
            EnableKerberos=json_data.get("EnableKerberos"),
            KdcDbKey=json_data.get("KdcDbKey"),
            KeyPassword=json_data.get("KeyPassword"),
            Keystore=json_data.get("Keystore"),
            KeystorePassword=json_data.get("KeystorePassword"),
            KmsKey=json_data.get("KmsKey"),
            Realm=json_data.get("Realm"),
            RootPrincipalPassword=json_data.get("RootPrincipalPassword"),
            TgtLifetimeHours=json_data.get("TgtLifetimeHours"),
            Truststore=json_data.get("Truststore"),
            TruststorePassword=json_data.get("TruststorePassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KerberosConfigDefinition = KerberosConfigDefinition


@dataclass
class SoftwareConfigDefinition(BaseModel):
    ImageVersion: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition9"]]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageVersion=json_data.get("ImageVersion"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition9),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareConfigDefinition = SoftwareConfigDefinition


@dataclass
class PropertiesDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition9 = PropertiesDefinition9


@dataclass
class WorkerConfigDefinition(BaseModel):
    Image: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Preemptibility: Optional[str]
    Accelerators: Optional[Sequence["_AcceleratorsDefinition"]]
    DiskConfig: Optional[Sequence["_DiskConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Preemptibility=json_data.get("Preemptibility"),
            Accelerators=deserialize_list(json_data.get("Accelerators"), AcceleratorsDefinition),
            DiskConfig=deserialize_list(json_data.get("DiskConfig"), DiskConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigDefinition = WorkerConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


