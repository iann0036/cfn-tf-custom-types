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
    DataFactoryName: Optional[str]
    Description: Optional[str]
    Edition: Optional[str]
    LicenseType: Optional[str]
    Location: Optional[str]
    MaxParallelExecutionsPerNode: Optional[float]
    Name: Optional[str]
    NodeSize: Optional[str]
    NumberOfNodes: Optional[float]
    ResourceGroupName: Optional[str]
    CatalogInfo: Optional[Sequence["_CatalogInfo"]]
    CustomSetupScript: Optional[Sequence["_CustomSetupScript"]]
    Timeouts: Optional["_Timeouts"]
    VnetIntegration: Optional[Sequence["_VnetIntegration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DataFactoryName=json_data.get("DataFactoryName"),
            Description=json_data.get("Description"),
            Edition=json_data.get("Edition"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            MaxParallelExecutionsPerNode=json_data.get("MaxParallelExecutionsPerNode"),
            Name=json_data.get("Name"),
            NodeSize=json_data.get("NodeSize"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            CatalogInfo=json_data.get("CatalogInfo"),
            CustomSetupScript=json_data.get("CustomSetupScript"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VnetIntegration=json_data.get("VnetIntegration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CatalogInfo:
    AdministratorLogin: Optional[str]
    AdministratorPassword: Optional[str]
    PricingTier: Optional[str]
    ServerEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogInfo"]:
        if not json_data:
            return None
        return cls(
            AdministratorLogin=json_data.get("AdministratorLogin"),
            AdministratorPassword=json_data.get("AdministratorPassword"),
            PricingTier=json_data.get("PricingTier"),
            ServerEndpoint=json_data.get("ServerEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogInfo = CatalogInfo


@dataclass
class CustomSetupScript:
    BlobContainerUri: Optional[str]
    SasToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSetupScript"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSetupScript"]:
        if not json_data:
            return None
        return cls(
            BlobContainerUri=json_data.get("BlobContainerUri"),
            SasToken=json_data.get("SasToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSetupScript = CustomSetupScript


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class VnetIntegration:
    SubnetName: Optional[str]
    VnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VnetIntegration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VnetIntegration"]:
        if not json_data:
            return None
        return cls(
            SubnetName=json_data.get("SubnetName"),
            VnetId=json_data.get("VnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VnetIntegration = VnetIntegration


