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
    Capabilities: Optional[Sequence[str]]
    DisableRollback: Optional[bool]
    IamRoleArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NotificationArns: Optional[Sequence[str]]
    OnFailure: Optional[str]
    Outputs: Optional[Sequence["_Outputs"]]
    Parameters: Optional[Sequence["_Parameters"]]
    PolicyBody: Optional[str]
    PolicyUrl: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TemplateBody: Optional[str]
    TemplateUrl: Optional[str]
    TimeoutInMinutes: Optional[float]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Capabilities=json_data.get("Capabilities"),
            DisableRollback=json_data.get("DisableRollback"),
            IamRoleArn=json_data.get("IamRoleArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotificationArns=json_data.get("NotificationArns"),
            OnFailure=json_data.get("OnFailure"),
            Outputs=json_data.get("Outputs"),
            Parameters=json_data.get("Parameters"),
            PolicyBody=json_data.get("PolicyBody"),
            PolicyUrl=json_data.get("PolicyUrl"),
            Tags=json_data.get("Tags"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateUrl=json_data.get("TemplateUrl"),
            TimeoutInMinutes=json_data.get("TimeoutInMinutes"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Outputs:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Outputs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Outputs"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Outputs = Outputs


@dataclass
class Parameters:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


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


