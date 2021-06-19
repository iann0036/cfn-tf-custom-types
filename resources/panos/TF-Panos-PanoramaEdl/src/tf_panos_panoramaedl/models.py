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
    CertificateProfile: Optional[str]
    Description: Optional[str]
    DeviceGroup: Optional[str]
    Exceptions: Optional[Sequence[str]]
    Id: Optional[str]
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
            CertificateProfile=json_data.get("CertificateProfile"),
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            Exceptions=json_data.get("Exceptions"),
            Id=json_data.get("Id"),
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
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


