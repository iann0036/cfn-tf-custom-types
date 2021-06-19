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
    Id: Optional[str]
    SchemaId: Optional[str]
    ServiceGraphName: Optional[str]
    ServiceNodeType: Optional[str]
    TemplateName: Optional[str]
    SiteNodes: Optional[Sequence["_SiteNodesDefinition"]]

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
            Id=json_data.get("Id"),
            SchemaId=json_data.get("SchemaId"),
            ServiceGraphName=json_data.get("ServiceGraphName"),
            ServiceNodeType=json_data.get("ServiceNodeType"),
            TemplateName=json_data.get("TemplateName"),
            SiteNodes=deserialize_list(json_data.get("SiteNodes"), SiteNodesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SiteNodesDefinition(BaseModel):
    NodeName: Optional[str]
    SiteId: Optional[str]
    TenantName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeName=json_data.get("NodeName"),
            SiteId=json_data.get("SiteId"),
            TenantName=json_data.get("TenantName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteNodesDefinition = SiteNodesDefinition


