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
    DataFactoryName: Optional[str]
    Description: Optional[str]
    Edition: Optional[str]
    Id: Optional[str]
    LicenseType: Optional[str]
    Location: Optional[str]
    MaxParallelExecutionsPerNode: Optional[float]
    Name: Optional[str]
    NodeSize: Optional[str]
    NumberOfNodes: Optional[float]
    ResourceGroupName: Optional[str]
    CatalogInfo: Optional[Sequence["_CatalogInfoDefinition"]]
    CustomSetupScript: Optional[Sequence["_CustomSetupScriptDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VnetIntegration: Optional[Sequence["_VnetIntegrationDefinition"]]

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
            DataFactoryName=json_data.get("DataFactoryName"),
            Description=json_data.get("Description"),
            Edition=json_data.get("Edition"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            MaxParallelExecutionsPerNode=json_data.get("MaxParallelExecutionsPerNode"),
            Name=json_data.get("Name"),
            NodeSize=json_data.get("NodeSize"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            CatalogInfo=deserialize_list(json_data.get("CatalogInfo"), CatalogInfoDefinition),
            CustomSetupScript=deserialize_list(json_data.get("CustomSetupScript"), CustomSetupScriptDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VnetIntegration=deserialize_list(json_data.get("VnetIntegration"), VnetIntegrationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CatalogInfoDefinition(BaseModel):
    AdministratorLogin: Optional[str]
    AdministratorPassword: Optional[str]
    PricingTier: Optional[str]
    ServerEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdministratorLogin=json_data.get("AdministratorLogin"),
            AdministratorPassword=json_data.get("AdministratorPassword"),
            PricingTier=json_data.get("PricingTier"),
            ServerEndpoint=json_data.get("ServerEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogInfoDefinition = CatalogInfoDefinition


@dataclass
class CustomSetupScriptDefinition(BaseModel):
    BlobContainerUri: Optional[str]
    SasToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSetupScriptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSetupScriptDefinition"]:
        if not json_data:
            return None
        return cls(
            BlobContainerUri=json_data.get("BlobContainerUri"),
            SasToken=json_data.get("SasToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSetupScriptDefinition = CustomSetupScriptDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VnetIntegrationDefinition(BaseModel):
    SubnetName: Optional[str]
    VnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VnetIntegrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VnetIntegrationDefinition"]:
        if not json_data:
            return None
        return cls(
            SubnetName=json_data.get("SubnetName"),
            VnetId=json_data.get("VnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VnetIntegrationDefinition = VnetIntegrationDefinition


