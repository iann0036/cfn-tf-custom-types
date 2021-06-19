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
    IsDefault: Optional[bool]
    Name: Optional[str]
    ServiceDomainId: Optional[str]
    Type: Optional[str]
    EbsStorageConfig: Optional[Sequence["_EbsStorageConfigDefinition"]]
    NutanixVolumesConfig: Optional[Sequence["_NutanixVolumesConfigDefinition"]]

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
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
            ServiceDomainId=json_data.get("ServiceDomainId"),
            Type=json_data.get("Type"),
            EbsStorageConfig=deserialize_list(json_data.get("EbsStorageConfig"), EbsStorageConfigDefinition),
            NutanixVolumesConfig=deserialize_list(json_data.get("NutanixVolumesConfig"), NutanixVolumesConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EbsStorageConfigDefinition(BaseModel):
    Encrypted: Optional[str]
    IopsPerGb: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsStorageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsStorageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            IopsPerGb=json_data.get("IopsPerGb"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsStorageConfigDefinition = EbsStorageConfigDefinition


@dataclass
class NutanixVolumesConfigDefinition(BaseModel):
    DataServicesIp: Optional[str]
    DataServicesPort: Optional[float]
    FlashMode: Optional[bool]
    PrismElementClusterPort: Optional[float]
    PrismElementClusterVip: Optional[str]
    PrismElementPassword: Optional[str]
    PrismElementStorageContainerName: Optional[str]
    PrismElementUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NutanixVolumesConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NutanixVolumesConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DataServicesIp=json_data.get("DataServicesIp"),
            DataServicesPort=json_data.get("DataServicesPort"),
            FlashMode=json_data.get("FlashMode"),
            PrismElementClusterPort=json_data.get("PrismElementClusterPort"),
            PrismElementClusterVip=json_data.get("PrismElementClusterVip"),
            PrismElementPassword=json_data.get("PrismElementPassword"),
            PrismElementStorageContainerName=json_data.get("PrismElementStorageContainerName"),
            PrismElementUsername=json_data.get("PrismElementUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NutanixVolumesConfigDefinition = NutanixVolumesConfigDefinition


