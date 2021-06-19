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
    AccountMoid: Optional[str]
    AciCniProfile: Optional[Sequence["_AciCniProfileDefinition"]]
    Action: Optional[str]
    ActionInfo: Optional[Sequence["_ActionInfoDefinition"]]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    AssociatedCluster: Optional[Sequence["_AssociatedClusterDefinition"]]
    CertConfig: Optional[Sequence["_CertConfigDefinition"]]
    ClassId: Optional[str]
    ClusterIpPools: Optional[Sequence["_ClusterIpPoolsDefinition"]]
    ConfigContext: Optional[Sequence["_ConfigContextDefinition"]]
    ContainerRuntimeConfig: Optional[Sequence["_ContainerRuntimeConfigDefinition"]]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    EssentialAddons: Optional[Sequence["_EssentialAddonsDefinition4"]]
    Id: Optional[str]
    KubeConfig: Optional[Sequence["_KubeConfigDefinition"]]
    LoadbalancerIpLeases: Optional[Sequence["_LoadbalancerIpLeasesDefinition"]]
    ManagedMode: Optional[str]
    ManagementConfig: Optional[Sequence["_ManagementConfigDefinition"]]
    MasterVipLease: Optional[Sequence["_MasterVipLeaseDefinition"]]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NetConfig: Optional[Sequence["_NetConfigDefinition"]]
    NodeGroups: Optional[Sequence["_NodeGroupsDefinition"]]
    ObjectType: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    PolicyBucket: Optional[Sequence["_PolicyBucketDefinition"]]
    SharedScope: Optional[str]
    SrcTemplate: Optional[Sequence["_SrcTemplateDefinition"]]
    Status: Optional[str]
    SysConfig: Optional[Sequence["_SysConfigDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TrustedRegistries: Optional[Sequence["_TrustedRegistriesDefinition"]]
    Type: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    WaitForCompletion: Optional[bool]
    WorkflowInfo: Optional[Sequence["_WorkflowInfoDefinition"]]

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
            AccountMoid=json_data.get("AccountMoid"),
            AciCniProfile=deserialize_list(json_data.get("AciCniProfile"), AciCniProfileDefinition),
            Action=json_data.get("Action"),
            ActionInfo=deserialize_list(json_data.get("ActionInfo"), ActionInfoDefinition),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            AssociatedCluster=deserialize_list(json_data.get("AssociatedCluster"), AssociatedClusterDefinition),
            CertConfig=deserialize_list(json_data.get("CertConfig"), CertConfigDefinition),
            ClassId=json_data.get("ClassId"),
            ClusterIpPools=deserialize_list(json_data.get("ClusterIpPools"), ClusterIpPoolsDefinition),
            ConfigContext=deserialize_list(json_data.get("ConfigContext"), ConfigContextDefinition),
            ContainerRuntimeConfig=deserialize_list(json_data.get("ContainerRuntimeConfig"), ContainerRuntimeConfigDefinition),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            EssentialAddons=deserialize_list(json_data.get("EssentialAddons"), EssentialAddonsDefinition4),
            Id=json_data.get("Id"),
            KubeConfig=deserialize_list(json_data.get("KubeConfig"), KubeConfigDefinition),
            LoadbalancerIpLeases=deserialize_list(json_data.get("LoadbalancerIpLeases"), LoadbalancerIpLeasesDefinition),
            ManagedMode=json_data.get("ManagedMode"),
            ManagementConfig=deserialize_list(json_data.get("ManagementConfig"), ManagementConfigDefinition),
            MasterVipLease=deserialize_list(json_data.get("MasterVipLease"), MasterVipLeaseDefinition),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NetConfig=deserialize_list(json_data.get("NetConfig"), NetConfigDefinition),
            NodeGroups=deserialize_list(json_data.get("NodeGroups"), NodeGroupsDefinition),
            ObjectType=json_data.get("ObjectType"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            PolicyBucket=deserialize_list(json_data.get("PolicyBucket"), PolicyBucketDefinition),
            SharedScope=json_data.get("SharedScope"),
            SrcTemplate=deserialize_list(json_data.get("SrcTemplate"), SrcTemplateDefinition),
            Status=json_data.get("Status"),
            SysConfig=deserialize_list(json_data.get("SysConfig"), SysConfigDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TrustedRegistries=deserialize_list(json_data.get("TrustedRegistries"), TrustedRegistriesDefinition),
            Type=json_data.get("Type"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            WaitForCompletion=json_data.get("WaitForCompletion"),
            WorkflowInfo=deserialize_list(json_data.get("WorkflowInfo"), WorkflowInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AciCniProfileDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AciCniProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AciCniProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AciCniProfileDefinition = AciCniProfileDefinition


@dataclass
class ActionInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    FailureReason: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            FailureReason=json_data.get("FailureReason"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionInfoDefinition = ActionInfoDefinition


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class AssociatedClusterDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociatedClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociatedClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociatedClusterDefinition = AssociatedClusterDefinition


@dataclass
class CertConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    CaCert: Optional[str]
    CaKey: Optional[str]
    ClassId: Optional[str]
    EtcdCert: Optional[str]
    EtcdEncryptionKey: Optional[Sequence[str]]
    EtcdKey: Optional[str]
    FrontProxyCert: Optional[str]
    FrontProxyKey: Optional[str]
    ObjectType: Optional[str]
    SaPrivateKey: Optional[str]
    SaPublicKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            CaCert=json_data.get("CaCert"),
            CaKey=json_data.get("CaKey"),
            ClassId=json_data.get("ClassId"),
            EtcdCert=json_data.get("EtcdCert"),
            EtcdEncryptionKey=json_data.get("EtcdEncryptionKey"),
            EtcdKey=json_data.get("EtcdKey"),
            FrontProxyCert=json_data.get("FrontProxyCert"),
            FrontProxyKey=json_data.get("FrontProxyKey"),
            ObjectType=json_data.get("ObjectType"),
            SaPrivateKey=json_data.get("SaPrivateKey"),
            SaPublicKey=json_data.get("SaPublicKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertConfigDefinition = CertConfigDefinition


@dataclass
class ClusterIpPoolsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterIpPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterIpPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterIpPoolsDefinition = ClusterIpPoolsDefinition


@dataclass
class ConfigContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ConfigState: Optional[str]
    ControlAction: Optional[str]
    ErrorState: Optional[str]
    ObjectType: Optional[str]
    OperState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ConfigState=json_data.get("ConfigState"),
            ControlAction=json_data.get("ControlAction"),
            ErrorState=json_data.get("ErrorState"),
            ObjectType=json_data.get("ObjectType"),
            OperState=json_data.get("OperState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigContextDefinition = ConfigContextDefinition


@dataclass
class ContainerRuntimeConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerRuntimeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerRuntimeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerRuntimeConfigDefinition = ContainerRuntimeConfigDefinition


@dataclass
class EssentialAddonsDefinition4(BaseModel):
    AdditionalProperties: Optional[str]
    AddonConfiguration: Optional[Sequence["_EssentialAddonsDefinition2"]]
    AddonDefinition: Optional[Sequence["_EssentialAddonsDefinition3"]]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EssentialAddonsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EssentialAddonsDefinition4"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AddonConfiguration=deserialize_list(json_data.get("AddonConfiguration"), EssentialAddonsDefinition2),
            AddonDefinition=deserialize_list(json_data.get("AddonDefinition"), EssentialAddonsDefinition3),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EssentialAddonsDefinition4 = EssentialAddonsDefinition4


@dataclass
class EssentialAddonsDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InstallStrategy: Optional[str]
    ObjectType: Optional[str]
    OverrideSets: Optional[Sequence["_EssentialAddonsDefinition"]]
    Overrides: Optional[str]
    ReleaseName: Optional[str]
    ReleaseNamespace: Optional[str]
    UpgradeStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EssentialAddonsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EssentialAddonsDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InstallStrategy=json_data.get("InstallStrategy"),
            ObjectType=json_data.get("ObjectType"),
            OverrideSets=deserialize_list(json_data.get("OverrideSets"), EssentialAddonsDefinition),
            Overrides=json_data.get("Overrides"),
            ReleaseName=json_data.get("ReleaseName"),
            ReleaseNamespace=json_data.get("ReleaseNamespace"),
            UpgradeStrategy=json_data.get("UpgradeStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EssentialAddonsDefinition2 = EssentialAddonsDefinition2


@dataclass
class EssentialAddonsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Key: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EssentialAddonsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EssentialAddonsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Key=json_data.get("Key"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EssentialAddonsDefinition = EssentialAddonsDefinition


@dataclass
class EssentialAddonsDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EssentialAddonsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EssentialAddonsDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EssentialAddonsDefinition3 = EssentialAddonsDefinition3


@dataclass
class KubeConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    KubeConfig: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            KubeConfig=json_data.get("KubeConfig"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeConfigDefinition = KubeConfigDefinition


@dataclass
class LoadbalancerIpLeasesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadbalancerIpLeasesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadbalancerIpLeasesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadbalancerIpLeasesDefinition = LoadbalancerIpLeasesDefinition


@dataclass
class ManagementConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EncryptedEtcd: Optional[bool]
    LoadBalancerCount: Optional[float]
    LoadBalancers: Optional[Sequence[str]]
    MasterVip: Optional[str]
    ObjectType: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SshUser: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EncryptedEtcd=json_data.get("EncryptedEtcd"),
            LoadBalancerCount=json_data.get("LoadBalancerCount"),
            LoadBalancers=json_data.get("LoadBalancers"),
            MasterVip=json_data.get("MasterVip"),
            ObjectType=json_data.get("ObjectType"),
            SshKeys=json_data.get("SshKeys"),
            SshUser=json_data.get("SshUser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementConfigDefinition = ManagementConfigDefinition


@dataclass
class MasterVipLeaseDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MasterVipLeaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterVipLeaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterVipLeaseDefinition = MasterVipLeaseDefinition


@dataclass
class NetConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetConfigDefinition = NetConfigDefinition


@dataclass
class NodeGroupsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeGroupsDefinition = NodeGroupsDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationDefinition = OrganizationDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class PolicyBucketDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyBucketDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyBucketDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyBucketDefinition = PolicyBucketDefinition


@dataclass
class SrcTemplateDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcTemplateDefinition = SrcTemplateDefinition


@dataclass
class SysConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SysConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysConfigDefinition = SysConfigDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TrustedRegistriesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedRegistriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedRegistriesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedRegistriesDefinition = TrustedRegistriesDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


@dataclass
class WorkflowInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowInfoDefinition = WorkflowInfoDefinition


