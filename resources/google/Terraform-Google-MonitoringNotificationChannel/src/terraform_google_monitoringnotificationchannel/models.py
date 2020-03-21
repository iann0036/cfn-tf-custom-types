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
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Project: Optional[str]
    Type: Optional[str]
    UserLabels: Optional[Sequence["_UserLabels"]]
    VerificationStatus: Optional[str]
    SensitiveLabels: Optional[Sequence["_SensitiveLabels"]]
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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Type=json_data.get("Type"),
            UserLabels=json_data.get("UserLabels"),
            VerificationStatus=json_data.get("VerificationStatus"),
            SensitiveLabels=json_data.get("SensitiveLabels"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class UserLabels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserLabels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserLabels = UserLabels


@dataclass
class SensitiveLabels:
    AuthToken: Optional[str]
    Password: Optional[str]
    ServiceKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SensitiveLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitiveLabels"]:
        if not json_data:
            return None
        return cls(
            AuthToken=json_data.get("AuthToken"),
            Password=json_data.get("Password"),
            ServiceKey=json_data.get("ServiceKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitiveLabels = SensitiveLabels


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


