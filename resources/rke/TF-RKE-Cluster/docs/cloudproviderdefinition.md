# TF::RKE::Cluster CloudProviderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customcloudconfig" title="CustomCloudConfig">CustomCloudConfig</a>" : <i>String</i>,
    "<a href="#customcloudprovider" title="CustomCloudProvider">CustomCloudProvider</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#awscloudconfig" title="AwsCloudConfig">AwsCloudConfig</a>" : <i>[ <a href="awscloudconfigdefinition.md">AwsCloudConfigDefinition</a>, ... ]</i>,
    "<a href="#awscloudprovider" title="AwsCloudProvider">AwsCloudProvider</a>" : <i>[ <a href="awscloudproviderdefinition.md">AwsCloudProviderDefinition</a>, ... ]</i>,
    "<a href="#azurecloudconfig" title="AzureCloudConfig">AzureCloudConfig</a>" : <i>[ <a href="azurecloudconfigdefinition.md">AzureCloudConfigDefinition</a>, ... ]</i>,
    "<a href="#azurecloudprovider" title="AzureCloudProvider">AzureCloudProvider</a>" : <i>[ <a href="azurecloudproviderdefinition.md">AzureCloudProviderDefinition</a>, ... ]</i>,
    "<a href="#openstackcloudconfig" title="OpenstackCloudConfig">OpenstackCloudConfig</a>" : <i>[ <a href="openstackcloudconfigdefinition.md">OpenstackCloudConfigDefinition</a>, ... ]</i>,
    "<a href="#openstackcloudprovider" title="OpenstackCloudProvider">OpenstackCloudProvider</a>" : <i>[ <a href="openstackcloudproviderdefinition.md">OpenstackCloudProviderDefinition</a>, ... ]</i>,
    "<a href="#vspherecloudconfig" title="VsphereCloudConfig">VsphereCloudConfig</a>" : <i>[ <a href="vspherecloudconfigdefinition.md">VsphereCloudConfigDefinition</a>, ... ]</i>,
    "<a href="#vspherecloudprovider" title="VsphereCloudProvider">VsphereCloudProvider</a>" : <i>[ <a href="vspherecloudproviderdefinition.md">VsphereCloudProviderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customcloudconfig" title="CustomCloudConfig">CustomCloudConfig</a>: <i>String</i>
<a href="#customcloudprovider" title="CustomCloudProvider">CustomCloudProvider</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#awscloudconfig" title="AwsCloudConfig">AwsCloudConfig</a>: <i>
      - <a href="awscloudconfigdefinition.md">AwsCloudConfigDefinition</a></i>
<a href="#awscloudprovider" title="AwsCloudProvider">AwsCloudProvider</a>: <i>
      - <a href="awscloudproviderdefinition.md">AwsCloudProviderDefinition</a></i>
<a href="#azurecloudconfig" title="AzureCloudConfig">AzureCloudConfig</a>: <i>
      - <a href="azurecloudconfigdefinition.md">AzureCloudConfigDefinition</a></i>
<a href="#azurecloudprovider" title="AzureCloudProvider">AzureCloudProvider</a>: <i>
      - <a href="azurecloudproviderdefinition.md">AzureCloudProviderDefinition</a></i>
<a href="#openstackcloudconfig" title="OpenstackCloudConfig">OpenstackCloudConfig</a>: <i>
      - <a href="openstackcloudconfigdefinition.md">OpenstackCloudConfigDefinition</a></i>
<a href="#openstackcloudprovider" title="OpenstackCloudProvider">OpenstackCloudProvider</a>: <i>
      - <a href="openstackcloudproviderdefinition.md">OpenstackCloudProviderDefinition</a></i>
<a href="#vspherecloudconfig" title="VsphereCloudConfig">VsphereCloudConfig</a>: <i>
      - <a href="vspherecloudconfigdefinition.md">VsphereCloudConfigDefinition</a></i>
<a href="#vspherecloudprovider" title="VsphereCloudProvider">VsphereCloudProvider</a>: <i>
      - <a href="vspherecloudproviderdefinition.md">VsphereCloudProviderDefinition</a></i>
</pre>

## Properties

#### CustomCloudConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCloudProvider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCloudConfig

_Required_: No

_Type_: List of <a href="awscloudconfigdefinition.md">AwsCloudConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCloudProvider

_Required_: No

_Type_: List of <a href="awscloudproviderdefinition.md">AwsCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureCloudConfig

_Required_: No

_Type_: List of <a href="azurecloudconfigdefinition.md">AzureCloudConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureCloudProvider

_Required_: No

_Type_: List of <a href="azurecloudproviderdefinition.md">AzureCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackCloudConfig

_Required_: No

_Type_: List of <a href="openstackcloudconfigdefinition.md">OpenstackCloudConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackCloudProvider

_Required_: No

_Type_: List of <a href="openstackcloudproviderdefinition.md">OpenstackCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereCloudConfig

_Required_: No

_Type_: List of <a href="vspherecloudconfigdefinition.md">VsphereCloudConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereCloudProvider

_Required_: No

_Type_: List of <a href="vspherecloudproviderdefinition.md">VsphereCloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

