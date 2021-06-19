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
    CreatedOrUpdatedBy: Optional[str]
    CreatedOrUpdatedTime: Optional[str]
    CustomTemplateFile: Optional[str]
    Enabled: Optional[bool]
    GroupIssuesBy: Optional[str]
    Id: Optional[str]
    IntgGuid: Optional[str]
    IssueType: Optional[str]
    JiraUrl: Optional[str]
    Name: Optional[str]
    OrgLevel: Optional[bool]
    Password: Optional[str]
    ProjectKey: Optional[str]
    TypeName: Optional[str]
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
            CreatedOrUpdatedBy=json_data.get("CreatedOrUpdatedBy"),
            CreatedOrUpdatedTime=json_data.get("CreatedOrUpdatedTime"),
            CustomTemplateFile=json_data.get("CustomTemplateFile"),
            Enabled=json_data.get("Enabled"),
            GroupIssuesBy=json_data.get("GroupIssuesBy"),
            Id=json_data.get("Id"),
            IntgGuid=json_data.get("IntgGuid"),
            IssueType=json_data.get("IssueType"),
            JiraUrl=json_data.get("JiraUrl"),
            Name=json_data.get("Name"),
            OrgLevel=json_data.get("OrgLevel"),
            Password=json_data.get("Password"),
            ProjectKey=json_data.get("ProjectKey"),
            TypeName=json_data.get("TypeName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


