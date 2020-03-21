# Terraform::Scaleway::K8sClusterBeta

CloudFormation equivalent of scaleway_k8s_cluster_beta

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::K8sClusterBeta",
    "Properties" : {
        "<a href="#admissionplugins" title="AdmissionPlugins">AdmissionPlugins</a>" : <i>[ String, ... ]</i>,
        "<a href="#cni" title="Cni">Cni</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabledashboard" title="EnableDashboard">EnableDashboard</a>" : <i>Boolean</i>,
        "<a href="#featuregates" title="FeatureGates">FeatureGates</a>" : <i>[ String, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#organizationid" title="OrganizationId">OrganizationId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>" : <i>[ &lt;a href=&#34;autoupgrade.md&#34;&gt;AutoUpgrade&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscalerconfig" title="AutoscalerConfig">AutoscalerConfig</a>" : <i>[ &lt;a href=&#34;autoscalerconfig.md&#34;&gt;AutoscalerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultpool" title="DefaultPool">DefaultPool</a>" : <i>[ &lt;a href=&#34;defaultpool.md&#34;&gt;DefaultPool&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::K8sClusterBeta
Properties:
    <a href="#admissionplugins" title="AdmissionPlugins">AdmissionPlugins</a>: <i>
      - String</i>
    <a href="#cni" title="Cni">Cni</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabledashboard" title="EnableDashboard">EnableDashboard</a>: <i>Boolean</i>
    <a href="#featuregates" title="FeatureGates">FeatureGates</a>: <i>
      - String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#organizationid" title="OrganizationId">OrganizationId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>: <i>
      - &lt;a href=&#34;autoupgrade.md&#34;&gt;AutoUpgrade&lt;/a&gt;</i>
    <a href="#autoscalerconfig" title="AutoscalerConfig">AutoscalerConfig</a>: <i>
      - &lt;a href=&#34;autoscalerconfig.md&#34;&gt;AutoscalerConfig&lt;/a&gt;</i>
    <a href="#defaultpool" title="DefaultPool">DefaultPool</a>: <i>
      - &lt;a href=&#34;defaultpool.md&#34;&gt;DefaultPool&lt;/a&gt;</i>
</pre>

## Properties

#### AdmissionPlugins

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cni

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDashboard

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureGates

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUpgrade

_Required_: No

_Type_: List of &lt;a href=&#34;autoupgrade.md&#34;&gt;AutoUpgrade&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;autoscalerconfig.md&#34;&gt;AutoscalerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPool

_Required_: No

_Type_: List of &lt;a href=&#34;defaultpool.md&#34;&gt;DefaultPool&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiserverUrl

Returns the &lt;code&gt;ApiserverUrl&lt;/code&gt; value.

#### CreatedAt

Returns the &lt;code&gt;CreatedAt&lt;/code&gt; value.

#### Kubeconfig

Returns the &lt;code&gt;Kubeconfig&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### UpdatedAt

Returns the &lt;code&gt;UpdatedAt&lt;/code&gt; value.

#### UpgradeAvailable

Returns the &lt;code&gt;UpgradeAvailable&lt;/code&gt; value.

#### WildcardDns

Returns the &lt;code&gt;WildcardDns&lt;/code&gt; value.

