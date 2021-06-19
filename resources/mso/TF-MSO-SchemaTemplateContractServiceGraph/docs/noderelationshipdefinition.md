# TF::MSO::SchemaTemplateContractServiceGraph NodeRelationshipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#consumerconnectorbdname" title="ConsumerConnectorBdName">ConsumerConnectorBdName</a>" : <i>String</i>,
    "<a href="#consumerconnectorbdschemaid" title="ConsumerConnectorBdSchemaId">ConsumerConnectorBdSchemaId</a>" : <i>String</i>,
    "<a href="#consumerconnectorbdtemplatename" title="ConsumerConnectorBdTemplateName">ConsumerConnectorBdTemplateName</a>" : <i>String</i>,
    "<a href="#consumerconnectorclusterinterface" title="ConsumerConnectorClusterInterface">ConsumerConnectorClusterInterface</a>" : <i>String</i>,
    "<a href="#consumerconnectorredirectpolicy" title="ConsumerConnectorRedirectPolicy">ConsumerConnectorRedirectPolicy</a>" : <i>String</i>,
    "<a href="#consumerconnectorredirectpolicytenant" title="ConsumerConnectorRedirectPolicyTenant">ConsumerConnectorRedirectPolicyTenant</a>" : <i>String</i>,
    "<a href="#consumersubnetips" title="ConsumerSubnetIps">ConsumerSubnetIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#providerconnectorbdname" title="ProviderConnectorBdName">ProviderConnectorBdName</a>" : <i>String</i>,
    "<a href="#providerconnectorbdschemaid" title="ProviderConnectorBdSchemaId">ProviderConnectorBdSchemaId</a>" : <i>String</i>,
    "<a href="#providerconnectorbdtemplatename" title="ProviderConnectorBdTemplateName">ProviderConnectorBdTemplateName</a>" : <i>String</i>,
    "<a href="#providerconnectorclusterinterface" title="ProviderConnectorClusterInterface">ProviderConnectorClusterInterface</a>" : <i>String</i>,
    "<a href="#providerconnectorredirectpolicy" title="ProviderConnectorRedirectPolicy">ProviderConnectorRedirectPolicy</a>" : <i>String</i>,
    "<a href="#providerconnectorredirectpolicytenant" title="ProviderConnectorRedirectPolicyTenant">ProviderConnectorRedirectPolicyTenant</a>" : <i>String</i>,
    "<a href="#providersubnetips" title="ProviderSubnetIps">ProviderSubnetIps</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#consumerconnectorbdname" title="ConsumerConnectorBdName">ConsumerConnectorBdName</a>: <i>String</i>
<a href="#consumerconnectorbdschemaid" title="ConsumerConnectorBdSchemaId">ConsumerConnectorBdSchemaId</a>: <i>String</i>
<a href="#consumerconnectorbdtemplatename" title="ConsumerConnectorBdTemplateName">ConsumerConnectorBdTemplateName</a>: <i>String</i>
<a href="#consumerconnectorclusterinterface" title="ConsumerConnectorClusterInterface">ConsumerConnectorClusterInterface</a>: <i>String</i>
<a href="#consumerconnectorredirectpolicy" title="ConsumerConnectorRedirectPolicy">ConsumerConnectorRedirectPolicy</a>: <i>String</i>
<a href="#consumerconnectorredirectpolicytenant" title="ConsumerConnectorRedirectPolicyTenant">ConsumerConnectorRedirectPolicyTenant</a>: <i>String</i>
<a href="#consumersubnetips" title="ConsumerSubnetIps">ConsumerSubnetIps</a>: <i>
      - String</i>
<a href="#providerconnectorbdname" title="ProviderConnectorBdName">ProviderConnectorBdName</a>: <i>String</i>
<a href="#providerconnectorbdschemaid" title="ProviderConnectorBdSchemaId">ProviderConnectorBdSchemaId</a>: <i>String</i>
<a href="#providerconnectorbdtemplatename" title="ProviderConnectorBdTemplateName">ProviderConnectorBdTemplateName</a>: <i>String</i>
<a href="#providerconnectorclusterinterface" title="ProviderConnectorClusterInterface">ProviderConnectorClusterInterface</a>: <i>String</i>
<a href="#providerconnectorredirectpolicy" title="ProviderConnectorRedirectPolicy">ProviderConnectorRedirectPolicy</a>: <i>String</i>
<a href="#providerconnectorredirectpolicytenant" title="ProviderConnectorRedirectPolicyTenant">ProviderConnectorRedirectPolicyTenant</a>: <i>String</i>
<a href="#providersubnetips" title="ProviderSubnetIps">ProviderSubnetIps</a>: <i>
      - String</i>
</pre>

## Properties

#### ConsumerConnectorBdName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumerConnectorBdSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumerConnectorBdTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumerConnectorClusterInterface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumerConnectorRedirectPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumerConnectorRedirectPolicyTenant

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumerSubnetIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderConnectorBdName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderConnectorBdSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderConnectorBdTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderConnectorClusterInterface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderConnectorRedirectPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderConnectorRedirectPolicyTenant

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderSubnetIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

