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
    AutoIsl: Optional[str]
    AutoIslHelloTimer: Optional[float]
    AutoIslPortGroup: Optional[float]
    AutoIslReceiveTimeout: Optional[float]
    AutoMclagIcl: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    MedTlvs: Optional[str]
    N8021Tlvs: Optional[str]
    N8023Tlvs: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    CustomTlvs: Optional[Sequence["_CustomTlvsDefinition"]]
    MedLocationService: Optional[Sequence["_MedLocationServiceDefinition"]]
    MedNetworkPolicy: Optional[Sequence["_MedNetworkPolicyDefinition"]]

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
            AutoIsl=json_data.get("AutoIsl"),
            AutoIslHelloTimer=json_data.get("AutoIslHelloTimer"),
            AutoIslPortGroup=json_data.get("AutoIslPortGroup"),
            AutoIslReceiveTimeout=json_data.get("AutoIslReceiveTimeout"),
            AutoMclagIcl=json_data.get("AutoMclagIcl"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            MedTlvs=json_data.get("MedTlvs"),
            N8021Tlvs=json_data.get("N8021Tlvs"),
            N8023Tlvs=json_data.get("N8023Tlvs"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            CustomTlvs=deserialize_list(json_data.get("CustomTlvs"), CustomTlvsDefinition),
            MedLocationService=deserialize_list(json_data.get("MedLocationService"), MedLocationServiceDefinition),
            MedNetworkPolicy=deserialize_list(json_data.get("MedNetworkPolicy"), MedNetworkPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomTlvsDefinition(BaseModel):
    InformationString: Optional[str]
    Name: Optional[str]
    Oui: Optional[str]
    Subtype: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTlvsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTlvsDefinition"]:
        if not json_data:
            return None
        return cls(
            InformationString=json_data.get("InformationString"),
            Name=json_data.get("Name"),
            Oui=json_data.get("Oui"),
            Subtype=json_data.get("Subtype"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTlvsDefinition = CustomTlvsDefinition


@dataclass
class MedLocationServiceDefinition(BaseModel):
    Name: Optional[str]
    Status: Optional[str]
    SysLocationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MedLocationServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MedLocationServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            SysLocationId=json_data.get("SysLocationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MedLocationServiceDefinition = MedLocationServiceDefinition


@dataclass
class MedNetworkPolicyDefinition(BaseModel):
    AssignVlan: Optional[str]
    Dscp: Optional[float]
    Name: Optional[str]
    Priority: Optional[float]
    Status: Optional[str]
    Vlan: Optional[float]
    VlanIntf: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MedNetworkPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MedNetworkPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignVlan=json_data.get("AssignVlan"),
            Dscp=json_data.get("Dscp"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Vlan=json_data.get("Vlan"),
            VlanIntf=json_data.get("VlanIntf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MedNetworkPolicyDefinition = MedNetworkPolicyDefinition


