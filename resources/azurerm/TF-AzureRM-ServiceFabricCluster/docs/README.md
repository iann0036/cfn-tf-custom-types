# TF::AzureRM::ServiceFabricCluster

Manages a Service Fabric Cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ServiceFabricCluster",
    "Properties" : {
        "<a href="#addonfeatures" title="AddOnFeatures">AddOnFeatures</a>" : <i>[ String, ... ]</i>,
        "<a href="#clustercodeversion" title="ClusterCodeVersion">ClusterCodeVersion</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reliabilitylevel" title="ReliabilityLevel">ReliabilityLevel</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#upgrademode" title="UpgradeMode">UpgradeMode</a>" : <i>String</i>,
        "<a href="#vmimage" title="VmImage">VmImage</a>" : <i>String</i>,
        "<a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>" : <i>[ <a href="azureactivedirectorydefinition.md">AzureActiveDirectoryDefinition</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
        "<a href="#certificatecommonnames" title="CertificateCommonNames">CertificateCommonNames</a>" : <i>[ <a href="certificatecommonnamesdefinition.md">CertificateCommonNamesDefinition</a>, ... ]</i>,
        "<a href="#clientcertificatecommonname" title="ClientCertificateCommonName">ClientCertificateCommonName</a>" : <i>[ <a href="clientcertificatecommonnamedefinition.md">ClientCertificateCommonNameDefinition</a>, ... ]</i>,
        "<a href="#clientcertificatethumbprint" title="ClientCertificateThumbprint">ClientCertificateThumbprint</a>" : <i>[ <a href="clientcertificatethumbprintdefinition.md">ClientCertificateThumbprintDefinition</a>, ... ]</i>,
        "<a href="#diagnosticsconfig" title="DiagnosticsConfig">DiagnosticsConfig</a>" : <i>[ <a href="diagnosticsconfigdefinition.md">DiagnosticsConfigDefinition</a>, ... ]</i>,
        "<a href="#fabricsettings" title="FabricSettings">FabricSettings</a>" : <i>[ <a href="fabricsettingsdefinition.md">FabricSettingsDefinition</a>, ... ]</i>,
        "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>[ <a href="nodetypedefinition.md">NodeTypeDefinition</a>, ... ]</i>,
        "<a href="#reverseproxycertificate" title="ReverseProxyCertificate">ReverseProxyCertificate</a>" : <i>[ <a href="reverseproxycertificatedefinition.md">ReverseProxyCertificateDefinition</a>, ... ]</i>,
        "<a href="#reverseproxycertificatecommonnames" title="ReverseProxyCertificateCommonNames">ReverseProxyCertificateCommonNames</a>" : <i>[ <a href="reverseproxycertificatecommonnamesdefinition.md">ReverseProxyCertificateCommonNamesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#upgradepolicy" title="UpgradePolicy">UpgradePolicy</a>" : <i>[ <a href="upgradepolicydefinition.md">UpgradePolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ServiceFabricCluster
Properties:
    <a href="#addonfeatures" title="AddOnFeatures">AddOnFeatures</a>: <i>
      - String</i>
    <a href="#clustercodeversion" title="ClusterCodeVersion">ClusterCodeVersion</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reliabilitylevel" title="ReliabilityLevel">ReliabilityLevel</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#upgrademode" title="UpgradeMode">UpgradeMode</a>: <i>String</i>
    <a href="#vmimage" title="VmImage">VmImage</a>: <i>String</i>
    <a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>: <i>
      - <a href="azureactivedirectorydefinition.md">AzureActiveDirectoryDefinition</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
    <a href="#certificatecommonnames" title="CertificateCommonNames">CertificateCommonNames</a>: <i>
      - <a href="certificatecommonnamesdefinition.md">CertificateCommonNamesDefinition</a></i>
    <a href="#clientcertificatecommonname" title="ClientCertificateCommonName">ClientCertificateCommonName</a>: <i>
      - <a href="clientcertificatecommonnamedefinition.md">ClientCertificateCommonNameDefinition</a></i>
    <a href="#clientcertificatethumbprint" title="ClientCertificateThumbprint">ClientCertificateThumbprint</a>: <i>
      - <a href="clientcertificatethumbprintdefinition.md">ClientCertificateThumbprintDefinition</a></i>
    <a href="#diagnosticsconfig" title="DiagnosticsConfig">DiagnosticsConfig</a>: <i>
      - <a href="diagnosticsconfigdefinition.md">DiagnosticsConfigDefinition</a></i>
    <a href="#fabricsettings" title="FabricSettings">FabricSettings</a>: <i>
      - <a href="fabricsettingsdefinition.md">FabricSettingsDefinition</a></i>
    <a href="#nodetype" title="NodeType">NodeType</a>: <i>
      - <a href="nodetypedefinition.md">NodeTypeDefinition</a></i>
    <a href="#reverseproxycertificate" title="ReverseProxyCertificate">ReverseProxyCertificate</a>: <i>
      - <a href="reverseproxycertificatedefinition.md">ReverseProxyCertificateDefinition</a></i>
    <a href="#reverseproxycertificatecommonnames" title="ReverseProxyCertificateCommonNames">ReverseProxyCertificateCommonNames</a>: <i>
      - <a href="reverseproxycertificatecommonnamesdefinition.md">ReverseProxyCertificateCommonNamesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#upgradepolicy" title="UpgradePolicy">UpgradePolicy</a>: <i>
      - <a href="upgradepolicydefinition.md">UpgradePolicyDefinition</a></i>
</pre>

## Properties

#### AddOnFeatures

A List of one or more features which should be enabled, such as `DnsService`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterCodeVersion

Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementEndpoint

Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Service Fabric Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReliabilityLevel

Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeMode

Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmImage

Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectory

_Required_: No

_Type_: List of <a href="azureactivedirectorydefinition.md">AzureActiveDirectoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateCommonNames

_Required_: No

_Type_: List of <a href="certificatecommonnamesdefinition.md">CertificateCommonNamesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateCommonName

_Required_: No

_Type_: List of <a href="clientcertificatecommonnamedefinition.md">ClientCertificateCommonNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateThumbprint

_Required_: No

_Type_: List of <a href="clientcertificatethumbprintdefinition.md">ClientCertificateThumbprintDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiagnosticsConfig

_Required_: No

_Type_: List of <a href="diagnosticsconfigdefinition.md">DiagnosticsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricSettings

_Required_: No

_Type_: List of <a href="fabricsettingsdefinition.md">FabricSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: No

_Type_: List of <a href="nodetypedefinition.md">NodeTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseProxyCertificate

_Required_: No

_Type_: List of <a href="reverseproxycertificatedefinition.md">ReverseProxyCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseProxyCertificateCommonNames

_Required_: No

_Type_: List of <a href="reverseproxycertificatecommonnamesdefinition.md">ReverseProxyCertificateCommonNamesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradePolicy

_Required_: No

_Type_: List of <a href="upgradepolicydefinition.md">UpgradePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterEndpoint

Returns the <code>ClusterEndpoint</code> value.

#### Id

Returns the <code>Id</code> value.

