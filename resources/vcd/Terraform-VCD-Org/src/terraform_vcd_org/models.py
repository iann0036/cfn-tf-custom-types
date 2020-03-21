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
    CanPublishCatalogs: Optional[bool]
    DelayAfterPowerOnSeconds: Optional[float]
    DeleteForce: Optional[bool]
    DeleteRecursive: Optional[bool]
    DeployedVmQuota: Optional[float]
    Description: Optional[str]
    FullName: Optional[str]
    IsEnabled: Optional[bool]
    Name: Optional[str]
    StoredVmQuota: Optional[float]
    VappLease: Optional[Sequence["_VappLease"]]
    VappTemplateLease: Optional[Sequence["_VappTemplateLease"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CanPublishCatalogs=json_data.get("CanPublishCatalogs"),
            DelayAfterPowerOnSeconds=json_data.get("DelayAfterPowerOnSeconds"),
            DeleteForce=json_data.get("DeleteForce"),
            DeleteRecursive=json_data.get("DeleteRecursive"),
            DeployedVmQuota=json_data.get("DeployedVmQuota"),
            Description=json_data.get("Description"),
            FullName=json_data.get("FullName"),
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            StoredVmQuota=json_data.get("StoredVmQuota"),
            VappLease=json_data.get("VappLease"),
            VappTemplateLease=json_data.get("VappTemplateLease"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VappLease:
    DeleteOnStorageLeaseExpiration: Optional[bool]
    MaximumRuntimeLeaseInSec: Optional[float]
    MaximumStorageLeaseInSec: Optional[float]
    PowerOffOnRuntimeLeaseExpiration: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VappLease"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VappLease"]:
        if not json_data:
            return None
        return cls(
            DeleteOnStorageLeaseExpiration=json_data.get("DeleteOnStorageLeaseExpiration"),
            MaximumRuntimeLeaseInSec=json_data.get("MaximumRuntimeLeaseInSec"),
            MaximumStorageLeaseInSec=json_data.get("MaximumStorageLeaseInSec"),
            PowerOffOnRuntimeLeaseExpiration=json_data.get("PowerOffOnRuntimeLeaseExpiration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VappLease = VappLease


@dataclass
class VappTemplateLease:
    DeleteOnStorageLeaseExpiration: Optional[bool]
    MaximumStorageLeaseInSec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VappTemplateLease"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VappTemplateLease"]:
        if not json_data:
            return None
        return cls(
            DeleteOnStorageLeaseExpiration=json_data.get("DeleteOnStorageLeaseExpiration"),
            MaximumStorageLeaseInSec=json_data.get("MaximumStorageLeaseInSec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VappTemplateLease = VappTemplateLease


