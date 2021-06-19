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
    DriverControlsFilesUri: Optional[str]
    DriverOutputResourceUri: Optional[str]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Project: Optional[str]
    Region: Optional[str]
    Status: Optional[Sequence["_StatusDefinition"]]
    HadoopConfig: Optional[Sequence["_HadoopConfigDefinition"]]
    HiveConfig: Optional[Sequence["_HiveConfigDefinition"]]
    PigConfig: Optional[Sequence["_PigConfigDefinition"]]
    Placement: Optional[Sequence["_PlacementDefinition"]]
    PysparkConfig: Optional[Sequence["_PysparkConfigDefinition"]]
    Reference: Optional[Sequence["_ReferenceDefinition"]]
    Scheduling: Optional[Sequence["_SchedulingDefinition"]]
    SparkConfig: Optional[Sequence["_SparkConfigDefinition"]]
    SparksqlConfig: Optional[Sequence["_SparksqlConfigDefinition"]]
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
            DriverControlsFilesUri=json_data.get("DriverControlsFilesUri"),
            DriverOutputResourceUri=json_data.get("DriverOutputResourceUri"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Status=deserialize_list(json_data.get("Status"), StatusDefinition),
            HadoopConfig=deserialize_list(json_data.get("HadoopConfig"), HadoopConfigDefinition),
            HiveConfig=deserialize_list(json_data.get("HiveConfig"), HiveConfigDefinition),
            PigConfig=deserialize_list(json_data.get("PigConfig"), PigConfigDefinition),
            Placement=deserialize_list(json_data.get("Placement"), PlacementDefinition),
            PysparkConfig=deserialize_list(json_data.get("PysparkConfig"), PysparkConfigDefinition),
            Reference=deserialize_list(json_data.get("Reference"), ReferenceDefinition),
            Scheduling=deserialize_list(json_data.get("Scheduling"), SchedulingDefinition),
            SparkConfig=deserialize_list(json_data.get("SparkConfig"), SparkConfigDefinition),
            SparksqlConfig=deserialize_list(json_data.get("SparksqlConfig"), SparksqlConfigDefinition),
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
class StatusDefinition(BaseModel):
    Details: Optional[str]
    State: Optional[str]
    StateStartTime: Optional[str]
    Substate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Details=json_data.get("Details"),
            State=json_data.get("State"),
            StateStartTime=json_data.get("StateStartTime"),
            Substate=json_data.get("Substate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


@dataclass
class HadoopConfigDefinition(BaseModel):
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
        cls: Type["_HadoopConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HadoopConfigDefinition"]:
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
_HadoopConfigDefinition = HadoopConfigDefinition


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
class HiveConfigDefinition(BaseModel):
    ContinueOnFailure: Optional[bool]
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_PropertiesDefinition2"]]
    QueryFileUri: Optional[str]
    QueryList: Optional[Sequence[str]]
    ScriptVariables: Optional[Sequence["_ScriptVariablesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            JarFileUris=json_data.get("JarFileUris"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition2),
            QueryFileUri=json_data.get("QueryFileUri"),
            QueryList=json_data.get("QueryList"),
            ScriptVariables=deserialize_list(json_data.get("ScriptVariables"), ScriptVariablesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveConfigDefinition = HiveConfigDefinition


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
class PigConfigDefinition(BaseModel):
    ContinueOnFailure: Optional[bool]
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_PropertiesDefinition3"]]
    QueryFileUri: Optional[str]
    QueryList: Optional[Sequence[str]]
    ScriptVariables: Optional[Sequence["_ScriptVariablesDefinition2"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PigConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PigConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ContinueOnFailure=json_data.get("ContinueOnFailure"),
            JarFileUris=json_data.get("JarFileUris"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition3),
            QueryFileUri=json_data.get("QueryFileUri"),
            QueryList=json_data.get("QueryList"),
            ScriptVariables=deserialize_list(json_data.get("ScriptVariables"), ScriptVariablesDefinition2),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PigConfigDefinition = PigConfigDefinition


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
class PlacementDefinition(BaseModel):
    ClusterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterName=json_data.get("ClusterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementDefinition = PlacementDefinition


@dataclass
class PysparkConfigDefinition(BaseModel):
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainPythonFileUri: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition4"]]
    PythonFileUris: Optional[Sequence[str]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PysparkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PysparkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainPythonFileUri=json_data.get("MainPythonFileUri"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition4),
            PythonFileUris=json_data.get("PythonFileUris"),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PysparkConfigDefinition = PysparkConfigDefinition


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
class ReferenceDefinition(BaseModel):
    JobId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            JobId=json_data.get("JobId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceDefinition = ReferenceDefinition


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
class SparkConfigDefinition(BaseModel):
    ArchiveUris: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    FileUris: Optional[Sequence[str]]
    JarFileUris: Optional[Sequence[str]]
    MainClass: Optional[str]
    MainJarFileUri: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition5"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveUris=json_data.get("ArchiveUris"),
            Args=json_data.get("Args"),
            FileUris=json_data.get("FileUris"),
            JarFileUris=json_data.get("JarFileUris"),
            MainClass=json_data.get("MainClass"),
            MainJarFileUri=json_data.get("MainJarFileUri"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition5),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkConfigDefinition = SparkConfigDefinition


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
class SparksqlConfigDefinition(BaseModel):
    JarFileUris: Optional[Sequence[str]]
    Properties: Optional[Sequence["_PropertiesDefinition6"]]
    QueryFileUri: Optional[str]
    QueryList: Optional[Sequence[str]]
    ScriptVariables: Optional[Sequence["_ScriptVariablesDefinition3"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SparksqlConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparksqlConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            JarFileUris=json_data.get("JarFileUris"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition6),
            QueryFileUri=json_data.get("QueryFileUri"),
            QueryList=json_data.get("QueryList"),
            ScriptVariables=deserialize_list(json_data.get("ScriptVariables"), ScriptVariablesDefinition3),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparksqlConfigDefinition = SparksqlConfigDefinition


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


