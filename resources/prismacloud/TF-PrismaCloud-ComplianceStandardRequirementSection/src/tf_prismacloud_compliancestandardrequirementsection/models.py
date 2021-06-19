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
    AssociatedPolicyIds: Optional[Sequence[str]]
    CreatedBy: Optional[str]
    CreatedOn: Optional[float]
    CsrId: Optional[str]
    CsrsId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Label: Optional[str]
    LastModifiedBy: Optional[str]
    LastModifiedOn: Optional[float]
    PoliciesAssignedCount: Optional[float]
    RequirementName: Optional[str]
    SectionId: Optional[str]
    StandardName: Optional[str]
    SystemDefault: Optional[bool]
    ViewOrder: Optional[float]

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
            AssociatedPolicyIds=json_data.get("AssociatedPolicyIds"),
            CreatedBy=json_data.get("CreatedBy"),
            CreatedOn=json_data.get("CreatedOn"),
            CsrId=json_data.get("CsrId"),
            CsrsId=json_data.get("CsrsId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            LastModifiedOn=json_data.get("LastModifiedOn"),
            PoliciesAssignedCount=json_data.get("PoliciesAssignedCount"),
            RequirementName=json_data.get("RequirementName"),
            SectionId=json_data.get("SectionId"),
            StandardName=json_data.get("StandardName"),
            SystemDefault=json_data.get("SystemDefault"),
            ViewOrder=json_data.get("ViewOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


