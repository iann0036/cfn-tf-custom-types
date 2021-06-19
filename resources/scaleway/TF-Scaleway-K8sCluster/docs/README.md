# TF::Scaleway::K8sCluster

Creates and manages Scaleway Kubernetes clusters. For more information, see [the documentation](https://developers.scaleway.com/en/products/k8s/api/).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Scaleway::K8sCluster",
    "Properties" : {
        "<a href="#admissionplugins" title="AdmissionPlugins">AdmissionPlugins</a>" : <i>[ String, ... ]</i>,
        "<a href="#apiservercertsans" title="ApiserverCertSans">ApiserverCertSans</a>" : <i>[ String, ... ]</i>,
        "<a href="#cni" title="Cni">Cni</a>" : <i>String</i>,
        "<a href="#deleteadditionalresources" title="DeleteAdditionalResources">DeleteAdditionalResources</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#featuregates" title="FeatureGates">FeatureGates</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>" : <i>[ <a href="autoupgradedefinition.md">AutoUpgradeDefinition</a>, ... ]</i>,
        "<a href="#autoscalerconfig" title="AutoscalerConfig">AutoscalerConfig</a>" : <i>[ <a href="autoscalerconfigdefinition.md">AutoscalerConfigDefinition</a>, ... ]</i>,
        "<a href="#openidconnectconfig" title="OpenIdConnectConfig">OpenIdConnectConfig</a>" : <i>[ <a href="openidconnectconfigdefinition.md">OpenIdConnectConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Scaleway::K8sCluster
Properties:
    <a href="#admissionplugins" title="AdmissionPlugins">AdmissionPlugins</a>: <i>
      - String</i>
    <a href="#apiservercertsans" title="ApiserverCertSans">ApiserverCertSans</a>: <i>
      - String</i>
    <a href="#cni" title="Cni">Cni</a>: <i>String</i>
    <a href="#deleteadditionalresources" title="DeleteAdditionalResources">DeleteAdditionalResources</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#featuregates" title="FeatureGates">FeatureGates</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>: <i>
      - <a href="autoupgradedefinition.md">AutoUpgradeDefinition</a></i>
    <a href="#autoscalerconfig" title="AutoscalerConfig">AutoscalerConfig</a>: <i>
      - <a href="autoscalerconfigdefinition.md">AutoscalerConfigDefinition</a></i>
    <a href="#openidconnectconfig" title="OpenIdConnectConfig">OpenIdConnectConfig</a>: <i>
      - <a href="openidconnectconfigdefinition.md">OpenIdConnectConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdmissionPlugins

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiserverCertSans

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cni

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAdditionalResources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureGates

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

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

_Type_: List of <a href="autoupgradedefinition.md">AutoUpgradeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalerConfig

_Required_: No

_Type_: List of <a href="autoscalerconfigdefinition.md">AutoscalerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenIdConnectConfig

_Required_: No

_Type_: List of <a href="openidconnectconfigdefinition.md">OpenIdConnectConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

Returns the <code>ApiserverUrl</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### Kubeconfig

Returns the <code>Kubeconfig</code> value.

#### OrganizationId

Returns the <code>OrganizationId</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

#### UpgradeAvailable

Returns the <code>UpgradeAvailable</code> value.

#### WildcardDns

Returns the <code>WildcardDns</code> value.

