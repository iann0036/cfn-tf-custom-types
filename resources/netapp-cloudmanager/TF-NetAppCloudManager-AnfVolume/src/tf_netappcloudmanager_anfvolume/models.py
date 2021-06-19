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
    Account: Optional[str]
    CapacityPool: Optional[str]
    ClientId: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetappAccount: Optional[str]
    ProtocolTypes: Optional[Sequence[str]]
    ResourceGroups: Optional[str]
    ServiceLevel: Optional[str]
    Size: Optional[float]
    SizeUnit: Optional[str]
    Subnet: Optional[str]
    Subscription: Optional[str]
    VirtualNetwork: Optional[str]
    VolumePath: Optional[str]
    WorkingEnvironmentName: Optional[str]
    ExportPolicy: Optional[Sequence["_ExportPolicyDefinition"]]

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
            Account=json_data.get("Account"),
            CapacityPool=json_data.get("CapacityPool"),
            ClientId=json_data.get("ClientId"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetappAccount=json_data.get("NetappAccount"),
            ProtocolTypes=json_data.get("ProtocolTypes"),
            ResourceGroups=json_data.get("ResourceGroups"),
            ServiceLevel=json_data.get("ServiceLevel"),
            Size=json_data.get("Size"),
            SizeUnit=json_data.get("SizeUnit"),
            Subnet=json_data.get("Subnet"),
            Subscription=json_data.get("Subscription"),
            VirtualNetwork=json_data.get("VirtualNetwork"),
            VolumePath=json_data.get("VolumePath"),
            WorkingEnvironmentName=json_data.get("WorkingEnvironmentName"),
            ExportPolicy=deserialize_list(json_data.get("ExportPolicy"), ExportPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExportPolicyDefinition(BaseModel):
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExportPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportPolicyDefinition = ExportPolicyDefinition


@dataclass
class RuleDefinition(BaseModel):
    AllowedClients: Optional[str]
    Cifs: Optional[bool]
    Nfsv3: Optional[bool]
    Nfsv41: Optional[bool]
    RuleIndex: Optional[float]
    UnixReadOnly: Optional[bool]
    UnixReadWrite: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedClients=json_data.get("AllowedClients"),
            Cifs=json_data.get("Cifs"),
            Nfsv3=json_data.get("Nfsv3"),
            Nfsv41=json_data.get("Nfsv41"),
            RuleIndex=json_data.get("RuleIndex"),
            UnixReadOnly=json_data.get("UnixReadOnly"),
            UnixReadWrite=json_data.get("UnixReadWrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


