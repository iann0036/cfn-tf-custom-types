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
    ApiVersion: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    State: Optional[str]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    StageList: Optional[Sequence["_StageListDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            StageList=deserialize_list(json_data.get("StageList"), StageListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


@dataclass
class OwnerReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class ParametersDefinition(BaseModel):
    FloatingIpAssignmentList: Optional[Sequence["_FloatingIpAssignmentListDefinition"]]
    NetworkMappingList: Optional[Sequence["_NetworkMappingListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            FloatingIpAssignmentList=deserialize_list(json_data.get("FloatingIpAssignmentList"), FloatingIpAssignmentListDefinition),
            NetworkMappingList=deserialize_list(json_data.get("NetworkMappingList"), NetworkMappingListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class FloatingIpAssignmentListDefinition(BaseModel):
    AvailabilityZoneUrl: Optional[str]
    VmIpAssignmentList: Optional[Sequence["_VmIpAssignmentListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIpAssignmentListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIpAssignmentListDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneUrl=json_data.get("AvailabilityZoneUrl"),
            VmIpAssignmentList=deserialize_list(json_data.get("VmIpAssignmentList"), VmIpAssignmentListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIpAssignmentListDefinition = FloatingIpAssignmentListDefinition


@dataclass
class VmIpAssignmentListDefinition(BaseModel):
    RecoveryFloatingIpConfig: Optional[Sequence["_RecoveryFloatingIpConfigDefinition"]]
    TestFloatingIpConfig: Optional[Sequence["_TestFloatingIpConfigDefinition"]]
    VmNicInformation: Optional[Sequence["_VmNicInformationDefinition"]]
    VmReference: Optional[Sequence["_VmReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VmIpAssignmentListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmIpAssignmentListDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryFloatingIpConfig=deserialize_list(json_data.get("RecoveryFloatingIpConfig"), RecoveryFloatingIpConfigDefinition),
            TestFloatingIpConfig=deserialize_list(json_data.get("TestFloatingIpConfig"), TestFloatingIpConfigDefinition),
            VmNicInformation=deserialize_list(json_data.get("VmNicInformation"), VmNicInformationDefinition),
            VmReference=deserialize_list(json_data.get("VmReference"), VmReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmIpAssignmentListDefinition = VmIpAssignmentListDefinition


@dataclass
class RecoveryFloatingIpConfigDefinition(BaseModel):
    Ip: Optional[str]
    ShouldAllocateDynamically: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryFloatingIpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryFloatingIpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            ShouldAllocateDynamically=json_data.get("ShouldAllocateDynamically"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryFloatingIpConfigDefinition = RecoveryFloatingIpConfigDefinition


@dataclass
class TestFloatingIpConfigDefinition(BaseModel):
    Ip: Optional[str]
    ShouldAllocateDynamically: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TestFloatingIpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestFloatingIpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            ShouldAllocateDynamically=json_data.get("ShouldAllocateDynamically"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestFloatingIpConfigDefinition = TestFloatingIpConfigDefinition


@dataclass
class VmNicInformationDefinition(BaseModel):
    Ip: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmNicInformationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmNicInformationDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmNicInformationDefinition = VmNicInformationDefinition


@dataclass
class VmReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmReferenceDefinition = VmReferenceDefinition


@dataclass
class NetworkMappingListDefinition(BaseModel):
    AreNetworksStretched: Optional[bool]
    AvailabilityZoneNetworkMappingList: Optional[Sequence["_AvailabilityZoneNetworkMappingListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkMappingListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkMappingListDefinition"]:
        if not json_data:
            return None
        return cls(
            AreNetworksStretched=json_data.get("AreNetworksStretched"),
            AvailabilityZoneNetworkMappingList=deserialize_list(json_data.get("AvailabilityZoneNetworkMappingList"), AvailabilityZoneNetworkMappingListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkMappingListDefinition = NetworkMappingListDefinition


@dataclass
class AvailabilityZoneNetworkMappingListDefinition(BaseModel):
    AvailabilityZoneUrl: Optional[str]
    ClusterReferenceList: Optional[Sequence["_ClusterReferenceListDefinition"]]
    RecoveryIpAssignmentList: Optional[Sequence["_RecoveryIpAssignmentListDefinition"]]
    RecoveryNetwork: Optional[Sequence["_RecoveryNetworkDefinition"]]
    TestIpAssignmentList: Optional[Sequence["_TestIpAssignmentListDefinition"]]
    TestNetwork: Optional[Sequence["_TestNetworkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneNetworkMappingListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneNetworkMappingListDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneUrl=json_data.get("AvailabilityZoneUrl"),
            ClusterReferenceList=deserialize_list(json_data.get("ClusterReferenceList"), ClusterReferenceListDefinition),
            RecoveryIpAssignmentList=deserialize_list(json_data.get("RecoveryIpAssignmentList"), RecoveryIpAssignmentListDefinition),
            RecoveryNetwork=deserialize_list(json_data.get("RecoveryNetwork"), RecoveryNetworkDefinition),
            TestIpAssignmentList=deserialize_list(json_data.get("TestIpAssignmentList"), TestIpAssignmentListDefinition),
            TestNetwork=deserialize_list(json_data.get("TestNetwork"), TestNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneNetworkMappingListDefinition = AvailabilityZoneNetworkMappingListDefinition


@dataclass
class ClusterReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterReferenceListDefinition = ClusterReferenceListDefinition


@dataclass
class RecoveryIpAssignmentListDefinition(BaseModel):
    IpConfigList: Optional[Sequence["_IpConfigListDefinition"]]
    VmReference: Optional[Sequence["_VmReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryIpAssignmentListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryIpAssignmentListDefinition"]:
        if not json_data:
            return None
        return cls(
            IpConfigList=deserialize_list(json_data.get("IpConfigList"), IpConfigListDefinition),
            VmReference=deserialize_list(json_data.get("VmReference"), VmReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryIpAssignmentListDefinition = RecoveryIpAssignmentListDefinition


@dataclass
class IpConfigListDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfigListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfigListDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigListDefinition = IpConfigListDefinition


@dataclass
class RecoveryNetworkDefinition(BaseModel):
    Name: Optional[str]
    UseVpcReference: Optional[bool]
    SubnetList: Optional[Sequence["_SubnetListDefinition"]]
    VirtualNetworkReference: Optional[Sequence["_VirtualNetworkReferenceDefinition"]]
    VpcReference: Optional[Sequence["_VpcReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UseVpcReference=json_data.get("UseVpcReference"),
            SubnetList=deserialize_list(json_data.get("SubnetList"), SubnetListDefinition),
            VirtualNetworkReference=deserialize_list(json_data.get("VirtualNetworkReference"), VirtualNetworkReferenceDefinition),
            VpcReference=deserialize_list(json_data.get("VpcReference"), VpcReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryNetworkDefinition = RecoveryNetworkDefinition


@dataclass
class SubnetListDefinition(BaseModel):
    ExternalConnectivityState: Optional[str]
    GatewayIp: Optional[str]
    PrefixLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalConnectivityState=json_data.get("ExternalConnectivityState"),
            GatewayIp=json_data.get("GatewayIp"),
            PrefixLength=json_data.get("PrefixLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetListDefinition = SubnetListDefinition


@dataclass
class VirtualNetworkReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkReferenceDefinition = VirtualNetworkReferenceDefinition


@dataclass
class VpcReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcReferenceDefinition = VpcReferenceDefinition


@dataclass
class TestIpAssignmentListDefinition(BaseModel):
    IpConfigList: Optional[Sequence["_IpConfigListDefinition"]]
    VmReference: Optional[Sequence["_VmReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TestIpAssignmentListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestIpAssignmentListDefinition"]:
        if not json_data:
            return None
        return cls(
            IpConfigList=deserialize_list(json_data.get("IpConfigList"), IpConfigListDefinition),
            VmReference=deserialize_list(json_data.get("VmReference"), VmReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestIpAssignmentListDefinition = TestIpAssignmentListDefinition


@dataclass
class TestNetworkDefinition(BaseModel):
    Name: Optional[str]
    UseVpcReference: Optional[bool]
    SubnetList: Optional[Sequence["_SubnetListDefinition"]]
    VirtualNetworkReference: Optional[Sequence["_VirtualNetworkReferenceDefinition"]]
    VpcReference: Optional[Sequence["_VpcReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TestNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UseVpcReference=json_data.get("UseVpcReference"),
            SubnetList=deserialize_list(json_data.get("SubnetList"), SubnetListDefinition),
            VirtualNetworkReference=deserialize_list(json_data.get("VirtualNetworkReference"), VirtualNetworkReferenceDefinition),
            VpcReference=deserialize_list(json_data.get("VpcReference"), VpcReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestNetworkDefinition = TestNetworkDefinition


@dataclass
class ProjectReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceDefinition = ProjectReferenceDefinition


@dataclass
class StageListDefinition(BaseModel):
    DelayTimeSecs: Optional[float]
    StageUuid: Optional[str]
    StageWork: Optional[Sequence["_StageWorkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StageListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageListDefinition"]:
        if not json_data:
            return None
        return cls(
            DelayTimeSecs=json_data.get("DelayTimeSecs"),
            StageUuid=json_data.get("StageUuid"),
            StageWork=deserialize_list(json_data.get("StageWork"), StageWorkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageListDefinition = StageListDefinition


@dataclass
class StageWorkDefinition(BaseModel):
    RecoverEntities: Optional[Sequence["_RecoverEntitiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StageWorkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageWorkDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoverEntities=deserialize_list(json_data.get("RecoverEntities"), RecoverEntitiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageWorkDefinition = StageWorkDefinition


@dataclass
class RecoverEntitiesDefinition(BaseModel):
    EntityInfoList: Optional[Sequence["_EntityInfoListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecoverEntitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoverEntitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            EntityInfoList=deserialize_list(json_data.get("EntityInfoList"), EntityInfoListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoverEntitiesDefinition = RecoverEntitiesDefinition


@dataclass
class EntityInfoListDefinition(BaseModel):
    AnyEntityReferenceKind: Optional[str]
    AnyEntityReferenceName: Optional[str]
    AnyEntityReferenceUuid: Optional[str]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    ScriptList: Optional[Sequence["_ScriptListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntityInfoListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityInfoListDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyEntityReferenceKind=json_data.get("AnyEntityReferenceKind"),
            AnyEntityReferenceName=json_data.get("AnyEntityReferenceName"),
            AnyEntityReferenceUuid=json_data.get("AnyEntityReferenceUuid"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            ScriptList=deserialize_list(json_data.get("ScriptList"), ScriptListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityInfoListDefinition = EntityInfoListDefinition


@dataclass
class ScriptListDefinition(BaseModel):
    EnableScriptExec: Optional[bool]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptListDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableScriptExec=json_data.get("EnableScriptExec"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptListDefinition = ScriptListDefinition


