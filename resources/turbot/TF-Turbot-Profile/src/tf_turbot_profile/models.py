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
    DirectoryPoolId: Optional[str]
    DisplayName: Optional[str]
    Email: Optional[str]
    ExternalId: Optional[str]
    FamilyName: Optional[str]
    GivenName: Optional[str]
    Id: Optional[str]
    LastLoginTimestamp: Optional[str]
    MiddleName: Optional[str]
    Parent: Optional[str]
    ParentAkas: Optional[Sequence[str]]
    Picture: Optional[str]
    ProfileId: Optional[str]
    Status: Optional[str]
    Title: Optional[str]

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
            DirectoryPoolId=json_data.get("DirectoryPoolId"),
            DisplayName=json_data.get("DisplayName"),
            Email=json_data.get("Email"),
            ExternalId=json_data.get("ExternalId"),
            FamilyName=json_data.get("FamilyName"),
            GivenName=json_data.get("GivenName"),
            Id=json_data.get("Id"),
            LastLoginTimestamp=json_data.get("LastLoginTimestamp"),
            MiddleName=json_data.get("MiddleName"),
            Parent=json_data.get("Parent"),
            ParentAkas=json_data.get("ParentAkas"),
            Picture=json_data.get("Picture"),
            ProfileId=json_data.get("ProfileId"),
            Status=json_data.get("Status"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


