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
    ContractName: Optional[str]
    Id: Optional[str]
    SchemaId: Optional[str]
    ServiceGraphName: Optional[str]
    ServiceGraphSchemaId: Optional[str]
    ServiceGraphSiteId: Optional[str]
    ServiceGraphTemplateName: Optional[str]
    SiteId: Optional[str]
    TemplateName: Optional[str]
    NodeRelationship: Optional[Sequence["_NodeRelationshipDefinition"]]

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
            ContractName=json_data.get("ContractName"),
            Id=json_data.get("Id"),
            SchemaId=json_data.get("SchemaId"),
            ServiceGraphName=json_data.get("ServiceGraphName"),
            ServiceGraphSchemaId=json_data.get("ServiceGraphSchemaId"),
            ServiceGraphSiteId=json_data.get("ServiceGraphSiteId"),
            ServiceGraphTemplateName=json_data.get("ServiceGraphTemplateName"),
            SiteId=json_data.get("SiteId"),
            TemplateName=json_data.get("TemplateName"),
            NodeRelationship=deserialize_list(json_data.get("NodeRelationship"), NodeRelationshipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeRelationshipDefinition(BaseModel):
    ConsumerConnectorBdName: Optional[str]
    ConsumerConnectorBdSchemaId: Optional[str]
    ConsumerConnectorBdTemplateName: Optional[str]
    ConsumerConnectorClusterInterface: Optional[str]
    ConsumerConnectorRedirectPolicy: Optional[str]
    ConsumerConnectorRedirectPolicyTenant: Optional[str]
    ConsumerSubnetIps: Optional[Sequence[str]]
    ProviderConnectorBdName: Optional[str]
    ProviderConnectorBdSchemaId: Optional[str]
    ProviderConnectorBdTemplateName: Optional[str]
    ProviderConnectorClusterInterface: Optional[str]
    ProviderConnectorRedirectPolicy: Optional[str]
    ProviderConnectorRedirectPolicyTenant: Optional[str]
    ProviderSubnetIps: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeRelationshipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeRelationshipDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsumerConnectorBdName=json_data.get("ConsumerConnectorBdName"),
            ConsumerConnectorBdSchemaId=json_data.get("ConsumerConnectorBdSchemaId"),
            ConsumerConnectorBdTemplateName=json_data.get("ConsumerConnectorBdTemplateName"),
            ConsumerConnectorClusterInterface=json_data.get("ConsumerConnectorClusterInterface"),
            ConsumerConnectorRedirectPolicy=json_data.get("ConsumerConnectorRedirectPolicy"),
            ConsumerConnectorRedirectPolicyTenant=json_data.get("ConsumerConnectorRedirectPolicyTenant"),
            ConsumerSubnetIps=json_data.get("ConsumerSubnetIps"),
            ProviderConnectorBdName=json_data.get("ProviderConnectorBdName"),
            ProviderConnectorBdSchemaId=json_data.get("ProviderConnectorBdSchemaId"),
            ProviderConnectorBdTemplateName=json_data.get("ProviderConnectorBdTemplateName"),
            ProviderConnectorClusterInterface=json_data.get("ProviderConnectorClusterInterface"),
            ProviderConnectorRedirectPolicy=json_data.get("ProviderConnectorRedirectPolicy"),
            ProviderConnectorRedirectPolicyTenant=json_data.get("ProviderConnectorRedirectPolicyTenant"),
            ProviderSubnetIps=json_data.get("ProviderSubnetIps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeRelationshipDefinition = NodeRelationshipDefinition


