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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    DisableFastAcl: Optional[bool]
    DisableForwardProxyPolicy: Optional[bool]
    DisableNetworkPolicy: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    ActiveFastAcls: Optional[Sequence["_ActiveFastAclsDefinition"]]
    ActiveForwardProxyPolicies: Optional[Sequence["_ActiveForwardProxyPoliciesDefinition"]]
    ActiveNetworkPolicies: Optional[Sequence["_ActiveNetworkPoliciesDefinition"]]
    FastAclSet: Optional[Sequence["_FastAclSetDefinition"]]
    ForwardProxyPolicySet: Optional[Sequence["_ForwardProxyPolicySetDefinition"]]
    NetworkPolicySet: Optional[Sequence["_NetworkPolicySetDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DisableFastAcl=json_data.get("DisableFastAcl"),
            DisableForwardProxyPolicy=json_data.get("DisableForwardProxyPolicy"),
            DisableNetworkPolicy=json_data.get("DisableNetworkPolicy"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            ActiveFastAcls=deserialize_list(json_data.get("ActiveFastAcls"), ActiveFastAclsDefinition),
            ActiveForwardProxyPolicies=deserialize_list(json_data.get("ActiveForwardProxyPolicies"), ActiveForwardProxyPoliciesDefinition),
            ActiveNetworkPolicies=deserialize_list(json_data.get("ActiveNetworkPolicies"), ActiveNetworkPoliciesDefinition),
            FastAclSet=deserialize_list(json_data.get("FastAclSet"), FastAclSetDefinition),
            ForwardProxyPolicySet=deserialize_list(json_data.get("ForwardProxyPolicySet"), ForwardProxyPolicySetDefinition),
            NetworkPolicySet=deserialize_list(json_data.get("NetworkPolicySet"), NetworkPolicySetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ActiveFastAclsDefinition(BaseModel):
    FastAcls: Optional[Sequence["_FastAclsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveFastAclsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveFastAclsDefinition"]:
        if not json_data:
            return None
        return cls(
            FastAcls=deserialize_list(json_data.get("FastAcls"), FastAclsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveFastAclsDefinition = ActiveFastAclsDefinition


@dataclass
class FastAclsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FastAclsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastAclsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastAclsDefinition = FastAclsDefinition


@dataclass
class ActiveForwardProxyPoliciesDefinition(BaseModel):
    ForwardProxyPolicies: Optional[Sequence["_ForwardProxyPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveForwardProxyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveForwardProxyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardProxyPolicies=deserialize_list(json_data.get("ForwardProxyPolicies"), ForwardProxyPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveForwardProxyPoliciesDefinition = ActiveForwardProxyPoliciesDefinition


@dataclass
class ForwardProxyPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardProxyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardProxyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardProxyPoliciesDefinition = ForwardProxyPoliciesDefinition


@dataclass
class ActiveNetworkPoliciesDefinition(BaseModel):
    NetworkPolicies: Optional[Sequence["_NetworkPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveNetworkPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveNetworkPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkPolicies=deserialize_list(json_data.get("NetworkPolicies"), NetworkPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveNetworkPoliciesDefinition = ActiveNetworkPoliciesDefinition


@dataclass
class NetworkPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPoliciesDefinition = NetworkPoliciesDefinition


@dataclass
class FastAclSetDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FastAclSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastAclSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastAclSetDefinition = FastAclSetDefinition


@dataclass
class ForwardProxyPolicySetDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardProxyPolicySetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardProxyPolicySetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardProxyPolicySetDefinition = ForwardProxyPolicySetDefinition


@dataclass
class NetworkPolicySetDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPolicySetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPolicySetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPolicySetDefinition = NetworkPolicySetDefinition


