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
    BusinessgroupId: Optional[str]
    BusinessgroupName: Optional[str]
    CatalogItemId: Optional[str]
    CatalogItemName: Optional[str]
    CreatedDate: Optional[str]
    DeploymentConfiguration: Optional[Sequence["_DeploymentConfigurationDefinition"]]
    DeploymentDestroy: Optional[bool]
    DeploymentId: Optional[str]
    Description: Optional[str]
    ExpiryDate: Optional[str]
    Id: Optional[str]
    LeaseDays: Optional[float]
    Name: Optional[str]
    Owners: Optional[Sequence["_OwnersDefinition"]]
    Reasons: Optional[str]
    RequestStatus: Optional[str]
    WaitTimeout: Optional[float]
    ResourceConfiguration: Optional[Sequence["_ResourceConfigurationDefinition"]]

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
            BusinessgroupId=json_data.get("BusinessgroupId"),
            BusinessgroupName=json_data.get("BusinessgroupName"),
            CatalogItemId=json_data.get("CatalogItemId"),
            CatalogItemName=json_data.get("CatalogItemName"),
            CreatedDate=json_data.get("CreatedDate"),
            DeploymentConfiguration=deserialize_list(json_data.get("DeploymentConfiguration"), DeploymentConfigurationDefinition),
            DeploymentDestroy=json_data.get("DeploymentDestroy"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            ExpiryDate=json_data.get("ExpiryDate"),
            Id=json_data.get("Id"),
            LeaseDays=json_data.get("LeaseDays"),
            Name=json_data.get("Name"),
            Owners=deserialize_list(json_data.get("Owners"), OwnersDefinition),
            Reasons=json_data.get("Reasons"),
            RequestStatus=json_data.get("RequestStatus"),
            WaitTimeout=json_data.get("WaitTimeout"),
            ResourceConfiguration=deserialize_list(json_data.get("ResourceConfiguration"), ResourceConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeploymentConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentConfigurationDefinition = DeploymentConfigurationDefinition


@dataclass
class OwnersDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnersDefinition = OwnersDefinition


@dataclass
class ResourceConfigurationDefinition(BaseModel):
    Cluster: Optional[float]
    ComponentName: Optional[str]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Cluster=json_data.get("Cluster"),
            ComponentName=json_data.get("ComponentName"),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceConfigurationDefinition = ResourceConfigurationDefinition


@dataclass
class ConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


