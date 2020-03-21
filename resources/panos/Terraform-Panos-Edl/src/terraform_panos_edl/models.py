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
    CertificateProfile: Optional[str]
    Description: Optional[str]
    Exceptions: Optional[Sequence[str]]
    Name: Optional[str]
    Password: Optional[str]
    PasswordEnc: Optional[str]
    Repeat: Optional[str]
    RepeatAt: Optional[str]
    RepeatDayOfMonth: Optional[float]
    RepeatDayOfWeek: Optional[str]
    Source: Optional[str]
    Type: Optional[str]
    Username: Optional[str]
    Vsys: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateProfile=json_data.get("CertificateProfile"),
            Description=json_data.get("Description"),
            Exceptions=json_data.get("Exceptions"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PasswordEnc=json_data.get("PasswordEnc"),
            Repeat=json_data.get("Repeat"),
            RepeatAt=json_data.get("RepeatAt"),
            RepeatDayOfMonth=json_data.get("RepeatDayOfMonth"),
            RepeatDayOfWeek=json_data.get("RepeatDayOfWeek"),
            Source=json_data.get("Source"),
            Type=json_data.get("Type"),
            Username=json_data.get("Username"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


