# TF::Rancher2::Cluster CloudProviderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customcloudprovider" title="CustomCloudProvider">CustomCloudProvider</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#awscloudprovider" title="AwsCloudProvider">AwsCloudProvider</a>" : <i>[ <a href="awscloudproviderdefinition.md">AwsCloudProviderDefinition</a>, ... ]</i>,
    "<a href="#azurecloudprovider" title="AzureCloudProvider">AzureCloudProvider</a>" : <i>[ <a href="azurecloudproviderdefinition.md">AzureCloudProviderDefinition</a>, ... ]</i>,
    "<a href="#openstackcloudprovider" title="OpenstackCloudProvider">OpenstackCloudProvider</a>" : <i>[ <a href="openstackcloudproviderdefinition.md">OpenstackCloudProviderDefinition</a>, ... ]</i>,
    "<a href="#vspherecloudprovider" title="VsphereCloudProvider">VsphereCloudProvider</a>" : <i>[ <a href="vspherecloudproviderdefinition.md">VsphereCloudProviderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customcloudprovider" title="CustomCloudProvider">CustomCloudProvider</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#awscloudprovider" title="AwsCloudProvider">AwsCloudProvider</a>: <i>
      - <a href="awscloudproviderdefinition.md">AwsCloudProviderDefinition</a></i>
<a href="#azurecloudprovider" title="AzureCloudProvider">AzureCloudProvider</a>: <i>
      - <a href="azurecloudproviderdefinition.md">AzureCloudProviderDefinition</a></i>
<a href="#openstackcloudprovider" title="OpenstackCloudProvider">OpenstackCloudProvider</a>: <i>
      - <a href="openstackcloudproviderdefinition.md">OpenstackCloudProviderDefinition</a></i>
<a href="#vspherecloudprovider" title="VsphereCloudProvider">VsphereCloudProvider</a>: <i>
      - <a href="vspherecloudproviderdefinition.md">VsphereCloudProviderDefinition</a></i>
</pre>

## Properties

#### CustomCloudProvider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCloudProvider

_Required_: No

_Type_: List of <a href="awscloudproviderdefinition.md">AwsCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureCloudProvider

_Required_: No

_Type_: List of <a href="azurecloudproviderdefinition.md">AzureCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackCloudProvider

_Required_: No

_Type_: List of <a href="openstackcloudproviderdefinition.md">OpenstackCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereCloudProvider

_Required_: No

_Type_: List of <a href="vspherecloudproviderdefinition.md">VsphereCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

