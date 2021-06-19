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
    Annotation: Optional[str]
    ConnConsumerDn: Optional[str]
    ConnProviderDn: Optional[str]
    Description: Optional[str]
    FuncTemplateType: Optional[str]
    FuncType: Optional[str]
    Id: Optional[str]
    IsCopy: Optional[str]
    L4L7ServiceGraphTemplateDn: Optional[str]
    Managed: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    RelationVnsRsDefaultScopeToTerm: Optional[str]
    RelationVnsRsNodeToAbsFuncProf: Optional[str]
    RelationVnsRsNodeToCloudLDev: Optional[str]
    RelationVnsRsNodeToLDev: Optional[str]
    RelationVnsRsNodeToMFunc: Optional[str]
    RoutingMode: Optional[str]
    SequenceNumber: Optional[str]
    ShareEncap: Optional[str]

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
            Annotation=json_data.get("Annotation"),
            ConnConsumerDn=json_data.get("ConnConsumerDn"),
            ConnProviderDn=json_data.get("ConnProviderDn"),
            Description=json_data.get("Description"),
            FuncTemplateType=json_data.get("FuncTemplateType"),
            FuncType=json_data.get("FuncType"),
            Id=json_data.get("Id"),
            IsCopy=json_data.get("IsCopy"),
            L4L7ServiceGraphTemplateDn=json_data.get("L4L7ServiceGraphTemplateDn"),
            Managed=json_data.get("Managed"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            RelationVnsRsDefaultScopeToTerm=json_data.get("RelationVnsRsDefaultScopeToTerm"),
            RelationVnsRsNodeToAbsFuncProf=json_data.get("RelationVnsRsNodeToAbsFuncProf"),
            RelationVnsRsNodeToCloudLDev=json_data.get("RelationVnsRsNodeToCloudLDev"),
            RelationVnsRsNodeToLDev=json_data.get("RelationVnsRsNodeToLDev"),
            RelationVnsRsNodeToMFunc=json_data.get("RelationVnsRsNodeToMFunc"),
            RoutingMode=json_data.get("RoutingMode"),
            SequenceNumber=json_data.get("SequenceNumber"),
            ShareEncap=json_data.get("ShareEncap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


