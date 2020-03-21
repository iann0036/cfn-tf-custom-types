# Terraform::AzureRM::ServiceFabricCluster

CloudFormation equivalent of azurerm_service_fabric_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ServiceFabricCluster",
    "Properties" : {
        "<a href="#addonfeatures" title="AddOnFeatures">AddOnFeatures</a>" : <i>[ String, ... ]</i>,
        "<a href="#clustercodeversion" title="ClusterCodeVersion">ClusterCodeVersion</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reliabilitylevel" title="ReliabilityLevel">ReliabilityLevel</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#upgrademode" title="UpgradeMode">UpgradeMode</a>" : <i>String</i>,
        "<a href="#vmimage" title="VmImage">VmImage</a>" : <i>String</i>,
        "<a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>" : <i>[ &lt;a href=&#34;azureactivedirectory.md&#34;&gt;AzureActiveDirectory&lt;/a&gt;, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;, ... ]</i>,
        "<a href="#certificatecommonnames" title="CertificateCommonNames">CertificateCommonNames</a>" : <i>[ &lt;a href=&#34;certificatecommonnames.md&#34;&gt;CertificateCommonNames&lt;/a&gt;, ... ]</i>,
        "<a href="#clientcertificatethumbprint" title="ClientCertificateThumbprint">ClientCertificateThumbprint</a>" : <i>[ &lt;a href=&#34;clientcertificatethumbprint.md&#34;&gt;ClientCertificateThumbprint&lt;/a&gt;, ... ]</i>,
        "<a href="#diagnosticsconfig" title="DiagnosticsConfig">DiagnosticsConfig</a>" : <i>[ &lt;a href=&#34;diagnosticsconfig.md&#34;&gt;DiagnosticsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#fabricsettings" title="FabricSettings">FabricSettings</a>" : <i>[ &lt;a href=&#34;fabricsettings.md&#34;&gt;FabricSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>[ &lt;a href=&#34;nodetype.md&#34;&gt;NodeType&lt;/a&gt;, ... ]</i>,
        "<a href="#reverseproxycertificate" title="ReverseProxyCertificate">ReverseProxyCertificate</a>" : <i>[ &lt;a href=&#34;reverseproxycertificate.md&#34;&gt;ReverseProxyCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#commonnames" title="CommonNames">CommonNames</a>" : <i>[ &lt;a href=&#34;commonnames.md&#34;&gt;CommonNames&lt;/a&gt;, ... ]</i>,
        "<a href="#applicationports" title="ApplicationPorts">ApplicationPorts</a>" : <i>[ &lt;a href=&#34;applicationports.md&#34;&gt;ApplicationPorts&lt;/a&gt;, ... ]</i>,
        "<a href="#ephemeralports" title="EphemeralPorts">EphemeralPorts</a>" : <i>[ &lt;a href=&#34;ephemeralports.md&#34;&gt;EphemeralPorts&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ServiceFabricCluster
Properties:
    <a href="#addonfeatures" title="AddOnFeatures">AddOnFeatures</a>: <i>
      - String</i>
    <a href="#clustercodeversion" title="ClusterCodeVersion">ClusterCodeVersion</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reliabilitylevel" title="ReliabilityLevel">ReliabilityLevel</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#upgrademode" title="UpgradeMode">UpgradeMode</a>: <i>String</i>
    <a href="#vmimage" title="VmImage">VmImage</a>: <i>String</i>
    <a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>: <i>
      - &lt;a href=&#34;azureactivedirectory.md&#34;&gt;AzureActiveDirectory&lt;/a&gt;</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;</i>
    <a href="#certificatecommonnames" title="CertificateCommonNames">CertificateCommonNames</a>: <i>
      - &lt;a href=&#34;certificatecommonnames.md&#34;&gt;CertificateCommonNames&lt;/a&gt;</i>
    <a href="#clientcertificatethumbprint" title="ClientCertificateThumbprint">ClientCertificateThumbprint</a>: <i>
      - &lt;a href=&#34;clientcertificatethumbprint.md&#34;&gt;ClientCertificateThumbprint&lt;/a&gt;</i>
    <a href="#diagnosticsconfig" title="DiagnosticsConfig">DiagnosticsConfig</a>: <i>
      - &lt;a href=&#34;diagnosticsconfig.md&#34;&gt;DiagnosticsConfig&lt;/a&gt;</i>
    <a href="#fabricsettings" title="FabricSettings">FabricSettings</a>: <i>
      - &lt;a href=&#34;fabricsettings.md&#34;&gt;FabricSettings&lt;/a&gt;</i>
    <a href="#nodetype" title="NodeType">NodeType</a>: <i>
      - &lt;a href=&#34;nodetype.md&#34;&gt;NodeType&lt;/a&gt;</i>
    <a href="#reverseproxycertificate" title="ReverseProxyCertificate">ReverseProxyCertificate</a>: <i>
      - &lt;a href=&#34;reverseproxycertificate.md&#34;&gt;ReverseProxyCertificate&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#commonnames" title="CommonNames">CommonNames</a>: <i>
      - &lt;a href=&#34;commonnames.md&#34;&gt;CommonNames&lt;/a&gt;</i>
    <a href="#applicationports" title="ApplicationPorts">ApplicationPorts</a>: <i>
      - &lt;a href=&#34;applicationports.md&#34;&gt;ApplicationPorts&lt;/a&gt;</i>
    <a href="#ephemeralports" title="EphemeralPorts">EphemeralPorts</a>: <i>
      - &lt;a href=&#34;ephemeralports.md&#34;&gt;EphemeralPorts&lt;/a&gt;</i>
</pre>

## Properties

#### AddOnFeatures

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterCodeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementEndpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReliabilityLevel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmImage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectory

_Required_: No

_Type_: List of &lt;a href=&#34;azureactivedirectory.md&#34;&gt;AzureActiveDirectory&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateCommonNames

_Required_: No

_Type_: List of &lt;a href=&#34;certificatecommonnames.md&#34;&gt;CertificateCommonNames&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateThumbprint

_Required_: No

_Type_: List of &lt;a href=&#34;clientcertificatethumbprint.md&#34;&gt;ClientCertificateThumbprint&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiagnosticsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;diagnosticsconfig.md&#34;&gt;DiagnosticsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricSettings

_Required_: No

_Type_: List of &lt;a href=&#34;fabricsettings.md&#34;&gt;FabricSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: No

_Type_: List of &lt;a href=&#34;nodetype.md&#34;&gt;NodeType&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseProxyCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;reverseproxycertificate.md&#34;&gt;ReverseProxyCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonNames

_Required_: No

_Type_: List of &lt;a href=&#34;commonnames.md&#34;&gt;CommonNames&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationPorts

_Required_: No

_Type_: List of &lt;a href=&#34;applicationports.md&#34;&gt;ApplicationPorts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralPorts

_Required_: No

_Type_: List of &lt;a href=&#34;ephemeralports.md&#34;&gt;EphemeralPorts&lt;/a&gt;

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

Returns the &lt;code&gt;ClusterEndpoint&lt;/code&gt; value.

