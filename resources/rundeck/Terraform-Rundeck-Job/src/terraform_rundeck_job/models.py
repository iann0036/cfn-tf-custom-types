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
    AllowConcurrentExecutions: Optional[bool]
    CommandOrderingStrategy: Optional[str]
    ContinueOnError: Optional[bool]
    Description: Optional[str]
    ExecutionEnabled: Optional[bool]
    GroupName: Optional[str]
    Id: Optional[str]
    LogLevel: Optional[str]
    MaxThreadCount: Optional[float]
    Name: Optional[str]
    NodeFilterExcludePrecedence: Optional[bool]
    NodeFilterQuery: Optional[str]
    PreserveOptionsOrder: Optional[bool]
    ProjectName: Optional[str]
    RankAttribute: Optional[str]
    RankOrder: Optional[str]
    Schedule: Optional[str]
    ScheduleEnabled: Optional[bool]
    SuccessOnEmptyNodeFilter: Optional[bool]
    Command: Optional[Sequence["_Command"]]
    Notification: Optional[Sequence["_Notification"]]
    Option: Optional[Sequence["_Option"]]
    Job: Optional[Sequence["_Job"]]
    NodeStepPlugin: Optional[Sequence["_NodeStepPlugin"]]
    StepPlugin: Optional[Sequence["_StepPlugin"]]
    Email: Optional[Sequence["_Email"]]
    Plugin: Optional[Sequence["_Plugin"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowConcurrentExecutions=json_data.get("AllowConcurrentExecutions"),
            CommandOrderingStrategy=json_data.get("CommandOrderingStrategy"),
            ContinueOnError=json_data.get("ContinueOnError"),
            Description=json_data.get("Description"),
            ExecutionEnabled=json_data.get("ExecutionEnabled"),
            GroupName=json_data.get("GroupName"),
            Id=json_data.get("Id"),
            LogLevel=json_data.get("LogLevel"),
            MaxThreadCount=json_data.get("MaxThreadCount"),
            Name=json_data.get("Name"),
            NodeFilterExcludePrecedence=json_data.get("NodeFilterExcludePrecedence"),
            NodeFilterQuery=json_data.get("NodeFilterQuery"),
            PreserveOptionsOrder=json_data.get("PreserveOptionsOrder"),
            ProjectName=json_data.get("ProjectName"),
            RankAttribute=json_data.get("RankAttribute"),
            RankOrder=json_data.get("RankOrder"),
            Schedule=json_data.get("Schedule"),
            ScheduleEnabled=json_data.get("ScheduleEnabled"),
            SuccessOnEmptyNodeFilter=json_data.get("SuccessOnEmptyNodeFilter"),
            Command=json_data.get("Command"),
            Notification=json_data.get("Notification"),
            Option=json_data.get("Option"),
            Job=json_data.get("Job"),
            NodeStepPlugin=json_data.get("NodeStepPlugin"),
            StepPlugin=json_data.get("StepPlugin"),
            Email=json_data.get("Email"),
            Plugin=json_data.get("Plugin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Command:
    Description: Optional[str]
    InlineScript: Optional[str]
    ScriptFile: Optional[str]
    ScriptFileArgs: Optional[str]
    ShellCommand: Optional[str]
    Job: Optional[Sequence["_Job"]]
    NodeStepPlugin: Optional[Sequence["_NodeStepPlugin"]]
    StepPlugin: Optional[Sequence["_StepPlugin"]]

    @classmethod
    def _deserialize(
        cls: Type["_Command"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Command"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            InlineScript=json_data.get("InlineScript"),
            ScriptFile=json_data.get("ScriptFile"),
            ScriptFileArgs=json_data.get("ScriptFileArgs"),
            ShellCommand=json_data.get("ShellCommand"),
            Job=json_data.get("Job"),
            NodeStepPlugin=json_data.get("NodeStepPlugin"),
            StepPlugin=json_data.get("StepPlugin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Command = Command


@dataclass
class Job:
    Args: Optional[str]
    GroupName: Optional[str]
    Name: Optional[str]
    Nodefilters: Optional[Sequence["_Nodefilters"]]
    RunForEachNode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Job"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Job"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            GroupName=json_data.get("GroupName"),
            Name=json_data.get("Name"),
            Nodefilters=json_data.get("Nodefilters"),
            RunForEachNode=json_data.get("RunForEachNode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Job = Job


@dataclass
class Nodefilters:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodefilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodefilters"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodefilters = Nodefilters


@dataclass
class NodeStepPlugin:
    Config: Optional[Sequence["_Config"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeStepPlugin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeStepPlugin"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeStepPlugin = NodeStepPlugin


@dataclass
class Config:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class StepPlugin:
    Config: Optional[Sequence["_Config2"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepPlugin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepPlugin"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepPlugin = StepPlugin


@dataclass
class Config2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config2 = Config2


@dataclass
class Notification:
    Type: Optional[str]
    WebhookUrls: Optional[Sequence[str]]
    Email: Optional[Sequence["_Email"]]
    Plugin: Optional[Sequence["_Plugin"]]

    @classmethod
    def _deserialize(
        cls: Type["_Notification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notification"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            WebhookUrls=json_data.get("WebhookUrls"),
            Email=json_data.get("Email"),
            Plugin=json_data.get("Plugin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notification = Notification


@dataclass
class Email:
    AttachLog: Optional[bool]
    Recipients: Optional[Sequence[str]]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Email"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Email"]:
        if not json_data:
            return None
        return cls(
            AttachLog=json_data.get("AttachLog"),
            Recipients=json_data.get("Recipients"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Email = Email


@dataclass
class Plugin:
    Config: Optional[Sequence["_Config3"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Plugin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Plugin"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Plugin = Plugin


@dataclass
class Config3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config3 = Config3


@dataclass
class Option:
    AllowMultipleValues: Optional[bool]
    DefaultValue: Optional[str]
    Description: Optional[str]
    ExposedToScripts: Optional[bool]
    MultiValueDelimiter: Optional[str]
    Name: Optional[str]
    ObscureInput: Optional[bool]
    RequirePredefinedChoice: Optional[bool]
    Required: Optional[bool]
    ValidationRegex: Optional[str]
    ValueChoices: Optional[Sequence[str]]
    ValueChoicesUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Option"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Option"]:
        if not json_data:
            return None
        return cls(
            AllowMultipleValues=json_data.get("AllowMultipleValues"),
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            ExposedToScripts=json_data.get("ExposedToScripts"),
            MultiValueDelimiter=json_data.get("MultiValueDelimiter"),
            Name=json_data.get("Name"),
            ObscureInput=json_data.get("ObscureInput"),
            RequirePredefinedChoice=json_data.get("RequirePredefinedChoice"),
            Required=json_data.get("Required"),
            ValidationRegex=json_data.get("ValidationRegex"),
            ValueChoices=json_data.get("ValueChoices"),
            ValueChoicesUrl=json_data.get("ValueChoicesUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Option = Option


