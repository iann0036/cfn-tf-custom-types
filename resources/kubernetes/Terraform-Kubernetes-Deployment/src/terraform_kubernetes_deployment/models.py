# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]
    Timeouts: Optional["_Timeouts"]
    Selector: Optional[Sequence["_Selector"]]
    Strategy: Optional[Sequence["_Strategy"]]
    Template: Optional[Sequence["_Template"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]
    RollingUpdate: Optional[Sequence["_RollingUpdate"]]
    Affinity: Optional[Sequence["_Affinity"]]
    Container: Optional[Sequence["_Container"]]
    DnsConfig: Optional[Sequence["_DnsConfig"]]
    HostAliases: Optional[Sequence["_HostAliases"]]
    ImagePullSecrets: Optional[Sequence["_ImagePullSecrets"]]
    InitContainer: Optional[Sequence["_InitContainer"]]
    SecurityContext: Optional[Sequence["_SecurityContext"]]
    Toleration: Optional[Sequence["_Toleration"]]
    Volume: Optional[Sequence["_Volume"]]
    NodeAffinity: Optional[Sequence["_NodeAffinity"]]
    PodAffinity: Optional[Sequence["_PodAffinity"]]
    PodAntiAffinity: Optional[Sequence["_PodAntiAffinity"]]
    Env: Optional[Sequence["_Env"]]
    EnvFrom: Optional[Sequence["_EnvFrom"]]
    Lifecycle: Optional[Sequence["_Lifecycle"]]
    LivenessProbe: Optional[Sequence["_LivenessProbe"]]
    Port: Optional[Sequence["_Port"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbe"]]
    Resources: Optional[Sequence["_Resources"]]
    StartupProbe: Optional[Sequence["_StartupProbe"]]
    VolumeMount: Optional[Sequence["_VolumeMount"]]
    Option: Optional[Sequence["_Option"]]
    Capabilities: Optional[Sequence["_Capabilities"]]
    SeLinuxOptions: Optional[Sequence["_SeLinuxOptions"]]
    AwsElasticBlockStore: Optional[Sequence["_AwsElasticBlockStore"]]
    AzureDisk: Optional[Sequence["_AzureDisk"]]
    AzureFile: Optional[Sequence["_AzureFile"]]
    CephFs: Optional[Sequence["_CephFs"]]
    Cinder: Optional[Sequence["_Cinder"]]
    ConfigMap: Optional[Sequence["_ConfigMap"]]
    DownwardApi: Optional[Sequence["_DownwardApi"]]
    EmptyDir: Optional[Sequence["_EmptyDir"]]
    Fc: Optional[Sequence["_Fc"]]
    FlexVolume: Optional[Sequence["_FlexVolume"]]
    Flocker: Optional[Sequence["_Flocker"]]
    GcePersistentDisk: Optional[Sequence["_GcePersistentDisk"]]
    GitRepo: Optional[Sequence["_GitRepo"]]
    Glusterfs: Optional[Sequence["_Glusterfs"]]
    HostPath: Optional[Sequence["_HostPath"]]
    Iscsi: Optional[Sequence["_Iscsi"]]
    Local: Optional[Sequence["_Local"]]
    Nfs: Optional[Sequence["_Nfs"]]
    PersistentVolumeClaim: Optional[Sequence["_PersistentVolumeClaim"]]
    PhotonPersistentDisk: Optional[Sequence["_PhotonPersistentDisk"]]
    Quobyte: Optional[Sequence["_Quobyte"]]
    Rbd: Optional[Sequence["_Rbd"]]
    Secret: Optional[Sequence["_Secret"]]
    VsphereVolume: Optional[Sequence["_VsphereVolume"]]
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecution"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecution"]]
    ValueFrom: Optional[Sequence["_ValueFrom"]]
    ConfigMapRef: Optional[Sequence["_ConfigMapRef"]]
    SecretRef: Optional[Sequence["_SecretRef"]]
    PostStart: Optional[Sequence["_PostStart"]]
    PreStop: Optional[Sequence["_PreStop"]]
    Exec: Optional[Sequence["_Exec"]]
    HttpGet: Optional[Sequence["_HttpGet"]]
    TcpSocket: Optional[Sequence["_TcpSocket"]]
    Limits: Optional[Sequence["_Limits"]]
    Requests: Optional[Sequence["_Requests"]]
    Items: Optional[Sequence["_Items"]]
    PodAffinityTerm: Optional[Sequence["_PodAffinityTerm"]]
    LabelSelector: Optional[Sequence["_LabelSelector"]]
    ConfigMapKeyRef: Optional[Sequence["_ConfigMapKeyRef"]]
    FieldRef: Optional[Sequence["_FieldRef"]]
    ResourceFieldRef: Optional[Sequence["_ResourceFieldRef"]]
    SecretKeyRef: Optional[Sequence["_SecretKeyRef"]]
    HttpHeader: Optional[Sequence["_HttpHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Selector=json_data.get("Selector"),
            Strategy=json_data.get("Strategy"),
            Template=json_data.get("Template"),
            MatchExpressions=json_data.get("MatchExpressions"),
            RollingUpdate=json_data.get("RollingUpdate"),
            Affinity=json_data.get("Affinity"),
            Container=json_data.get("Container"),
            DnsConfig=json_data.get("DnsConfig"),
            HostAliases=json_data.get("HostAliases"),
            ImagePullSecrets=json_data.get("ImagePullSecrets"),
            InitContainer=json_data.get("InitContainer"),
            SecurityContext=json_data.get("SecurityContext"),
            Toleration=json_data.get("Toleration"),
            Volume=json_data.get("Volume"),
            NodeAffinity=json_data.get("NodeAffinity"),
            PodAffinity=json_data.get("PodAffinity"),
            PodAntiAffinity=json_data.get("PodAntiAffinity"),
            Env=json_data.get("Env"),
            EnvFrom=json_data.get("EnvFrom"),
            Lifecycle=json_data.get("Lifecycle"),
            LivenessProbe=json_data.get("LivenessProbe"),
            Port=json_data.get("Port"),
            ReadinessProbe=json_data.get("ReadinessProbe"),
            Resources=json_data.get("Resources"),
            StartupProbe=json_data.get("StartupProbe"),
            VolumeMount=json_data.get("VolumeMount"),
            Option=json_data.get("Option"),
            Capabilities=json_data.get("Capabilities"),
            SeLinuxOptions=json_data.get("SeLinuxOptions"),
            AwsElasticBlockStore=json_data.get("AwsElasticBlockStore"),
            AzureDisk=json_data.get("AzureDisk"),
            AzureFile=json_data.get("AzureFile"),
            CephFs=json_data.get("CephFs"),
            Cinder=json_data.get("Cinder"),
            ConfigMap=json_data.get("ConfigMap"),
            DownwardApi=json_data.get("DownwardApi"),
            EmptyDir=json_data.get("EmptyDir"),
            Fc=json_data.get("Fc"),
            FlexVolume=json_data.get("FlexVolume"),
            Flocker=json_data.get("Flocker"),
            GcePersistentDisk=json_data.get("GcePersistentDisk"),
            GitRepo=json_data.get("GitRepo"),
            Glusterfs=json_data.get("Glusterfs"),
            HostPath=json_data.get("HostPath"),
            Iscsi=json_data.get("Iscsi"),
            Local=json_data.get("Local"),
            Nfs=json_data.get("Nfs"),
            PersistentVolumeClaim=json_data.get("PersistentVolumeClaim"),
            PhotonPersistentDisk=json_data.get("PhotonPersistentDisk"),
            Quobyte=json_data.get("Quobyte"),
            Rbd=json_data.get("Rbd"),
            Secret=json_data.get("Secret"),
            VsphereVolume=json_data.get("VsphereVolume"),
            PreferredDuringSchedulingIgnoredDuringExecution=json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"),
            RequiredDuringSchedulingIgnoredDuringExecution=json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"),
            ValueFrom=json_data.get("ValueFrom"),
            ConfigMapRef=json_data.get("ConfigMapRef"),
            SecretRef=json_data.get("SecretRef"),
            PostStart=json_data.get("PostStart"),
            PreStop=json_data.get("PreStop"),
            Exec=json_data.get("Exec"),
            HttpGet=json_data.get("HttpGet"),
            TcpSocket=json_data.get("TcpSocket"),
            Limits=json_data.get("Limits"),
            Requests=json_data.get("Requests"),
            Items=json_data.get("Items"),
            PodAffinityTerm=json_data.get("PodAffinityTerm"),
            LabelSelector=json_data.get("LabelSelector"),
            ConfigMapKeyRef=json_data.get("ConfigMapKeyRef"),
            FieldRef=json_data.get("FieldRef"),
            ResourceFieldRef=json_data.get("ResourceFieldRef"),
            SecretKeyRef=json_data.get("SecretKeyRef"),
            HttpHeader=json_data.get("HttpHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Annotations: Optional[Sequence["_Annotations"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Annotations=json_data.get("Annotations"),
            GenerateName=json_data.get("GenerateName"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Annotations:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Spec:
    ActiveDeadlineSeconds: Optional[float]
    AutomountServiceAccountToken: Optional[bool]
    DnsPolicy: Optional[str]
    HostIpc: Optional[bool]
    HostNetwork: Optional[bool]
    HostPid: Optional[bool]
    Hostname: Optional[str]
    NodeName: Optional[str]
    NodeSelector: Optional[Sequence["_NodeSelector"]]
    PriorityClassName: Optional[str]
    RestartPolicy: Optional[str]
    ServiceAccountName: Optional[str]
    ShareProcessNamespace: Optional[bool]
    Subdomain: Optional[str]
    TerminationGracePeriodSeconds: Optional[float]
    Affinity: Optional[Sequence["_Affinity"]]
    Container: Optional[Sequence["_Container"]]
    DnsConfig: Optional[Sequence["_DnsConfig"]]
    HostAliases: Optional[Sequence["_HostAliases"]]
    ImagePullSecrets: Optional[Sequence["_ImagePullSecrets"]]
    InitContainer: Optional[Sequence["_InitContainer"]]
    SecurityContext: Optional[Sequence["_SecurityContext"]]
    Toleration: Optional[Sequence["_Toleration"]]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            ActiveDeadlineSeconds=json_data.get("ActiveDeadlineSeconds"),
            AutomountServiceAccountToken=json_data.get("AutomountServiceAccountToken"),
            DnsPolicy=json_data.get("DnsPolicy"),
            HostIpc=json_data.get("HostIpc"),
            HostNetwork=json_data.get("HostNetwork"),
            HostPid=json_data.get("HostPid"),
            Hostname=json_data.get("Hostname"),
            NodeName=json_data.get("NodeName"),
            NodeSelector=json_data.get("NodeSelector"),
            PriorityClassName=json_data.get("PriorityClassName"),
            RestartPolicy=json_data.get("RestartPolicy"),
            ServiceAccountName=json_data.get("ServiceAccountName"),
            ShareProcessNamespace=json_data.get("ShareProcessNamespace"),
            Subdomain=json_data.get("Subdomain"),
            TerminationGracePeriodSeconds=json_data.get("TerminationGracePeriodSeconds"),
            Affinity=json_data.get("Affinity"),
            Container=json_data.get("Container"),
            DnsConfig=json_data.get("DnsConfig"),
            HostAliases=json_data.get("HostAliases"),
            ImagePullSecrets=json_data.get("ImagePullSecrets"),
            InitContainer=json_data.get("InitContainer"),
            SecurityContext=json_data.get("SecurityContext"),
            Toleration=json_data.get("Toleration"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class NodeSelector:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelector"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelector = NodeSelector


@dataclass
class Affinity:
    NodeAffinity: Optional[Sequence["_NodeAffinity"]]
    PodAffinity: Optional[Sequence["_PodAffinity"]]
    PodAntiAffinity: Optional[Sequence["_PodAntiAffinity"]]

    @classmethod
    def _deserialize(
        cls: Type["_Affinity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Affinity"]:
        if not json_data:
            return None
        return cls(
            NodeAffinity=json_data.get("NodeAffinity"),
            PodAffinity=json_data.get("PodAffinity"),
            PodAntiAffinity=json_data.get("PodAntiAffinity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Affinity = Affinity


@dataclass
class NodeAffinity:
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecution"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecution"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinity"]:
        if not json_data:
            return None
        return cls(
            PreferredDuringSchedulingIgnoredDuringExecution=json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"),
            RequiredDuringSchedulingIgnoredDuringExecution=json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinity = NodeAffinity


@dataclass
class PreferredDuringSchedulingIgnoredDuringExecution:
    Weight: Optional[float]
    PodAffinityTerm: Optional[Sequence["_PodAffinityTerm"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreferredDuringSchedulingIgnoredDuringExecution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreferredDuringSchedulingIgnoredDuringExecution"]:
        if not json_data:
            return None
        return cls(
            Weight=json_data.get("Weight"),
            PodAffinityTerm=json_data.get("PodAffinityTerm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreferredDuringSchedulingIgnoredDuringExecution = PreferredDuringSchedulingIgnoredDuringExecution


@dataclass
class PodAffinityTerm:
    Namespaces: Optional[Sequence[str]]
    TopologyKey: Optional[str]
    LabelSelector: Optional[Sequence["_LabelSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodAffinityTerm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodAffinityTerm"]:
        if not json_data:
            return None
        return cls(
            Namespaces=json_data.get("Namespaces"),
            TopologyKey=json_data.get("TopologyKey"),
            LabelSelector=json_data.get("LabelSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodAffinityTerm = PodAffinityTerm


@dataclass
class LabelSelector:
    MatchLabels: Optional[Sequence["_MatchLabels"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]

    @classmethod
    def _deserialize(
        cls: Type["_LabelSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelSelector"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=json_data.get("MatchLabels"),
            MatchExpressions=json_data.get("MatchExpressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelSelector = LabelSelector


@dataclass
class MatchLabels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabels = MatchLabels


@dataclass
class MatchExpressions:
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressions = MatchExpressions


@dataclass
class RequiredDuringSchedulingIgnoredDuringExecution:
    Namespaces: Optional[Sequence[str]]
    TopologyKey: Optional[str]
    LabelSelector: Optional[Sequence["_LabelSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredDuringSchedulingIgnoredDuringExecution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredDuringSchedulingIgnoredDuringExecution"]:
        if not json_data:
            return None
        return cls(
            Namespaces=json_data.get("Namespaces"),
            TopologyKey=json_data.get("TopologyKey"),
            LabelSelector=json_data.get("LabelSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredDuringSchedulingIgnoredDuringExecution = RequiredDuringSchedulingIgnoredDuringExecution


@dataclass
class PodAffinity:
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecution"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecution"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodAffinity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodAffinity"]:
        if not json_data:
            return None
        return cls(
            PreferredDuringSchedulingIgnoredDuringExecution=json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"),
            RequiredDuringSchedulingIgnoredDuringExecution=json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodAffinity = PodAffinity


@dataclass
class PodAntiAffinity:
    PreferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_PreferredDuringSchedulingIgnoredDuringExecution"]]
    RequiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence["_RequiredDuringSchedulingIgnoredDuringExecution"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodAntiAffinity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodAntiAffinity"]:
        if not json_data:
            return None
        return cls(
            PreferredDuringSchedulingIgnoredDuringExecution=json_data.get("PreferredDuringSchedulingIgnoredDuringExecution"),
            RequiredDuringSchedulingIgnoredDuringExecution=json_data.get("RequiredDuringSchedulingIgnoredDuringExecution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodAntiAffinity = PodAntiAffinity


@dataclass
class Container:
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Name: Optional[str]
    Stdin: Optional[bool]
    StdinOnce: Optional[bool]
    TerminationMessagePath: Optional[str]
    Tty: Optional[bool]
    WorkingDir: Optional[str]
    Env: Optional[Sequence["_Env"]]
    EnvFrom: Optional[Sequence["_EnvFrom"]]
    Lifecycle: Optional[Sequence["_Lifecycle"]]
    LivenessProbe: Optional[Sequence["_LivenessProbe"]]
    Port: Optional[Sequence["_Port"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbe"]]
    Resources: Optional[Sequence["_Resources"]]
    SecurityContext: Optional[Sequence["_SecurityContext"]]
    StartupProbe: Optional[Sequence["_StartupProbe"]]
    VolumeMount: Optional[Sequence["_VolumeMount"]]

    @classmethod
    def _deserialize(
        cls: Type["_Container"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Container"]:
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
            Tty=json_data.get("Tty"),
            WorkingDir=json_data.get("WorkingDir"),
            Env=json_data.get("Env"),
            EnvFrom=json_data.get("EnvFrom"),
            Lifecycle=json_data.get("Lifecycle"),
            LivenessProbe=json_data.get("LivenessProbe"),
            Port=json_data.get("Port"),
            ReadinessProbe=json_data.get("ReadinessProbe"),
            Resources=json_data.get("Resources"),
            SecurityContext=json_data.get("SecurityContext"),
            StartupProbe=json_data.get("StartupProbe"),
            VolumeMount=json_data.get("VolumeMount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Container = Container


@dataclass
class Env:
    Name: Optional[str]
    Value: Optional[str]
    ValueFrom: Optional[Sequence["_ValueFrom"]]

    @classmethod
    def _deserialize(
        cls: Type["_Env"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Env"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
            ValueFrom=json_data.get("ValueFrom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Env = Env


@dataclass
class ValueFrom:
    ConfigMapKeyRef: Optional[Sequence["_ConfigMapKeyRef"]]
    FieldRef: Optional[Sequence["_FieldRef"]]
    ResourceFieldRef: Optional[Sequence["_ResourceFieldRef"]]
    SecretKeyRef: Optional[Sequence["_SecretKeyRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueFrom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueFrom"]:
        if not json_data:
            return None
        return cls(
            ConfigMapKeyRef=json_data.get("ConfigMapKeyRef"),
            FieldRef=json_data.get("FieldRef"),
            ResourceFieldRef=json_data.get("ResourceFieldRef"),
            SecretKeyRef=json_data.get("SecretKeyRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueFrom = ValueFrom


@dataclass
class ConfigMapKeyRef:
    Key: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapKeyRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapKeyRef"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapKeyRef = ConfigMapKeyRef


@dataclass
class FieldRef:
    ApiVersion: Optional[str]
    FieldPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldRef"]:
        if not json_data:
            return None
        return cls(
            ApiVersion=json_data.get("ApiVersion"),
            FieldPath=json_data.get("FieldPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldRef = FieldRef


@dataclass
class ResourceFieldRef:
    ContainerName: Optional[str]
    Resource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceFieldRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceFieldRef"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Resource=json_data.get("Resource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceFieldRef = ResourceFieldRef


@dataclass
class SecretKeyRef:
    Key: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretKeyRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretKeyRef"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretKeyRef = SecretKeyRef


@dataclass
class EnvFrom:
    Prefix: Optional[str]
    ConfigMapRef: Optional[Sequence["_ConfigMapRef"]]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvFrom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvFrom"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            ConfigMapRef=json_data.get("ConfigMapRef"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvFrom = EnvFrom


@dataclass
class ConfigMapRef:
    Name: Optional[str]
    Optional: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapRef"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Optional=json_data.get("Optional"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapRef = ConfigMapRef


@dataclass
class SecretRef:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRef"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRef = SecretRef


@dataclass
class Lifecycle:
    PostStart: Optional[Sequence["_PostStart"]]
    PreStop: Optional[Sequence["_PreStop"]]

    @classmethod
    def _deserialize(
        cls: Type["_Lifecycle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lifecycle"]:
        if not json_data:
            return None
        return cls(
            PostStart=json_data.get("PostStart"),
            PreStop=json_data.get("PreStop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lifecycle = Lifecycle


@dataclass
class PostStart:
    Exec: Optional[Sequence["_Exec"]]
    HttpGet: Optional[Sequence["_HttpGet"]]
    TcpSocket: Optional[Sequence["_TcpSocket"]]

    @classmethod
    def _deserialize(
        cls: Type["_PostStart"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostStart"]:
        if not json_data:
            return None
        return cls(
            Exec=json_data.get("Exec"),
            HttpGet=json_data.get("HttpGet"),
            TcpSocket=json_data.get("TcpSocket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostStart = PostStart


@dataclass
class Exec:
    Command: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Exec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Exec"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Exec = Exec


@dataclass
class HttpGet:
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[str]
    Scheme: Optional[str]
    HttpHeader: Optional[Sequence["_HttpHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGet"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Scheme=json_data.get("Scheme"),
            HttpHeader=json_data.get("HttpHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGet = HttpGet


@dataclass
class HttpHeader:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeader = HttpHeader


@dataclass
class TcpSocket:
    Port: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpSocket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpSocket"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpSocket = TcpSocket


@dataclass
class PreStop:
    Exec: Optional[Sequence["_Exec"]]
    HttpGet: Optional[Sequence["_HttpGet"]]
    TcpSocket: Optional[Sequence["_TcpSocket"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreStop"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreStop"]:
        if not json_data:
            return None
        return cls(
            Exec=json_data.get("Exec"),
            HttpGet=json_data.get("HttpGet"),
            TcpSocket=json_data.get("TcpSocket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreStop = PreStop


@dataclass
class LivenessProbe:
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    Exec: Optional[Sequence["_Exec"]]
    HttpGet: Optional[Sequence["_HttpGet"]]
    TcpSocket: Optional[Sequence["_TcpSocket"]]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessProbe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessProbe"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Exec=json_data.get("Exec"),
            HttpGet=json_data.get("HttpGet"),
            TcpSocket=json_data.get("TcpSocket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessProbe = LivenessProbe


@dataclass
class Port:
    ContainerPort: Optional[float]
    HostIp: Optional[str]
    HostPort: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Port"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Port"]:
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
_Port = Port


@dataclass
class ReadinessProbe:
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    Exec: Optional[Sequence["_Exec"]]
    HttpGet: Optional[Sequence["_HttpGet"]]
    TcpSocket: Optional[Sequence["_TcpSocket"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessProbe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessProbe"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Exec=json_data.get("Exec"),
            HttpGet=json_data.get("HttpGet"),
            TcpSocket=json_data.get("TcpSocket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessProbe = ReadinessProbe


@dataclass
class Resources:
    Limits: Optional[Sequence["_Limits"]]
    Requests: Optional[Sequence["_Requests"]]

    @classmethod
    def _deserialize(
        cls: Type["_Resources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resources"]:
        if not json_data:
            return None
        return cls(
            Limits=json_data.get("Limits"),
            Requests=json_data.get("Requests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resources = Resources


@dataclass
class Limits:
    Cpu: Optional[str]
    Memory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class Requests:
    Cpu: Optional[str]
    Memory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Requests"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Requests"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Requests = Requests


@dataclass
class SecurityContext:
    AllowPrivilegeEscalation: Optional[bool]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]
    RunAsGroup: Optional[float]
    RunAsNonRoot: Optional[bool]
    RunAsUser: Optional[float]
    Capabilities: Optional[Sequence["_Capabilities"]]
    SeLinuxOptions: Optional[Sequence["_SeLinuxOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityContext"]:
        if not json_data:
            return None
        return cls(
            AllowPrivilegeEscalation=json_data.get("AllowPrivilegeEscalation"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
            RunAsGroup=json_data.get("RunAsGroup"),
            RunAsNonRoot=json_data.get("RunAsNonRoot"),
            RunAsUser=json_data.get("RunAsUser"),
            Capabilities=json_data.get("Capabilities"),
            SeLinuxOptions=json_data.get("SeLinuxOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityContext = SecurityContext


@dataclass
class Capabilities:
    Add: Optional[Sequence[str]]
    Drop: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Capabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capabilities"]:
        if not json_data:
            return None
        return cls(
            Add=json_data.get("Add"),
            Drop=json_data.get("Drop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capabilities = Capabilities


@dataclass
class SeLinuxOptions:
    Level: Optional[str]
    Role: Optional[str]
    Type: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxOptions"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Role=json_data.get("Role"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxOptions = SeLinuxOptions


@dataclass
class StartupProbe:
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    Exec: Optional[Sequence["_Exec"]]
    HttpGet: Optional[Sequence["_HttpGet"]]
    TcpSocket: Optional[Sequence["_TcpSocket"]]

    @classmethod
    def _deserialize(
        cls: Type["_StartupProbe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartupProbe"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Exec=json_data.get("Exec"),
            HttpGet=json_data.get("HttpGet"),
            TcpSocket=json_data.get("TcpSocket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartupProbe = StartupProbe


@dataclass
class VolumeMount:
    MountPath: Optional[str]
    MountPropagation: Optional[str]
    Name: Optional[str]
    ReadOnly: Optional[bool]
    SubPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeMount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeMount"]:
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
_VolumeMount = VolumeMount


@dataclass
class DnsConfig:
    Nameservers: Optional[Sequence[str]]
    Searches: Optional[Sequence[str]]
    Option: Optional[Sequence["_Option"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfig"]:
        if not json_data:
            return None
        return cls(
            Nameservers=json_data.get("Nameservers"),
            Searches=json_data.get("Searches"),
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfig = DnsConfig


@dataclass
class Option:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Option"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Option"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Option = Option


@dataclass
class HostAliases:
    Hostnames: Optional[Sequence[str]]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostAliases"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostAliases"]:
        if not json_data:
            return None
        return cls(
            Hostnames=json_data.get("Hostnames"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostAliases = HostAliases


@dataclass
class ImagePullSecrets:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImagePullSecrets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImagePullSecrets"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImagePullSecrets = ImagePullSecrets


@dataclass
class InitContainer:
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Name: Optional[str]
    Stdin: Optional[bool]
    StdinOnce: Optional[bool]
    TerminationMessagePath: Optional[str]
    Tty: Optional[bool]
    WorkingDir: Optional[str]
    Env: Optional[Sequence["_Env"]]
    EnvFrom: Optional[Sequence["_EnvFrom"]]
    Lifecycle: Optional[Sequence["_Lifecycle"]]
    LivenessProbe: Optional[Sequence["_LivenessProbe"]]
    Port: Optional[Sequence["_Port"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbe"]]
    Resources: Optional[Sequence["_Resources"]]
    SecurityContext: Optional[Sequence["_SecurityContext"]]
    StartupProbe: Optional[Sequence["_StartupProbe"]]
    VolumeMount: Optional[Sequence["_VolumeMount"]]

    @classmethod
    def _deserialize(
        cls: Type["_InitContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitContainer"]:
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
            Tty=json_data.get("Tty"),
            WorkingDir=json_data.get("WorkingDir"),
            Env=json_data.get("Env"),
            EnvFrom=json_data.get("EnvFrom"),
            Lifecycle=json_data.get("Lifecycle"),
            LivenessProbe=json_data.get("LivenessProbe"),
            Port=json_data.get("Port"),
            ReadinessProbe=json_data.get("ReadinessProbe"),
            Resources=json_data.get("Resources"),
            SecurityContext=json_data.get("SecurityContext"),
            StartupProbe=json_data.get("StartupProbe"),
            VolumeMount=json_data.get("VolumeMount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitContainer = InitContainer


@dataclass
class Toleration:
    Effect: Optional[str]
    Key: Optional[str]
    Operator: Optional[str]
    TolerationSeconds: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Toleration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Toleration"]:
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
_Toleration = Toleration


@dataclass
class Volume:
    Name: Optional[str]
    AwsElasticBlockStore: Optional[Sequence["_AwsElasticBlockStore"]]
    AzureDisk: Optional[Sequence["_AzureDisk"]]
    AzureFile: Optional[Sequence["_AzureFile"]]
    CephFs: Optional[Sequence["_CephFs"]]
    Cinder: Optional[Sequence["_Cinder"]]
    ConfigMap: Optional[Sequence["_ConfigMap"]]
    DownwardApi: Optional[Sequence["_DownwardApi"]]
    EmptyDir: Optional[Sequence["_EmptyDir"]]
    Fc: Optional[Sequence["_Fc"]]
    FlexVolume: Optional[Sequence["_FlexVolume"]]
    Flocker: Optional[Sequence["_Flocker"]]
    GcePersistentDisk: Optional[Sequence["_GcePersistentDisk"]]
    GitRepo: Optional[Sequence["_GitRepo"]]
    Glusterfs: Optional[Sequence["_Glusterfs"]]
    HostPath: Optional[Sequence["_HostPath"]]
    Iscsi: Optional[Sequence["_Iscsi"]]
    Local: Optional[Sequence["_Local"]]
    Nfs: Optional[Sequence["_Nfs"]]
    PersistentVolumeClaim: Optional[Sequence["_PersistentVolumeClaim"]]
    PhotonPersistentDisk: Optional[Sequence["_PhotonPersistentDisk"]]
    Quobyte: Optional[Sequence["_Quobyte"]]
    Rbd: Optional[Sequence["_Rbd"]]
    Secret: Optional[Sequence["_Secret"]]
    VsphereVolume: Optional[Sequence["_VsphereVolume"]]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            AwsElasticBlockStore=json_data.get("AwsElasticBlockStore"),
            AzureDisk=json_data.get("AzureDisk"),
            AzureFile=json_data.get("AzureFile"),
            CephFs=json_data.get("CephFs"),
            Cinder=json_data.get("Cinder"),
            ConfigMap=json_data.get("ConfigMap"),
            DownwardApi=json_data.get("DownwardApi"),
            EmptyDir=json_data.get("EmptyDir"),
            Fc=json_data.get("Fc"),
            FlexVolume=json_data.get("FlexVolume"),
            Flocker=json_data.get("Flocker"),
            GcePersistentDisk=json_data.get("GcePersistentDisk"),
            GitRepo=json_data.get("GitRepo"),
            Glusterfs=json_data.get("Glusterfs"),
            HostPath=json_data.get("HostPath"),
            Iscsi=json_data.get("Iscsi"),
            Local=json_data.get("Local"),
            Nfs=json_data.get("Nfs"),
            PersistentVolumeClaim=json_data.get("PersistentVolumeClaim"),
            PhotonPersistentDisk=json_data.get("PhotonPersistentDisk"),
            Quobyte=json_data.get("Quobyte"),
            Rbd=json_data.get("Rbd"),
            Secret=json_data.get("Secret"),
            VsphereVolume=json_data.get("VsphereVolume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class AwsElasticBlockStore:
    FsType: Optional[str]
    Partition: Optional[float]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticBlockStore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticBlockStore"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticBlockStore = AwsElasticBlockStore


@dataclass
class AzureDisk:
    CachingMode: Optional[str]
    DataDiskUri: Optional[str]
    DiskName: Optional[str]
    FsType: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDisk"]:
        if not json_data:
            return None
        return cls(
            CachingMode=json_data.get("CachingMode"),
            DataDiskUri=json_data.get("DataDiskUri"),
            DiskName=json_data.get("DiskName"),
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDisk = AzureDisk


@dataclass
class AzureFile:
    ReadOnly: Optional[bool]
    SecretName: Optional[str]
    ShareName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFile"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SecretName=json_data.get("SecretName"),
            ShareName=json_data.get("ShareName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFile = AzureFile


@dataclass
class CephFs:
    Monitors: Optional[Sequence[str]]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    SecretFile: Optional[str]
    User: Optional[str]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_CephFs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CephFs"]:
        if not json_data:
            return None
        return cls(
            Monitors=json_data.get("Monitors"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretFile=json_data.get("SecretFile"),
            User=json_data.get("User"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CephFs = CephFs


@dataclass
class Cinder:
    FsType: Optional[str]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cinder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cinder"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cinder = Cinder


@dataclass
class ConfigMap:
    DefaultMode: Optional[str]
    Name: Optional[str]
    Items: Optional[Sequence["_Items"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMap"]:
        if not json_data:
            return None
        return cls(
            DefaultMode=json_data.get("DefaultMode"),
            Name=json_data.get("Name"),
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMap = ConfigMap


@dataclass
class Items:
    Key: Optional[str]
    Mode: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Items"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Items"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Mode=json_data.get("Mode"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Items = Items


@dataclass
class DownwardApi:
    DefaultMode: Optional[str]
    Items: Optional[Sequence["_Items"]]

    @classmethod
    def _deserialize(
        cls: Type["_DownwardApi"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DownwardApi"]:
        if not json_data:
            return None
        return cls(
            DefaultMode=json_data.get("DefaultMode"),
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DownwardApi = DownwardApi


@dataclass
class EmptyDir:
    Medium: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmptyDir"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmptyDir"]:
        if not json_data:
            return None
        return cls(
            Medium=json_data.get("Medium"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmptyDir = EmptyDir


@dataclass
class Fc:
    FsType: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetWwNs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Fc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Fc"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Lun=json_data.get("Lun"),
            ReadOnly=json_data.get("ReadOnly"),
            TargetWwNs=json_data.get("TargetWwNs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Fc = Fc


@dataclass
class FlexVolume:
    Driver: Optional[str]
    FsType: Optional[str]
    Options: Optional[Sequence["_Options"]]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlexVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlexVolume"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            FsType=json_data.get("FsType"),
            Options=json_data.get("Options"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlexVolume = FlexVolume


@dataclass
class Options:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class Flocker:
    DatasetName: Optional[str]
    DatasetUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Flocker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Flocker"]:
        if not json_data:
            return None
        return cls(
            DatasetName=json_data.get("DatasetName"),
            DatasetUuid=json_data.get("DatasetUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Flocker = Flocker


@dataclass
class GcePersistentDisk:
    FsType: Optional[str]
    Partition: Optional[float]
    PdName: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GcePersistentDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcePersistentDisk"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            PdName=json_data.get("PdName"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcePersistentDisk = GcePersistentDisk


@dataclass
class GitRepo:
    Directory: Optional[str]
    Repository: Optional[str]
    Revision: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitRepo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitRepo"]:
        if not json_data:
            return None
        return cls(
            Directory=json_data.get("Directory"),
            Repository=json_data.get("Repository"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitRepo = GitRepo


@dataclass
class Glusterfs:
    EndpointsName: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Glusterfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Glusterfs"]:
        if not json_data:
            return None
        return cls(
            EndpointsName=json_data.get("EndpointsName"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Glusterfs = Glusterfs


@dataclass
class HostPath:
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostPath"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostPath = HostPath


@dataclass
class Iscsi:
    FsType: Optional[str]
    Iqn: Optional[str]
    IscsiInterface: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetPortal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Iscsi"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iscsi"]:
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
_Iscsi = Iscsi


@dataclass
class Local:
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Local"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Local"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Local = Local


@dataclass
class Nfs:
    Path: Optional[str]
    ReadOnly: Optional[bool]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nfs"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nfs = Nfs


@dataclass
class PersistentVolumeClaim:
    ClaimName: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PersistentVolumeClaim"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PersistentVolumeClaim"]:
        if not json_data:
            return None
        return cls(
            ClaimName=json_data.get("ClaimName"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PersistentVolumeClaim = PersistentVolumeClaim


@dataclass
class PhotonPersistentDisk:
    FsType: Optional[str]
    PdId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhotonPersistentDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhotonPersistentDisk"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            PdId=json_data.get("PdId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhotonPersistentDisk = PhotonPersistentDisk


@dataclass
class Quobyte:
    Group: Optional[str]
    ReadOnly: Optional[bool]
    Registry: Optional[str]
    User: Optional[str]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Quobyte"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Quobyte"]:
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
_Quobyte = Quobyte


@dataclass
class Rbd:
    CephMonitors: Optional[Sequence[str]]
    FsType: Optional[str]
    Keyring: Optional[str]
    RadosUser: Optional[str]
    RbdImage: Optional[str]
    RbdPool: Optional[str]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rbd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rbd"]:
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
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rbd = Rbd


@dataclass
class Secret:
    DefaultMode: Optional[str]
    Optional: Optional[bool]
    SecretName: Optional[str]
    Items: Optional[Sequence["_Items"]]

    @classmethod
    def _deserialize(
        cls: Type["_Secret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secret"]:
        if not json_data:
            return None
        return cls(
            DefaultMode=json_data.get("DefaultMode"),
            Optional=json_data.get("Optional"),
            SecretName=json_data.get("SecretName"),
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secret = Secret


@dataclass
class VsphereVolume:
    FsType: Optional[str]
    VolumePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereVolume"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            VolumePath=json_data.get("VolumePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereVolume = VsphereVolume


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class Selector:
    MatchLabels: Optional[Sequence["_MatchLabels2"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Selector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Selector"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=json_data.get("MatchLabels"),
            MatchExpressions=json_data.get("MatchExpressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Selector = Selector


@dataclass
class MatchLabels2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabels2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabels2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabels2 = MatchLabels2


@dataclass
class Strategy:
    Type: Optional[str]
    RollingUpdate: Optional[Sequence["_RollingUpdate"]]

    @classmethod
    def _deserialize(
        cls: Type["_Strategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Strategy"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            RollingUpdate=json_data.get("RollingUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Strategy = Strategy


@dataclass
class RollingUpdate:
    MaxSurge: Optional[str]
    MaxUnavailable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollingUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollingUpdate"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
            MaxUnavailable=json_data.get("MaxUnavailable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollingUpdate = RollingUpdate


@dataclass
class Template:
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]

    @classmethod
    def _deserialize(
        cls: Type["_Template"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Template"]:
        if not json_data:
            return None
        return cls(
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Template = Template


