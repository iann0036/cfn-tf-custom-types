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
    GlobalAccessEnable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    NoClusterWideApps: Optional[bool]
    NoGlobalAccess: Optional[bool]
    NoInsecureRegistries: Optional[bool]
    NoLocalAccess: Optional[bool]
    UseDefaultClusterRoleBindings: Optional[bool]
    UseDefaultClusterRoles: Optional[bool]
    UseDefaultPsp: Optional[bool]
    ClusterWideAppList: Optional[Sequence["_ClusterWideAppListDefinition"]]
    InsecureRegistryList: Optional[Sequence["_InsecureRegistryListDefinition"]]
    LocalAccessConfig: Optional[Sequence["_LocalAccessConfigDefinition"]]
    UseCustomClusterRoleBindings: Optional[Sequence["_UseCustomClusterRoleBindingsDefinition"]]
    UseCustomClusterRoleList: Optional[Sequence["_UseCustomClusterRoleListDefinition"]]
    UseCustomPspList: Optional[Sequence["_UseCustomPspListDefinition"]]

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
            GlobalAccessEnable=json_data.get("GlobalAccessEnable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NoClusterWideApps=json_data.get("NoClusterWideApps"),
            NoGlobalAccess=json_data.get("NoGlobalAccess"),
            NoInsecureRegistries=json_data.get("NoInsecureRegistries"),
            NoLocalAccess=json_data.get("NoLocalAccess"),
            UseDefaultClusterRoleBindings=json_data.get("UseDefaultClusterRoleBindings"),
            UseDefaultClusterRoles=json_data.get("UseDefaultClusterRoles"),
            UseDefaultPsp=json_data.get("UseDefaultPsp"),
            ClusterWideAppList=deserialize_list(json_data.get("ClusterWideAppList"), ClusterWideAppListDefinition),
            InsecureRegistryList=deserialize_list(json_data.get("InsecureRegistryList"), InsecureRegistryListDefinition),
            LocalAccessConfig=deserialize_list(json_data.get("LocalAccessConfig"), LocalAccessConfigDefinition),
            UseCustomClusterRoleBindings=deserialize_list(json_data.get("UseCustomClusterRoleBindings"), UseCustomClusterRoleBindingsDefinition),
            UseCustomClusterRoleList=deserialize_list(json_data.get("UseCustomClusterRoleList"), UseCustomClusterRoleListDefinition),
            UseCustomPspList=deserialize_list(json_data.get("UseCustomPspList"), UseCustomPspListDefinition),
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
class ClusterWideAppListDefinition(BaseModel):
    ClusterWideApps: Optional[Sequence["_ClusterWideAppsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterWideAppListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterWideAppListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterWideApps=deserialize_list(json_data.get("ClusterWideApps"), ClusterWideAppsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterWideAppListDefinition = ClusterWideAppListDefinition


@dataclass
class ClusterWideAppsDefinition(BaseModel):
    ArgoCd: Optional[Sequence["_ArgoCdDefinition"]]
    Dashboard: Optional[Sequence["_DashboardDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterWideAppsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterWideAppsDefinition"]:
        if not json_data:
            return None
        return cls(
            ArgoCd=deserialize_list(json_data.get("ArgoCd"), ArgoCdDefinition),
            Dashboard=deserialize_list(json_data.get("Dashboard"), DashboardDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterWideAppsDefinition = ClusterWideAppsDefinition


@dataclass
class ArgoCdDefinition(BaseModel):
    GeneratedYaml: Optional[str]
    LocalDomain: Optional[Sequence["_LocalDomainDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArgoCdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArgoCdDefinition"]:
        if not json_data:
            return None
        return cls(
            GeneratedYaml=json_data.get("GeneratedYaml"),
            LocalDomain=deserialize_list(json_data.get("LocalDomain"), LocalDomainDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArgoCdDefinition = ArgoCdDefinition


@dataclass
class LocalDomainDefinition(BaseModel):
    DefaultPort: Optional[bool]
    LocalDomain: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LocalDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultPort=json_data.get("DefaultPort"),
            LocalDomain=json_data.get("LocalDomain"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalDomainDefinition = LocalDomainDefinition


@dataclass
class DashboardDefinition(BaseModel):
    GeneratedYaml: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DashboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashboardDefinition"]:
        if not json_data:
            return None
        return cls(
            GeneratedYaml=json_data.get("GeneratedYaml"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashboardDefinition = DashboardDefinition


@dataclass
class InsecureRegistryListDefinition(BaseModel):
    InsecureRegistries: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InsecureRegistryListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsecureRegistryListDefinition"]:
        if not json_data:
            return None
        return cls(
            InsecureRegistries=json_data.get("InsecureRegistries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsecureRegistryListDefinition = InsecureRegistryListDefinition


@dataclass
class LocalAccessConfigDefinition(BaseModel):
    DefaultPort: Optional[bool]
    LocalDomain: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LocalAccessConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalAccessConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultPort=json_data.get("DefaultPort"),
            LocalDomain=json_data.get("LocalDomain"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalAccessConfigDefinition = LocalAccessConfigDefinition


@dataclass
class UseCustomClusterRoleBindingsDefinition(BaseModel):
    ClusterRoleBindings: Optional[Sequence["_ClusterRoleBindingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UseCustomClusterRoleBindingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseCustomClusterRoleBindingsDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterRoleBindings=deserialize_list(json_data.get("ClusterRoleBindings"), ClusterRoleBindingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseCustomClusterRoleBindingsDefinition = UseCustomClusterRoleBindingsDefinition


@dataclass
class ClusterRoleBindingsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterRoleBindingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterRoleBindingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterRoleBindingsDefinition = ClusterRoleBindingsDefinition


@dataclass
class UseCustomClusterRoleListDefinition(BaseModel):
    ClusterRoles: Optional[Sequence["_ClusterRolesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UseCustomClusterRoleListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseCustomClusterRoleListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterRoles=deserialize_list(json_data.get("ClusterRoles"), ClusterRolesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseCustomClusterRoleListDefinition = UseCustomClusterRoleListDefinition


@dataclass
class ClusterRolesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterRolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterRolesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterRolesDefinition = ClusterRolesDefinition


@dataclass
class UseCustomPspListDefinition(BaseModel):
    PodSecurityPolicies: Optional[Sequence["_PodSecurityPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UseCustomPspListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseCustomPspListDefinition"]:
        if not json_data:
            return None
        return cls(
            PodSecurityPolicies=deserialize_list(json_data.get("PodSecurityPolicies"), PodSecurityPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseCustomPspListDefinition = UseCustomPspListDefinition


@dataclass
class PodSecurityPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PodSecurityPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodSecurityPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodSecurityPoliciesDefinition = PodSecurityPoliciesDefinition


