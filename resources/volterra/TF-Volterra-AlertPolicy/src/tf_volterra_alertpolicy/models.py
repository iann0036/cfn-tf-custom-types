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
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    NotificationParameters: Optional[Sequence["_NotificationParametersDefinition"]]
    Receivers: Optional[Sequence["_ReceiversDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]

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
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NotificationParameters=deserialize_list(json_data.get("NotificationParameters"), NotificationParametersDefinition),
            Receivers=deserialize_list(json_data.get("Receivers"), ReceiversDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
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
class NotificationParametersDefinition(BaseModel):
    Default: Optional[bool]
    GroupInterval: Optional[str]
    GroupWait: Optional[str]
    Individual: Optional[bool]
    RepeatInterval: Optional[str]
    VesIoGroup: Optional[bool]
    Custom: Optional[Sequence["_CustomDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            GroupInterval=json_data.get("GroupInterval"),
            GroupWait=json_data.get("GroupWait"),
            Individual=json_data.get("Individual"),
            RepeatInterval=json_data.get("RepeatInterval"),
            VesIoGroup=json_data.get("VesIoGroup"),
            Custom=deserialize_list(json_data.get("Custom"), CustomDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationParametersDefinition = NotificationParametersDefinition


@dataclass
class CustomDefinition(BaseModel):
    Labels: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDefinition = CustomDefinition


@dataclass
class ReceiversDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReceiversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReceiversDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReceiversDefinition = ReceiversDefinition


@dataclass
class RoutesDefinition(BaseModel):
    Alertname: Optional[str]
    AlertnameRegex: Optional[str]
    Any: Optional[bool]
    DontSend: Optional[bool]
    Send: Optional[bool]
    Custom: Optional[Sequence["_CustomDefinition"]]
    Group: Optional[Sequence["_GroupDefinition"]]
    NotificationParameters: Optional[Sequence["_NotificationParametersDefinition"]]
    Severity: Optional[Sequence["_SeverityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Alertname=json_data.get("Alertname"),
            AlertnameRegex=json_data.get("AlertnameRegex"),
            Any=json_data.get("Any"),
            DontSend=json_data.get("DontSend"),
            Send=json_data.get("Send"),
            Custom=deserialize_list(json_data.get("Custom"), CustomDefinition),
            Group=deserialize_list(json_data.get("Group"), GroupDefinition),
            NotificationParameters=deserialize_list(json_data.get("NotificationParameters"), NotificationParametersDefinition),
            Severity=deserialize_list(json_data.get("Severity"), SeverityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class GroupDefinition(BaseModel):
    ExactMatch: Optional[str]
    RegexMatch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactMatch=json_data.get("ExactMatch"),
            RegexMatch=json_data.get("RegexMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupDefinition = GroupDefinition


@dataclass
class SeverityDefinition(BaseModel):
    ExactMatch: Optional[str]
    RegexMatch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactMatch=json_data.get("ExactMatch"),
            RegexMatch=json_data.get("RegexMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityDefinition = SeverityDefinition


