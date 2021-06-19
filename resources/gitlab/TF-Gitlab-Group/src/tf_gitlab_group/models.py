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
    AutoDevopsEnabled: Optional[bool]
    Description: Optional[str]
    EmailsDisabled: Optional[bool]
    FullName: Optional[str]
    FullPath: Optional[str]
    Id: Optional[str]
    LfsEnabled: Optional[bool]
    MentionsDisabled: Optional[bool]
    Name: Optional[str]
    ParentId: Optional[float]
    Path: Optional[str]
    ProjectCreationLevel: Optional[str]
    RequestAccessEnabled: Optional[bool]
    RequireTwoFactorAuthentication: Optional[bool]
    RunnersToken: Optional[str]
    ShareWithGroupLock: Optional[bool]
    SubgroupCreationLevel: Optional[str]
    TwoFactorGracePeriod: Optional[float]
    VisibilityLevel: Optional[str]
    WebUrl: Optional[str]

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
            AutoDevopsEnabled=json_data.get("AutoDevopsEnabled"),
            Description=json_data.get("Description"),
            EmailsDisabled=json_data.get("EmailsDisabled"),
            FullName=json_data.get("FullName"),
            FullPath=json_data.get("FullPath"),
            Id=json_data.get("Id"),
            LfsEnabled=json_data.get("LfsEnabled"),
            MentionsDisabled=json_data.get("MentionsDisabled"),
            Name=json_data.get("Name"),
            ParentId=json_data.get("ParentId"),
            Path=json_data.get("Path"),
            ProjectCreationLevel=json_data.get("ProjectCreationLevel"),
            RequestAccessEnabled=json_data.get("RequestAccessEnabled"),
            RequireTwoFactorAuthentication=json_data.get("RequireTwoFactorAuthentication"),
            RunnersToken=json_data.get("RunnersToken"),
            ShareWithGroupLock=json_data.get("ShareWithGroupLock"),
            SubgroupCreationLevel=json_data.get("SubgroupCreationLevel"),
            TwoFactorGracePeriod=json_data.get("TwoFactorGracePeriod"),
            VisibilityLevel=json_data.get("VisibilityLevel"),
            WebUrl=json_data.get("WebUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


