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
    AdvertiseDefaultRoute: Optional[str]
    AdvertiseHostRoute: Optional[str]
    Deploy: Optional[bool]
    DeployTimeout: Optional[float]
    Description: Optional[str]
    ExtensionTemplate: Optional[str]
    FabricName: Optional[str]
    Id: Optional[str]
    IntfDescription: Optional[str]
    Ipv6LinkLocalFlag: Optional[str]
    LoopbackId: Optional[float]
    MaxBgpPath: Optional[float]
    MaxIbgpPath: Optional[float]
    Mtu: Optional[float]
    MutlicastAddress: Optional[str]
    MutlicastGroup: Optional[str]
    Name: Optional[str]
    RpAddress: Optional[str]
    RpExternalFlag: Optional[str]
    SegmentId: Optional[str]
    ServiceTemplate: Optional[str]
    Source: Optional[str]
    StaticDefaultRoute: Optional[str]
    Tag: Optional[str]
    Template: Optional[str]
    TrmBgwMsiteFlag: Optional[str]
    TrmEnable: Optional[str]
    VlanId: Optional[float]
    VlanName: Optional[str]
    Attachments: Optional[Sequence["_AttachmentsDefinition"]]

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
            AdvertiseDefaultRoute=json_data.get("AdvertiseDefaultRoute"),
            AdvertiseHostRoute=json_data.get("AdvertiseHostRoute"),
            Deploy=json_data.get("Deploy"),
            DeployTimeout=json_data.get("DeployTimeout"),
            Description=json_data.get("Description"),
            ExtensionTemplate=json_data.get("ExtensionTemplate"),
            FabricName=json_data.get("FabricName"),
            Id=json_data.get("Id"),
            IntfDescription=json_data.get("IntfDescription"),
            Ipv6LinkLocalFlag=json_data.get("Ipv6LinkLocalFlag"),
            LoopbackId=json_data.get("LoopbackId"),
            MaxBgpPath=json_data.get("MaxBgpPath"),
            MaxIbgpPath=json_data.get("MaxIbgpPath"),
            Mtu=json_data.get("Mtu"),
            MutlicastAddress=json_data.get("MutlicastAddress"),
            MutlicastGroup=json_data.get("MutlicastGroup"),
            Name=json_data.get("Name"),
            RpAddress=json_data.get("RpAddress"),
            RpExternalFlag=json_data.get("RpExternalFlag"),
            SegmentId=json_data.get("SegmentId"),
            ServiceTemplate=json_data.get("ServiceTemplate"),
            Source=json_data.get("Source"),
            StaticDefaultRoute=json_data.get("StaticDefaultRoute"),
            Tag=json_data.get("Tag"),
            Template=json_data.get("Template"),
            TrmBgwMsiteFlag=json_data.get("TrmBgwMsiteFlag"),
            TrmEnable=json_data.get("TrmEnable"),
            VlanId=json_data.get("VlanId"),
            VlanName=json_data.get("VlanName"),
            Attachments=deserialize_list(json_data.get("Attachments"), AttachmentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttachmentsDefinition(BaseModel):
    Attach: Optional[bool]
    ExtensionValues: Optional[str]
    FreeFormConfig: Optional[str]
    LoopbackId: Optional[float]
    LoopbackIpv4: Optional[str]
    LoopbackIpv6: Optional[str]
    SerialNumber: Optional[str]
    VlanId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Attach=json_data.get("Attach"),
            ExtensionValues=json_data.get("ExtensionValues"),
            FreeFormConfig=json_data.get("FreeFormConfig"),
            LoopbackId=json_data.get("LoopbackId"),
            LoopbackIpv4=json_data.get("LoopbackIpv4"),
            LoopbackIpv6=json_data.get("LoopbackIpv6"),
            SerialNumber=json_data.get("SerialNumber"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentsDefinition = AttachmentsDefinition


