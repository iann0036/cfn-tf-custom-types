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
    BillingTags: Optional[Sequence[float]]
    CredentialId: Optional[str]
    Cxp: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    LicenseType: Optional[str]
    ManagementSegment: Optional[str]
    MaxInstanceCount: Optional[float]
    MinInstanceCount: Optional[float]
    Name: Optional[str]
    PanoramaDeviceGroup: Optional[str]
    PanoramaEnabled: Optional[str]
    PanoramaIpAddress: Optional[str]
    PanoramaTemplate: Optional[str]
    Segments: Optional[Sequence[str]]
    ServiceId: Optional[float]
    Size: Optional[str]
    Type: Optional[str]
    Version: Optional[str]
    Instance: Optional[Sequence["_InstanceDefinition"]]
    ZonesToGroups: Optional[Sequence["_ZonesToGroupsDefinition"]]

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
            BillingTags=json_data.get("BillingTags"),
            CredentialId=json_data.get("CredentialId"),
            Cxp=json_data.get("Cxp"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            ManagementSegment=json_data.get("ManagementSegment"),
            MaxInstanceCount=json_data.get("MaxInstanceCount"),
            MinInstanceCount=json_data.get("MinInstanceCount"),
            Name=json_data.get("Name"),
            PanoramaDeviceGroup=json_data.get("PanoramaDeviceGroup"),
            PanoramaEnabled=json_data.get("PanoramaEnabled"),
            PanoramaIpAddress=json_data.get("PanoramaIpAddress"),
            PanoramaTemplate=json_data.get("PanoramaTemplate"),
            Segments=json_data.get("Segments"),
            ServiceId=json_data.get("ServiceId"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Instance=deserialize_list(json_data.get("Instance"), InstanceDefinition),
            ZonesToGroups=deserialize_list(json_data.get("ZonesToGroups"), ZonesToGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceDefinition(BaseModel):
    CredentialId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceDefinition"]:
        if not json_data:
            return None
        return cls(
            CredentialId=json_data.get("CredentialId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceDefinition = InstanceDefinition


@dataclass
class ZonesToGroupsDefinition(BaseModel):
    Groups: Optional[Sequence[str]]
    SegmentName: Optional[str]
    ZoneName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZonesToGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZonesToGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Groups=json_data.get("Groups"),
            SegmentName=json_data.get("SegmentName"),
            ZoneName=json_data.get("ZoneName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZonesToGroupsDefinition = ZonesToGroupsDefinition


