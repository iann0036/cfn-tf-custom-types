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
    WaitForRollout: Optional[bool]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            WaitForRollout=json_data.get("WaitForRollout"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition2"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition2),
            GenerateName=json_data.get("GenerateName"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AnnotationsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition2 = AnnotationsDefinition2


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class SpecDefinition(BaseModel):
    ActiveDeadlineSeconds: Optional[float]
    AutomountServiceAccountToken: Optional[bool]
    DnsPolicy: Optional[str]
    EnableServiceLinks: Optional[bool]
    HostIpc: Optional[bool]
    HostNetwork: Optional[bool]
    HostPid: Optional[bool]
    Hostname: Optional[str]
    NodeName: Optional[str]
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition"]]
    PriorityClassName: Optional[str]
    RestartPolicy: Optional[str]
    ServiceAccountName: Optional[str]
    ShareProcessNamespace: Optional[bool]
    Subdomain: Optional[str]
    TerminationGracePeriodSeconds: Optional[float]
    Affinity: Optional[Sequence["_AffinityDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    DnsConfig: Optional[Sequence["_DnsConfigDefinition"]]
    HostAliases: Optional[Sequence["_HostAliasesDefinition"]]
    ImagePullSecrets: Optional[Sequence["_ImagePullSecretsDefinition"]]
    InitContainer: Optional[Sequence["_InitContainerDefinition"]]
    ReadinessGate: Optional[Sequence["_ReadinessGateDefinition"]]
    SecurityContext: Optional[Sequence["_SecurityContextDefinition"]]
    Toleration: Optional[Sequence["_TolerationDefinition"]]
    TopologySpreadConstraint: Optional[Sequence["_TopologySpreadConstraintDefinition"]]
    Volume: Optional[Sequence["_VolumeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveDeadlineSeconds=json_data.get("ActiveDeadlineSeconds"),
            AutomountServiceAccountToken=json_data.get("AutomountServiceAccountToken"),
            DnsPolicy=json_data.get("DnsPolicy"),
            EnableServiceLinks=json_data.get("EnableServiceLinks"),
            HostIpc=json_data.get("HostIpc"),
            HostNetwork=json_data.get("HostNetwork"),
            HostPid=json_data.get("HostPid"),
            Hostname=json_data.get("Hostname"),
            NodeName=json_data.get("NodeName"),
            NodeSelector=deserialize_list(json_data.get("NodeSelector"), NodeSelectorDefinition),
            PriorityClassName=json_data.get("PriorityClassName"),
            RestartPolicy=json_data.get("RestartPolicy"),
            ServiceAccountName=json_data.get("ServiceAccountName"),
            ShareProcessNamespace=json_data.get("ShareProcessNamespace"),
            Subdomain=json_data.get("Subdomain"),
            TerminationGracePeriodSeconds=json_data.get("TerminationGracePeriodSeconds"),
            Affinity=deserialize_list(json_data.get("Affinity"), AffinityDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            DnsConfig=deserialize_list(json_data.get("DnsConfig"), DnsConfigDefinition),
            HostAliases=deserialize_list(json_data.get("HostAliases"), HostAliasesDefinition),
            ImagePullSecrets=deserialize_list(json_data.get("ImagePullSecrets"), ImagePullSecretsDefinition),
            InitContainer=deserialize_list(json_data.get("InitContainer"), InitContainerDefinition),
            ReadinessGate=deserialize_list(json_data.get("ReadinessGate"), ReadinessGateDefinition),
            SecurityContext=deserialize_list(json_data.get("SecurityContext"), SecurityContextDefinition),
            Toleration=deserialize_list(json_data.get("Toleration"), TolerationDefinition),
            TopologySpreadConstraint=deserialize_list(json_data.get("TopologySpreadConstraint"), TopologySpreadConstraintDefinition),
            Volume=deserialize_list(json_data.get("Volume"), VolumeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class NodeSelectorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorDefinition = NodeSelectorDefinition


@dataclass
class AffinityDefinition(BaseModel):
    NodeAffinity: Optional[Sequence["_NodeAffinityDefinition"]]
    PodAffinity: Optional[Sequence["_PodAffinityDefinition"]]
    PodAntiAffinity: Optional[Sequence["_PodAntiAffinityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeAffinity=deserialize_list(json_data.get("NodeAffinity"), NodeAffinityDefinition),
            PodAffinity=deserialize_list(json_data.get("PodAffinity"), PodAffinityDefinition),
            PodAntiAffinity=deserialize_list(json_data.get("PodAntiAffinity"), PodAntiAffinityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AffinityDefinition = AffinityDefinition


@dataclass
class NodeAffinityDefinition(BaseModel):
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecutionDefinition"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecutionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            PreferredDuringSchedulingIgnoredDuringExecution=deserialize_list(json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"), PreferredDuringSchedulingIgnoredDuringExecutionDefinition),
            RequiredDuringSchedulingIgnoredDuringExecution=deserialize_list(json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"), RequiredDuringSchedulingIgnoredDuringExecutionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinityDefinition = NodeAffinityDefinition


@dataclass
class PreferredDuringSchedulingIgnoredDuringExecutionDefinition(BaseModel):
    Weight: Optional[float]
    PodAffinityTerm: Optional[Sequence["_PodAffinityTermDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreferredDuringSchedulingIgnoredDuringExecutionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreferredDuringSchedulingIgnoredDuringExecutionDefinition"]:
        if not json_data:
            return None
        return cls(
            Weight=json_data.get("Weight"),
            PodAffinityTerm=deserialize_list(json_data.get("PodAffinityTerm"), PodAffinityTermDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreferredDuringSchedulingIgnoredDuringExecutionDefinition = PreferredDuringSchedulingIgnoredDuringExecutionDefinition


@dataclass
class PodAffinityTermDefinition(BaseModel):
    Namespaces: Optional[Sequence[str]]
    TopologyKey: Optional[str]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodAffinityTermDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodAffinityTermDefinition"]:
        if not json_data:
            return None
        return cls(
            Namespaces=json_data.get("Namespaces"),
            TopologyKey=json_data.get("TopologyKey"),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodAffinityTermDefinition = PodAffinityTermDefinition


@dataclass
class LabelSelectorDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition3"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LabelSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition3),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelSelectorDefinition = LabelSelectorDefinition


@dataclass
class MatchLabelsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabelsDefinition3 = MatchLabelsDefinition3


@dataclass
class MatchExpressionsDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressionsDefinition = MatchExpressionsDefinition


@dataclass
class RequiredDuringSchedulingIgnoredDuringExecutionDefinition(BaseModel):
    Namespaces: Optional[Sequence[str]]
    TopologyKey: Optional[str]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredDuringSchedulingIgnoredDuringExecutionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredDuringSchedulingIgnoredDuringExecutionDefinition"]:
        if not json_data:
            return None
        return cls(
            Namespaces=json_data.get("Namespaces"),
            TopologyKey=json_data.get("TopologyKey"),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredDuringSchedulingIgnoredDuringExecutionDefinition = RequiredDuringSchedulingIgnoredDuringExecutionDefinition


@dataclass
class PodAffinityDefinition(BaseModel):
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecutionDefinition"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecutionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            PreferredDuringSchedulingIgnoredDuringExecution=deserialize_list(json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"), PreferredDuringSchedulingIgnoredDuringExecutionDefinition),
            RequiredDuringSchedulingIgnoredDuringExecution=deserialize_list(json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"), RequiredDuringSchedulingIgnoredDuringExecutionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodAffinityDefinition = PodAffinityDefinition


@dataclass
class PodAntiAffinityDefinition(BaseModel):
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecutionDefinition"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecutionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodAntiAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodAntiAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            PreferredDuringSchedulingIgnoredDuringExecution=deserialize_list(json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"), PreferredDuringSchedulingIgnoredDuringExecutionDefinition),
            RequiredDuringSchedulingIgnoredDuringExecution=deserialize_list(json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"), RequiredDuringSchedulingIgnoredDuringExecutionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodAntiAffinityDefinition = PodAntiAffinityDefinition


@dataclass
class ContainerDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Name: Optional[str]
    Stdin: Optional[bool]
    StdinOnce: Optional[bool]
    TerminationMessagePath: Optional[str]
    TerminationMessagePolicy: Optional[str]
    Tty: Optional[bool]
    WorkingDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    EnvFrom: Optional[Sequence["_EnvFromDefinition"]]
    Lifecycle: Optional[Sequence["_LifecycleDefinition"]]
    LivenessProbe: Optional[Sequence["_LivenessProbeDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbeDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]
    SecurityContext: Optional[Sequence["_SecurityContextDefinition"]]
    StartupProbe: Optional[Sequence["_StartupProbeDefinition"]]
    VolumeMount: Optional[Sequence["_VolumeMountDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Command=json_data.get("Command"),
            Image=json_data.get("Image"),
            ImagePullPolicy=json_data.get("ImagePullPolicy"),
            Name=json_data.get("Name"),
            Stdin=json_data.get("Stdin"),
            StdinOnce=json_data.get("StdinOnce"),
            TerminationMessagePath=json_data.get("TerminationMessagePath"),
            TerminationMessagePolicy=json_data.get("TerminationMessagePolicy"),
            Tty=json_data.get("Tty"),
            WorkingDir=json_data.get("WorkingDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            EnvFrom=deserialize_list(json_data.get("EnvFrom"), EnvFromDefinition),
            Lifecycle=deserialize_list(json_data.get("Lifecycle"), LifecycleDefinition),
            LivenessProbe=deserialize_list(json_data.get("LivenessProbe"), LivenessProbeDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            ReadinessProbe=deserialize_list(json_data.get("ReadinessProbe"), ReadinessProbeDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
            SecurityContext=deserialize_list(json_data.get("SecurityContext"), SecurityContextDefinition),
            StartupProbe=deserialize_list(json_data.get("StartupProbe"), StartupProbeDefinition),
            VolumeMount=deserialize_list(json_data.get("VolumeMount"), VolumeMountDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class EnvDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]
    ValueFrom: Optional[Sequence["_ValueFromDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
            ValueFrom=deserialize_list(json_data.get("ValueFrom"), ValueFromDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvDefinition = EnvDefinition


@dataclass
class ValueFromDefinition(BaseModel):
    ConfigMapKeyRef: Optional[Sequence["_ConfigMapKeyRefDefinition"]]
    FieldRef: Optional[Sequence["_FieldRefDefinition"]]
    ResourceFieldRef: Optional[Sequence["_ResourceFieldRefDefinition"]]
    SecretKeyRef: Optional[Sequence["_SecretKeyRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueFromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueFromDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigMapKeyRef=deserialize_list(json_data.get("ConfigMapKeyRef"), ConfigMapKeyRefDefinition),
            FieldRef=deserialize_list(json_data.get("FieldRef"), FieldRefDefinition),
            ResourceFieldRef=deserialize_list(json_data.get("ResourceFieldRef"), ResourceFieldRefDefinition),
            SecretKeyRef=deserialize_list(json_data.get("SecretKeyRef"), SecretKeyRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueFromDefinition = ValueFromDefinition


@dataclass
class ConfigMapKeyRefDefinition(BaseModel):
    Key: Optional[str]
    Name: Optional[str]
    Optional: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapKeyRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapKeyRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Optional=json_data.get("Optional"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapKeyRefDefinition = ConfigMapKeyRefDefinition


@dataclass
class FieldRefDefinition(BaseModel):
    ApiVersion: Optional[str]
    FieldPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldRefDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiVersion=json_data.get("ApiVersion"),
            FieldPath=json_data.get("FieldPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldRefDefinition = FieldRefDefinition


@dataclass
class ResourceFieldRefDefinition(BaseModel):
    ContainerName: Optional[str]
    Divisor: Optional[str]
    Resource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceFieldRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceFieldRefDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Divisor=json_data.get("Divisor"),
            Resource=json_data.get("Resource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceFieldRefDefinition = ResourceFieldRefDefinition


@dataclass
class SecretKeyRefDefinition(BaseModel):
    Key: Optional[str]
    Name: Optional[str]
    Optional: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SecretKeyRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretKeyRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Optional=json_data.get("Optional"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretKeyRefDefinition = SecretKeyRefDefinition


@dataclass
class EnvFromDefinition(BaseModel):
    Prefix: Optional[str]
    ConfigMapRef: Optional[Sequence["_ConfigMapRefDefinition"]]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvFromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvFromDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            ConfigMapRef=deserialize_list(json_data.get("ConfigMapRef"), ConfigMapRefDefinition),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvFromDefinition = EnvFromDefinition


@dataclass
class ConfigMapRefDefinition(BaseModel):
    Name: Optional[str]
    Optional: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Optional=json_data.get("Optional"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapRefDefinition = ConfigMapRefDefinition


@dataclass
class SecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRefDefinition = SecretRefDefinition


@dataclass
class LifecycleDefinition(BaseModel):
    PostStart: Optional[Sequence["_PostStartDefinition"]]
    PreStop: Optional[Sequence["_PreStopDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleDefinition"]:
        if not json_data:
            return None
        return cls(
            PostStart=deserialize_list(json_data.get("PostStart"), PostStartDefinition),
            PreStop=deserialize_list(json_data.get("PreStop"), PreStopDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleDefinition = LifecycleDefinition


@dataclass
class PostStartDefinition(BaseModel):
    Exec: Optional[Sequence["_ExecDefinition"]]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PostStartDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostStartDefinition"]:
        if not json_data:
            return None
        return cls(
            Exec=deserialize_list(json_data.get("Exec"), ExecDefinition),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostStartDefinition = PostStartDefinition


@dataclass
class ExecDefinition(BaseModel):
    Command: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ExecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecDefinition"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecDefinition = ExecDefinition


@dataclass
class HttpGetDefinition(BaseModel):
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[str]
    Scheme: Optional[str]
    HttpHeader: Optional[Sequence["_HttpHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGetDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Scheme=json_data.get("Scheme"),
            HttpHeader=deserialize_list(json_data.get("HttpHeader"), HttpHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGetDefinition = HttpGetDefinition


@dataclass
class HttpHeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderDefinition = HttpHeaderDefinition


@dataclass
class TcpSocketDefinition(BaseModel):
    Port: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpSocketDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpSocketDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpSocketDefinition = TcpSocketDefinition


@dataclass
class PreStopDefinition(BaseModel):
    Exec: Optional[Sequence["_ExecDefinition"]]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreStopDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreStopDefinition"]:
        if not json_data:
            return None
        return cls(
            Exec=deserialize_list(json_data.get("Exec"), ExecDefinition),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreStopDefinition = PreStopDefinition


@dataclass
class LivenessProbeDefinition(BaseModel):
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    Exec: Optional[Sequence["_ExecDefinition"]]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Exec=deserialize_list(json_data.get("Exec"), ExecDefinition),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessProbeDefinition = LivenessProbeDefinition


@dataclass
class PortDefinition(BaseModel):
    ContainerPort: Optional[float]
    HostIp: Optional[str]
    HostPort: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerPort=json_data.get("ContainerPort"),
            HostIp=json_data.get("HostIp"),
            HostPort=json_data.get("HostPort"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


@dataclass
class ReadinessProbeDefinition(BaseModel):
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    Exec: Optional[Sequence["_ExecDefinition"]]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Exec=deserialize_list(json_data.get("Exec"), ExecDefinition),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessProbeDefinition = ReadinessProbeDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Limits: Optional[Sequence["_LimitsDefinition"]]
    Requests: Optional[Sequence["_RequestsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Limits=deserialize_list(json_data.get("Limits"), LimitsDefinition),
            Requests=deserialize_list(json_data.get("Requests"), RequestsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class LimitsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitsDefinition = LimitsDefinition


@dataclass
class RequestsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestsDefinition = RequestsDefinition


@dataclass
class SecurityContextDefinition(BaseModel):
    AllowPrivilegeEscalation: Optional[bool]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]
    RunAsGroup: Optional[str]
    RunAsNonRoot: Optional[bool]
    RunAsUser: Optional[str]
    Capabilities: Optional[Sequence["_CapabilitiesDefinition"]]
    SeLinuxOptions: Optional[Sequence["_SeLinuxOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowPrivilegeEscalation=json_data.get("AllowPrivilegeEscalation"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
            RunAsGroup=json_data.get("RunAsGroup"),
            RunAsNonRoot=json_data.get("RunAsNonRoot"),
            RunAsUser=json_data.get("RunAsUser"),
            Capabilities=deserialize_list(json_data.get("Capabilities"), CapabilitiesDefinition),
            SeLinuxOptions=deserialize_list(json_data.get("SeLinuxOptions"), SeLinuxOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityContextDefinition = SecurityContextDefinition


@dataclass
class CapabilitiesDefinition(BaseModel):
    Add: Optional[Sequence[str]]
    Drop: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Add=json_data.get("Add"),
            Drop=json_data.get("Drop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapabilitiesDefinition = CapabilitiesDefinition


@dataclass
class SeLinuxOptionsDefinition(BaseModel):
    Level: Optional[str]
    Role: Optional[str]
    Type: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Role=json_data.get("Role"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxOptionsDefinition = SeLinuxOptionsDefinition


@dataclass
class StartupProbeDefinition(BaseModel):
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    Exec: Optional[Sequence["_ExecDefinition"]]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]
    TcpSocket: Optional[Sequence["_TcpSocketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StartupProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartupProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Exec=deserialize_list(json_data.get("Exec"), ExecDefinition),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
            TcpSocket=deserialize_list(json_data.get("TcpSocket"), TcpSocketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartupProbeDefinition = StartupProbeDefinition


@dataclass
class VolumeMountDefinition(BaseModel):
    MountPath: Optional[str]
    MountPropagation: Optional[str]
    Name: Optional[str]
    ReadOnly: Optional[bool]
    SubPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeMountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeMountDefinition"]:
        if not json_data:
            return None
        return cls(
            MountPath=json_data.get("MountPath"),
            MountPropagation=json_data.get("MountPropagation"),
            Name=json_data.get("Name"),
            ReadOnly=json_data.get("ReadOnly"),
            SubPath=json_data.get("SubPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeMountDefinition = VolumeMountDefinition


@dataclass
class DnsConfigDefinition(BaseModel):
    Nameservers: Optional[Sequence[str]]
    Searches: Optional[Sequence[str]]
    Option: Optional[Sequence["_OptionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Nameservers=json_data.get("Nameservers"),
            Searches=json_data.get("Searches"),
            Option=deserialize_list(json_data.get("Option"), OptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigDefinition = DnsConfigDefinition


@dataclass
class OptionDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionDefinition = OptionDefinition


@dataclass
class HostAliasesDefinition(BaseModel):
    Hostnames: Optional[Sequence[str]]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostAliasesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostAliasesDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostnames=json_data.get("Hostnames"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostAliasesDefinition = HostAliasesDefinition


@dataclass
class ImagePullSecretsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImagePullSecretsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImagePullSecretsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImagePullSecretsDefinition = ImagePullSecretsDefinition


@dataclass
class InitContainerDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Name: Optional[str]
    Stdin: Optional[bool]
    StdinOnce: Optional[bool]
    TerminationMessagePath: Optional[str]
    TerminationMessagePolicy: Optional[str]
    Tty: Optional[bool]
    WorkingDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    EnvFrom: Optional[Sequence["_EnvFromDefinition"]]
    Lifecycle: Optional[Sequence["_LifecycleDefinition"]]
    LivenessProbe: Optional[Sequence["_LivenessProbeDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbeDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]
    SecurityContext: Optional[Sequence["_SecurityContextDefinition"]]
    StartupProbe: Optional[Sequence["_StartupProbeDefinition"]]
    VolumeMount: Optional[Sequence["_VolumeMountDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InitContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Command=json_data.get("Command"),
            Image=json_data.get("Image"),
            ImagePullPolicy=json_data.get("ImagePullPolicy"),
            Name=json_data.get("Name"),
            Stdin=json_data.get("Stdin"),
            StdinOnce=json_data.get("StdinOnce"),
            TerminationMessagePath=json_data.get("TerminationMessagePath"),
            TerminationMessagePolicy=json_data.get("TerminationMessagePolicy"),
            Tty=json_data.get("Tty"),
            WorkingDir=json_data.get("WorkingDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            EnvFrom=deserialize_list(json_data.get("EnvFrom"), EnvFromDefinition),
            Lifecycle=deserialize_list(json_data.get("Lifecycle"), LifecycleDefinition),
            LivenessProbe=deserialize_list(json_data.get("LivenessProbe"), LivenessProbeDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            ReadinessProbe=deserialize_list(json_data.get("ReadinessProbe"), ReadinessProbeDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
            SecurityContext=deserialize_list(json_data.get("SecurityContext"), SecurityContextDefinition),
            StartupProbe=deserialize_list(json_data.get("StartupProbe"), StartupProbeDefinition),
            VolumeMount=deserialize_list(json_data.get("VolumeMount"), VolumeMountDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitContainerDefinition = InitContainerDefinition


@dataclass
class ReadinessGateDefinition(BaseModel):
    ConditionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessGateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessGateDefinition"]:
        if not json_data:
            return None
        return cls(
            ConditionType=json_data.get("ConditionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessGateDefinition = ReadinessGateDefinition


@dataclass
class TolerationDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Operator: Optional[str]
    TolerationSeconds: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TolerationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TolerationDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            TolerationSeconds=json_data.get("TolerationSeconds"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TolerationDefinition = TolerationDefinition


@dataclass
class TopologySpreadConstraintDefinition(BaseModel):
    MaxSkew: Optional[float]
    TopologyKey: Optional[str]
    WhenUnsatisfiable: Optional[str]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TopologySpreadConstraintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopologySpreadConstraintDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSkew=json_data.get("MaxSkew"),
            TopologyKey=json_data.get("TopologyKey"),
            WhenUnsatisfiable=json_data.get("WhenUnsatisfiable"),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopologySpreadConstraintDefinition = TopologySpreadConstraintDefinition


@dataclass
class VolumeDefinition(BaseModel):
    Name: Optional[str]
    AwsElasticBlockStore: Optional[Sequence["_AwsElasticBlockStoreDefinition"]]
    AzureDisk: Optional[Sequence["_AzureDiskDefinition"]]
    AzureFile: Optional[Sequence["_AzureFileDefinition"]]
    CephFs: Optional[Sequence["_CephFsDefinition"]]
    Cinder: Optional[Sequence["_CinderDefinition"]]
    ConfigMap: Optional[Sequence["_ConfigMapDefinition"]]
    Csi: Optional[Sequence["_CsiDefinition"]]
    DownwardApi: Optional[Sequence["_DownwardApiDefinition"]]
    EmptyDir: Optional[Sequence["_EmptyDirDefinition"]]
    Fc: Optional[Sequence["_FcDefinition"]]
    FlexVolume: Optional[Sequence["_FlexVolumeDefinition"]]
    Flocker: Optional[Sequence["_FlockerDefinition"]]
    GcePersistentDisk: Optional[Sequence["_GcePersistentDiskDefinition"]]
    GitRepo: Optional[Sequence["_GitRepoDefinition"]]
    Glusterfs: Optional[Sequence["_GlusterfsDefinition"]]
    HostPath: Optional[Sequence["_HostPathDefinition"]]
    Iscsi: Optional[Sequence["_IscsiDefinition"]]
    Local: Optional[Sequence["_LocalDefinition"]]
    Nfs: Optional[Sequence["_NfsDefinition"]]
    PersistentVolumeClaim: Optional[Sequence["_PersistentVolumeClaimDefinition"]]
    PhotonPersistentDisk: Optional[Sequence["_PhotonPersistentDiskDefinition"]]
    Projected: Optional[Sequence["_ProjectedDefinition"]]
    Quobyte: Optional[Sequence["_QuobyteDefinition"]]
    Rbd: Optional[Sequence["_RbdDefinition"]]
    Secret: Optional[Sequence["_SecretDefinition"]]
    VsphereVolume: Optional[Sequence["_VsphereVolumeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            AwsElasticBlockStore=deserialize_list(json_data.get("AwsElasticBlockStore"), AwsElasticBlockStoreDefinition),
            AzureDisk=deserialize_list(json_data.get("AzureDisk"), AzureDiskDefinition),
            AzureFile=deserialize_list(json_data.get("AzureFile"), AzureFileDefinition),
            CephFs=deserialize_list(json_data.get("CephFs"), CephFsDefinition),
            Cinder=deserialize_list(json_data.get("Cinder"), CinderDefinition),
            ConfigMap=deserialize_list(json_data.get("ConfigMap"), ConfigMapDefinition),
            Csi=deserialize_list(json_data.get("Csi"), CsiDefinition),
            DownwardApi=deserialize_list(json_data.get("DownwardApi"), DownwardApiDefinition),
            EmptyDir=deserialize_list(json_data.get("EmptyDir"), EmptyDirDefinition),
            Fc=deserialize_list(json_data.get("Fc"), FcDefinition),
            FlexVolume=deserialize_list(json_data.get("FlexVolume"), FlexVolumeDefinition),
            Flocker=deserialize_list(json_data.get("Flocker"), FlockerDefinition),
            GcePersistentDisk=deserialize_list(json_data.get("GcePersistentDisk"), GcePersistentDiskDefinition),
            GitRepo=deserialize_list(json_data.get("GitRepo"), GitRepoDefinition),
            Glusterfs=deserialize_list(json_data.get("Glusterfs"), GlusterfsDefinition),
            HostPath=deserialize_list(json_data.get("HostPath"), HostPathDefinition),
            Iscsi=deserialize_list(json_data.get("Iscsi"), IscsiDefinition),
            Local=deserialize_list(json_data.get("Local"), LocalDefinition),
            Nfs=deserialize_list(json_data.get("Nfs"), NfsDefinition),
            PersistentVolumeClaim=deserialize_list(json_data.get("PersistentVolumeClaim"), PersistentVolumeClaimDefinition),
            PhotonPersistentDisk=deserialize_list(json_data.get("PhotonPersistentDisk"), PhotonPersistentDiskDefinition),
            Projected=deserialize_list(json_data.get("Projected"), ProjectedDefinition),
            Quobyte=deserialize_list(json_data.get("Quobyte"), QuobyteDefinition),
            Rbd=deserialize_list(json_data.get("Rbd"), RbdDefinition),
            Secret=deserialize_list(json_data.get("Secret"), SecretDefinition),
            VsphereVolume=deserialize_list(json_data.get("VsphereVolume"), VsphereVolumeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeDefinition = VolumeDefinition


@dataclass
class AwsElasticBlockStoreDefinition(BaseModel):
    FsType: Optional[str]
    Partition: Optional[float]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticBlockStoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticBlockStoreDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticBlockStoreDefinition = AwsElasticBlockStoreDefinition


@dataclass
class AzureDiskDefinition(BaseModel):
    CachingMode: Optional[str]
    DataDiskUri: Optional[str]
    DiskName: Optional[str]
    FsType: Optional[str]
    Kind: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            CachingMode=json_data.get("CachingMode"),
            DataDiskUri=json_data.get("DataDiskUri"),
            DiskName=json_data.get("DiskName"),
            FsType=json_data.get("FsType"),
            Kind=json_data.get("Kind"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDiskDefinition = AzureDiskDefinition


@dataclass
class AzureFileDefinition(BaseModel):
    ReadOnly: Optional[bool]
    SecretName: Optional[str]
    SecretNamespace: Optional[str]
    ShareName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFileDefinition"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SecretName=json_data.get("SecretName"),
            SecretNamespace=json_data.get("SecretNamespace"),
            ShareName=json_data.get("ShareName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFileDefinition = AzureFileDefinition


@dataclass
class CephFsDefinition(BaseModel):
    Monitors: Optional[Sequence[str]]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    SecretFile: Optional[str]
    User: Optional[str]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CephFsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CephFsDefinition"]:
        if not json_data:
            return None
        return cls(
            Monitors=json_data.get("Monitors"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretFile=json_data.get("SecretFile"),
            User=json_data.get("User"),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CephFsDefinition = CephFsDefinition


@dataclass
class CinderDefinition(BaseModel):
    FsType: Optional[str]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CinderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CinderDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CinderDefinition = CinderDefinition


@dataclass
class ConfigMapDefinition(BaseModel):
    Name: Optional[str]
    Optional: Optional[bool]
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Optional=json_data.get("Optional"),
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapDefinition = ConfigMapDefinition


@dataclass
class ItemsDefinition(BaseModel):
    Key: Optional[str]
    Mode: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ItemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Mode=json_data.get("Mode"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemsDefinition = ItemsDefinition


@dataclass
class CsiDefinition(BaseModel):
    Driver: Optional[str]
    FsType: Optional[str]
    ReadOnly: Optional[bool]
    VolumeAttributes: Optional[Sequence["_VolumeAttributesDefinition"]]
    VolumeHandle: Optional[str]
    ControllerExpandSecretRef: Optional[Sequence["_ControllerExpandSecretRefDefinition"]]
    ControllerPublishSecretRef: Optional[Sequence["_ControllerPublishSecretRefDefinition"]]
    NodePublishSecretRef: Optional[Sequence["_NodePublishSecretRefDefinition"]]
    NodeStageSecretRef: Optional[Sequence["_NodeStageSecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CsiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsiDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeAttributes=deserialize_list(json_data.get("VolumeAttributes"), VolumeAttributesDefinition),
            VolumeHandle=json_data.get("VolumeHandle"),
            ControllerExpandSecretRef=deserialize_list(json_data.get("ControllerExpandSecretRef"), ControllerExpandSecretRefDefinition),
            ControllerPublishSecretRef=deserialize_list(json_data.get("ControllerPublishSecretRef"), ControllerPublishSecretRefDefinition),
            NodePublishSecretRef=deserialize_list(json_data.get("NodePublishSecretRef"), NodePublishSecretRefDefinition),
            NodeStageSecretRef=deserialize_list(json_data.get("NodeStageSecretRef"), NodeStageSecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsiDefinition = CsiDefinition


@dataclass
class VolumeAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeAttributesDefinition = VolumeAttributesDefinition


@dataclass
class ControllerExpandSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerExpandSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerExpandSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerExpandSecretRefDefinition = ControllerExpandSecretRefDefinition


@dataclass
class ControllerPublishSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerPublishSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerPublishSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerPublishSecretRefDefinition = ControllerPublishSecretRefDefinition


@dataclass
class NodePublishSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodePublishSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePublishSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePublishSecretRefDefinition = NodePublishSecretRefDefinition


@dataclass
class NodeStageSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeStageSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeStageSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeStageSecretRefDefinition = NodeStageSecretRefDefinition


@dataclass
class DownwardApiDefinition(BaseModel):
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DownwardApiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DownwardApiDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DownwardApiDefinition = DownwardApiDefinition


@dataclass
class EmptyDirDefinition(BaseModel):
    Medium: Optional[str]
    SizeLimit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmptyDirDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmptyDirDefinition"]:
        if not json_data:
            return None
        return cls(
            Medium=json_data.get("Medium"),
            SizeLimit=json_data.get("SizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmptyDirDefinition = EmptyDirDefinition


@dataclass
class FcDefinition(BaseModel):
    FsType: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetWwNs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FcDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Lun=json_data.get("Lun"),
            ReadOnly=json_data.get("ReadOnly"),
            TargetWwNs=json_data.get("TargetWwNs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FcDefinition = FcDefinition


@dataclass
class FlexVolumeDefinition(BaseModel):
    Driver: Optional[str]
    FsType: Optional[str]
    Options: Optional[Sequence["_OptionsDefinition"]]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlexVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlexVolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            FsType=json_data.get("FsType"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            ReadOnly=json_data.get("ReadOnly"),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlexVolumeDefinition = FlexVolumeDefinition


@dataclass
class OptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class FlockerDefinition(BaseModel):
    DatasetName: Optional[str]
    DatasetUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FlockerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlockerDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetName=json_data.get("DatasetName"),
            DatasetUuid=json_data.get("DatasetUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlockerDefinition = FlockerDefinition


@dataclass
class GcePersistentDiskDefinition(BaseModel):
    FsType: Optional[str]
    Partition: Optional[float]
    PdName: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GcePersistentDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcePersistentDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            PdName=json_data.get("PdName"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcePersistentDiskDefinition = GcePersistentDiskDefinition


@dataclass
class GitRepoDefinition(BaseModel):
    Directory: Optional[str]
    Repository: Optional[str]
    Revision: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitRepoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitRepoDefinition"]:
        if not json_data:
            return None
        return cls(
            Directory=json_data.get("Directory"),
            Repository=json_data.get("Repository"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitRepoDefinition = GitRepoDefinition


@dataclass
class GlusterfsDefinition(BaseModel):
    EndpointsName: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GlusterfsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlusterfsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointsName=json_data.get("EndpointsName"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlusterfsDefinition = GlusterfsDefinition


@dataclass
class HostPathDefinition(BaseModel):
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostPathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostPathDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostPathDefinition = HostPathDefinition


@dataclass
class IscsiDefinition(BaseModel):
    FsType: Optional[str]
    Iqn: Optional[str]
    IscsiInterface: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetPortal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IscsiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IscsiDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Iqn=json_data.get("Iqn"),
            IscsiInterface=json_data.get("IscsiInterface"),
            Lun=json_data.get("Lun"),
            ReadOnly=json_data.get("ReadOnly"),
            TargetPortal=json_data.get("TargetPortal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IscsiDefinition = IscsiDefinition


@dataclass
class LocalDefinition(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalDefinition = LocalDefinition


@dataclass
class NfsDefinition(BaseModel):
    Path: Optional[str]
    ReadOnly: Optional[bool]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NfsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NfsDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NfsDefinition = NfsDefinition


@dataclass
class PersistentVolumeClaimDefinition(BaseModel):
    ClaimName: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PersistentVolumeClaimDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PersistentVolumeClaimDefinition"]:
        if not json_data:
            return None
        return cls(
            ClaimName=json_data.get("ClaimName"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PersistentVolumeClaimDefinition = PersistentVolumeClaimDefinition


@dataclass
class PhotonPersistentDiskDefinition(BaseModel):
    FsType: Optional[str]
    PdId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhotonPersistentDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhotonPersistentDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            PdId=json_data.get("PdId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhotonPersistentDiskDefinition = PhotonPersistentDiskDefinition


@dataclass
class ProjectedDefinition(BaseModel):
    DefaultMode: Optional[str]
    Sources: Optional[Sequence["_SourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectedDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultMode=json_data.get("DefaultMode"),
            Sources=deserialize_list(json_data.get("Sources"), SourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectedDefinition = ProjectedDefinition


@dataclass
class SourcesDefinition(BaseModel):
    ConfigMap: Optional[Sequence["_ConfigMapDefinition"]]
    DownwardApi: Optional[Sequence["_DownwardApiDefinition"]]
    Secret: Optional[Sequence["_SecretDefinition"]]
    ServiceAccountToken: Optional[Sequence["_ServiceAccountTokenDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigMap=deserialize_list(json_data.get("ConfigMap"), ConfigMapDefinition),
            DownwardApi=deserialize_list(json_data.get("DownwardApi"), DownwardApiDefinition),
            Secret=deserialize_list(json_data.get("Secret"), SecretDefinition),
            ServiceAccountToken=deserialize_list(json_data.get("ServiceAccountToken"), ServiceAccountTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcesDefinition = SourcesDefinition


@dataclass
class SecretDefinition(BaseModel):
    Name: Optional[str]
    Optional: Optional[bool]
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecretDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Optional=json_data.get("Optional"),
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretDefinition = SecretDefinition


@dataclass
class ServiceAccountTokenDefinition(BaseModel):
    Audience: Optional[str]
    ExpirationSeconds: Optional[float]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceAccountTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceAccountTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            ExpirationSeconds=json_data.get("ExpirationSeconds"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceAccountTokenDefinition = ServiceAccountTokenDefinition


@dataclass
class QuobyteDefinition(BaseModel):
    Group: Optional[str]
    ReadOnly: Optional[bool]
    Registry: Optional[str]
    User: Optional[str]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuobyteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuobyteDefinition"]:
        if not json_data:
            return None
        return cls(
            Group=json_data.get("Group"),
            ReadOnly=json_data.get("ReadOnly"),
            Registry=json_data.get("Registry"),
            User=json_data.get("User"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuobyteDefinition = QuobyteDefinition


@dataclass
class RbdDefinition(BaseModel):
    CephMonitors: Optional[Sequence[str]]
    FsType: Optional[str]
    Keyring: Optional[str]
    RadosUser: Optional[str]
    RbdImage: Optional[str]
    RbdPool: Optional[str]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RbdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RbdDefinition"]:
        if not json_data:
            return None
        return cls(
            CephMonitors=json_data.get("CephMonitors"),
            FsType=json_data.get("FsType"),
            Keyring=json_data.get("Keyring"),
            RadosUser=json_data.get("RadosUser"),
            RbdImage=json_data.get("RbdImage"),
            RbdPool=json_data.get("RbdPool"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RbdDefinition = RbdDefinition


@dataclass
class VsphereVolumeDefinition(BaseModel):
    FsType: Optional[str]
    VolumePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereVolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            VolumePath=json_data.get("VolumePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereVolumeDefinition = VsphereVolumeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


